from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableInput import LinkableInput as _LinkableInput


class QuaternionInput(SubclassBaseFile):
    ResourceType = 0x62A56ED4
    ParentResourceType = _LinkableInput.ResourceType
    parent: _LinkableInput

