from pyUbiForge2.api.game import SubclassBaseFile
from .GliderControlEvent import GliderControlEvent as _GliderControlEvent


class GliderControlDoFlyEvent(SubclassBaseFile):
    ResourceType = 0x1FE4B1B9
    ParentResourceType = _GliderControlEvent.ResourceType
    parent: _GliderControlEvent

