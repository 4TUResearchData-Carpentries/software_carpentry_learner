# Participant Exercises in Software Carpentry: The Unix Shell

## Section 2: Introducing The Shell

### Exercise 1: Exploring More ls Options

Like many shell commands, ls can also use two options at the same time. 
What does the command ls do when used with the -l option?
What about if you use both the -l and the -h option?

Some of its output is about properties that we do not cover in this lesson (such as file permissions and ownership), 
but the rest should be useful nevertheless.

### Exercise 2: Listing in Reverse Chronological Order 

By default, ls lists the contents of a directory in alphabetical order by name. 
The command ls -t lists items by time of last change instead of alphabetically. 
The command ls -r lists the contents of a directory in reverse order. 
Which file is displayed last when you combine the -t and -r options? 
Hint: You may need to use the -l option to see the last changed dates.

### Exercise 3: Absolute vs Relative Paths

Starting from /Users/nelle/data, which of the following commands could Nelle use to navigate to her home directory, which is /Users/nelle?

1. cd .
2. cd /
3. cd /home/nelle
4. cd ../..
5. cd ~
6. cd home
7. cd ~/data/..
8. cd
9. cd ..

### Exercise 4: Relative Path Resolution

Using the filesystem diagram below, if pwd displays /Users/thing, what will ls -F ../backup display?
![Diagram of filesystem hierarchy](./img/filesystem-challenge.svg)

1. ../backup: No such file or directory
2. 2012-12-01 2013-01-08 2013-01-27
3. 2012-12-01/ 2013-01-08/ 2013-01-27/
4. original/ pnas_final/ pnas_sub/

### Exercise 5: ls Reading Comprehension

Using the filesystem diagram below, if pwd displays /Users/backup, 
and -r tells ls to display things in reverse order, what command(s) 
will result in the following output:

    pnas_sub/ pnas_final/ original/

![Diagram of second filesystem hierarchy](./img/filesystem-challenge-2.svg)

1. ls pwd
2. ls -r -F
3. ls -r -F /Users/backup

## Section 3: Working With Files and Directories

### Exercise 1: Creating Files A Different Way

We have seen how to create text files using the nano editor. Now, try the following command:

    touch my_file.txt

1. What did the touch command do? When you look at your current directory using the GUI file explorer, does the file show up?
2. Use ls -l to inspect the files. How large is my_file.txt?
3. When might you want to create a file this way?

To avoid confusion later on, we suggest removing the file you’ve just created before proceeding with the rest of the episode, otherwise future outputs may vary from those given in the lesson. To do this, use the following command:

    rm my_file.txt

### Exercise 2: Moving Files To A New Folder

After running the following commands, Jamie realizes that she put the files sucrose.dat and 
maltose.dat into the wrong folder. The files should have been placed in the raw folder:

    $ ls -F
     analyzed/ raw/
    $ ls -F analyzed
     fructose.dat glucose.dat maltose.dat sucrose.dat
    $ cd analyzed

Fill in the blanks to move these files to the raw/ folder (i.e. the one she forgot to put them in):

    $ mv sucrose.dat maltose.dat ____/____

### Exercise 3: Renaming Files

Suppose that you created a plain-text file in your current directory to contain a list of the 
statistical tests you will need to do to analyze your data, and named it statstics.txt

After creating and saving this file you realize you misspelled the filename! 
You want to correct the mistake, which of the following commands could you use to do so:

1. cp statstics.txt statistics.txt
2. mv statstics.txt statistics.txt
3. mv statstics.txt .
4. cp statstics.txt .

### Exercise 4: Moving and Copying

What is the output of the closing ls command in the sequence shown below:

    $ pwd
     /Users/jamie/data

    $ ls
     proteins.dat

    $ mkdir recombined
    $ mv proteins.dat recombined/
    $ cp recombined/proteins.dat ../proteins-saved.dat
    $ ls

1. proteins-saved.dat recombined
2. recombined
3. proteins.dat recombined
4. proteins-saved.dat

### Exercise 5: Using rm Safely

What happens when we execute:

    rm -i thesis_backup/quotations.txt 

Why would we want this protection when using rm?

### Exercise 6: Copy With Multiple Filenames

For this exercise, you can test the commands in the shell-lesson-data/exercise-data directory.

In the example below, what does cp do when given several filenames and a directory name?

    $ mkdir backup
    $ cp creatures/minotaur.dat creatures/unicorn.dat backup/

In the example below, what does cp do when given three or more file names?

    $ cd creatures
    $ ls -F
     basilisk.dat  minotaur.dat  unicorn.dat
    $ cp basilisk.dat  minotaur.dat  unicorn.dat
    

