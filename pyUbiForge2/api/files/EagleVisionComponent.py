from pyUbiForge2.api.game import SubclassBaseFile
from .FXComponent import FXComponent as _FXComponent


class EagleVisionComponent(SubclassBaseFile):
    ResourceType = 0x13E03B07
    ParentResourceType = _FXComponent.ResourceType
    parent: _FXComponent

