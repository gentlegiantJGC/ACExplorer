from pyUbiForge2.api.game import SubclassBaseFile
from .ConfrontationMode import ConfrontationMode as _ConfrontationMode


class FindCorpseMode(SubclassBaseFile):
    ResourceType = 0xFE5A4B51
    ParentResourceType = _ConfrontationMode.ResourceType
    parent: _ConfrontationMode
