from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class Projector(SubclassBaseFile):
    ResourceType = 0xD968D421
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject

