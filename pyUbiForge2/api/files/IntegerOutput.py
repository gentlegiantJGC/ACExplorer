from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableOutput import LinkableOutput as _LinkableOutput


class IntegerOutput(SubclassBaseFile):
    ResourceType = 0x2C74BF29
    ParentResourceType = _LinkableOutput.ResourceType
    parent: _LinkableOutput

