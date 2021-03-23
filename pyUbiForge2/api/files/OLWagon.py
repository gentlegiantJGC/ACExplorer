from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLWagon(SubclassBaseFile):
    ResourceType = 0x5BEB75D6
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract

