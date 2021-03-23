from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class ActionPSPItemsUpdate(SubclassBaseFile):
    ResourceType = 0x0CA3D982
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

