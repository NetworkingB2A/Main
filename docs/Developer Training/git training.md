What is Git?
  - Git allows you to have version control of your software.
  - Git tracks changes to source code.

Why do you need git?
  - git allows sharing code amongst developers




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
  - git reset  
    - this will allow us to throw changes away 
    - allows us to move commits from history to our working or staging area
    - can be a destructive command
    - three real options
      - use a --soft (commit-ID), move commit to staging area
      - use a --mixed (commit-ID), move commit to the working directory 
      - use a --hard (commit-ID), this will move you commits to the trash
  - git rm (file name)
    - this will stop tracking a file/delete the file
    - Adding a --cached file name will stop tracking the file but will not remove it

git checkout (newer versions of git can use a get switch)
  git checkout (some commit id)
  - this will allow you to change between commits
  - this will take that commit and puts in our file system
  - in doing this you can grab your old commit that was working and have it fix a new bug that you may have introduced 
  git checkout (branch-Name) or git switch (branch-Name)
  - This will allow you to Branch your code
  - When using the -c flag with git switch it will create a branch and switch it over the to new branch.
  - 

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
  - How to resolve conflicts?
    - multi-step process
    - Git tells you which file.
    - you need to open file and fix conflict.
      - You pick which changes you want. head is the one you are merging into, the other branch shows the code you are trying to merge in.
      - remove the conflict markers and save the new file and create a commit.
    - commit the fixed conflict.  
  
  Fast forward merge  
          --0--0--0 <- master branch
         /
  --0--0/

3-way merge
       ---0-0--0--
       /          \
      /            \        
--0--0----0----0----0-- Master



What is a Branch?
  - is a way of taking your code and branching off of your main code.
  - exactly like a tree

What is a conflict?
  - if two commits change the same line of code. you can have a conflict in that code.

What is HEAD?
- HEAD is essentially a pointer. if you switch from working on branch main to a branch called new_branch. then HEAD is moved from main to new_branch.

What is a detached head?
- You are pointing head at a specific commit and not at a branch reference in your repo.

How to reattach your head.
- You can switch to a branch and that will fix the detached head state.
- You can switch to a commit and then create a new branch which will fix HEAD again.

One way to undo changes to a file is to use the following command
- git restore <file name>

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

git clone "hyperlink"
   - this is copy a git repository to your computer

git pull
  - this will pull the updates from a online repository to your local repository.

git pull request
  - This one messed with my head for a while, the following is the best way I think to explain it
  - if you make a change to someone else's source code and you want that change to be in the source code you submit a pull request.
  - Meaning you are asking them to pull your changes into their code.


git add (file name or directory location)
  - Also called Git stages
  - This is stage your commit and get them ready for commiting your change
  - You want to stage like code changes together and commit those changes at one time because you can add notes and look at different commits when auditing the code.



git branch 
 
 - To understand this it really helps to understand how pointers work or cnames
 - a Cname is just an alias that points to the main domain name. you can make changes to the cname and never update the original record.
 - In this case i can creating an alias of the code, updating the alias. Then later i may ask my branch to update the main code
 - This actual code will show the branches i have, or i can create and delete my branches 



git pull vs git fetch 
  - A git fetch will pull down changes from the remote repo and put them into out local repo. The local repo is where a change goes once you have committed it. Those changes are not integrated into our working files.
  - A git pull will pull down the changes from the remote repo and install them into our workspace.

What is a git remote?
- Before we can push anything to Github we need to talk git about the remote repo on github. We need to setup a destination to push to.
- In git, we refer to these destinations as remotes. Each remote is simply a URL where a hosted repo lives.
- git remote or git remote -v
- when creating a new remote (which if you use a git clone this will happen automatically for you) use the following command. git remote add {name} {url}
- When you see "origin" that 

#### Git rebase
What is git rebase?
- Its a way to avoid doing merge commits. 
- Example - You are working on a branch and you want your branch to include the changes that were made to your main branch. normally you need to do a git pull to update your working files. then you need to merge the changes from main into your branch. when you do this merge you must create a kind of useless commit that is just a merge commit. and you may need to do this many many times as you keep working on your branch
- instead you can do a rebase and that allow you to skip doing a merge commit and essentially pull the changes from main into your branch without the commit.

What is the use case for git rebase?  
- There are two main ways to use the git rebase command:
  - as an alternative to merging
  - as a cleanup tool

When should you not use rebase?
- Golden rule - Never rebase commits that have been shared with others. if you have already pushed commits up to github... DO NOT rebase them unless you are positive no one on the team is using those commits.