### Exercise 7: List Filenames Matching A Pattern

When run in the alkanes directory, which ls command(s) will produce this output:

    ethane.pdb methane.pdb

1. ls *t*ane.pdb
2. ls *t?ne.*
3. ls *t??ne.pdb
4. ls ethane.*

### Exercise 8: More On Wildcards

Sam has a directory containing calibration data, datasets, and descriptions of the datasets:

    .
    ├── 2015-10-23-calibration.txt
    ├── 2015-10-23-dataset1.txt
    ├── 2015-10-23-dataset2.txt
    ├── 2015-10-23-dataset_overview.txt
    ├── 2015-10-26-calibration.txt
    ├── 2015-10-26-dataset1.txt
    ├── 2015-10-26-dataset2.txt
    ├── 2015-10-26-dataset_overview.txt
    ├── 2015-11-23-calibration.txt
    ├── 2015-11-23-dataset1.txt
    ├── 2015-11-23-dataset2.txt
    ├── 2015-11-23-dataset_overview.txt
    ├── backup
    │   ├── calibration
    │   └── datasets
    └── send_to_bob
        ├── all_datasets_created_on_a_23rd
        └── all_november_files

Before heading off to another field trip, she wants to back up her data and send some datasets 
to her colleague Bob. Sam uses the following commands to get the job done:

    $ cp *dataset* backup/datasets
    $ cp ____calibration____ backup/calibration
    $ cp 2015-____-____ send_to_bob/all_november_files/
    $ cp ____ send_to_bob/all_datasets_created_on_a_23rd/

Help Sam by filling in the blanks.

The resulting directory structure should look like this:

    .
    ├── 2015-10-23-calibration.txt
    ├── 2015-10-23-dataset1.txt
    ├── 2015-10-23-dataset2.txt
    ├── 2015-10-23-dataset_overview.txt
    ├── 2015-10-26-calibration.txt
    ├── 2015-10-26-dataset1.txt
    ├── 2015-10-26-dataset2.txt
    ├── 2015-10-26-dataset_overview.txt
    ├── 2015-11-23-calibration.txt
    ├── 2015-11-23-dataset1.txt
    ├── 2015-11-23-dataset2.txt
    ├── 2015-11-23-dataset_overview.txt
    ├── backup
    │   ├── calibration
    │   │   ├── 2015-10-23-calibration.txt
    │   │   ├── 2015-10-26-calibration.txt
    │   │   └── 2015-11-23-calibration.txt
    │   └── datasets
    │       ├── 2015-10-23-dataset1.txt
    │       ├── 2015-10-23-dataset2.txt
    │       ├── 2015-10-23-dataset_overview.txt
    │       ├── 2015-10-26-dataset1.txt
    │       ├── 2015-10-26-dataset2.txt
    │       ├── 2015-10-26-dataset_overview.txt
    │       ├── 2015-11-23-dataset1.txt
    │       ├── 2015-11-23-dataset2.txt
    │       └── 2015-11-23-dataset_overview.txt
    └── send_to_bob
        ├── all_datasets_created_on_a_23rd
        │   ├── 2015-10-23-dataset1.txt
        │   ├── 2015-10-23-dataset2.txt
        │   ├── 2015-10-23-dataset_overview.txt
        │   ├── 2015-11-23-dataset1.txt
        │   ├── 2015-11-23-dataset2.txt
        │   └── 2015-11-23-dataset_overview.txt
        └── all_november_files
            ├── 2015-11-23-calibration.txt
            ├── 2015-11-23-dataset1.txt
            ├── 2015-11-23-dataset2.txt
            └── 2015-11-23-dataset_overview.txt

### Exercise 9: Organizing Directories And Files

Jamie is working on a project, and she sees that her files aren’t very well organized:

    $ ls -F
     analyzed/  fructose.dat    raw/   sucrose.dat

The fructose.dat and sucrose.dat files contain output from her data analysis.
What command(s) covered in this lesson does she need to run so that the commands below 
will produce the output shown?

    $ ls -F
     analyzed/   raw/

    $ ls analyzed
     fructose.dat    sucrose.dat

### Exercise 10: Reproduce A Folder Structure

You’re starting a new experiment and would like to duplicate the directory structure from your previous experiment so you can add new data.

Assume that the previous experiment is in a folder called 2016-05-18, which contains a data folder 
that in turn contains folders named raw and processed that contain data files. The goal is to copy 
the folder structure of the 2016-05-18 folder into a folder called 2016-05-20 so that your final 
directory structure looks like this:

    2016-05-20/
    └── data
       ├── processed
       └── raw

