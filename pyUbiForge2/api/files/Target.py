from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Target(SubclassBaseFile):
    ResourceType = 0x1AC52ADE
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

