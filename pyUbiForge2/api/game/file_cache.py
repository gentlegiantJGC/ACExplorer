from typing import Dict
from typing import OrderedDict as OrderedDictType
from collections import OrderedDict

from pyUbiForge2.api.data_types import ForgeFileName, DataFileIdentifier, FileIdentifier, FileIdentifierTriplet


class FileCache:
    """A class to hold decompressed file data and handle unloading it when memory goes above a limit."""
    def __init__(self, cache_megabytes: int = 1000):
        """A class to hold decompressed file data and handle unloading it when memory goes above a limit."""
        self._cache_size_limit = cache_megabytes * 1_000_000
        self._cache_size = 0
        self._cache: OrderedDictType[
            FileIdentifierTriplet,
            bytes
        ] = OrderedDict()

    def add_data_file(
            self,
            forge_file: ForgeFileName,
            data_file_id: DataFileIdentifier,
            files: Dict[FileIdentifier, bytes]
    ):
        """Add all the files contained in a datafile to the cache."""
        for file_id, file in files.items():
            file_triplet = (forge_file, data_file_id, file_id)
            if file_triplet in self._cache:
                self._cache.move_to_end(file_triplet)
            else:
                self._cache[file_triplet] = file
                self._cache_size += len(file)

        if self._cache_size > self._cache_size_limit:
            for _ in range(len(self._cache)//4):
                file_triplet, file = self._cache.popitem(False)
                self._cache_size -= len(file)

    def contains(
            self,
            forge_file: ForgeFileName,
            data_file_id: DataFileIdentifier,
            file_id: FileIdentifier
    ) -> bool:
        """Does the file exist in the cache."""
        return (forge_file, data_file_id, file_id) in self._cache

    def get_file(
            self,
            forge_file: ForgeFileName,
            data_file_id: DataFileIdentifier,
            file_id: FileIdentifier
    ):
        """Get the binary data for a file.
        Use .contains to check if it exists in cache first."""
        return self._cache[(forge_file, data_file_id, file_id)]
