from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WorldAreaParticleData(SubclassBaseFile):
    ResourceType = 0x4346995A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject
