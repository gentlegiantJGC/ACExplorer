from pyUbiForge2.api.game import SubclassBaseFile
from .UIEvent import UIEvent as _UIEvent


class MissionStateSetConstraintUIEvent(SubclassBaseFile):
    ResourceType = 0x2F41D879
    ParentResourceType = _UIEvent.ResourceType
    parent: _UIEvent

