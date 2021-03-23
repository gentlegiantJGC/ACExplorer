from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLLadder(SubclassBaseFile):
    ResourceType = 0x97E70895
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract

