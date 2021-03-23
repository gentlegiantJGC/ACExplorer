from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ChildFXContainer(SubclassBaseFile):
    ResourceType = 0xCC48AB84
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
