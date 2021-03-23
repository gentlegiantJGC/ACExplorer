from pyUbiForge2.api.game import SubclassBaseFile
from .ManagedObject import ManagedObject as _ManagedObject


class MaterialTemplate(SubclassBaseFile):
    ResourceType = 0xBCFB3C7A
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

