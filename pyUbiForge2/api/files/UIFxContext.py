from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class UIFxContext(SubclassBaseFile):
    ResourceType = 0x62707FD4
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext
