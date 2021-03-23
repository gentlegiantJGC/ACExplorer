from pyUbiForge2.api.game import SubclassBaseFile
from .AnimSetLayer import AnimSetLayer as _AnimSetLayer


class AIAnimSetLayer(SubclassBaseFile):
    ResourceType = 0x6F03DA58
    ParentResourceType = _AnimSetLayer.ResourceType
    parent: _AnimSetLayer
