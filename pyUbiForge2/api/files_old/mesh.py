import numpy
from typing import List


class BaseMesh:
    _name: str = "unknown"
    _vertices: numpy.ndarray = numpy.array((0, 3), numpy.float)
    _texture_vertices: numpy.ndarray = numpy.array((0, 3), numpy.float)
    _normals: numpy.ndarray = numpy.array((0, 3), numpy.float)
    _faces: List[numpy.ndarray] = []
    _meshes: numpy.ndarray = None
    _materials: numpy.ndarray = None
    _bones = None

    @property
    def name(self) -> str:
        return self._name

    @property
    def vertices(self) -> numpy.ndarray:
        return self._vertices

    @property
    def texture_vertices(self) -> numpy.ndarray:
        return self._texture_vertices

    @property
    def normals(self) -> numpy.ndarray:
        return self._normals

    @property
    def faces(self) -> List[numpy.ndarray]:
        return self._faces

    @property
    def meshes(self) -> numpy.ndarray:
        return self._meshes

    @property
    def materials(self) -> numpy.ndarray:
        return self._materials

    @property
    def bones(self):
        return self._bones
