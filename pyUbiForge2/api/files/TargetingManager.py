from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class TargetingManager(SubclassBaseFile):
    ResourceType = 0x4615DF4F
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
