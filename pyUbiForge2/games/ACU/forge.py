from typing import Tuple, Dict, Optional

from pyUbiForge2.api import BaseForge
from pyUbiForge2.api.data_types import (
    DataFileMetadata,
    DataFileByteLocations,
    DataFileIdentifier,
    FileIdentifier,
    FileResourceType,
    FileName,
)


class ACUForge(BaseForge):
    GameIdentifier = "ACU"

    def __init__(self, path: str):
        super().__init__(path)

    def _parse_forge(self) -> Tuple[
        DataFileMetadata,
        DataFileByteLocations
    ]:
        pass

    def decompress_data_file(self, data_file_id: DataFileIdentifier, metadata_only=False) -> Dict[
        FileIdentifier,
        Tuple[
            FileResourceType,
            FileName,
            Optional[bytes]
        ]
    ]:
        pass
