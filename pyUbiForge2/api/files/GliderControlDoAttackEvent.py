from pyUbiForge2.api.game import SubclassBaseFile
from .GliderControlEvent import GliderControlEvent as _GliderControlEvent


class GliderControlDoAttackEvent(SubclassBaseFile):
    ResourceType = 0x0FB8042E
    ParentResourceType = _GliderControlEvent.ResourceType
    parent: _GliderControlEvent
