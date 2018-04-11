import os
from os import makedirs, chdir
from os.path import isfile, join, exists, abspath, splitext
from pathlib import Path 
import argparse

ignore_punct = {'(', ')', '[', ']', '{', '}', '<', '>'}
unify_punct = {'-'}

# To read: http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html
def tokenize(file_in, file_out, file_err): 
	"""
		Tokenizes the content of file_in and stores it into file_out. 
		Unlike typical tokenization programs, most kinds of punctuation are not considered tokens and are simply dropped.
		Brackets like '(' and ')' are permitted since they may appear in mathematics and have some additional semantic meaning. 

		If file_in contains a character that breaks UTF-8, we note the name of the file and then skip to the next file.

		This works by looking at each character individually. Two indices are used to keep track of the left and right bound of the current token.
		Let c be the character we are currently looking at:
			If c is recognizable in some alphabet (not necessarily english) or a kind of bracket, then we move to the next character.
			If c is in the unify_punct set (i.e., '-' currently), then we merge the tokens on the left and right together. 
				For example, "post-modernism" is converted to "postmodernism" and is treated as a single token
				We also handle the case of intermediate newlines. i.e., "post-\nmodernism" becomes "postmodernism"
			If c is anything else, we add the string bounded by the left and right indices to the list. Then update the indices to look at the next character. 

		file_in, file_out, and file_err should be valid file locations. 
		file_out and file_err will be created if it doesn't currently exist, but the directory structure is assumed to be correct.
	"""
	assert exists(file_in)
	
	with open(file_in) as fin, open(file_out, mode="w") as fout, open(file_err, mode="a") as ferr:
		tokens = [] 
		ind_left, ind_right = 0, 0
		merge_string = ""

		try: 
			original = fin.read()
		except UnicodeDecodeError:
			ferr.write("Unicode Error detected in file {}\n".format(str(file_in)))
			# print("Unicode Error detected in file {}".format(str(file_in)))
			return

		for i in range(len(original)):
			if original[ind_right].isalpha() or original[ind_right] in ignore_punct: # This kind of punctuation is permitted to behave like a character
				ind_right += 1
			elif original[ind_right] in unify_punct:
				merge_string += original[ind_left : ind_right] # Copy should not be necessary
				ind_right += 1 
				while ind_right != len(original) and original[ind_right] == "\n": # Skip past all newlines
					ind_right += 1
				ind_left = ind_right
			else: 
				if merge_string: # Exists 
					tokens.append(merge_string) 
					merge_string = ""
					ind_right += 1
					ind_left = ind_right
				elif ind_left != ind_right:
					tokens.append(original[ind_left : ind_right])
					ind_right += 1
					ind_left = ind_right
				else:
					ind_right += 1
					ind_left = ind_right
		fout.write(str(tokens))
	
def recurse_dirs(in_dir, out_dir, err): 
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
			tokenize(fin, fout, err)
		chdir("../")
		return 
	else: # We can recurse further. If the output file directory does not currently exist, make it.
		next_out = [join(out_dir, x) for x in next_in]
		for dir in next_out:
			if not exists(dir): 
				makedirs(dir)
		for i, o in zip(next_in, next_out): 
			recurse_dirs(i, o, err)
		chdir("../")

if __name__ == "__main__": 
	# This script should be called from the command line with three arguments: input_directory, output_directory, and error_file
	# Three optional arguments can be used to test the tokenize function directly
	parser = argparse.ArgumentParser() 
	parser.add_argument("input_dir", help="The directory that contains the input files")
	parser.add_argument("output_dir", help="The directory that contains the output files")
	parser.add_argument("error_file", help="The file that we will write errors to")
	parser.add_argument("-t", "--testing", help="An optional argument that exists so we can directly test the tokenize function")
	parser.add_argument("-ti", "--testing_fin", type=str, help="An optional argument that indicates the location of an input text file")
	parser.add_argument("-to", "--testing_fout", type=str, help="An optional argument that indicates the location of an output text file")
	args = parser.parse_args() 
	id = args.input_dir 
	od = abspath(args.output_dir)
	err = abspath(args.error_file)
	if not exists(err):
		Path(err).touch()

	if args.testing:
		tokenize(args.testing_fin, args.testing_fout, err)
	else:
		recurse_dirs(id, od, err)