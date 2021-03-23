from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvReactionCooldown(SubclassBaseFile):
    ResourceType = 0x01A0E9D1
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract

