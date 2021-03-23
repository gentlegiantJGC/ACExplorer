from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WorldDataLayerManager(SubclassBaseFile):
    ResourceType = 0xECEF6DDB
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