Which of the following set of commands would achieve this objective? What would the other commands do?

#### A
    $ mkdir 2016-05-20
    $ mkdir 2016-05-20/data
    $ mkdir 2016-05-20/data/processed
    $ mkdir 2016-05-20/data/raw

#### B
    $ mkdir 2016-05-20
    $ cd 2016-05-20
    $ mkdir data
    $ cd data
    $ mkdir raw processed

#### C
    $ mkdir 2016-05-20/data/raw
    $ mkdir 2016-05-20/data/processed

#### D
    $ mkdir -p 2016-05-20/data/raw
    $ mkdir -p 2016-05-20/data/processed

#### E
    $ mkdir 2016-05-20
    $ cd 2016-05-20
    $ mkdir data
    $ mkdir raw processed

## Section 4: Pipes and Filters

### Exercise 1: What Does sort -n Do?

The file shell-lesson-data/exercise-data/numbers.txt contains the following lines:

    10
    2
    19
    22
    6
If we run sort on this file, the output is:

    10
    19
    2
    22
    6
If we run sort -n on the same file, we get this instead:

    2
    6
    10
    19
    22
Explain why -n has this effect.

### Exercise 2: What Does >> Mean?

We have seen the use of >, but there is a similar operator >> which works slightly differently. We’ll learn about the differences between these two operators by printing some strings. We can use the echo command to print strings e.g.


    $ echo The echo command prints text
    The echo command prints text
Now test the commands below to reveal the difference between the two operators:

    $ echo hello > testfile01.txt
and:

    $ echo hello >> testfile02.txt
Hint: Try executing each command twice in a row and then examining the output files.

### Exercise 3: Appending Data

We have already met the head command, which prints lines from the start of a file. tail is similar, but prints lines from the end of a file instead.

Consider the file shell-lesson-data/exercise-data/animal-counts/animals.csv. After these commands, select the answer that corresponds to the file animals-subset.csv:

    $ head -n 3 animals.csv > animals-subset.csv
    $ tail -n 2 animals.csv >> animals-subset.csv

1. The first three lines of animals.csv
2. The last two lines of animals.csv
3. The first three lines and the last two lines of animals.csv
4. The second and third lines of animals.csv

### Exercise 4: Piping Commands Together

In our current directory, we want to find the 3 files which have the least number of lines. Which command listed below would work?

1. wc -l * > sort -n > head -n 3
2. wc -l * | sort -n | head -n 1-3
3. wc -l * | head -n 3 | sort -n
4. wc -l * | sort -n | head -n 3

### Exercise 5: Pipe Reading Comprehension

A file called animals.csv (in the shell-lesson-data/exercise-data/animal-counts folder) contains the following data:

    2012-11-05,deer,5
    2012-11-05,rabbit,22
    2012-11-05,raccoon,7
    2012-11-06,rabbit,19
    2012-11-06,deer,2
    2012-11-06,fox,4
    2012-11-07,rabbit,16
    2012-11-07,bear,1
What text passes through each of the pipes and the final redirect in the pipeline below? Note, the sort -r command sorts in reverse order.

    $ cat animals.csv | head -n 5 | tail -n 3 | sort -r > final.txt
Hint: build the pipeline up one command at a time to test your understanding

### Exercise 6: Pipe Construction

For the file animals.csv from the previous exercise, consider the following command:

    $ cut -d , -f 2 animals.csv
The cut command is used to remove or ‘cut out’ certain sections of each line in the file, and cut expects the lines to be separated into columns by a Tab character. A character used in this way is called a delimiter. In the example above we use the -d option to specify the comma as our delimiter character. We have also used the -f option to specify that we want to extract the second field (column). This gives the following output:

    deer
    rabbit
    raccoon
    rabbit
    deer
    fox
    rabbit
    bear
The uniq command filters out adjacent matching lines in a file. How could you extend this pipeline (using uniq and another command) to find out what animals the file contains (without any duplicates in their names)?

### Exercise 7: Which Pipe?

The file animals.csv contains 8 lines of data formatted as follows:

    2012-11-05,deer,5
    2012-11-05,rabbit,22
    2012-11-05,raccoon,7
    2012-11-06,rabbit,19
    ...
The uniq command has a -c option which gives a count of the number of times a line occurs in its input. Assuming your current directory is shell-lesson-data/exercise-data/animal-counts, what command would you use to produce a table that shows the total count of each type of animal in the file?

    sort animals.csv | uniq -c
    sort -t, -k2,2 animals.csv | uniq -c
    cut -d, -f 2 animals.csv | uniq -c
    cut -d, -f 2 animals.csv | sort | uniq -c
    cut -d, -f 2 animals.csv | sort | uniq -c | wc -l

