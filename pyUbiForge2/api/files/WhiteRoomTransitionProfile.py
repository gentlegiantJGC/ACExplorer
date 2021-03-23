from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WhiteRoomTransitionProfile(SubclassBaseFile):
    ResourceType = 0x1756B2BA
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
