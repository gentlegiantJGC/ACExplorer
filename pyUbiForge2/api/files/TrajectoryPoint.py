from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class TrajectoryPoint(SubclassBaseFile):
    ResourceType = 0x917C611D
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

