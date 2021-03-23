from pyUbiForge2.api.game import SubclassBaseFile
from .UiInfoContext import UiInfoContext as _UiInfoContext


class FamilyTreeContext(SubclassBaseFile):
    ResourceType = 0x110D52BA
    ParentResourceType = _UiInfoContext.ResourceType
    parent: _UiInfoContext
