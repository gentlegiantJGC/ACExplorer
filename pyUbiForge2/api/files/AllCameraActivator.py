from pyUbiForge2.api.game import SubclassBaseFile
from .CollectionCameraActivator import (
    CollectionCameraActivator as _CollectionCameraActivator,
)


class AllCameraActivator(SubclassBaseFile):
    ResourceType = 0xBB840A88
    ParentResourceType = _CollectionCameraActivator.ResourceType
    parent: _CollectionCameraActivator
