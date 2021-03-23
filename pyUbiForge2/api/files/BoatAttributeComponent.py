from pyUbiForge2.api.game import SubclassBaseFile
from .GuidanceBuilderComponent import (
    GuidanceBuilderComponent as _GuidanceBuilderComponent,
)


class BoatAttributeComponent(SubclassBaseFile):
    ResourceType = 0xFBDE5036
    ParentResourceType = _GuidanceBuilderComponent.ResourceType
    parent: _GuidanceBuilderComponent
