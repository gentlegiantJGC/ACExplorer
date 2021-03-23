from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CustomOperatorDefinition(SubclassBaseFile):
    ResourceType = 0x3153E6F5
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
