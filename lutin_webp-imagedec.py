#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "webp-imagedec library"

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
	    'webp/imageio/image_dec.c',
	    'webp/imageio/jpegdec.c',
	    'webp/imageio/metadata.c',
	    'webp/imageio/pngdec.c',
	    'webp/imageio/pnmdec.c',
	    'webp/imageio/tiffdec.c',
	    'webp/imageio/webpdec.c',
	    'webp/imageio/wicdec.c',
	    ])
	
	my_module.add_header_file([
	    'webp/imageio/*.h',
	    ], clip_path='webp')
	
	my_module.add_path([
	    'webp/imageio',
	    'webp/src/',
	    'webp/build/src/',
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
	    'png',
	    'z',
	    'jpeg',
	    'tiff',
	    'pthread',
	    'webp-imageioutil',
	    'webp-webp',
	    ])
	return True


