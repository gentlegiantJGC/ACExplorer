from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class FightManager(SubclassBaseFile):
    ResourceType = 0x4249F2BE
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent

