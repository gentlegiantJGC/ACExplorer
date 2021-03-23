from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableOutput import LinkableOutput as _LinkableOutput


class FloatOutput(SubclassBaseFile):
    ResourceType = 0x63AD2CDD
    ParentResourceType = _LinkableOutput.ResourceType
    parent: _LinkableOutput
