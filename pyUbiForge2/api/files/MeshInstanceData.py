from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObjectInstanceData import (
    GraphicObjectInstanceData as _GraphicObjectInstanceData,
)


class MeshInstanceData(SubclassBaseFile):
    ResourceType = 0x536E963B
    ParentResourceType = _GraphicObjectInstanceData.ResourceType
    parent: _GraphicObjectInstanceData
