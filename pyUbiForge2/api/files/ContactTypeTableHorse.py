from pyUbiForge2.api.game import SubclassBaseFile
from .ContactTypeTableBase import ContactTypeTableBase as _ContactTypeTableBase


class ContactTypeTableHorse(SubclassBaseFile):
    ResourceType = 0xD6CB8DB8
    ParentResourceType = _ContactTypeTableBase.ResourceType
    parent: _ContactTypeTableBase
