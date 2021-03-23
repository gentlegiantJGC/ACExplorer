from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableInput import LinkableInput as _LinkableInput


class IntegerInput(SubclassBaseFile):
    ResourceType = 0xA76A9BDD
    ParentResourceType = _LinkableInput.ResourceType
    parent: _LinkableInput
