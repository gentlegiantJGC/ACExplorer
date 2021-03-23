from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class DynamicMesh(SubclassBaseFile):
    ResourceType = 0xF4BBBB9E
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject
