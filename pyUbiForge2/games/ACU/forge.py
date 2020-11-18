from typing import Tuple, Dict, List
import struct
import numpy
from io import BytesIO

from pyUbiForge2.api import BaseForge
from pyUbiForge2.api.data_types import (
    FileIdentifier,
    FileResourceType,
    FileName,
)
from pyUbiForge2.util.compression import decompress


class ACUForge(BaseForge):
    NonContainerDataFiles = {16, 145}
