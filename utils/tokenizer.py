import os
from os import makedirs, chdir
from os.path import isfile, join, exists, abspath, splitext
from pathlib import Path 
import argparse

# To read: http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html
def tokenize(file_in, file_out): 
	"""
		Tokenizes the content of file_in and stores it into file_out
		
		file_in and file_out should be valid file locations 
	"""
	assert exists(file_in)
	
	with open(file_in) as fin, open(file_out, mode='w') as fout: 
		# original = fin.read().strip().replace("\n", "")
		# This currently doesn't work because of Unicode decoding/encoding issues. Some of these files have completely unknown symbols in them. 
		# Need to figure out the scope of unexpected encoding behavior and put it into a try/except block
		Pass
	
	

def recurse_dirs(in_dir, out_dir): 
	"""
		Recursively traverses the directories containing data 
		Stops when we get to a directory that contains no further directories to explore 
		These leaf directories contain the data (not true in a general case, just true for this particular case) 
		
		in_dir and out_dir should be valid file paths
		
		This is definitely not the fastest way to do this, but it's pretty late at night. Come back and make this faster later. 
	"""	
	chdir(in_dir)
	p = Path('.')
	next_in = [x for x in p.iterdir() if x.is_dir()]
	if len(next_in) == 0: # We've hit a leaf directory. All contained files are data files that we want to tokenize. 
		files_in = [x for x in p.iterdir() if isfile(x)]
		files_out = [join(out_dir, splitext(x)[0] + "_tokenized" + splitext(x)[1]) for x in files_in]
		for fin, fout in zip(files_in, files_out):
			tokenize(fin, fout)
		chdir("../")
		return 
	else: # We can recurse further. If the output file directory does not currently exist, make it.
		next_out = [join(out_dir, x) for x in next_in]
		for dir in next_out:
			if not exists(dir): 
				makedirs(dir)
		for i, o in zip(next_in, next_out): 
			recurse_dirs(i, o)
		chdir("../")

if __name__ == "__main__": 
	# This script should be called from the command line with two arguments: input_directory and output_directory
	parser = argparse.ArgumentParser() 
	parser.add_argument("input_dir", help="The directory that contains the input files")
	parser.add_argument("output_dir", help="The directory that contains the output files")
	args = parser.parse_args() 
	id = args.input_dir 
	od = args.output_dir 
	recurse_dirs(id, abspath(od))