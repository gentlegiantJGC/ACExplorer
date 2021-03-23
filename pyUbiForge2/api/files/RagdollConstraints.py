from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class RagdollConstraints(SubclassBaseFile):
    ResourceType = 0xC89F10F4
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
