from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class CollectibleComponent(SubclassBaseFile):
    ResourceType = 0x4EC96943
    ParentResourceType = _Component.ResourceType
    parent: _Component

