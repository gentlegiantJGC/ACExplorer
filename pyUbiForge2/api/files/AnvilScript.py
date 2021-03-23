from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AnvilScript(SubclassBaseFile):
    ResourceType = 0x198B47F1
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
