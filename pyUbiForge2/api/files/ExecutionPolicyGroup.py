from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ExecutionPolicyGroup(SubclassBaseFile):
    ResourceType = 0x71033E8A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

