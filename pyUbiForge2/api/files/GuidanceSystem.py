from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceSystemComponent import GuidanceSystemComponent as _GuidanceSystemComponent


class GuidanceSystem(SubclassBaseFile):
    ResourceType = 0x55AF1C3E
    ParentResourceType = _GuidanceSystemComponent.ResourceType
    parent: _GuidanceSystemComponent
