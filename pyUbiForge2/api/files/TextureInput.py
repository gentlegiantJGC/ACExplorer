from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableInput import LinkableInput as _LinkableInput


class TextureInput(SubclassBaseFile):
    ResourceType = 0x354FE002
    ParentResourceType = _LinkableInput.ResourceType
    parent: _LinkableInput
