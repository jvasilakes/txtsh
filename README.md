A crappy little shell for text analysis.

./txtsh to run


	   +++COMMANDS+++

     +++ Main shell commands +++
     ---------------------------
     !info: display version information.
     !log: display contents of log file.
     !help: display this help screen.
     !quit: quit the shell.
     !update: update txtsh to the latest version.
     !load DATA_TYPE, DATA: load DATA into database. 
		DATA_TYPE must be 'string' or 'file'.
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
