from pyUbiForge2.api.game import SubclassBaseFile
from .CSAbstract import CSAbstract as _CSAbstract


class CSPlayerFeedback(SubclassBaseFile):
    ResourceType = 0x56D5BE3F
    ParentResourceType = _CSAbstract.ResourceType
    parent: _CSAbstract

