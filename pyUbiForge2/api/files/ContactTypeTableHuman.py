from pyUbiForge2.api.game import SubclassBaseFile
from .ContactTypeTableBase import ContactTypeTableBase as _ContactTypeTableBase


class ContactTypeTableHuman(SubclassBaseFile):
    ResourceType = 0x11337755
    ParentResourceType = _ContactTypeTableBase.ResourceType
    parent: _ContactTypeTableBase
