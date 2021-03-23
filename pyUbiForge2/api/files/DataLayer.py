from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class DataLayer(SubclassBaseFile):
    ResourceType = 0x41813744
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
