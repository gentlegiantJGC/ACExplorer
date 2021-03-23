from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class VillaBuildingList(SubclassBaseFile):
    ResourceType = 0xE025A853
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
