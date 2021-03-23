from pyUbiForge2.api.game import SubclassBaseFile
from .UIParams import UIParams as _UIParams


class UIVillaItemListParams(SubclassBaseFile):
    ResourceType = 0x286E65BE
    ParentResourceType = _UIParams.ResourceType
    parent: _UIParams
