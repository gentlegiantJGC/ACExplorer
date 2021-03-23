from pyUbiForge2.api.game import SubclassBaseFile
from .EagleVisionComponent import EagleVisionComponent as _EagleVisionComponent


class GlyphComponent(SubclassBaseFile):
    ResourceType = 0xC971DD1B
    ParentResourceType = _EagleVisionComponent.ResourceType
    parent: _EagleVisionComponent
