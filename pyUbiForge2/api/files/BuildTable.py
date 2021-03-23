from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class BuildTable(SubclassBaseFile):
    ResourceType = 0x22ECBE63
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
