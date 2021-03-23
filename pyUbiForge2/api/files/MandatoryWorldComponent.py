from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class MandatoryWorldComponent(SubclassBaseFile):
    ResourceType = 0x87DB1FB6
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

