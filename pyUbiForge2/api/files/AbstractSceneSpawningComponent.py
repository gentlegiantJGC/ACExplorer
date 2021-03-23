from pyUbiForge2.api.game import SubclassBaseFile
from .Component import Component as _Component


class AbstractSceneSpawningComponent(SubclassBaseFile):
    ResourceType = 0xA80A0435
    ParentResourceType = _Component.ResourceType
    parent: _Component
