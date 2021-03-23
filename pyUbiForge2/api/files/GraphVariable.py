from pyUbiForge2.api.game import SubclassBaseFile
from .IGraphVariable import IGraphVariable as _IGraphVariable


class GraphVariable(SubclassBaseFile):
    ResourceType = 0xD74A1B74
    ParentResourceType = _IGraphVariable.ResourceType
    parent: _IGraphVariable

