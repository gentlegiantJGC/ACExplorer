from pyUbiForge2.api.game import SubclassBaseFile
from .AnalogReader import AnalogReader as _AnalogReader


class PadAnalogStickAxisReader(SubclassBaseFile):
    ResourceType = 0x8810C129
    ParentResourceType = _AnalogReader.ResourceType
    parent: _AnalogReader
