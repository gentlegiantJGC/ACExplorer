from pyUbiForge2.api.game import SubclassBaseFile
from .GroupManipulationDictionary import GroupManipulationDictionary as _GroupManipulationDictionary


class GcLGMDictionaryMercenary(SubclassBaseFile):
    ResourceType = 0xD41635F4
    ParentResourceType = _GroupManipulationDictionary.ResourceType
    parent: _GroupManipulationDictionary

