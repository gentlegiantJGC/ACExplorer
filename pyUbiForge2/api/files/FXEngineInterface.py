from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FXEngineInterface(SubclassBaseFile):
    ResourceType = 0x95F6E970
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
