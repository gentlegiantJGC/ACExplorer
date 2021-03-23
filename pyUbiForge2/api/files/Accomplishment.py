from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class Accomplishment(SubclassBaseFile):
    ResourceType = 0x60B663FB
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

