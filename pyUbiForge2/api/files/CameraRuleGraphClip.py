from pyUbiForge2.api.game import SubclassBaseFile
from .RuleGraphClip import RuleGraphClip as _RuleGraphClip


class CameraRuleGraphClip(SubclassBaseFile):
    ResourceType = 0xEECA29DF
    ParentResourceType = _RuleGraphClip.ResourceType
    parent: _RuleGraphClip
