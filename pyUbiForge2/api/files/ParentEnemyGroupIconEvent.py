from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class ParentEnemyGroupIconEvent(SubclassBaseFile):
    ResourceType = 0x48B48D27
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent
