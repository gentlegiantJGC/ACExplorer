from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class UIVideoContext(SubclassBaseFile):
    ResourceType = 0xC76BA14F
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext
