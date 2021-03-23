from pyUbiForge2.api.game import SubclassBaseFile
from .GroupManipulationDictionary import (
    GroupManipulationDictionary as _GroupManipulationDictionary,
)


class GcLGMDictionaryCourtesan(SubclassBaseFile):
    ResourceType = 0xF7269766
    ParentResourceType = _GroupManipulationDictionary.ResourceType
    parent: _GroupManipulationDictionary
