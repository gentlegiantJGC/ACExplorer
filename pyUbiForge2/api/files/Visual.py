from pyUbiForge2.api.game import SubclassBaseFile
from .VisualComponent import VisualComponent as _VisualComponent


class Visual(SubclassBaseFile):
    ResourceType = 0xEC658D29
    ParentResourceType = _VisualComponent.ResourceType
    parent: _VisualComponent

