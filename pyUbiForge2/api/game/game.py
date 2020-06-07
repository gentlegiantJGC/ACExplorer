from typing import Generator, Tuple, Optional, Dict, TYPE_CHECKING, Type
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

if TYPE_CHECKING:
    from pyUbiForge2.api.game import BaseFile
    from pyUbiForge2.api.game import BaseForge


class BaseGame:
    ForgeClass: Type["BaseForge"] = None
    GameIdentifier: str = None
    FileIDType: str = None
    ResourceType: str = None
    endianness = "<"

    def __init__(self, game_directory: str, cache_megabytes: int = 1000, init=True):
        if self.__class__ is BaseGame:
            raise Exception("BaseGame must be subclassed")
        for attr, attr_name in (
                (self.GameIdentifier, "GameIdentifier"),
                (self.FileIDType, "FileIDType"),
                (self.ResourceType, "ResourceType")
        ):
            if attr is None:
                raise Exception(f"{attr_name} has not been set in {self.__class__.__name__}")
        if self.ForgeClass is None:
            raise Exception("ForgeClass attribute has not been overwritten.")
        if self.GameIdentifier != self.ForgeClass.GameIdentifier:
            raise Exception("ForgeClass game identifier does not match Game game identifier")
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
            forge_file = self.ForgeClass(forge_file_path)
            memory_sum += forge_file.file_size
            self._forge_files[forge_file.forge_name] = forge_file

        progress = 0
        for forge_name, forge in self.forge_files.items():
            forge_progress_step = forge.file_size / memory_sum  # the amount this forge file contributes to the whole loading.
            for forge_progress in forge.init_iter():
                yield progress + forge_progress * forge_progress_step, forge_progress
            log.info(f"Loaded {forge_name}")
            progress += forge_progress_step

        # TODO: populate file finder

    @property
    def game_directory(self):
        return self._game_directory

    @property
    def forge_files(self) -> ForgeStorage:
        """A dictionary of forge file ids and the corresponding ForgeFile class."""
        return self._forge_files

    @property
    def forge_file_names(self) -> Tuple[ForgeFileName, ...]:
        """A tuple of forge file names contained within this game file."""
        return tuple(self._forge_files.keys())

    def get_forge_file(self, forge_file: ForgeFileName) -> "BaseForge":
        """Get the ForgeFile class for a given id.
        Will raise KeyError if the ForgeFile does not exist."""
        return self._forge_files[forge_file]

    @property
    def file_types(self) -> Dict[int, str]:
        """A dictionary mapping resource type to a prettier name"""
        # implement this in subclasses
        return {}

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
        file = self.get_file_bytes(file_id, forge_file, data_file_id)
        if isinstance(format_file_path, str):
            os.makedirs(os.path.dirname(format_file_path), exist_ok=True)
            with open(format_file_path, 'w') as f:
                file_wrapper = FileFormatDataWrapper(file, self, f)
                return self.read_file(file_wrapper)
        else:
            file_wrapper = FileDataWrapper(file, self)
            return self.read_file(file_wrapper)

    def read_file(self, file: FileDataWrapper) -> "BaseFile":
        """Read a file id, resource type and the file payload and return the data packed into a class."""
        raise NotImplementedError
