from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WangTiler(SubclassBaseFile):
    ResourceType = 0x4EF2FC5A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
