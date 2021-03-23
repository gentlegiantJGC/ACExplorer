from pyUbiForge2.api.game import SubclassBaseFile
from .TargetCamera import TargetCamera as _TargetCamera


class PolarCamera(SubclassBaseFile):
    ResourceType = 0x63466A32
    ParentResourceType = _TargetCamera.ResourceType
    parent: _TargetCamera

