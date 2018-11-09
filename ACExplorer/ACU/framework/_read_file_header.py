def read_file_header(file_object_data_wrapper):
	file_object_data_wrapper.read_str(1)
	file_object_data_wrapper.read_uint64()
	return file_object_data_wrapper.read_uint32()
