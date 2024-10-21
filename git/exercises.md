# Participant Exercises in Software Carpentry: Version Control With Git

## Section 1: Automated Version Control

### Exercise 1: Paper Writing

- Imagine you drafted an excellent paragraph for a paper you are writing, but later ruin it. How would you retrieve the excellent version of your conclusion? Is it even possible?
- Imagine you have 5 co-authors. How would you manage the changes and comments they make to your paper? If you use LibreOffice Writer or Microsoft Word, what happens if you accept changes made using the Track Changes option? Do you have a history of those changes?

## Section 3: Creating A Repository

### Exercise 1: Places To Create Git Repositories

Along with tracking information about recipes (the project we have already created), Alfredo would also like to track information about desserts specifically. Alfredo creates a desserts project inside his recipes project with the following sequence of commands:

    $ cd ~/Desktop    # return to Desktop directory
    $ cd recipes      # go into recipes directory, which is already a Git repository
    $ ls -a           # ensure the .git subdirectory is still present in the recipes directory
    $ mkdir desserts # make a sub-directory recipes/desserts
    $ cd desserts    # go into desserts subdirectory
    $ git init        # make the desserts subdirectory a Git repository
    $ ls -a           # ensure the .git subdirectory is present indicating we have created a new Git repository
Is the git init command, run inside the desserts subdirectory, required for tracking files stored in the desserts subdirectory?

### Exercise 2: Correcting git init Mistakes

Jimmy explains to Alfredo how a nested repository is redundant and may cause confusion down the road. 
Alfredo would like to go back to a single git repository. How can Alfredo undo his last git init in the desserts subdirectory?

