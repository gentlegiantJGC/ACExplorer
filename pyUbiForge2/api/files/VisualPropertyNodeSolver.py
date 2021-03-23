from pyUbiForge2.api.game import SubclassBaseFile
from .PropertyPathNodeSolver import PropertyPathNodeSolver as _PropertyPathNodeSolver


class VisualPropertyNodeSolver(SubclassBaseFile):
    ResourceType = 0x1D6F0AE7
    ParentResourceType = _PropertyPathNodeSolver.ResourceType
    parent: _PropertyPathNodeSolver

