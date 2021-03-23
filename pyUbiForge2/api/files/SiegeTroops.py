from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class SiegeTroops(SubclassBaseFile):
    ResourceType = 0x608DE00E
    ParentResourceType = _Component.ResourceType
    parent: _Component
