from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Camera2(SubclassBaseFile):
    ResourceType = 0xA5396FF0
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
