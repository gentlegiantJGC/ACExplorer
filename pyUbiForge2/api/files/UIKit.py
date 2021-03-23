from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class UIKit(SubclassBaseFile):
    ResourceType = 0x4F55A7FB
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
