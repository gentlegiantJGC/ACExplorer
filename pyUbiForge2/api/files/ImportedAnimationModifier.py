from pyUbiForge2.api.game import SubclassBaseFile
from .CameraModifier import CameraModifier as _CameraModifier


class ImportedAnimationModifier(SubclassBaseFile):
    ResourceType = 0xC54DA4EE
    ParentResourceType = _CameraModifier.ResourceType
    parent: _CameraModifier

