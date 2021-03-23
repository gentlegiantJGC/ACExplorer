from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class VillaBuildingSettings(SubclassBaseFile):
    ResourceType = 0xFF87BB19
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

