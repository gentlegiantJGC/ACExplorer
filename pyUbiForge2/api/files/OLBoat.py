from pyUbiForge2.api.game import SubclassBaseFile
from .OLAbstract import OLAbstract as _OLAbstract


class OLBoat(SubclassBaseFile):
    ResourceType = 0x8BD75F3A
    ParentResourceType = _OLAbstract.ResourceType
    parent: _OLAbstract

