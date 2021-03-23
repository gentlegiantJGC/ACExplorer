from pyUbiForge2.api.game import SubclassBaseFile
from .ConfrontationMode import ConfrontationMode as _ConfrontationMode


class InvestigateMode(SubclassBaseFile):
    ResourceType = 0xCE6C4562
    ParentResourceType = _ConfrontationMode.ResourceType
    parent: _ConfrontationMode
