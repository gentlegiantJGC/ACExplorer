from typing import Generator, Tuple, Optional
import glob
import os

from pyUbiForge2.api.game.forge import BaseForge
from pyUbiForge2.api.game.cache import FileCache
from pyUbiForge2.api.game.file_finder import FileFinder
from pyUbiForge2.api.data_types import (
    ForgeStorage,
    ForgeFileName,
    DataFileIdentifier,
    FileIdentifier,
)


class BaseGame:
    ForgeClass = BaseForge
    GameIdentifier = None

    def __init__(self, game_directory: str, cache_megabytes: int = 1000):
        if self.__class__ is BaseGame:
            raise Exception("BaseGame must be subclassed")
        if self.GameIdentifier is None:
            raise Exception(f"GameIdentifier has not been set in {self.__class__.__name__}")
        if self.ForgeClass is BaseForge:
            raise Exception("ForgeClass attribute has not been overwritten.")
        if self.GameIdentifier != self.ForgeClass.GameIdentifier:
            raise Exception("ForgeClass game identifier does not match Game game identifier")
        self._game_directory = game_directory
        self._forge_files: ForgeStorage = {}  # storage for forge classes
        self._file_cache = FileCache()  # store raw data for files
        self._file_finder = FileFinder()  # find where a given file is stored

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
            progress += forge_progress_step

    @property
    def game_directory(self):
        return self._game_directory

    @property
    def forge_files(self) -> ForgeStorage:
        """A dictionary of forge file ids and the corresponding ForgeFile class."""
        return self._forge_files

    @property
    def forge_file_ids(self) -> Tuple[ForgeFileName, ...]:
        """A tuple of forge file ids contained within this forge file."""
        return tuple(self._forge_files.keys())

    def get_forge_file(self, forge_file: ForgeFileName) -> BaseForge:
        """Get the ForgeFile class for a given id.
        Will raise KeyError if the ForgeFile does not exist."""
        return self._forge_files[forge_file]

    def get_file(
            self,
            file_id: FileIdentifier,
            forge_file: Optional[ForgeFileName] = None,
            data_file_id: Optional[DataFileIdentifier] = None
    ):
        pass


