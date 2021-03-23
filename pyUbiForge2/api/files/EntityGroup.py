from pyUbiForge2.api.game import SubclassBaseFile
from .Entity import Entity as _Entity


class EntityGroup(SubclassBaseFile):
    ResourceType = 0x3F742D26
    ParentResourceType = _Entity.ResourceType
    parent: _Entity

