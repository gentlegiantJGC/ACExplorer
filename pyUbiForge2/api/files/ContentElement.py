from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class ContentElement(SubclassBaseFile):
    ResourceType = 0xD29C8852
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
