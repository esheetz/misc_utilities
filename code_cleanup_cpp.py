#!/usr/bin/python3

"""
Script for cleaning C++ header and code files.

Recursively searches a directory for .h, .hpp, or .cpp files
and modifies each file to follow conventions:
- no tabs, always 4 spaces
- no extra whitespace on empty lines
- no trailing whitespace at ends of lines
"""

import sys
import os

def recursively_clean(dir_name):
	# recursively walk through directory
	for path, dir_names, file_names in os.walk(dir_name):
		# ignore any git directories
		if ".git" not in path:
			for fname in file_names:
				# only clean C++ header or cpp files
				if is_cpp_file(fname):
					clean_file(path, fname)

def clean_file(path_name, file_name):
	# get full file name
	fname = path_name + file_name
	print("cleaning file", fname)

	# open file for reading
	f = open(fname, 'r')
	# get lines
	lines = f.readlines()
	# close file
	f.close()

	# initialize cleaned lines
	cleaned_lines = []

	# clean all lines
	for l in lines:
		cleaned_l = l.replace("\t", "    ")
		cleaned_l = remove_whitespace_before_newline(cleaned_l)
		cleaned_lines.append(cleaned_l)

	# open file for overwriting
	f = open(fname, 'w')
	# write cleaned lines to file
	for cl in cleaned_lines:
		f.write(cl)
	# close file
	f.close()

	return

def remove_whitespace_before_newline(line):
	# check for whitespace before newline
	while line.find(" \n") != -1:
		# remove whitespace
		line = line.replace(" \n", "\n")

	return line

def is_cpp_file(file_name):
	# get file extension
	idx = file_name.rfind(".")
	if idx == -1:
		return False
	else:
		file_extn = file_name[idx:]
		return file_extn in ['.h', '.hpp', '.cpp']

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Incorrect use of script. Expected use: code_cleanup_cpp.py <directory-name>")
	else:
		dir_name = sys.argv[1]
		print("Recursively cleaning directory", dir_name)
		recursively_clean(dir_name)
