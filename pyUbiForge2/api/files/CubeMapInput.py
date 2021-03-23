from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableInput import LinkableInput as _LinkableInput


class CubeMapInput(SubclassBaseFile):
    ResourceType = 0x3B0B3A1A
    ParentResourceType = _LinkableInput.ResourceType
    parent: _LinkableInput

