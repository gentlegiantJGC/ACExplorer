from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLShock(SubclassBaseFile):
    ResourceType = 0xC60F1CD3
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
