from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class MemoriesContext(SubclassBaseFile):
    ResourceType = 0xF55A5707
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext

