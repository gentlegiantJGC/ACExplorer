from pyUbiForge2.api.game import SubclassBaseFile
from .PickableData import PickableData as _PickableData


class PickableObjectData(SubclassBaseFile):
    ResourceType = 0x35B562B3
    ParentResourceType = _PickableData.ResourceType
    parent: _PickableData

