from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class ProceduralPolarCurveModifier(SubclassBaseFile):
    ResourceType = 0x86E15494
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

