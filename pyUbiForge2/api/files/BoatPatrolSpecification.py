from pyUbiForge2.api.game import SubclassBaseFile
from .PatrolSpecification import PatrolSpecification as _PatrolSpecification


class BoatPatrolSpecification(SubclassBaseFile):
    ResourceType = 0x626945CD
    ParentResourceType = _PatrolSpecification.ResourceType
    parent: _PatrolSpecification

