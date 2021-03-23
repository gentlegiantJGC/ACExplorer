from pyUbiForge2.api.game import SubclassBaseFile
from .CameraCustomizer import CameraCustomizer as _CameraCustomizer


class InitialCurveRatioCustomizer(SubclassBaseFile):
    ResourceType = 0x9B1BAEBD
    ParentResourceType = _CameraCustomizer.ResourceType
    parent: _CameraCustomizer
