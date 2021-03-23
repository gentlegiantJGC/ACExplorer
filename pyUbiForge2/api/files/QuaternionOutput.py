from pyUbiForge2.api.game import SubclassBaseFile
from .LinkableOutput import LinkableOutput as _LinkableOutput


class QuaternionOutput(SubclassBaseFile):
    ResourceType = 0x556DC878
    ParentResourceType = _LinkableOutput.ResourceType
    parent: _LinkableOutput
