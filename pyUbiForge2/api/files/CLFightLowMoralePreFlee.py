from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLFightLowMoralePreFlee(SubclassBaseFile):
    ResourceType = 0xD9C63B61
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
