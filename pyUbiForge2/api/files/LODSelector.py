from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObject import GraphicObject as _GraphicObject


class LODSelector(SubclassBaseFile):
    ResourceType = 0x51DC6B80
    ParentResourceType = _GraphicObject.ResourceType
    parent: _GraphicObject

