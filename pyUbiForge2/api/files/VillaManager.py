from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class VillaManager(SubclassBaseFile):
    ResourceType = 0x4632640E
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
