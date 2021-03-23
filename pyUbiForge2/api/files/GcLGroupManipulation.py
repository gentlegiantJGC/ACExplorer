from pyUbiForge2.api.game import SubclassBaseFile
from .GcLAbstract import GcLAbstract as _GcLAbstract


class GcLGroupManipulation(SubclassBaseFile):
    ResourceType = 0x7073DFA9
    ParentResourceType = _GcLAbstract.ResourceType
    parent: _GcLAbstract
