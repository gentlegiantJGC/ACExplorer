from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Component(SubclassBaseFile):
    ResourceType = 0xCB0F23F4
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

