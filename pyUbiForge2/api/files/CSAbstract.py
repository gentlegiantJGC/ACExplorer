from pyUbiForge2.api.game import SubclassBaseFile
from .ESAbstract import ESAbstract as _ESAbstract


class CSAbstract(SubclassBaseFile):
    ResourceType = 0x34B94BF8
    ParentResourceType = _ESAbstract.ResourceType
    parent: _ESAbstract
