from pyUbiForge2.api.game import SubclassBaseFile
from .CLAbstract import CLAbstract as _CLAbstract


class CRLDetectNPC(SubclassBaseFile):
    ResourceType = 0xD6B26143
    ParentResourceType = _CLAbstract.ResourceType
    parent: _CLAbstract
