from pyUbiForge2.api.game import SubclassBaseFile
from .UIParams import UIParams as _UIParams


class UIVillaCodexParams(SubclassBaseFile):
    ResourceType = 0x15C8A77F
    ParentResourceType = _UIParams.ResourceType
    parent: _UIParams
