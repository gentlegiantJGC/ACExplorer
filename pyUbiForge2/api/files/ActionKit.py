from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ActionKit(SubclassBaseFile):
    ResourceType = 0x195B695E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
