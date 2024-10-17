# Solutions to Exercises in Software Carpentry: The Unix Shell

## Section 2: Introducing The Shell

### Exercise 1: Exploring More ls Options

The -l option makes ls use a long listing format, showing not only 
the file/directory names but also additional information, such as the 
file size and the time of its last modification. If you use both the 
-h option and the -l option, this makes the file size ‘human readable’, 
i.e. displaying something like 5.3K instead of 5369.

### Exercise 2: Listing in Reverse Chronological Order

The most recently changed file is listed last when using -rt. 
This can be very useful for finding your most recent edits or checking to 
see if a new output file was written.

### Exercise 3: Absolute vs Relative Paths

1. No: . stands for the current directory.
2. No: / stands for the root directory.
3. No: Nelle’s home directory is /Users/nelle.
4. No: this command goes up two levels, i.e. ends in /Users.
5. Yes: ~ stands for the user’s home directory, in this case /Users/nelle.
6. No: this command would navigate into a directory home in the current directory if it exists.
7. Yes: unnecessarily complicated, but correct.
8. Yes: shortcut to go back to the user’s home directory.
9. Yes: goes up one level.

### Exercise 4: Relative Path Resolution

1. ../backup: No such file or directory
2. 2012-12-01 2013-01-08 2013-01-27
3. 2012-12-01/ 2013-01-08/ 2013-01-27/
4. original/ pnas_final/ pnas_sub/

### Exercise 5: ls Reading Comprehension

1. No: pwd is not the name of a directory.
2. Yes: ls without directory argument lists files and directories in the current directory.
3. Yes: uses the absolute path explicitly.
