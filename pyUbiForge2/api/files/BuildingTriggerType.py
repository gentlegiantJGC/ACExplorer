from pyUbiForge2.api.game import SubclassBaseFile
from .TriggerType import TriggerType as _TriggerType


class BuildingTriggerType(SubclassBaseFile):
    ResourceType = 0x88A7457D
    ParentResourceType = _TriggerType.ResourceType
    parent: _TriggerType
