from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AIAction(SubclassBaseFile):
    ResourceType = 0xA02405B7
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
