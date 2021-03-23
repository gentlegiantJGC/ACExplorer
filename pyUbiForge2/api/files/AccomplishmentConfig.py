from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AccomplishmentConfig(SubclassBaseFile):
    ResourceType = 0x022F146B
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

