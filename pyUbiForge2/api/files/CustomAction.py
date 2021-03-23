from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class CustomAction(SubclassBaseFile):
    ResourceType = 0x116446A9
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

