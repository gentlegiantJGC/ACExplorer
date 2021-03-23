from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class MapContext(SubclassBaseFile):
    ResourceType = 0xDF0A838D
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext

