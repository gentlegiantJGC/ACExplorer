from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AccomplishmentLookUpTable(SubclassBaseFile):
    ResourceType = 0x69C04DD8
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

