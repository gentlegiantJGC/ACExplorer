from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AccomplishmentManager(SubclassBaseFile):
    ResourceType = 0x79210545
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

