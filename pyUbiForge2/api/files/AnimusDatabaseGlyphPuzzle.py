from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class AnimusDatabaseGlyphPuzzle(SubclassBaseFile):
    ResourceType = 0x2C88D63F
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

