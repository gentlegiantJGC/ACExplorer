from pyUbiForge2.api.game import SubclassBaseFile
from .CumulativeBuffer import CumulativeBuffer as _CumulativeBuffer


class IntegerCumulativeBuffer(SubclassBaseFile):
    ResourceType = 0xE006229E
    ParentResourceType = _CumulativeBuffer.ResourceType
    parent: _CumulativeBuffer
