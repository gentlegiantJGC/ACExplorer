from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLTargetReactToCommotion(SubclassBaseFile):
    ResourceType = 0x38112A0A
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

