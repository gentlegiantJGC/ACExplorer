from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AccomplishmentOutputWrapper(SubclassBaseFile):
    ResourceType = 0x5A3BC3A9
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

