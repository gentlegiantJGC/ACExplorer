from pyUbiForge2.api.game import SubclassBaseFile
from .FireItem import FireItem as _FireItem


class MissionFailedMessageBox(SubclassBaseFile):
    ResourceType = 0x6C58B35A
    ParentResourceType = _FireItem.ResourceType
    parent: _FireItem
