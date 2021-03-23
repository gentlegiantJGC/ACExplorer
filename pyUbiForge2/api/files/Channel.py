from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Channel(SubclassBaseFile):
    ResourceType = 0x6D44B7DB
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
