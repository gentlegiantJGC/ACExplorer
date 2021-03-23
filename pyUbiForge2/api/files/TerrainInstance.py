from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObjectInstanceData import GraphicObjectInstanceData as _GraphicObjectInstanceData


class TerrainInstance(SubclassBaseFile):
    ResourceType = 0x3FFC85C3
    ParentResourceType = _GraphicObjectInstanceData.ResourceType
    parent: _GraphicObjectInstanceData

