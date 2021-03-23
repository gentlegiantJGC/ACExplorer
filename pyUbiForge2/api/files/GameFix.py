from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GameFix(SubclassBaseFile):
    ResourceType = 0x2CC42429
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
