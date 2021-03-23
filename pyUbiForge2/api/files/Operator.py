from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Operator(SubclassBaseFile):
    ResourceType = 0x2ED0C5D7
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

