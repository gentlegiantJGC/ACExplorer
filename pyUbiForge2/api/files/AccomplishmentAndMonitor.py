from pyUbiForge2.api.game import SubclassBaseFile
from .AccomplishmentCollectionMonitor import AccomplishmentCollectionMonitor as _AccomplishmentCollectionMonitor


class AccomplishmentAndMonitor(SubclassBaseFile):
    ResourceType = 0xF75BD632
    ParentResourceType = _AccomplishmentCollectionMonitor.ResourceType
    parent: _AccomplishmentCollectionMonitor

