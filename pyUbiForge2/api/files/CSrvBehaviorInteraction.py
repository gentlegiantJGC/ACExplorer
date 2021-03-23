from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvBehaviorInteraction(SubclassBaseFile):
    ResourceType = 0xD9BE9799
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
