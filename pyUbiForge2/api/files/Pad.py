from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Pad(SubclassBaseFile):
    ResourceType = 0xA5C40805
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
