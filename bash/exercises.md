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
