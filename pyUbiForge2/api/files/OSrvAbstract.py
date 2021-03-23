from pyUbiForge2.api.game import SubclassBaseFile
from .ESrvAbstract import ESrvAbstract as _ESrvAbstract


class OSrvAbstract(SubclassBaseFile):
    ResourceType = 0x401A58AF
    ParentResourceType = _ESrvAbstract.ResourceType
    parent: _ESrvAbstract

