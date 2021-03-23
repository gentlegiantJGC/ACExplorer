from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class SoundPropagationMap(SubclassBaseFile):
    ResourceType = 0x97FCF21E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

