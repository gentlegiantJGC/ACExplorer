from pyUbiForge2.api.game import SubclassBaseFile
from .WorldComponent import WorldComponent as _WorldComponent


class BlobSettings(SubclassBaseFile):
    ResourceType = 0xD62B00DA
    ParentResourceType = _WorldComponent.ResourceType
    parent: _WorldComponent
