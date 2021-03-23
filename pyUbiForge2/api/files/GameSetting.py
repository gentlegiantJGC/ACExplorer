from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GameSetting(SubclassBaseFile):
    ResourceType = 0x52534498
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
