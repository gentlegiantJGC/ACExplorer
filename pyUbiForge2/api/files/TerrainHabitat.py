from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TerrainHabitat(SubclassBaseFile):
    ResourceType = 0xF09D1E67
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

