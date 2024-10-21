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

## Section 3: Working With Files and Directories

### Exercise 1: Creating Files A Different Way

1. The touch command generates a new file called my_file.txt in your current directory. You can observe this newly generated file by typing ls at the command line prompt. my_file.txt can also be viewed in your GUI file explorer.
2. When you inspect the file with ls -l, note that the size of my_file.txt is 0 bytes. In other words, it contains no data. If you open my_file.txt using your text editor it is blank.
3. Some programs do not generate output files themselves, but instead require that empty files have already been generated. When the program is run, it searches for an existing file to populate with its output. The touch command allows you to efficiently generate a blank text file to be used by such programs.

### Exercise 2: Movilg Files To A New Folder

    $ mv sucrose.dat maltose.dat ../raw

Recall that .. refers to the parent directory (i.e. one above the current directory) and that . refers to the current directory.

### Exercise 3: Renaming Files

1. No. While this would create a file with the correct name, the incorrectly named file still exists in the directory and would need to be deleted.
2. Yes, this would work to rename the file.
3. No, the period(.) indicates where to move the file, but does not provide a new file name; identical file names cannot be created.
4. No, the period(.) indicates where to copy the file, but does not provide a new file name; identical file names cannot be created.

### Exercise 4: Moving And Copying

We start in the /Users/jamie/data directory, and create a new folder called recombined. The second line moves (mv) the file proteins.dat to the new folder (recombined). The third line makes a copy of the file we just moved. The tricky part here is where the file was copied to. Recall that .. means ‘go up a level’, so the copied file is now in /Users/jamie. Notice that .. is interpreted with respect to the current working directory, not with respect to the location of the file being copied. So, the only thing that will show using ls (in /Users/jamie/data) is the recombined folder.

1. No, see explanation above. proteins-saved.dat is located at /Users/jamie
2. Yes
3. No, see explanation above. proteins.dat is located at /Users/jamie/data/recombined
4. No, see explanation above. proteins-saved.dat is located at /Users/jamie

### Exercise 5: Using rm Safely

    rm: remove regular file 'thesis_backup/quotations.txt'? y

The -i option will prompt before (every) removal (use Y to confirm deletion or N to keep the file). The Unix shell doesn’t have a trash bin, so all the files removed will disappear forever. By using the -i option, we have the chance to check that we are deleting only the files that we want to remove.

### Exercise 6: Copy With Multiple Filenames

If given more than one file name followed by a directory name (i.e. the destination directory must be the last argument), cp copies the files to the named directory.

If given three file names, cp throws an error such as the one below, because it is expecting a directory name as the last argument.

    cp: target 'basilisk.dat' is not a directory

### Exercise 7: List Filenames Matching A Pattern

The solution is 3.

1. shows all files whose names contain zero or more characters (*) followed by the letter t, then zero or more characters (*) followed by ane.pdb. This gives ethane.pdb methane.pdb octane.pdb pentane.pdb.
2. shows all files whose names start with zero or more characters (*) followed by the letter t, then a single character (?), then ne. followed by zero or more characters (*). This will give us octane.pdb and pentane.pdb but doesn’t match anything which ends in thane.pdb.
3. fixes the problems of option 2 by matching two characters (??) between t and ne. This is the solution.
4. only shows files starting with ethane..

### Exercise 8: More On Wildcards

    $ cp *calibration.txt backup/calibration
    $ cp 2015-11-* send_to_bob/all_november_files/
    $ cp *-23-dataset* send_to_bob/all_datasets_created_on_a_23rd/

### Exercise 9: Organizing Files And Directories

    mv *.dat analyzed

Jamie needs to move her files fructose.dat and sucrose.dat to the analyzed directory. 
The shell will expand *.dat to match all .dat files in the current directory. 
The mv command then moves the list of .dat files to the ‘analyzed’ directory.

### Exercise 10: Reproduce A Folder Structure

The first two sets of commands achieve this objective. The first set uses relative paths to create the top-level directory before the subdirectories.

