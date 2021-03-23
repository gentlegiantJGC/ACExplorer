from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TerrainLayer(SubclassBaseFile):
    ResourceType = 0x9A6B1DAA
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
