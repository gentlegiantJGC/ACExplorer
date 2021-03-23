from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WorldParticleSettings(SubclassBaseFile):
    ResourceType = 0xA9FB5674
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
