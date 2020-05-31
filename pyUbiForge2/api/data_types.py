from typing import Tuple, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .game.forge import BaseForge
    from .game.data_file import DataFile

ForgeFileName = str
DataFileIdentifier = FileIdentifier = int
DataFileResource = FileResource = int
DataFileName = FileName = str

DataFileIdentifierDoublet = Tuple[ForgeFileName, DataFileIdentifier]
FileIdentifierTriplet = Tuple[ForgeFileName, DataFileIdentifier, FileIdentifier]

ForgeStorage = Dict[
    ForgeFileName,
    "BaseForge"
]
DataFileStorage = Dict[
    DataFileIdentifier,
    "DataFile"
]


SerialisedMetadata = Dict[
    DataFileIdentifier,
    Tuple[
        DataFileResource,
        DataFileName,
        Tuple[
            Tuple[
                FileIdentifier,
                FileResource,
                FileName
            ], ...
        ]
    ]
]
