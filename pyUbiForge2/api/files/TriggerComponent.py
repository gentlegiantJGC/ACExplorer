from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class TriggerComponent(SubclassBaseFile):
    ResourceType = 0xADF1D5E6
    ParentResourceType = _Component.ResourceType
    parent: _Component

