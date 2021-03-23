from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class EagleVisionManager(SubclassBaseFile):
    ResourceType = 0xBECAA0EC
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
