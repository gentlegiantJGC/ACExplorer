from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CLDazedBySmoke(SubclassBaseFile):
    ResourceType = 0x7B49300B
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract

