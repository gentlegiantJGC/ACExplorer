from pyUbiForge2.api.game import SubclassBaseFile
from .TestStatechartEventBase import TestStatechartEventBase as _TestStatechartEventBase


class TestStatechartEventDerived(SubclassBaseFile):
    ResourceType = 0x0554D625
    ParentResourceType = _TestStatechartEventBase.ResourceType
    parent: _TestStatechartEventBase
