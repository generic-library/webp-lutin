#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "webp-imageenc library"

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
	    'webp/src/dsp/alpha_processing.c',
	    'webp/src/dsp/alpha_processing_mips_dsp_r2.c',
	    'webp/src/dsp/cpu.c',
	    'webp/src/dsp/dec.c',
	    'webp/src/dsp/dec_clip_tables.c',
	    'webp/src/dsp/dec_mips32.c',
	    'webp/src/dsp/dec_mips_dsp_r2.c',
	    'webp/src/dsp/filters.c',
	    'webp/src/dsp/filters_mips_dsp_r2.c',
	    'webp/src/dsp/lossless.c',
	    'webp/src/dsp/lossless_mips_dsp_r2.c',
	    'webp/src/dsp/rescaler.c',
	    'webp/src/dsp/rescaler_mips32.c',
	    'webp/src/dsp/rescaler_mips_dsp_r2.c',
	    'webp/src/dsp/upsampling.c',
	    'webp/src/dsp/upsampling_mips_dsp_r2.c',
	    'webp/src/dsp/yuv.c',
	    'webp/src/dsp/yuv_mips32.c',
	    'webp/src/dsp/yuv_mips_dsp_r2.c',
	    'webp/src/dsp/alpha_processing_sse41.c',
	    'webp/src/dsp/dec_sse41.c',
	    'webp/src/dsp/upsampling_sse41.c',
	    'webp/src/dsp/yuv_sse41.c',
	    'webp/src/dsp/alpha_processing_sse2.c',
	    'webp/src/dsp/dec_sse2.c',
	    'webp/src/dsp/filters_sse2.c',
	    'webp/src/dsp/lossless_sse2.c',
	    'webp/src/dsp/rescaler_sse2.c',
	    'webp/src/dsp/upsampling_sse2.c',
	    'webp/src/dsp/yuv_sse2.c',
	    'webp/imageio/image_enc.c',
	    ])
	
	my_module.add_header_file([
	    'webp/src/dsp/*.h',
	    'webp/imageio/*.h',
	    ], clip_path='webp')
	
	my_module.add_path([
	    'webp/src/dsp',
	    'webp/imageio',
	    'webp/build/',
	    'webp/',
	    'webp/src/',
	    'webp/build/src/',
	    ], export=False)
	
	
	my_module.add_flag('c', [
	    '-DHAVE_CONFIG_H',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-Wall',
	    '-msse4.1',
	    ])
	
	
	my_module.add_depend([
	    'cxx',
	    'pthread',
	    'webp-imageioutil',
	    'webp-webp',
	    ])
	return True


