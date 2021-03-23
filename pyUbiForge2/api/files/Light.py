from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class Light(SubclassBaseFile):
    ResourceType = 0xAADB73F3
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject

