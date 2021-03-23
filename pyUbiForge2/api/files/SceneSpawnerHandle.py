from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SceneSpawnerHandle(SubclassBaseFile):
    ResourceType = 0x9891626B
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
