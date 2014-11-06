The little text-analysis shell that could.


+++ Main shell commands +++
---------------------------
	!info: display version information.

	!log: display contents of log file.

	!help: display this help screen.

	!quit: quit the shell.

	!load <DATA_TYPE>, <DATA>: load DATA into database.
		Possible values for DATA_TYPE: 'string', 'file'
			if 'string', DATA must be a sequence of characters
			    surrounded by quotes.
			if 'file', DATA may be left blank, in which case
			    a file explorer will open, or it may be the full 
			    path to a plain text file.

	!free ID: unload text object stored in ID.

	!use ID: go to subshell to manipulate text data stored in ID.

	!list: print all loaded objects.


+++ Subshell commands +++
-------------------------
	!drop: Drop out of subshell created by '!use'.

	!print: Display loaded text.

	!words: Display word data for loaded text.

	!punct: Display punctuation data for loaded text.

	!nums: Display number data for loaded text.

	!hist: Histogram of word lengths in file.
