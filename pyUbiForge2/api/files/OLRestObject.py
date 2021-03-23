from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLRestObject(SubclassBaseFile):
    ResourceType = 0x6A5E9A6A
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract
