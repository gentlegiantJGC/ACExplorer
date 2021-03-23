from pyUbiForge2.api.game import SubclassBaseFile
from .UniverseComponent import UniverseComponent as _UniverseComponent


class FightStrategyManager(SubclassBaseFile):
    ResourceType = 0x5977F59D
    ParentResourceType = _UniverseComponent.ResourceType
    parent: _UniverseComponent
