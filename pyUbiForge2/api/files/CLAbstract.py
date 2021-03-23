from pyUbiForge2.api.game import SubclassBaseFile
from .ELAbstract import ELAbstract as _ELAbstract


class CLAbstract(SubclassBaseFile):
    ResourceType = 0x47C0C658
    ParentResourceType = _ELAbstract.ResourceType
    parent: _ELAbstract