### Exercise 8: Removing Unneeded Files

Suppose you want to delete your processed data files, and only keep your raw files and processing script to save storage. The raw files end in .dat and the processed files end in .txt. Which of the following would remove all the processed data files, and only the processed data files?

1. rm ?.txt
2. rm *.txt
3. rm * .txt
4. rm *.*


## Section 5: Loops

### Exercise 1: Write Your Own Loop

How would you write a loop that echoes all 10 numbers from 0 to 9?

### Exercise 2: Variables In Loops

This exercise refers to the shell-lesson-data/exercise-data/alkanes directory. ls *.pdb gives the following output:

    cubane.pdb  ethane.pdb  methane.pdb  octane.pdb  pentane.pdb  propane.pdb
What is the output of the following code?

    $ for datafile in *.pdb
    > do
    >     ls *.pdb
    > done
Now, what is the output of the following code?

    $ for datafile in *.pdb
    > do
    >     ls $datafile
    > done
Why do these two loops give different outputs?

### Exercise 3: Limiting Sets Of Files

What would be the output of running the following loop in the shell-lesson-data/exercise-data/alkanes directory?

    $ for filename in c*
    > do
    >     ls $filename
    > done

1. No files are listed.
2. All files are listed.
3. Only cubane.pdb, octane.pdb and pentane.pdb are listed.
4. Only cubane.pdb is listed.

### Exercise 4: Limiting Sets Of Files (Continued)

How would the output differ from using this command instead?

    $ for filename in *c*
    > do
    >     ls $filename
    > done

1. The same files would be listed.
2. All the files are listed this time.
3. No files are listed this time.
4. The files cubane.pdb and octane.pdb will be listed.
5. Only the file octane.pdb will be listed.

### Exercise 5: Saving To A File In A  Loop - Part One

In the shell-lesson-data/exercise-data/alkanes directory, what is the effect of this loop?

    for alkanes in *.pdb
    do
        echo $alkanes
        cat $alkanes > alkanes.pdb
    done

1. Prints cubane.pdb, ethane.pdb, methane.pdb, octane.pdb, pentane.pdb and propane.pdb, and the text from propane.pdb will be saved to a file called alkanes.pdb.
2. Prints cubane.pdb, ethane.pdb, and methane.pdb, and the text from all three files would be concatenated and saved to a file called alkanes.pdb.
3. Prints cubane.pdb, ethane.pdb, methane.pdb, octane.pdb, and pentane.pdb, and the text from propane.pdb will be saved to a file called alkanes.pdb.
4. None of the above.

### Exercise 6: Saving To A File In A  Loop - Part Two

Also in the shell-lesson-data/exercise-data/alkanes directory, what would be the output of the following loop?

    for datafile in *.pdb
    do
        cat $datafile >> all.pdb
    done
    
1. All of the text from cubane.pdb, ethane.pdb, methane.pdb, octane.pdb, and pentane.pdb would be concatenated and saved to a file called all.pdb.
2. The text from ethane.pdb will be saved to a file called all.pdb.
3. All of the text from cubane.pdb, ethane.pdb, methane.pdb, octane.pdb, pentane.pdb and propane.pdb would be concatenated and saved to a file called all.pdb.
4. All of the text from cubane.pdb, ethane.pdb, methane.pdb, octane.pdb, pentane.pdb and propane.pdb would be printed to the screen and saved to a file called all.pdb.

### Exercise 7: Doing A Dry Run

A loop is a way to do many things at once — or to make many mistakes at once if it does the wrong thing. One way to check what a loop would do is to echo the commands it would run instead of actually running them.

Suppose we want to preview the commands the following loop will execute without actually running those commands:

    $ for datafile in *.pdb
    > do
    >     cat $datafile >> all.pdb
    > done
What is the difference between the two loops below, and which one would we want to run?

    # Version 1
    $ for datafile in *.pdb
    > do
    >     echo cat $datafile >> all.pdb
    > done


    # Version 2
    $ for datafile in *.pdb
    > do
    >     echo "cat $datafile >> all.pdb"
    > done

### Exercise 8: Nested Loops

Suppose we want to set up a directory structure to organize some experiments measuring reaction rate constants with different compounds and different temperatures. What would be the result of the following code:

    $ for species in cubane ethane methane
    > do
    >     for temperature in 25 30 37 40
    >     do
    >         mkdir $species-$temperature
    >     done
    > done
