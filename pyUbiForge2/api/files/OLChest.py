from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLChest(SubclassBaseFile):
    ResourceType = 0xAB127B57
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract

