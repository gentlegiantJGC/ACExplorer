from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class LookAtDataGeneral(SubclassBaseFile):
    ResourceType = 0x515C31CD
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

