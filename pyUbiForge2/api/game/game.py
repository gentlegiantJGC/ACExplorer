from typing import Generator, Tuple, Optional, Dict, TYPE_CHECKING, Type, List, Union, KeysView
import glob
import os

from pyUbiForge2.api import log
from pyUbiForge2.api.file_object import FileDataWrapper, FileFormatDataWrapper
from pyUbiForge2.api.game.file_cache import FileCache
from pyUbiForge2.api.game.file_finder import FileFinder
from pyUbiForge2.api.data_types import (
    ForgeStorage,
    ForgeFileName,
    DataFileIdentifier,
    FileIdentifier,
)
from pyUbiForge2.api.errors import FileNotExhaustedError, FileParserNotFound

if TYPE_CHECKING:
    from pyUbiForge2.api.game import BaseFile
    from pyUbiForge2.api.game import BaseForge


class BaseGame:
    ForgeClass: Type["BaseForge"] = None
    GameIdentifier: str = None
    FileIDType: str = None
    ResourceDType: str = None
    endianness = "<"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        if self.__class__ is BaseGame:
            raise Exception("BaseGame must be subclassed")
        for attr, attr_name in (
                (self.GameIdentifier, "GameIdentifier"),
                (self.FileIDType, "FileIDType"),
                (self.ResourceDType, "ResourceDType")
        ):
            if attr is None:
                raise Exception(f"{attr_name} has not been set in {self.__class__.__name__}")
        if self.ForgeClass is None:
            raise Exception("ForgeClass attribute has not been overwritten.")
        self._file_readers: Dict[int, Type["BaseFile"]] = {}
        self._game_directory = game_directory
        self._forge_files: ForgeStorage = {}  # storage for forge classes
        self._file_cache = FileCache(cache_megabytes)  # store raw data for files
        self._file_finder = FileFinder()  # find where a given file is stored

        if init:
            self.init()

    def init(self):
        """Load the forge file classes and metadata"""
        for _ in self.init_iter():
            pass

    def init_iter(self) -> Generator[Tuple[float, float], None, None]:
        """Load the forge file classes and metadata.
        Yields a float in the range 0.0 to 1.0 to give an indicator of progress."""
        memory_sum = 0
        for forge_file_path in glob.glob(os.path.join(self._game_directory, "*.forge")):
            forge_file = self.ForgeClass(self.GameIdentifier, forge_file_path)
            memory_sum += forge_file.file_size
            self._forge_files[forge_file.forge_name] = forge_file

        progress = 0
        for forge_name, forge in self.forge_files.items():
            forge_progress_step = forge.file_size / memory_sum  # the amount this forge file contributes to the whole loading.
            for forge_progress in forge.init_iter():
                yield progress + forge_progress * forge_progress_step, forge_progress
            log.info(f"Loaded {forge_name}")
            progress += forge_progress_step

        log.info("Populating file finder")
        for forge_file_name, forge_file in self.forge_files.items():
            for data_file_id, data_file in forge_file.data_files.items():
                self._file_finder.add_data_file(forge_file_name, data_file_id, data_file.file_ids)
        log.info("Finished populating file finder")

    @property
    def game_directory(self):
        return self._game_directory

    @property
    def forge_files(self) -> ForgeStorage:
        """A dictionary of forge file ids and the corresponding ForgeFile class."""
        return self._forge_files.copy()

    @property
    def forge_file_names(self) -> Tuple[ForgeFileName, ...]:
        """A tuple of forge file names contained within this game file."""
        return tuple(self._forge_files.keys())

    def get_forge_file(self, forge_file: ForgeFileName) -> "BaseForge":
        """Get the ForgeFile class for a given id.
        Will raise KeyError if the ForgeFile does not exist."""
        return self._forge_files[forge_file]

    @property
    def resource_types(self) -> KeysView[int]:
        """A dictionary mapping resource type to a prettier name"""
        # implement this in subclasses
        return self._file_readers.keys()

    def get_parser_name(self, resource_type: int) -> str:
        if resource_type in self._file_readers:
            return self._file_readers[resource_type].__class__.__name__
        else:
            return "No Parser Found"

    def find_file(
            self,
            file_id: FileIdentifier,
            forge_file: Optional[ForgeFileName] = None,
            data_file_id: Optional[DataFileIdentifier] = None
    ) -> Optional[
        Tuple[ForgeFileName, DataFileIdentifier]
    ]:
        """Find the forge file name and data file id for a given file id.
        Will return None if the file does not exist."""
        return self._file_finder.find(file_id, forge_file, data_file_id)

    def get_file_bytes(
            self,
            file_id: FileIdentifier,
            forge_file: Optional[ForgeFileName] = None,
            data_file_id: Optional[DataFileIdentifier] = None
    ) -> Optional[bytes]:
        """Get the binary representation of a given file id.
        Will return None if the file does not exist."""
        key = self.find_file(file_id, forge_file, data_file_id)
        if key is None:
            return
        else:
            forge_file, data_file_id = key
            if self._file_cache.contains(forge_file, data_file_id, file_id):
                return self._file_cache.get_file(forge_file, data_file_id, file_id)
            else:
                files = self.get_forge_file(forge_file).get_decompressed_files_bytes(data_file_id)
                self._file_cache.add_data_file(forge_file, data_file_id, files)
                return files[file_id]

    def get_file(
            self,
            file_id: FileIdentifier,
            forge_file: Optional[ForgeFileName] = None,
            data_file_id: Optional[DataFileIdentifier] = None,
            format_file_path: str = None
    ):
        """Get the python class representation of a given file id.
        Will return None if the file does not exist.
        May throw an exception if parsing the file failed."""
        file_bytes = self.get_file_bytes(file_id, forge_file, data_file_id)

        if isinstance(format_file_path, str):
            os.makedirs(os.path.dirname(format_file_path), exist_ok=True)
            f = open(format_file_path, 'w')
            file_wrapper = FileFormatDataWrapper(file_bytes, self, f)
        else:
            f = None
            file_wrapper = FileDataWrapper(file_bytes, self)

        try:
            try:
                file = self.read_main_file(file_wrapper)
            except Exception as e:
                file_wrapper.clever_format()
                raise e
            if file_wrapper.clever_format():
                raise FileNotExhaustedError("More of file remaining")
            return file
        except Exception as e:
            stack = " > ".join(f"{rt:08X}" for rt in file_wrapper.call_stack)
            log.error(f"Call Stack: {stack}  ---> reason ---> {e}")
            raise e
        finally:
            if f is not None:
                f.close()

    def read_main_file(self, file: FileDataWrapper) -> "BaseFile":
        assert file.read_uint_8() == 1, "Expected the first byte to be 1"
        return file.read_file()

    def read_header_file(self, file: FileDataWrapper) -> Union["BaseFile", int]:
        """Read a file with an extra byte before."""
        switch = file.read_uint_8()
        if switch == 0:
            return file.read_file()
        elif switch == 2:
            count = file.read_uint_32()
            raise NotImplementedError("Header switch == 2")  # might be nothing
        elif switch == 3:
            return 0
        else:
            raise NotImplementedError(f"Header switch == {switch}")

    def read_file_switch(self, file: FileDataWrapper) -> Union["BaseFile", int]:
        switch = file.read_uint_8()
        if switch == 0:
            return file.read_header_file()
        elif 1 <= switch <= 2:
            return file.read_file_id()
        elif switch == 3:
            return 0
        elif switch == 4:
            return file.read_header_file()
        elif switch == 5:
            return file.read_file_id()
        raise Exception("I am not quite sure what to do here.")

    def read_file(self, file: FileDataWrapper) -> "BaseFile":
        """Read a file id, resource type and the file payload and return the data packed into a class."""
        file_id = file.read_file_id()
        resource_type = file.read_resource_type()
        return self.read_file_data(file, file_id, resource_type)

    def read_file_data(self, file: FileDataWrapper, file_id: int, resource_type: int) -> "BaseFile":
        """Read the file payload for a given resource type."""
        file.call_stack.append(resource_type)
        if resource_type in self._file_readers:
            ret = self._file_readers[resource_type](file_id, file)
        else:
            raise FileParserNotFound(f"{resource_type:08X}")
        file.call_stack.pop()
        return ret
