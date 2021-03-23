from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class EulerModifier(SubclassBaseFile):
    ResourceType = 0x9781D684
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

