from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimSetLayer import AIAnimSetLayer as _AIAnimSetLayer


class CharacterAnimSetLayer(SubclassBaseFile):
    ResourceType = 0xEEDCD5BE
    ParentResourceType = _AIAnimSetLayer.ResourceType
    parent: _AIAnimSetLayer