The third set of commands will give an error because the default behavior of mkdir won’t create a subdirectory of a non-existent directory: the intermediate level folders must be created first.

The fourth set of commands achieve this objective. Remember, the -p option, followed by a path of one or more directories, will cause mkdir to create any intermediate subdirectories as required.

The final set of commands generates the ‘raw’ and ‘processed’ directories at the same level as the ‘data’ directory.

## Section 4: Pipes And Filters

### Exercise 1: What Does sort -n Do?

The -n option specifies a numerical rather than an alphanumerical sort.

### Exercise 2: What Does >> Mean?

In the first example with >, the string ‘hello’ is written to testfile01.txt, but the file gets overwritten each time we run the command.

We see from the second example that the >> operator also writes ‘hello’ to a file (in this case testfile02.txt), but appends the string to the file if it already exists (i.e. when we run it for the second time).

### Exercise 3: Appending Data

Option 3 is correct. For option 1 to be correct we would only run the head command. For option 2 to be correct we would only run the tail command. For option 4 to be correct we would have to pipe the output of head into tail -n 2 by doing head -n 3 animals.csv | tail -n 2 > animals-subset.csv

### Exercise 4: Piping Commands Together

Option 4 is the solution. The pipe character | is used to connect the output from one command to the input of another. > is used to redirect standard output to a file. Try it in the shell-lesson-data/exercise-data/alkanes directory!

### Exercise 5: Piping Reading Comprehension

The head command extracts the first 5 lines from animals.csv. Then, the last 3 lines are extracted from the previous 5 by using the tail command. With the sort -r command those 3 lines are sorted in reverse order. Finally, the output is redirected to a file: final.txt. The content of this file can be checked by executing cat final.txt. The file should contain the following lines:

    2012-11-06,rabbit,19
    2012-11-06,deer,2
    2012-11-05,raccoon,7

### Exercise 6: Pipe Construction

    $ cut -d , -f 2 animals.csv | sort | uniq

### Exercise 7: Which Pipe?

Option 4. is the correct answer. If you have difficulty understanding why, try running the commands, or sub-sections of the pipelines (make sure you are in the shell-lesson-data/exercise-data/animal-counts directory).

### Exercise 8: Removing Unneeded Files

1. This would remove .txt files with one-character names
2. This is the correct answer
3. The shell would expand * to match everything in the current directory, so the command would try to remove all matched files and an additional file called .txt
4. The shell expands *.* to match all filenames containing at least one ., including the processed files (.txt) and raw files (.dat)

## Section 5: Loops

### Exercise 1: Write Your Own Loop

    $ for loop_variable in 0 1 2 3 4 5 6 7 8 9
    > do
    >     echo $loop_variable
    > done

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

### Exercise 2: Variables In Loops

The first code block gives the same output on each iteration through the loop. Bash expands the wildcard *.pdb within the loop body (as well as before the loop starts) to match all files ending in .pdb and then lists them using ls. The expanded loop would look like this:

    $ for datafile in cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    > do
    >     ls cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    > done

    cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
    
The second code block lists a different file on each loop iteration. The value of the datafile variable is evaluated using $datafile, and then listed using ls.

### Exercise 3: Limiting Sets Of Files

4 is the correct answer. * matches zero or more characters, so any file name starting with the letter c, followed by zero or more other characters will be matched.

### Exercise 4: Limiting Sets Of Files (Continued)

4 is the correct answer. * matches zero or more characters, so a file name with zero or more characters before a letter c and zero or more characters after the letter c will be matched.

### Exercise 5: Saving To A File In A loop - Part One

1. The text from each file in turn gets written to the alkanes.pdb file. However, the file gets overwritten on each loop iteration, so the final content of alkanes.pdb is the text from the propane.pdb file.

### Exercise 6: Saving To A File In A loop - Part Two

3 is the correct answer. >> appends to a file, rather than overwriting it with the redirected output from a command. Given the output from the cat command has been redirected, nothing is printed to the screen.

### Exercise 7: Doing A Dry Run

