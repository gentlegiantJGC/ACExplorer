from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class LiteRagdoll(SubclassBaseFile):
    ResourceType = 0x891043D5
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
