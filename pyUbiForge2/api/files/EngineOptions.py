from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class EngineOptions(SubclassBaseFile):
    ResourceType = 0xB4E69FA1
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

