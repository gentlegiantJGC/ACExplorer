from pyUbiForge2.api.game import SubclassBaseFile
from .GliderControlEvent import GliderControlEvent as _GliderControlEvent


class GliderControlDoScratchEvent(SubclassBaseFile):
    ResourceType = 0xD5B572AF
    ParentResourceType = _GliderControlEvent.ResourceType
    parent: _GliderControlEvent

