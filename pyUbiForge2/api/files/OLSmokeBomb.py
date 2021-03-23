from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLSmokeBomb(SubclassBaseFile):
    ResourceType = 0xE5E641AF
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract

