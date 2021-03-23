from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ClassInfos(SubclassBaseFile):
    ResourceType = 0x890EE9ED
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
