from pyUbiForge2.api.game import SubclassBaseFile
from .PolarCameraControl import PolarCameraControl as _PolarCameraControl


class PadPolarCameraControl(SubclassBaseFile):
    ResourceType = 0x1B4871CA
    ParentResourceType = _PolarCameraControl.ResourceType
    parent: _PolarCameraControl
