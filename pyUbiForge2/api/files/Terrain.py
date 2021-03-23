from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class Terrain(SubclassBaseFile):
    ResourceType = 0x07CB6A2D
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject
