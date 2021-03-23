from pyUbiForge2.api.game import SubclassBaseFile
from .TriggerComponent import TriggerComponent as _TriggerComponent


class AC2CameraReachHighPointZone(SubclassBaseFile):
    ResourceType = 0x6319DCF7
    ParentResourceType = _TriggerComponent.ResourceType
    parent: _TriggerComponent
