from pyUbiForge2.api.game import SubclassBaseFile
from .ICSrvNavigation import ICSrvNavigation as _ICSrvNavigation


class CSrvNavigation(SubclassBaseFile):
    ResourceType = 0x6328D910
    ParentResourceType = _ICSrvNavigation.ResourceType
    parent: _ICSrvNavigation
