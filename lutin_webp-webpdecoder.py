#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "webp-webpdecoder library"

#def get_licence():
#	return "UNKNOW"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "webp"

#def get_maintainer():
#	return "UNKNOW"

def get_version():
	return "version.txt"

def configure(target, my_module):
	my_module.add_src_file([
	    'webp/src/utils/bit_reader_utils.c',
	    'webp/src/utils/color_cache_utils.c',
	    'webp/src/utils/filters_utils.c',
	    'webp/src/utils/huffman_utils.c',
	    'webp/src/utils/quant_levels_dec_utils.c',
	    'webp/src/utils/rescaler_utils.c',
	    'webp/src/utils/random_utils.c',
	    'webp/src/utils/thread_utils.c',
	    'webp/src/utils/utils.c',
	    ])
	
	my_module.add_header_file([
	    'webp/src/utils/*.h',
	    ], clip_path='webp')
	
	my_module.add_path([
	    'webp/src/utils',
	    'webp/build/',
	    'webp/',
	    ], export=False)
	
	
	my_module.add_flag('c', [
	    '-DHAVE_CONFIG_H',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-Wall',
	    ])
	
	
	my_module.add_depend([
	    'cxx',
	    'pthread',
	    'webp-webp',
	    ])
	return True


