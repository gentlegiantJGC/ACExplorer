from pyUbiForge2.api.game import SubclassBaseFile
from .IGraphRule import IGraphRule as _IGraphRule


class GraphRuleBook(SubclassBaseFile):
    ResourceType = 0x4A77CEFE
    ParentResourceType = _IGraphRule.ResourceType
    parent: _IGraphRule
