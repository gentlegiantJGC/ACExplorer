from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class VillaBuildingComponent(SubclassBaseFile):
    ResourceType = 0xC681FDB3
    ParentResourceType = _Component.ResourceType
    parent: _Component
