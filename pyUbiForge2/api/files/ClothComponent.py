from pyUbiForge2.api.game import SubclassBaseFile
from .SoftBodyComponent import SoftBodyComponent as _SoftBodyComponent


class ClothComponent(SubclassBaseFile):
    ResourceType = 0x8321699E
    ParentResourceType = _SoftBodyComponent.ResourceType
    parent: _SoftBodyComponent

