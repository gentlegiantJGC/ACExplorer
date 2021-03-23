from pyUbiForge2.api.game import SubclassBaseFile
from .CompiledResource import CompiledResource as _CompiledResource


class CompiledMesh(SubclassBaseFile):
    ResourceType = 0xFC9E1595
    ParentResourceType = _CompiledResource.ResourceType
    parent: _CompiledResource

