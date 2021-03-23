from pyUbiForge2.api.game import SubclassBaseFile
from .ESAbstract import ESAbstract as _ESAbstract


class OSAbstract(SubclassBaseFile):
    ResourceType = 0x2E85AB76
    ParentResourceType = _ESAbstract.ResourceType
    parent: _ESAbstract

