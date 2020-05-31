from typing import Dict, Tuple

from pyUbiForge2.api.data_types import ForgeFileName, DataFileIdentifier, FileIdentifier, FileIdentifierTriplet

from .history_manager import HistoryManager


class FileCache:
    """A class to hold decompressed file data and handle unloading it when memory goes above a limit."""
    def __init__(self):
        """A class to hold decompressed file data and handle unloading it when memory goes above a limit."""
        self._history_manager = HistoryManager()
        self._cache: Dict[
            FileIdentifierTriplet,
            bytes
        ] = {}

    def add_data_file(self, forge_file: ForgeFileName, data_file_id: DataFileIdentifier, files: Dict[FileIdentifier, bytes]):
        for file_id, file in files.items():
            self._cache.setdefault((forge_file, data_file_id, file_id), file)

    def get_file(self, ):
