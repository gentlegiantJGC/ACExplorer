from pyUbiForge2.api.game import SubclassBaseFile
from .CollectionCameraActivator import CollectionCameraActivator as _CollectionCameraActivator


class AnyCameraActivator(SubclassBaseFile):
    ResourceType = 0xF3C679C7
    ParentResourceType = _CollectionCameraActivator.ResourceType
    parent: _CollectionCameraActivator

