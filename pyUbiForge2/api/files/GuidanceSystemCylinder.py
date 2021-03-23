from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceSystemComponent import GuidanceSystemComponent as _GuidanceSystemComponent


class GuidanceSystemCylinder(SubclassBaseFile):
    ResourceType = 0x4AF26DC9
    ParentResourceType = _GuidanceSystemComponent.ResourceType
    parent: _GuidanceSystemComponent
