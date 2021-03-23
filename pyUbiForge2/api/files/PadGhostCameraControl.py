from pyUbiForge2.api.game import SubclassBaseFile
from .PadPolarCameraControl import PadPolarCameraControl as _PadPolarCameraControl


class PadGhostCameraControl(SubclassBaseFile):
    ResourceType = 0xC9B98A67
    ParentResourceType = _PadPolarCameraControl.ResourceType
    parent: _PadPolarCameraControl

