from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class UIParams(SubclassBaseFile):
    ResourceType = 0x90D7B807
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

