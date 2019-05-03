#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "BINARY"


def get_desc():
	return "webp-img2webp library"

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
	    'webp/examples/img2webp.c',
	    ])
	
	my_module.add_header_file([
	    'webp/examples/*.h',
	    ], clip_path='webp')
	
	my_module.add_path([
	    'webp/examples',
	    'webp/build/src/',
	    'webp/src/',
	    ], export=False)
	
	
	my_module.add_flag('c', [
	    '-DHAVE_CONFIG_H',
	    '-DNDEBUG',
	    ])
	
	my_module.add_flag('link', [
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-Wall',
	    ])
	
	
	my_module.add_depend([
	    'cxx',
	    'webp-exampleutil',
	    'webp-imagedec',
	    'webp-imageioutil',
	    'webp-webp',
	    'webp-webpmux',
	    'webp-webpdemux',
	    'png',
	    'z',
	    'jpeg',
	    'tiff',
	    'pthread',
	    'm',
	    ])
	return True


