from pyUbiForge2.api.game import SubclassBaseFile
from .TriggerComponent import TriggerComponent as _TriggerComponent


class CameraZone(SubclassBaseFile):
    ResourceType = 0x8C5AD508
    ParentResourceType = _TriggerComponent.ResourceType
    parent: _TriggerComponent
