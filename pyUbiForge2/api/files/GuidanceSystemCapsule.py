from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceSystemComponent import GuidanceSystemComponent as _GuidanceSystemComponent


class GuidanceSystemCapsule(SubclassBaseFile):
    ResourceType = 0x8F397327
    ParentResourceType = _GuidanceSystemComponent.ResourceType
    parent: _GuidanceSystemComponent
