from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AccomplishmentAccumulator(SubclassBaseFile):
    ResourceType = 0xDD28B05B
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

