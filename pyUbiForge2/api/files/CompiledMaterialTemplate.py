from pyUbiForge2.api.game import SubclassBaseFile
from .CompiledResource import CompiledResource as _CompiledResource


class CompiledMaterialTemplate(SubclassBaseFile):
    ResourceType = 0x3B9B7477
    ParentResourceType = _CompiledResource.ResourceType
    parent: _CompiledResource

