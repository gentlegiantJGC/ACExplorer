from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SpatialTopology(SubclassBaseFile):
    ResourceType = 0x7456EEC9
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

