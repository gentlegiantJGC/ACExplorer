from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class LookAtDataSkeletonDefinition(SubclassBaseFile):
    ResourceType = 0xD86B9F28
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
