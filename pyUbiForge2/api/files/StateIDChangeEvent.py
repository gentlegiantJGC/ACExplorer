from pyUbiForge2.api.game import SubclassBaseFile
from .StateChangeOccuredEvent import StateChangeOccuredEvent as _StateChangeOccuredEvent


class StateIDChangeEvent(SubclassBaseFile):
    ResourceType = 0x3D83A082
    ParentResourceType = _StateChangeOccuredEvent.ResourceType
    parent: _StateChangeOccuredEvent
