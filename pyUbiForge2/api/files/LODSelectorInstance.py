from pyUbiForge2.api.game import SubclassBaseFile
from .GraphicObjectInstanceData import (
    GraphicObjectInstanceData as _GraphicObjectInstanceData,
)


class LODSelectorInstance(SubclassBaseFile):
    ResourceType = 0x01437462
    ParentResourceType = _GraphicObjectInstanceData.ResourceType
    parent: _GraphicObjectInstanceData
