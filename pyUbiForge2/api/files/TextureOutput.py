from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableOutput import LinkableOutput as _LinkableOutput


class TextureOutput(SubclassBaseFile):
    ResourceType = 0x3A8A5517
    ParentResourceType = _LinkableOutput.ResourceType
    parent: _LinkableOutput

