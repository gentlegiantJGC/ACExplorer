from pyUbiForge2.api.game import SubclassBaseFile
from .MandatoryWorldComponent import MandatoryWorldComponent as _MandatoryWorldComponent


class NavigationManager(SubclassBaseFile):
    ResourceType = 0x09B9C3F3
    ParentResourceType = _MandatoryWorldComponent.ResourceType
    parent: _MandatoryWorldComponent
