from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableInput import LinkableInput as _LinkableInput


class VectorInput(SubclassBaseFile):
    ResourceType = 0x656931BC
    ParentResourceType = _LinkableInput.ResourceType
    parent: _LinkableInput
