from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TerrainTile(SubclassBaseFile):
    ResourceType = 0x77CFA409
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
