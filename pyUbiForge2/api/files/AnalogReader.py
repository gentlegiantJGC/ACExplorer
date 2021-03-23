from pyUbiForge2.api.game import SubclassBaseFile
from .InputReader import InputReader as _InputReader


class AnalogReader(SubclassBaseFile):
    ResourceType = 0x6B4870E5
    ParentResourceType = _InputReader.ResourceType
    parent: _InputReader

