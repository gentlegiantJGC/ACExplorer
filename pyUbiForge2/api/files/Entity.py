from pyUbiForge2.api.game import SubclassBaseFile
from .BaseEntity import BaseEntity as _BaseEntity


class Entity(SubclassBaseFile):
    ResourceType = 0x0984415E
    ParentResourceType = _BaseEntity.ResourceType
    parent: _BaseEntity

