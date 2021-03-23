from pyUbiForge2.api.game import SubclassBaseFile
from .GliderControlEvent import GliderControlEvent as _GliderControlEvent


class GliderControlDoCrashEvent(SubclassBaseFile):
    ResourceType = 0xF23C7A75
    ParentResourceType = _GliderControlEvent.ResourceType
    parent: _GliderControlEvent

