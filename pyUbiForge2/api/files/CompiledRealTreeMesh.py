from pyUbiForge2.api.game import SubclassBaseFile
from .CompiledResource import CompiledResource as _CompiledResource


class CompiledRealTreeMesh(SubclassBaseFile):
    ResourceType = 0x5E5E7E30
    ParentResourceType = _CompiledResource.ResourceType
    parent: _CompiledResource

