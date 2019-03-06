from pyUbiForge.misc.file_object import FileObjectDataWrapper
from pyUbiForge.misc.file_readers import BaseReader
from pyUbiForge.misc import Material


class Reader(BaseReader, Material):
	file_type = 'D70E6670'

	def __init__(self, py_ubi_forge, file_object_data_wrapper: FileObjectDataWrapper, out_file, indent_count):
		Material.__init__(self, None)

		texture_table = file_object_data_wrapper.read_numpy([('', '<u2'), ('texture_id', '<u8')], 120, out_file, indent_count)
		self.diffuse, self.normal, self.specular, \
			self.height, tex5, self.transmission, tex7, \
			self.mask1, self.mask2, tex10, tex11, tex12 \
			= [texture_id if texture_id != 0 else None for texture_id in texture_table['texture_id']]

		for var, pos in [[tex5, 5], [tex7, 7], [tex10, 10], [tex11, 11], [tex12, 12]]:
			if var is not None:
				py_ubi_forge.log.info(f'found a texture set with an id in position {pos}')
