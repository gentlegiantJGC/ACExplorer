from pyUbiForge2.api.game import SubclassBaseFile
from .PolarCameraControl import PolarCameraControl as _PolarCameraControl


class PadR6VCameraControl(SubclassBaseFile):
    ResourceType = 0x907B40E4
    ParentResourceType = _PolarCameraControl.ResourceType
    parent: _PolarCameraControl
