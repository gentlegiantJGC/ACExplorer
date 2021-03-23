from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AssassinTool2(SubclassBaseFile):
    ResourceType = 0x4EBD7F03
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

