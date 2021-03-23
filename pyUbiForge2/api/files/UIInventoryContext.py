from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class UIInventoryContext(SubclassBaseFile):
    ResourceType = 0x04B49419
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext
