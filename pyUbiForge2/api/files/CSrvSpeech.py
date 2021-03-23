from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvSpeech(SubclassBaseFile):
    ResourceType = 0x80809FF8
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

