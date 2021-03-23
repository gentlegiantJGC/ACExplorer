from pyUbiForge2.api.game import SubclassBaseFile
from .Event import Event as _Event


class VillaTransferIncomeEvent(SubclassBaseFile):
    ResourceType = 0xC14AB6B2
    ParentResourceType = _Event.ResourceType
    parent: _Event

