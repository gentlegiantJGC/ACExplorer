from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoundAmbienceSet(SubclassBaseFile):
    ResourceType = 0x3CFD0BBB
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

