from pyUbiForge2.api.game import SubclassBaseFile
from .FootIK import FootIK as _FootIK


class QuadrupedFootIK(SubclassBaseFile):
    ResourceType = 0xE55857CB
    ParentResourceType = _FootIK.ResourceType
    parent: _FootIK
