from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class RagdollNew(SubclassBaseFile):
    ResourceType = 0xC8DBDE7F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

