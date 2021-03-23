from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class World(SubclassBaseFile):
    ResourceType = 0xFBB63E47
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
