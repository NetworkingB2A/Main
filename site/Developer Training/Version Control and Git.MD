# Version control
### What is Version control?
Version control is the ability to produce code to a repository and keep the history of all the changes made to that code. I should be able to go years back and look at a commit, to find out what changes were made with that one commit. 

### Advantages to version control?
- Version control allows multiple develops to work on the same code and avoid the problem with document locking.
- You can look through all the code changes and compare commit to commit to see the differences.
- You can branch and merge your code. which will allow you to work on code in an isolated environment. You can change code without hurting the main software. This will also help you to avoid conflicts, meaning that if you and someone else and editing the same line of code, you will not have to worry ( at least right now) about you change impacting their work. 

## Git
What is Git?
  - Git is a type of version control.
  - Git tracks changes to source code.
  - Git is a distributed version control system. Meaning everyone has a full copy of all the source code.
  - Github is a common platform for developing code. Keep in mind that Git and Github are two different items.
Understanding how git works
  - Git keeps a running history of every commit you make. This history (called a snapshot in git terms) details all the changes to the software over time and ensure the integrity o this record by using SHA-1 hash.
  - This has is 40 character string. It is possible that two commits could have the same hash, but that likelihood is almost impossible
Fun notes
- The standard user friendly commands are called "porcelain" commands. The more complicated inner workings of git are called "plumbing".
- Where ever the head is pointing is where you are currently working. if the head was pointed to 2 commits back you are working on code that is two commits old.

### Git tree structure

- Local workspace
  - This is where you store source code
- Staging area
  - This is an intermediary storage area
- Head, or local repository
  - This is where you store all committed items.

#### git file status
- Untracked
  - When you first create a file the file starts in untracked mode
- Unmodified
  - this is where git watches the file but file has been unchanged
- Modified
  - This is where you edit a file for your repo
- Staged
  - at this point your files has been committed. Now that the file has been committed the file moves back to unmodified status.


basic Git commands/terminology

create these first when you want to pull down config. This is meta data about yourself, needed for git commands later on.
  - git config --global user.name "Your Name"
  - git config --global user.email "your_email@whatever.com"

Creating a new repository
  - create a directory
    - mkdir train_git
    - cd train_git
    - touch "hello_world.txt"
  - create a new repository
    - git init 
      - This will create a repository for your project. That repository is stored on your computer.
    - git add hello_world.txt  
      - This will create a snapshot of the project. you can add a single file or many files. This didn't create the snapshot. this is just the first step. this is actually called the index in git.
    - git commit -m "adding first file" 
      - This will create a snapshot from your index, and this will add to your repository. good practice to give details about this commit. you should only commit the files that you want to change.
      - git message tips and tricks (https://chris.beams.io/posts/git-commit/)
        - separate subject line from body with a blank line 
        - limit the subject line to 50 characters
        - Capitalize the subject line
        - Do not end teh subject line with a period
        - use the imperative mood in the subject line 
        - Wrap the body at 72 characters
        - Use the body to explain what and why vs how


Data about your current git project ( I cant think of a better name yet.) 
  - git log 
    - this will show the history of the snapshot
    - git log -(number) 
      - this will show a certain number of commits
    - git log --oneline
      - shortens to one line showing commit message and hash code
    - git log --stat 
      - shows number of lines that changed with each commit 
    - git log --diff
      - shows all the differences in the commits
  - git status 
    - This will tell you if your file are committed in your repository.
    - You can put a --short or -s and you will see a shorter list of your current status ( kinda nice when you do this via cli)
  - git diff (some commit id) (some other commit id )
    - this will show the differences in the git snapshots. if you want to see the differences in your commits your must put the commit code. you only need to see the first few digits and not the whole code.
    - if you add a --staged you will see a difference between your committed files and your staged files 
    - if you want to see a difference in your working directory that has not been staged, just use a git diff.
    - if you add --cached : This command shows any changes between the index and your last commit
  - git reset  
    - this will allow us to throw changes away 
    - allows us to move commits from history to our working or staging area
    - can be a destructive command
    - three real options
      - use a --soft (commit-ID), move commit to staging area
      - use a --mixed (commit-ID), move commit to the working directory 
      - use a --hard (commit-ID), this will move you commits to the trash

Adding a file to the commit
git commit
  - good practice is to keep your commit messages under 50 characters 
  - git commit -m "your short message"

Adding/removing/Move a file
git add (file name or directory location)
  - Also called Git stages
  - This is stage your commit and get them ready for committing your change
  - You want to stage like code changes together and commit those changes at one time because you can add notes and look at different commits when auditing the code.
  - git add . or -A : Adds everything in the entire local workspace
  - git add {filename} : Adds a single file
git remove (file name or directory)
  - git rm (-r) (-f) {directory/file}
  - this will stop tracking a file/delete the file
  - Adding a --cached file name will stop tracking the file but will not remove it
git move
  - git mv (-f) {source} {destination}
  - This will move a file from one location to another location.
  - When you use this command you will not need to git add to add the file to a staging area.
git stash {parameters}
- temporarily store modified tracked files
- This is a good way to store your files quickly without doing a git commit.
- git stash pop brings your files back to the main workspace for you.


What is a Branch?
  - is a way of taking your code and branching off of your main code.
  - exactly like a tree
Creating a new branch
  - to add a new branch - git branch {branchname}
  - to delete a branch - git branch -d {branchname}
Moving toa  new branch
  - git checkout -b {branchname}
What is a conflict?
  - if two commits change the same line of code. you can have a conflict in that code.


git merge 
  git merge (main-branch)
  - this will allow you to keep two different versions of code and keep one as you main and the other as your different set of features. (kind of hard to explain for me.)
  - if you have an app. one paid version of the app and the other free version. if you wanted all you paid version of the app to have all the same features of your free version plus some extra features. you would do the following.
    - You would have two branches -Free -Paid
    - you would then switch to your paid version
    - You would then merge to your free version
    - doing this would allow you to take all your code from the free version and have it in your paid branch
    - But it would not work in reverse. your free version would not have the features from your paid version.
  - some terminology
    - Target branch - The branch of where the changes are being pulled from
    - Receiving branch - The branch where your changes are being pulled into.
  - Conflicts in file changes need to be resolved manually
  - You will often use a git merge and git fetch together.

  Fast forward merge
          --0--0--0 <- master branch
         /
  --0--0/

3-way merge
       ---0-0--0--
       /          \
      /            \        
--0--0----0----0----0-- Master

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

git clone "hyperlink"
   - this is copy a git repository to your computer

git pull
  - this will pull the updates from a online repository branch to your local repository and merge the branch.

git pull request
  - This one messed with my head for a while, the following is the best way I think to explain it
  - if you make a change to someone else's source code and you want that change to be in the source code you submit a pull request.
  - Meaning you are asking them to pull your changes into their code.

git remote {parameters}
- Manage remote repositories.






git branch 
 
 - To understand this it really helps to understand how pointers work or cnames
 - a Cname is just an alias that points to the main domain name. you can make changes to the cname and never update the original record.
 - In this case i can creating an alias of the code, updating the alias. Then later i may ask my branch to update the main code
 - This actual code will show the branches i have, or i can create and delete my branches 


git fetch 
  - Fetches changes from the remote repository.
  - Fetch will be used to get the remote branches
  - Fetch will get changes and store them in your local repository, a git pull will merge those changes

The only two reasons i would use this next part is
  - because I dont want to log into the gui
  - I want to change my repository name

Glossary
Repository is a directory that is initalized with git. It is where a all your files are stored.