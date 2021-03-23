from pyUbiForge2.api.game import SubclassBaseFile
from .UIParams import UIParams as _UIParams


class UIVillaTrophyParams(SubclassBaseFile):
    ResourceType = 0x89FB5083
    ParentResourceType = _UIParams.ResourceType
    parent: _UIParams

