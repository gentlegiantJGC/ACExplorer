from pyUbiForge2.api.game import SubclassBaseFile
from pyUbiForge2.api.file_object import FileDataWrapper
from .ManagedObject import ManagedObject as _ManagedObject


class GridCellDataBlock(SubclassBaseFile):
    ResourceType = 0xAC2BBF68
    ParentResourceType = _ManagedObject.ResourceType
    parent: _ManagedObject

    def __init__(self, file_id: int, file: FileDataWrapper):
        super().__init__(file_id, file)
        self.children = []
