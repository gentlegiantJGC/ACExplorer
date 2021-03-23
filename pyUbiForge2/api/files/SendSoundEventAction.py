from pyUbiForge2.api.game import SubclassBaseFile
from .AIAction import AIAction as _AIAction


class SendSoundEventAction(SubclassBaseFile):
    ResourceType = 0xFEBD2C9C
    ParentResourceType = _AIAction.ResourceType
    parent: _AIAction

