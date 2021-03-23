from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimSetLayer import AIAnimSetLayer as _AIAnimSetLayer


class MilitaryAnimSetLayer(SubclassBaseFile):
    ResourceType = 0x4E361614
    ParentResourceType = _AIAnimSetLayer.ResourceType
    parent: _AIAnimSetLayer
