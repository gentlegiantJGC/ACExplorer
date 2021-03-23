from pyUbiForge2.api.game import SubclassBaseFile
from .ESrvAbstract import ESrvAbstract as _ESrvAbstract


class CSrvAbstract(SubclassBaseFile):
    ResourceType = 0x4510152E
    ParentResourceType = _ESrvAbstract.ResourceType
    parent: _ESrvAbstract
