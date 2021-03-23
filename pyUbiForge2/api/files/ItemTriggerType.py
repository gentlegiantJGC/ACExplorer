from pyUbiForge2.api.game import SubclassBaseFile
from .TriggerType import TriggerType as _TriggerType


class ItemTriggerType(SubclassBaseFile):
    ResourceType = 0xB51F4A78
    ParentResourceType = _TriggerType.ResourceType
    parent: _TriggerType

