def read_file_header(file_object_data_wrapper, out_file, indent_count):
	file_object_data_wrapper.read_str(1, out_file, indent_count)
	file_object_data_wrapper.read_uint_64(out_file, indent_count)
	return file_object_data_wrapper.read_uint_32(out_file, indent_count)
