from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimSetLayer import AIAnimSetLayer as _AIAnimSetLayer


class BodyReactionAnimSetLayer(SubclassBaseFile):
    ResourceType = 0x8ADD96E9
    ParentResourceType = _AIAnimSetLayer.ResourceType
    parent: _AIAnimSetLayer
