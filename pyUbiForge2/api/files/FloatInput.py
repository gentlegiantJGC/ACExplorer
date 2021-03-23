from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableInput import LinkableInput as _LinkableInput


class FloatInput(SubclassBaseFile):
    ResourceType = 0xA10B3D7E
    ParentResourceType = _LinkableInput.ResourceType
    parent: _LinkableInput
