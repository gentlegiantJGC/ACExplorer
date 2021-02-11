from pyUbiForge2 import BaseFile, FileDataWrapper
from pyUbiForge2.games.ACU import register_file_reader
from typing import List
from pyUbiForge2.games.ACU.files.D77FB524 import Reader as Fake


@register_file_reader('C69A7F31')
class Reader(BaseFile):
    def __init__(
            self,
            file_id: int,
            file: FileDataWrapper
    ):
        BaseFile.__init__(self, file_id)
        fake_count = file.read_uint_32()
        self.fakes: List[Fake] = []
        for _ in range(fake_count):
            self.fakes.append(
                file.read_file()
            )
        near_fake_count = file.read_uint_32()
        self.near_fakes = []
        for _ in range(near_fake_count):
            self.near_fakes.append(
                file.read_file()
            )
        file.read_bytes(1)
