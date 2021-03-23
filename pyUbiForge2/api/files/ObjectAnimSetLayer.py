from pyUbiForge2.api.game import SubclassBaseFile
from .AIAnimSetLayer import AIAnimSetLayer as _AIAnimSetLayer


class ObjectAnimSetLayer(SubclassBaseFile):
    ResourceType = 0xE29C82F4
    ParentResourceType = _AIAnimSetLayer.ResourceType
    parent: _AIAnimSetLayer

