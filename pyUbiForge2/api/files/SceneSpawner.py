from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SceneSpawner(SubclassBaseFile):
    ResourceType = 0x6D0FD49C
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
