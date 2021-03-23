from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AbstractAIEntityGroup(SubclassBaseFile):
    ResourceType = 0xC8AEE147
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

