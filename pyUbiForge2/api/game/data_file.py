from typing import Tuple
from dataclasses import dataclass

from pyUbiForge2.api.data_types import (
    DataFileIdentifier,
    DataFileResourceType,
    DataFileName,
    FileStorage
)


@dataclass
class DataFile:
    id: DataFileIdentifier
    resource_type: DataFileResourceType
    name: DataFileName
    files: FileStorage

