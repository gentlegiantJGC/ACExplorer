from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class PolarCurveModifier(SubclassBaseFile):
    ResourceType = 0xE85D8507
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier
