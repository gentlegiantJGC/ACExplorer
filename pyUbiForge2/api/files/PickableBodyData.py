from pyUbiForge2.api.game import SubclassBaseFile
from .PickableData import PickableData as _PickableData


class PickableBodyData(SubclassBaseFile):
    ResourceType = 0x322C8416
    ParentResourceType = _PickableData.ResourceType
    parent: _PickableData

