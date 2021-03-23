from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class GraphicObject(SubclassBaseFile):
    ResourceType = 0xEC6AC357
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

