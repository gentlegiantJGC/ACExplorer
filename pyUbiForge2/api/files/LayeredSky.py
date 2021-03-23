from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class LayeredSky(SubclassBaseFile):
    ResourceType = 0x24D32CF8
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject

