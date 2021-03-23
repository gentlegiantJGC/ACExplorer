from pyUbiForge2.api.game import SubclassBaseFile
from .ButtonHeldCameraActivator import ButtonHeldCameraActivator as _ButtonHeldCameraActivator


class HighestDetectingNPCCameraActivator(SubclassBaseFile):
    ResourceType = 0x7807B7A2
    ParentResourceType = _ButtonHeldCameraActivator.ResourceType
    parent: _ButtonHeldCameraActivator

