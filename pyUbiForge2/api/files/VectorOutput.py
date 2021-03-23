from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableOutput import LinkableOutput as _LinkableOutput


class VectorOutput(SubclassBaseFile):
    ResourceType = 0x1603ED4D
    ParentResourceType = _LinkableOutput.ResourceType
    parent: _LinkableOutput

