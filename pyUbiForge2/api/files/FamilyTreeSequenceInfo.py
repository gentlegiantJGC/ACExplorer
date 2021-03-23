from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FamilyTreeSequenceInfo(SubclassBaseFile):
    ResourceType = 0x88C9C903
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

