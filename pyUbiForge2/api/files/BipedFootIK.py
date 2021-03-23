from pyUbiForge2.api.game import SubclassBaseFile
from .FootIKInterface import FootIKInterface as _FootIKInterface


class BipedFootIK(SubclassBaseFile):
    ResourceType = 0xED6B79E4
    ParentResourceType = _FootIKInterface.ResourceType
    parent: _FootIKInterface
