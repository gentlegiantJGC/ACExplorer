from pyUbiForge2.api.game import SubclassBaseFile
from .GraphRuleBook import GraphRuleBook as _GraphRuleBook


class CameraGraphRuleBook(SubclassBaseFile):
    ResourceType = 0xE487F4CC
    ParentResourceType = _GraphRuleBook.ResourceType
    parent: _GraphRuleBook

