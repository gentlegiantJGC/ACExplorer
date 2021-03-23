from pyUbiForge2.api.game import SubclassBaseFile
from .ELAbstract import ELAbstract as _ELAbstract


class OLAbstract(SubclassBaseFile):
    ResourceType = 0x5DFC26D6
    ParentResourceType = _ELAbstract.ResourceType
    parent: _ELAbstract

