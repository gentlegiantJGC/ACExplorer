from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class WeaponHandSwitchEvent(SubclassBaseFile):
    ResourceType = 0xCE8C718B
    ParentResourceType = _Event.ResourceType
    parent: _Event

