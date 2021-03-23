from pyUbiForge2.api.game import SubclassBaseFile
from .FXElement import FXElement as _FXElement


class FXPostEffects(SubclassBaseFile):
    ResourceType = 0x8BD71CED
    ParentResourceType = _FXElement.ResourceType
    parent: _FXElement

