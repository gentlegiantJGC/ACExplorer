from pyUbiForge2.api.game import SubclassBaseFile
from .CompiledResource import CompiledResource as _CompiledResource


class CompiledMeshInstance(SubclassBaseFile):
    ResourceType = 0x4368101B
    ParentResourceType = _CompiledResource.ResourceType
    parent: _CompiledResource

