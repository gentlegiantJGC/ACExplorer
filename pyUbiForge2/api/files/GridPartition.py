from pyUbiForge2.api.game import SubclassBaseFile
from .SpatialTopology import SpatialTopology as _SpatialTopology


class GridPartition(SubclassBaseFile):
    ResourceType = 0x0E2F4444
    ParentResourceType = _SpatialTopology.ResourceType
    parent: _SpatialTopology
