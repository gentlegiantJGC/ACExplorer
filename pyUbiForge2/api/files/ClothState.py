from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBodyState import SoftBodyState as _SoftBodyState


class ClothState(SubclassBaseFile):
    ResourceType = 0x7D6B679F
    ParentResourceType = _SoftBodyState.ResourceType
    parent: _SoftBodyState

