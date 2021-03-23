from pyUbiForge2.api.game import SubclassBaseFile
from .UnaryAction import UnaryAction as _UnaryAction


class PidControllerAction(SubclassBaseFile):
    ResourceType = 0xDFE31AFD
    ParentResourceType = _UnaryAction.ResourceType
    parent: _UnaryAction
