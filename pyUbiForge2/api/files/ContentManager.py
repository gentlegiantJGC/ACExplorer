from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ContentManager(SubclassBaseFile):
    ResourceType = 0x69F8F3D2
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

