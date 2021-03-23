from pyUbiForge2.api.game import SubclassBaseFile
from .CompiledResource import CompiledResource as _CompiledResource


class CompiledTextureMap(SubclassBaseFile):
    ResourceType = 0x13237FE9
    ParentResourceType = _CompiledResource.ResourceType
    parent: _CompiledResource
