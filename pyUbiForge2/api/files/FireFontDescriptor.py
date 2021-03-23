from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class FireFontDescriptor(SubclassBaseFile):
    ResourceType = 0x58E38D86
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
