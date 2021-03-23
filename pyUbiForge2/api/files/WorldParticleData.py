from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class WorldParticleData(SubclassBaseFile):
    ResourceType = 0x5730D30E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

