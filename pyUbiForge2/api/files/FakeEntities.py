from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FakeEntities(SubclassBaseFile):
    ResourceType = 0xC69A7F31
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
