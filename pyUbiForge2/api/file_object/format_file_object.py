import struct
from typing import TextIO, Tuple, Any, TYPE_CHECKING, Union
from .file_object import FileDataWrapper, Indent
from pyUbiForge2.api.errors import FileOverflowError

if TYPE_CHECKING:
    from pyUbiForge2 import BaseGame, BaseFile

NEWLINE = "\n"


class FormatIndent(Indent):
    def __init__(self, wrapper: "FileFormatDataWrapper"):
        self._wrapper = wrapper

    def __enter__(self):
        self._wrapper.indent_count += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._wrapper.indent_count -= 1

    def __call__(self, count: int = 1):
        self._wrapper.indent_count += count


class FileFormatDataWrapper(FileDataWrapper):
    def __init__(self, file: bytes, game: "BaseGame", out_file: TextIO):
        super().__init__(file, game)
        self._out_file = out_file
        self.indent_count = 0
        self.indent_chr = "\t"

    @property
    def indent(self):
        return FormatIndent(self)

    @staticmethod
    def _hex_string(binary: bytes) -> str:
        return " ".join(f"{b:02X}" for b in binary)

    def close(self):
        super().close()
        self._out_file.close()

    def seek(self, offset: int, whence: int = 0):
        if whence == 0:  # absolute
            count = offset - self.tell()
            if count > 0:
                self._out_file.write(
                    f"{self.indent_count * self.indent_chr}{self._hex_string(self.read(count))}\n"
                )
            elif count < 0:
                self._out_file.write(f"Skipped back {abs(count)} bytes\n")
                super().seek(offset, whence)
        elif whence == 1:  # relative
            if offset > 0:
                self._out_file.write(
                    f"{self.indent_count * self.indent_chr}{self._hex_string(self.read(offset))}\n"
                )
            elif offset < 0:
                self._out_file.write(f"Skipped back {abs(offset)} bytes\n")
                super().seek(offset, whence)
        elif whence == 2:  # relative to end
            file_pointer = self.tell()
            super().seek(offset, 2)
            count = self.tell() - file_pointer
            super().seek(file_pointer)
            if count > 0:
                self._out_file.write(
                    f"{self.indent_count * self.indent_chr}{self._hex_string(self.read(count))}\n"
                )
            elif count < 0:
                self._out_file.write(f"Skipped back {abs(count)} bytes\n")
                super().seek(offset, whence)

    def out_file_write(self, val: str):
        self._out_file.write(f"{self.indent_count * self.indent_chr}{val}")

    def _read_struct(self, data_type: str, trailing_newline: bool = True) -> Tuple[Any]:
        fmt = f"{self._endianness}{data_type}"
        num_len = struct.calcsize(fmt)
        binary = self.read(num_len)
        if len(binary) != num_len:
            raise FileOverflowError("Reached End Of File")
        val = struct.unpack(fmt, binary)
        self._out_file.write(
            f"{self.indent_count * self.indent_chr}{self._hex_string(binary)}\t\t{val}{NEWLINE * trailing_newline}"
        )
        return val

    def read_file_id(self) -> int:
        file_id = self._read_struct(self._game.FileIDType, False)[0]
        file_location = self._game.find_file(file_id)
        if file_location is None:
            self._out_file.write("\t\tUnknown File ID\n")
        else:
            forge_file, data_file = file_location
            file_type, file_name = (
                self._game.get_forge_file(forge_file)
                .get_data_file(data_file)
                .get_file(file_id)
            )
            self._out_file.write(f"\t\t{file_name}\t{file_type}\n")
        return file_id

    def read_resource_type(self) -> int:
        file_type = self._read_struct(self._game.ResourceDType, False)[0]
        resource_parser = self._game.get_parser_name(file_type)
        self._out_file.write(f"\t\t{file_type:08X}\t\t{resource_parser}\n")
        return file_type

    def read_header_file(self) -> "BaseFile":
        with self.indent:
            return super().read_header_file()

    def read_file_switch(self) -> Union["BaseFile", int]:
        with self.indent:
            return super().read_file_switch()

    def read_file(self) -> "BaseFile":
        with self.indent:
            return super().read_file()

    def read_file_data(self, file_id: int, resource_type: int):
        with self.indent:
            return super().read_file_data(file_id, resource_type)

    def read_numpy(self, dtype, binary_size: int):
        val = super().read_numpy(dtype, binary_size)
        indent = self.indent_count * self.indent_chr
        self._out_file.write(f"{indent}{str(val).replace(NEWLINE, indent)}\n")
        return val

    def read_rest(self) -> bytes:
        binary = self.read()
        self._out_file.write(
            f"{self.indent_count * self.indent_chr}{self._hex_string(binary)}\n"
        )
        return binary

    def clever_format(self):
        self.read_rest()

    #     self.out_file_write("Initiate clever format\n")
    #     hex_str = []
    #     file_bytes = [self.read(4)]
    #     might_be_a_file_type = ''.join(f'{b:02X}' for b in file_bytes[-1][::-1])
    #     while len(might_be_a_file_type) == 8:
    #         if int(might_be_a_file_type, 16) in self._game.resource_types:
    #             self._out_file.write(f'{self.indent_count * self.indent_chr}{" ".join(hex_str[:-8])}\n')
    #             hex_str.clear()
    #             super().seek(-12, 1)
    #             try:
    #                 self.read_file()
    #             except Exception as e:
    #                 self.out_file_write(f"Failed reading file type {might_be_a_file_type.upper()} {e}\n")
    #             file_bytes.append(self.read(4))
    #             might_be_a_file_type = ''.join(f'{b:02X}' for b in file_bytes[-1][::-1])
    #         else:
    #             hex_str.append(might_be_a_file_type[6:])
    #             next_chr = self.read(1)
    #             if next_chr:
    #                 file_bytes.append(next_chr)
    #                 might_be_a_file_type = f'{next_chr[0]:02X}{might_be_a_file_type[:6]}'
    #             else:
    #                 might_be_a_file_type = might_be_a_file_type[:6]
    #
    #     while might_be_a_file_type:
    #         hex_str.append(might_be_a_file_type[-2:])
    #         might_be_a_file_type = might_be_a_file_type[:-2]
    #     self._out_file.write(f'{self.indent_count * self.indent_chr}{" ".join(hex_str)}\n')
    #     return b"".join(file_bytes)
