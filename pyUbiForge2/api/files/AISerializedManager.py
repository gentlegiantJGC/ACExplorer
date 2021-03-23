from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AISerializedManager(SubclassBaseFile):
    ResourceType = 0x0AC71715
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

