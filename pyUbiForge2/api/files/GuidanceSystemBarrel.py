from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceSystemComponent import GuidanceSystemComponent as _GuidanceSystemComponent


class GuidanceSystemBarrel(SubclassBaseFile):
    ResourceType = 0x79D2CBD7
    ParentResourceType = _GuidanceSystemComponent.ResourceType
    parent: _GuidanceSystemComponent
