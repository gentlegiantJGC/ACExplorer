from typing import Tuple, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .game.forge import BaseForge
    from .game.data_file import DataFile

ForgeFileName = str  # the name of the forge file without the .forge extension
DataFileIdentifier = FileIdentifier = int  # the id "unique" to that file / data file
DataFileResourceType = (
    FileResourceType
) = int  # the resource type of the file / data file
DataFileName = FileName = str  # the name of the file / data file

DataFileIdentifierDoublet = Tuple[ForgeFileName, DataFileIdentifier]
FileIdentifierTriplet = Tuple[ForgeFileName, DataFileIdentifier, FileIdentifier]

ForgeStorage = Dict[ForgeFileName, "BaseForge"]
DataFileStorage = Dict[DataFileIdentifier, "DataFile"]
FileMetadata = Tuple[FileResourceType, FileName]
FileStorage = Dict[FileIdentifier, FileMetadata]
SerialisedDataFile = Tuple[DataFileResourceType, DataFileName, FileStorage]
SerialisedMetadata = Dict[DataFileIdentifier, SerialisedDataFile]

DataFileMetadata = Dict[DataFileIdentifier, Tuple[DataFileResourceType, DataFileName]]
DataFileByteLocations = Dict[
    DataFileIdentifier, Tuple[int, int]  # start byte  # length
]
