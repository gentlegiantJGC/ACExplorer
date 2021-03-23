from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class UISoundContext(SubclassBaseFile):
    ResourceType = 0xA02E7441
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext
