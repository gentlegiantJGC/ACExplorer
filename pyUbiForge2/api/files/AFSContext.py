from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class AFSContext(SubclassBaseFile):
    ResourceType = 0x545FE9DC
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext

