from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CRLDetect(SubclassBaseFile):
    ResourceType = 0xE35CC3DC
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
