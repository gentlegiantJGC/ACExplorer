from pyUbiForge2.api.game import SubclassBaseFile
from .CameraFX import CameraFX as _CameraFX


class CameraFXInterface(SubclassBaseFile):
    ResourceType = 0x4B398318
    ParentResourceType = _CameraFX.ResourceType
    parent: _CameraFX
