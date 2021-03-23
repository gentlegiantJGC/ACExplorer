from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableOutput import LinkableOutput as _LinkableOutput


class CubeMapOutput(SubclassBaseFile):
    ResourceType = 0x29E8899B
    ParentResourceType = _LinkableOutput.ResourceType
    parent: _LinkableOutput
