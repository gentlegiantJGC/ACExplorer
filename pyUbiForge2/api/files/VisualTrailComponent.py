from pyUbiForge2.api.game import SubclassBaseFile
from .Visual import Visual as _Visual


class VisualTrailComponent(SubclassBaseFile):
    ResourceType = 0x52AD4779
    ParentResourceType = _Visual.ResourceType
    parent: _Visual
