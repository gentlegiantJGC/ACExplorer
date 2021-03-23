from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvBoatDriverCrowdInteraction(SubclassBaseFile):
    ResourceType = 0x4FF543F9
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
