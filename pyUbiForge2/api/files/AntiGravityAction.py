from pyUbiForge2.api.game import SubclassBaseFile
from .UnaryAction import UnaryAction as _UnaryAction


class AntiGravityAction(SubclassBaseFile):
    ResourceType = 0x966DCA55
    ParentResourceType = _UnaryAction.ResourceType
    parent: _UnaryAction
