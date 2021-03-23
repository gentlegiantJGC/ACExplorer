from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WorldAmbiance(SubclassBaseFile):
    ResourceType = 0x21C2D472
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

