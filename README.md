# Miscellaneous Utilities
Contains miscellaneous utilities to make life easier.

## Scripts:
Currently supported scripts are:
- `code_cleanup_cpp.py`: recursively finds and cleans all C++ files (either .h, .hpp, or .cpp extensions).  The code files are cleaned to meet the following conventions:
	- no tabs, 4 spaces instead
	- no extra whitespace on empty lines
	- no trailing whitespace at ends of lines
To run, provide a directory to recursively clean:
```
./clode_cleanup_cpp.py <full-path-to-directory>
```
