from typing import Dict, Tuple, Union, Sequence, Optional

from pyUbiForge2.api.data_types import (
    ForgeFileName,
    DataFileIdentifier,
    FileIdentifier,
    FileIdentifierTriplet,
    DataFileIdentifierDoublet,
)

FileLookupKeyType = Union[
                Tuple[None, None, FileIdentifier],
                Tuple[ForgeFileName, None, FileIdentifier],
                FileIdentifierTriplet,
            ]

FileLookupType = Dict[
            FileLookupKeyType,
            DataFileIdentifierDoublet
        ]


class FileFinder:
    """A class to help find the forge file and data file any given file is stored in."""
    def __init__(self):
        """A class to help find the forge file and data file any given file is stored in."""
        self._file_lookup: FileLookupType = {}

    def contains(
            self,
            file: FileIdentifier,
            forge_file: Optional[ForgeFileName] = None,
            data_file: Optional[DataFileIdentifier] = None
    ) -> bool:
        """Does the file exist."""
        return (forge_file, data_file, file) in self._file_lookup

    def add_data_file(
            self,
            forge_file: ForgeFileName,
            data_file: DataFileIdentifier,
            files: Sequence[FileIdentifier]
    ):
        """Populate the database for a data file and its files."""
        # if this key is already present the data file has been added before
        if (forge_file, data_file, data_file) not in self._file_lookup:
            data_file_key = (forge_file, data_file)
            for file in files:
                self._file_lookup[(None, None, file)] = data_file_key
                self._file_lookup[(forge_file, None, file)] = data_file_key
                self._file_lookup[(forge_file, data_file, file)] = data_file_key

    def find(
            self,
            file: FileIdentifier,
            forge_file: Optional[ForgeFileName] = None,
            data_file: Optional[DataFileIdentifier] = None
    ) -> Optional[
        Tuple[ForgeFileName, DataFileIdentifier]
    ]:
        """Returns the forge file and data file where a file can be found.
        None if the file cannot be found"""
        location = self._file_lookup.get((forge_file, data_file, file))
        if location is None:
            location = self._file_lookup.get((forge_file, None, file))
            if location is None:
                location = self._file_lookup.get((None, None, file))
        return location
