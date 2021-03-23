from pyUbiForge2.api.game import SubclassBaseFile
from .BaseReactionData import BaseReactionData as _BaseReactionData


class ProximityData(SubclassBaseFile):
    ResourceType = 0x05C90C81
    ParentResourceType = _BaseReactionData.ResourceType
    parent: _BaseReactionData
