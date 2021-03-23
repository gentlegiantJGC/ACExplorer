from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimSetLayer import AIAnimSetLayer as _AIAnimSetLayer


class FacialReactionAnimSetLayer(SubclassBaseFile):
    ResourceType = 0xCC0B966C
    ParentResourceType = _AIAnimSetLayer.ResourceType
    parent: _AIAnimSetLayer
