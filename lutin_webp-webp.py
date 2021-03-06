#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "webp-webp library"

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
	    'webp/src/dsp/cost.c',
	    'webp/src/dsp/enc.c',
	    'webp/src/dsp/lossless_enc.c',
	    'webp/src/dsp/ssim.c',
	    'webp/src/dsp/enc_avx2.c',
	    'webp/src/dsp/cost_sse2.c',
	    'webp/src/dsp/enc_sse2.c',
	    'webp/src/dsp/lossless_enc_sse2.c',
	    'webp/src/dsp/ssim_sse2.c',
	    'webp/src/dsp/enc_sse41.c',
	    'webp/src/dsp/lossless_enc_sse41.c',
	    'webp/src/enc/alpha_enc.c',
	    'webp/src/enc/analysis_enc.c',
	    'webp/src/enc/backward_references_cost_enc.c',
	    'webp/src/enc/backward_references_enc.c',
	    'webp/src/enc/config_enc.c',
	    'webp/src/enc/cost_enc.c',
	    'webp/src/enc/filter_enc.c',
	    'webp/src/enc/frame_enc.c',
	    'webp/src/enc/histogram_enc.c',
	    'webp/src/enc/iterator_enc.c',
	    'webp/src/enc/near_lossless_enc.c',
	    'webp/src/enc/picture_enc.c',
	    'webp/src/enc/picture_csp_enc.c',
	    'webp/src/enc/picture_psnr_enc.c',
	    'webp/src/enc/picture_rescale_enc.c',
	    'webp/src/enc/picture_tools_enc.c',
	    'webp/src/enc/predictor_enc.c',
	    'webp/src/enc/quant_enc.c',
	    'webp/src/enc/syntax_enc.c',
	    'webp/src/enc/token_enc.c',
	    'webp/src/enc/tree_enc.c',
	    'webp/src/enc/vp8l_enc.c',
	    'webp/src/enc/webp_enc.c',
	    'webp/src/dec/alpha_dec.c',
	    'webp/src/dec/buffer_dec.c',
	    'webp/src/dec/frame_dec.c',
	    'webp/src/dec/idec_dec.c',
	    'webp/src/dec/io_dec.c',
	    'webp/src/dec/quant_dec.c',
	    'webp/src/dec/tree_dec.c',
	    'webp/src/dec/vp8_dec.c',
	    'webp/src/dec/vp8l_dec.c',
	    'webp/src/dec/webp_dec.c',
	    'webp/src/utils/bit_reader_utils.c',
	    'webp/src/utils/color_cache_utils.c',
	    'webp/src/utils/filters_utils.c',
	    'webp/src/utils/huffman_utils.c',
	    'webp/src/utils/quant_levels_dec_utils.c',
	    'webp/src/utils/rescaler_utils.c',
	    'webp/src/utils/random_utils.c',
	    'webp/src/utils/thread_utils.c',
	    'webp/src/utils/utils.c',
	    'webp/src/utils/bit_writer_utils.c',
	    'webp/src/utils/huffman_encode_utils.c',
	    'webp/src/utils/quant_levels_utils.c',
	    ])
	
	my_module.add_header_file([
	    'webp/src/dsp/*.h',
	    'webp/src/enc/*.h',
	    'webp/src/dec/*.h',
	    'webp/src/utils/*.h',
	    ], clip_path='webp')
	
	my_module.add_path([
	    'webp/src/dsp',
	    'webp/src/enc',
	    'webp/src/dec',
	    'webp/src/utils',
	    'webp/build/',
	    'webp/',
	    ], export=False)
	
	
	my_module.add_path([
	    'generate/',
	    ], export=True)
	
	my_module.add_flag('c', [
	    '-DHAVE_CONFIG_H',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-Wall',
	    '-msse4.1',
	    '-mavx2',
	    ])
	
	# build in C++ mode
	my_module.compile_version("c", 1999)
	
	my_module.add_depend([
	    'cxx',
	    'pthread',
	    ])
	return True


