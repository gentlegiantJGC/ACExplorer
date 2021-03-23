from pyUbiForge2.api.game import SubclassBaseFile
from .CumulativeBuffer import CumulativeBuffer as _CumulativeBuffer


class FloatCumulativeBuffer(SubclassBaseFile):
    ResourceType = 0xA1A81821
    ParentResourceType = _CumulativeBuffer.ResourceType
    parent: _CumulativeBuffer
