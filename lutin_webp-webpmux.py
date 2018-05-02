#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "webp-webpmux library"

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
	    'webp/src/mux/anim_encode.c',
	    'webp/src/mux/muxedit.c',
	    'webp/src/mux/muxinternal.c',
	    'webp/src/mux/muxread.c',
	    ])
	
	my_module.add_header_file([
	    'webp/src/mux/*.h',
	    ], clip_path='webp')
	
	my_module.add_path([
	    'webp/src/mux',
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
	    ])
	return True


