from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLMoney(SubclassBaseFile):
    ResourceType = 0xE789DB04
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract
