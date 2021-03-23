from pyUbiForge2.api.game import SubclassBaseFile
from .Visual import Visual as _Visual


class ClutterComponent(SubclassBaseFile):
    ResourceType = 0x2132CC6E
    ParentResourceType = _Visual.ResourceType
    parent: _Visual

