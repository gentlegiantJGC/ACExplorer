from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AITask(SubclassBaseFile):
    ResourceType = 0xF32DE955
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