The second version is the one we want to run. This prints to screen everything enclosed in the quote marks, expanding the loop variable name because we have prefixed it with a dollar sign. It also does not modify nor create the file all.pdb, as the >> is treated literally as part of a string rather than as a redirection instruction.

The first version appends the output from the command echo cat $datafile to the file, all.pdb. This file will just contain the list; cat cubane.pdb, cat ethane.pdb, cat methane.pdb etc.

Try both versions for yourself to see the output! Be sure to open the all.pdb file to view its contents.

### Exercise 8: Nested Loops

We have a nested loop, i.e. contained within another loop, so for each species in the outer loop, the inner loop (the nested loop) iterates over the list of temperatures, and creates a new directory for each combination.

Try running the code for yourself to see which directories are created!

## Section 6: Shell Scripts

### Exercise 1: List Unique Species

Leah has several hundred data files, each of which is formatted like this:

    2013-11-05,deer,5
    2013-11-05,rabbit,22
    2013-11-05,raccoon,7
    2013-11-06,rabbit,19
    2013-11-06,deer,2
    2013-11-06,fox,1
    2013-11-07,rabbit,18
    2013-11-07,bear,1
An example of this type of file is given in shell-lesson-data/exercise-data/animal-counts/animals.csv.

We can use the command cut -d , -f 2 animals.csv | sort | uniq to produce the unique species in animals.csv. In order to avoid having to type out this series of commands every time, a scientist may choose to write a shell script instead.

Write a shell script called species.sh that takes any number of filenames as command-line arguments and uses a variation of the above command to print a list of the unique species appearing in each of those files separately.

### Exercise 2: Why Record Commands In The History Before Running Them?

If you run the command:

    $ history | tail -n 5 > recent.sh
the last command in the file is the history command itself, i.e., the shell has added history to the command log before actually running it. In fact, the shell always adds commands to the log before running them. Why do you think it does this?

### Exercise 3: Variables In Shell Scripts

In the alkanes directory, imagine you have a shell script called script.sh containing the following commands:

    head -n $2 $1
    tail -n $3 $1
While you are in the alkanes directory, you type the following command:

    $ bash script.sh '*.pdb' 1 1
Which of the following outputs would you expect to see?

1. All of the lines between the first and the last lines of each file ending in .pdb in the alkanes directory
2. The first and the last line of each file ending in .pdb in the alkanes directory
3. The first and the last line of each file in the alkanes directory
4. An error because of the quotes around *.pdb

### Exercise 4: Find The Longest File With A Given Extension

Write a shell script called longest.sh that takes the name of a directory and a filename extension as its arguments, and prints out the name of the file with the most lines in that directory with that extension. For example:

    $ bash longest.sh shell-lesson-data/exercise-data/alkanes pdb
would print the name of the .pdb file in shell-lesson-data/exercise-data/alkanes that has the most lines.

Feel free to test your script on another directory e.g.

    $ bash longest.sh shell-lesson-data/exercise-data/writing txt

### Exercise 5: Script Reading Comprehension

For this question, consider the shell-lesson-data/exercise-data/alkanes directory once again. This contains a number of .pdb files in addition to any other files you may have created. Explain what each of the following three scripts would do when run as bash script1.sh *.pdb, bash script2.sh *.pdb, and bash script3.sh *.pdb respectively.

    # Script 1
    echo *.*


    # Script 2
    for filename in $1 $2 $3
    do
        cat $filename
    done


    # Script 3
    echo $@.pdb

### Exercise 6: Debugging Scripts

Suppose you have saved the following script in a file called do-errors.sh in Nelle’s north-pacific-gyre directory:

    # Calculate stats for data files.
    for datafile in "$@"
    do
        echo $datfile
        bash goostats.sh $datafile stats-$datafile
    done

When you run it from the north-pacific-gyre directory:

    $ bash do-errors.sh NENE*A.txt NENE*B.txt

the output is blank. To figure out why, re-run the script using the -x option:

    $ bash -x do-errors.sh NENE*A.txt NENE*B.txt

What is the output showing you? Which line is responsible for the error?

