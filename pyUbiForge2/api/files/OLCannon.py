from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLCannon(SubclassBaseFile):
    ResourceType = 0xEA756B37
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract

