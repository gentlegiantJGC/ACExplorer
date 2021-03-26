import struct
import numpy
from typing import Tuple, Any, TYPE_CHECKING, Union, List, Type
from io import BytesIO

from pyUbiForge2.api.errors import FileOverflowError

if TYPE_CHECKING:
    from pyUbiForge2 import BaseGame, BaseFile


class Indent:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, count: int = 1):
        pass


class FileDataWrapper(BytesIO):
    def __init__(self, file: bytes, game: "BaseGame"):
        assert isinstance(file, bytes), "File must be bytes"
        assert game.endianness in ("<", ">"), 'Endianness marker must be "<" or ">"'
        super().__init__(file)
        self._game = game
        self._endianness = game.endianness
        self._call_stack: List[int] = []

    @property
    def indent(self):
        """with file.indent:"""
        return Indent()

    @property
    def call_stack(self) -> List[int]:
        return self._call_stack

    def out_file_write(self, val: str):
        pass

    def _read_struct(self, data_type: str) -> Tuple[Any]:
        fmt = f"{self._endianness}{data_type}"
        num_len = struct.calcsize(fmt)
        binary = self.read(num_len)
        if len(binary) != num_len:
            raise FileOverflowError("Reached End Of File")
        return struct.unpack(fmt, binary)

    def read_struct(self, data_types: str) -> Tuple[Any]:
        # data_types should not be prefixed with the endianness (this is added on for you)
        return self._read_struct(data_types)

    def read_bool(self) -> bool:
        return self._read_struct("?")[0]

    def read_int_8(self) -> int:
        return self._read_struct("b")[0]

    def read_uint_8(self) -> int:
        return self._read_struct("B")[0]

    def read_int_16(self) -> int:
        return self._read_struct("h")[0]

    def read_uint_16(self) -> int:
        return self._read_struct("H")[0]

    def read_int_32(self) -> int:
        return self._read_struct("i")[0]

    def read_uint_32(self) -> int:
        return self._read_struct("I")[0]

    def read_float_32(self) -> int:
        return self._read_struct("f")[0]

    def read_int_64(self) -> int:
        return self._read_struct("q")[0]

    def read_uint_64(self) -> int:
        return self._read_struct("Q")[0]

    def read_bytes(self, chr_len: int) -> bytes:
        return self._read_struct(f"{chr_len}s")[0]

    def read_file_id(self) -> int:
        return self._read_struct(self._game.FileIDType)[0]

    def read_resource_type(self) -> int:
        return self._read_struct(self._game.ResourceDType)[0]

    def get_object_ref(self):
        self._game.get_object_ref(self)

    def read_header_file(self) -> Union["BaseFile", int]:
        return self._game.read_header_file(self)

    def read_file_switch(self) -> Union["BaseFile", int]:
        return self._game.read_file_switch(self)

    def read_switch(self) -> int:
        return self._game.read_switch(self)

    def read_large_switch(self):
        return self._game.read_large_switch(self)

    def get_parser(self, resource_type: int) -> Type["BaseFile"]:
        return self._game.get_parser(resource_type)

    def read_file(self) -> "BaseFile":
        return self._game.read_file(self)

    def read_file_data(self, file_id: int, resource_type: int):
        return self._game.read_file_data(self, file_id, resource_type)

    def read_numpy(self, dtype, binary_size: int) -> numpy.ndarray:
        binary = self.read(binary_size)
        if len(binary) != binary_size:
            raise FileOverflowError("Reached End Of File")
        return numpy.copy(numpy.frombuffer(binary, dtype))

    def read_rest(self) -> bytes:
        return self.read()

    def clever_format(self):
        return self.read()
