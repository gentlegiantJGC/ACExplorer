from pyUbiForge2.api.game import SubclassBaseFile
from .CameraCustomizer import CameraCustomizer as _CameraCustomizer


class InitialAzimuthCustomizer(SubclassBaseFile):
    ResourceType = 0x3A55F274
    ParentResourceType = _CameraCustomizer.ResourceType
    parent: _CameraCustomizer

