from pyUbiForge2.api.game import SubclassBaseFile
from .LoadOnDemandObject import LoadOnDemandObject as _LoadOnDemandObject


class LoadOnDemandFX(SubclassBaseFile):
    ResourceType = 0x084BEC13
    ParentResourceType = _LoadOnDemandObject.ResourceType
    parent: _LoadOnDemandObject
