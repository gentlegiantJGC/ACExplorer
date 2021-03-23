from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FamilyTreeStepInfo(SubclassBaseFile):
    ResourceType = 0x2834D40F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

