from pyUbiForge2.api.game import SubclassBaseFile
from .GroupManipulationDictionary import GroupManipulationDictionary as _GroupManipulationDictionary


class GcLGMDictionaryThief(SubclassBaseFile):
    ResourceType = 0x054DCA18
    ParentResourceType = _GroupManipulationDictionary.ResourceType
    parent: _GroupManipulationDictionary

