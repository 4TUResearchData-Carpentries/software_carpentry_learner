# Participant Exercises in Software Carpentry: The Unix Shell


**### Exercise 1: Relative Path Resolution** (specific for the lesson)

Using the filesystem diagram below, if pwd displays /Users/thing, what will ls -F ../backup display?

../backup: No such file or directory
2012-12-01 2013-01-08 2013-01-27
2012-12-01/ 2013-01-08/ 2013-01-27/
original/ pnas_final/ pnas_sub/



**## Exercise 2: Moving Files to a new folder** (specific for the lesson)

After running the following commands,
Jamie realizes that she put the files `sucrose.dat` and `maltose.dat` into the wrong folder.
The files should have been placed in the `raw` folder.

```bash
$ ls -F
 analyzed/ raw/
$ ls -F analyzed
fructose.dat glucose.dat maltose.dat sucrose.dat
$ cd analyzed
```

Fill in the blanks to move these files to the `raw/` folder
(i.e. the one she forgot to put them in)

```bash
$ mv sucrose.dat maltose.dat ____/____
```



## Exercise 3: List filenames matching a pattern

https://swcarpentry.github.io/shell-novice/instructor/03-create.html#operations-with-multiple-files-and-directories


When run in the alkanes directory, which ls command(s) will produce this output?

ethane.pdb methane.pdb

1. ls *t*ane.pdb
2. ls *t?ne.*
3. ls *t??ne.pdb
4. ls ethane.*

### Exercise 4: Matching and Subtracting (https://swcarpentry.github.io/shell-novice/07-find.html)

The -v option to grep inverts pattern matching, so that only lines which do not match the pattern are printed. Given that, which of the following commands will find all .dat files in creatures except unicorn.dat? Once you have thought about your answer, you can test the commands in the shell-lesson-data/exercise-data directory.

1. `find creatures -name "*.dat" | grep -v unicorn`
2. `find creatures -name *.dat | grep -v unicorn`
3. `grep -v "unicorn" $(find creatures -name "*.dat")`
4. `None of the above.`