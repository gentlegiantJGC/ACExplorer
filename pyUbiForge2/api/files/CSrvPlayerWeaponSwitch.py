from pyUbiForge2.api.game import SubclassBaseFile
from .CSrvAbstract import CSrvAbstract as _CSrvAbstract


class CSrvPlayerWeaponSwitch(SubclassBaseFile):
    ResourceType = 0x943BC031
    ParentResourceType = _CSrvAbstract.ResourceType
    parent: _CSrvAbstract
