Occasionally I work on small C projects and I like to test my work incrementally as I go.  I prefer using a light text editor and the command line, so I end up manually compiling and recompiling many times to perform syntax checking and unit testing.  This didn't make for a very fluid workflow, so I set up this script to listen on changes to ".c" and ".h" files in my current directory and automatically recompile from source when edits occur.  This gives me real-time feedback from the compiler and I don't have to constantly switch back and forth between editor and command line.  Helps me catch syntax mistakes quickly and perform testing/debugging much more fluidly.  My C projects aren't too crazy so the script uses gcc and only watches files in the current directory, however it wouldn't be too tough to add support for other compilers and additional directories.


Requirements:
	Written on OSX, probably works on most Linux distros, might work on Windows
	Written for Python 2.7.6, might work with Python 3
	Uses the watchdog module, install with - "sudo pip install watchdog"


Usage:
	python recompiler.py <executable-name> [<compiler-flags>]

	I put it in ~/bin and added alias autogcc="python ~/bin/recompiler.py" to my .bash_profile 