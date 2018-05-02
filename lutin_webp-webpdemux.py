#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "webp-webpdemux library"

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
	    'webp/src/demux/anim_decode.c',
	    'webp/src/demux/demux.c',
	    ])
	
	my_module.add_header_file([
	    'webp/src/demux/*.h',
	    ], clip_path='webp')
	
	my_module.add_path([
	    'webp/src/demux',
	    'webp/',
	    'webp/build/',
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


