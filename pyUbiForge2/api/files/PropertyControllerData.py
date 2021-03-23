from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class PropertyControllerData(SubclassBaseFile):
    ResourceType = 0x3255221E
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

