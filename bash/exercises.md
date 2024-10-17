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

cd .
cd /
cd /home/nelle
cd ../..
cd ~
cd home
cd ~/data/..
cd
cd ..

### Exercise 4: Relative Path Resolution

Using the filesystem diagram below, if pwd displays /Users/thing, what will ls -F ../backup display?
![Diagram of filesystem hierarchy](./filesystem-challenge.svg)
../backup: No such file or directory
2012-12-01 2013-01-08 2013-01-27
2012-12-01/ 2013-01-08/ 2013-01-27/
original/ pnas_final/ pnas_sub/

### Exercise 5: ls Reading Comprehension

Using the filesystem diagram below, if pwd displays /Users/backup, 
and -r tells ls to display things in reverse order, what command(s) 
will result in the following output:

    pnas_sub/ pnas_final/ original/

![Diagram of second filesystem hierarchy](./filesystem-challenge-2.svg)

ls pwd
ls -r -F
ls -r -F /Users/backup
