from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXSpawnedEntity(SubclassBaseFile):
    ResourceType = 0xF5500873
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement
