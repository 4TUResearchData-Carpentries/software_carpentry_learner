# Solutions to Exercises in Software Carpentry: Version Control With Git

## Section 1: Automated Version Control

### Exercise 1: Paper Writing

- Recovering the excellent version is only possible if you created a copy of the old version of the paper. The danger of losing good versions often leads to the problematic workflow illustrated in the PhD Comics cartoon at the top of this page.
- Collaborative writing with traditional word processors is cumbersome. Either every collaborator has to work on a document sequentially (slowing down the process of writing), or you have to send out a version to all collaborators and manually merge their comments into your document. The ‘track changes’ or ‘record changes’ option can highlight changes for you and simplifies merging, but as soon as you accept changes you will lose their history. You will then no longer know who suggested that change, why it was suggested, or when it was merged into the rest of the document. Even online word processors like Google Docs or Microsoft Office Online do not fully resolve these problems.

## Section 3: Crearting A Repository

### Exercise 1: Places To Create Git Repositories

No. Alfredo does not need to make the desserts subdirectory a Git repository because the recipes repository will track all files, 
sub-directories, and subdirectory files under the recipes directory. Thus, in order to track all information about desserts, 
Alfredo only needed to add the desserts subdirectory to the recipes directory.

Additionally, Git repositories can interfere with each other if they are “nested”: the outer repository will try to version-control 
the inner repository. Therefore, it’s best to create each new Git repository in a separate directory. To be sure that there is no 
conflicting repository in the directory, check the output of git status. If it looks like the following, you are good to go to create 
a new repository as shown above:

    $ git status
    fatal: Not a git repository (or any of the parent directories): .git

### Exercise 2: Correcting git init Mistakes

**Background**

Removing files from a Git repository needs to be done with caution. But we have not learned yet how to tell Git to track a particular file; we will learn this in the next episode. Files that are not tracked by Git can easily be removed like any other “ordinary” files with

    $ rm filename
Similarly a directory can be removed using rm -r dirname. If the files or folder being removed in this fashion are tracked by Git, then their removal becomes another change that we will need to track, as we will see in the next episode.

**Solution**

Git keeps all of its files in the .git directory. To recover from this little mistake, Alfredo can remove the .git folder in the desserts subdirectory by running the following command from inside the recipes directory:

    $ rm -rf desserts/.git
But be careful! Running this command in the wrong directory will remove the entire Git history of a project you might want to keep. In general, deleting files and directories using rm from the command line cannot be reversed. Therefore, always check your current directory using the command pwd.

## Section 4: Tracking Changes

### Exercise 1: Choosing A Commit Message

Answer 1 is not descriptive enough, and the purpose of the commit is unclear; and answer 2 is redundant to using “git diff” to see what changed in this commit; but answer 3 is good: short, descriptive, and imperative.

### Exercise 2: Committing Changes To git

1. Would only create a commit if files have already been staged.
2. Would try to create a new repository.
3. Is correct: first add the file to the staging area, then commit.
4. Would try to commit a file “my recent changes” with the message myfile.txt.

### Exercise 3: Committing Multiple Files

First we make our changes to the guacamole.md and groceries.md files:

    $ nano guacamole.md
    $ cat guacamole.md
    # Guacamole
    ## Ingredients
    * avocado (1.35)
    * lime (0.64)
    * salt (2)


    $ nano groceries.md
    $ cat groceries.md

    # Market A
    * avocado: 1.35 per unit.
    * lime: 0.64 per unit
    * salt: 2 per kg
Now you can add both files to the staging area. We can do that in one line:

    $ git add guacamole.md groceries.md
Or with multiple commands:

    $ git add guacamole.md
    $ git add groceries.md
Now the files are ready to commit. You can check that using git status. If you are ready to commit use:

    $ git commit -m "Write prices for ingredients and their source"
    [main cc127c2]
    Write prices for ingredients and their source
    2 files changed, 7 insertions(+)
    create mode 100644 groceries.md

### Exercise 4: bio Repository

If needed, move out of the recipes folder:

    $ cd ..
Create a new folder called bio and ‘move’ into it:

    $ mkdir bio
    $ cd bio
Initialise git:

    $ git init
Create your biography file me.txt using nano or another text editor. Once in place, add and commit it to the repository:

    $ git add me.txt
    $ git commit -m "Add biography file"
Modify the file as described (modify one line, add a fourth line). To display the differences between its updated state and its original state, use git diff:

    $ git diff me.txt

## Section 5: Exploring History
