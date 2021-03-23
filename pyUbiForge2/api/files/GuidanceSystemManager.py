from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GuidanceSystemManager(SubclassBaseFile):
    ResourceType = 0xB775F71D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

