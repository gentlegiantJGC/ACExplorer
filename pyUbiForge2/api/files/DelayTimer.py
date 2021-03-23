from pyUbiForge2.api.game import SubclassBaseFile
from .IGraphVariable import IGraphVariable as _IGraphVariable


class DelayTimer(SubclassBaseFile):
    ResourceType = 0x89B4A3E8
    ParentResourceType = _IGraphVariable.ResourceType
    parent: _IGraphVariable

