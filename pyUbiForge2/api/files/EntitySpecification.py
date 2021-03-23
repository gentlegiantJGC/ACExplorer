from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class EntitySpecification(SubclassBaseFile):
    ResourceType = 0xDEC6FCE6
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

