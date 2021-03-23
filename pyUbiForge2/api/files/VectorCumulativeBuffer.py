from pyUbiForge2.api.game import SubclassBaseFile
from .CumulativeBuffer import CumulativeBuffer as _CumulativeBuffer


class VectorCumulativeBuffer(SubclassBaseFile):
    ResourceType = 0xCE288DF1
    ParentResourceType = _CumulativeBuffer.ResourceType
    parent: _CumulativeBuffer
