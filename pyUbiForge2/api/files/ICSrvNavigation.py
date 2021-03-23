from pyUbiForge2.api.game import SubclassBaseFile
from .ICSrvNavigationEngine import ICSrvNavigationEngine as _ICSrvNavigationEngine


class ICSrvNavigation(SubclassBaseFile):
    ResourceType = 0xD9C9CF22
    ParentResourceType = _ICSrvNavigationEngine.ResourceType
    parent: _ICSrvNavigationEngine

