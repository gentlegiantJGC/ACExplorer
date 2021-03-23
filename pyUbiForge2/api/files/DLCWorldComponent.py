from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class DLCWorldComponent(SubclassBaseFile):
    ResourceType = 0xB98B6142
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
