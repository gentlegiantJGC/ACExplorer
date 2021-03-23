from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentCollectionMonitor import (
    AccomplishmentCollectionMonitor as _AccomplishmentCollectionMonitor,
)


class AccomplishmentOrMonitor(SubclassBaseFile):
    ResourceType = 0xBB05BE2D
    ParentResourceType = _AccomplishmentCollectionMonitor.ResourceType
    parent: _AccomplishmentCollectionMonitor
