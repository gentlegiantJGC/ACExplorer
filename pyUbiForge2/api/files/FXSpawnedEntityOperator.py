from pyUbiForge2.api.game import SubclassBaseFile
from .FXElementOperator import FXElementOperator as _FXElementOperator


class FXSpawnedEntityOperator(SubclassBaseFile):
    ResourceType = 0xB3BACA19
    ParentResourceType = _FXElementOperator.ResourceType
    parent: _FXElementOperator

