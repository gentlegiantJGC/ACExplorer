from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GenericObject(SubclassBaseFile):
    ResourceType = 0xFF7BB1A1
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

