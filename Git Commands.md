# Git Commands<br>
Git is a Version Controlling System (VCS), used to manage projects. To manage your PROJECT with **Git**, enter the following Commands as your need.<br><br>
For full Documentation on Git Visit [**Here**](https://git-scm.com/docs/) and [**Here**](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.md#styled-git-log) <br><br>
If you speak **Bengali**, you can visit [**Here**](https://www.youtube.com/watch?v=M2a7OQX8te4&index=1&list=PLoR56CteKZnC0lBlHdnVnq0J3yDhgbi9w) .



## Index: 
- [Git Initialize](#git-initialize) <br>
- [Add whole project to git](#add-whole-project-to-git-or-add-everything-in-a-directory) <br>
- [Adding File or Directory to git](#adding-file-or-directory-to-git) <br>
- [Remove from git before commit](#remove-from-git-before-commit) <br>
- [Status of Git](#status-of-git) <br>
- [Configuring Git](#configuring-git) <br>
- [Git Commit](#git-commit) <br>
- [Commit Count](#commit-count) <br>
- [Viewing the Commit History](#viewing-the-commit-history) <br>
- [Go back to previous commit](#go-back-to-previous-commit) <br>
- [Branching](#branching)
  - [View all branches](view-all-branches)
  - [Create new branch](create-new-branch)
  - [Delete branch](delete-branch)
  - [Rename the current branch](rename-the-current-branch)
- [Push an existing repository to server](#push-an-existing-repository-to-server) <br>
- [Pull or Fetch a repository from server to PC](#pull-or-fetch-a-repository-from-server-to-pc) <br>



## Git Initialize
**Command:** 
```cmd
git init
```
In a whole Project Directory, **git is to be initialized only once**, and obviously this is the first Command inside a Project Directory.<br><br>
[Return to Index](#index)


## Add whole project to git or add everything in a directory
At first, enter into the directory using `cd path/to/dir` & then run
```cmd
git add .
```
[Return to Index](#index)



## Adding File or Directory to git
**Adding a File:** 
```cmd
cd path/to/file's/dir
git add file_name.extension
```
Or 
```cmd
git add path/to/file_name.extension
```
**Adding multiple Files:** 
```cmd
cd path/to/files'/dir
git add file_name.extension file2_name.extension fileN_name.extension
```
Or 
```cmd
git add path/to/file1_name.extension path/to/file2_name.extension path/to/fileN_name.extension
```
**Adding a Directory:** 
```cmd
cd path/to/dir's/dir 
git add dir_name
```
**Adding multiple Directories:** 
```cmd
cd path/to/dirs'/dir 
git add dir1_name dir1_name dir2_name dirN_name
```
[Return to Index](#index)


## Remove from git before commit
To undo add for a singe file or directory
```cmd
git reset <filename or directory name>
```
To undo whole project
```cmd
git reset
```
[Return to Index](#index)


## Status of Git
```
git status
```
This Command will show you the UNTRACKED files, i.e. the files that have not yet been added to git, and the files that have been changed but not yet been committed. <br><br>
[Return to Index](#index)



## Configuring Git
**Default Configuration for all Repository:** <br>
To set your default account's identity, run following command
```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```
**Current Repository Configuration:** <br>
To set identity for the current repository only, run the following command (Just omit --global from the previous one) 
```
git config user.email "you@example.com"
git config user.name "Your Name"
```
**[Note]:** These configurations applies only to your local machine. <br>
**Change configuration:** <br>
Open **.giconfig** file in your home directory (~/.gitconfig) & edit the info and then **save** the file. <br>
**Viewing your configuration:** <br>
- Run `git config <KEY>` to get the value of KEY. KEY can be your user.namer, user.email or some other things. You can check  the keys running `git config --list` <br>
- To get username run `git config user.name` in your terminal. <br>
- To get user email run `git config user.email` in your terminal. <br>
- To get all configuration, run `git config --list` in your terminal. <br><br>
[Return to Index](#index)



## Git Commit
**Commit Single File:** <br>
```cmd
cd path/to/your/file's/dir
git commit -m "Your Commit Words" filename_with_extension
```
Or
```cmd
git commit -m "Your Commit Words" path/to/your/filename_with_extension 
```
**Commit all Uncommited files:**
```cmd
git commit -am "Your Commit Words"
```
**Commit all Files under a Directory Tree:**
```cmd
cd path/to/your/dirnames's/dir
git commit -m "Your Commit Words" dirname
```
Or
```cmd
git commit -m "Your Commit Words" path/to/dirname
```
[Return to Index](#index)



## Commit Count
**To get a commit count for a revision (HEAD, master, a commit hash)**
```
git rev-list --count <revision>
```
**To get the commit count across all branches**
```
git rev-list --all --count
```
**To count of commits grouped by committers**
```
git shortlog -s
```
[**Know more HERE**](https://stackoverflow.com/questions/677436/how-do-i-get-the-git-commit-count) <br><br>
[Return to Index](#index)

## Viewing the Commit History
#### Draw a text-based graphical representation of the commit history
```cmd
git log --oneline --graph --color --all --decorate
```
1. [**Watch this awesome Documentation to get clear concept**](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) <br><br>
2. [**git log [1]**](https://git-scm.com/docs/git-log) <br><br>
[Return to Index](#index)



## Go back to Previous Commit
**To view the files' content at a commit**
```cmd
git show <commit_hash>
```
**To view the Whole Project State at a specific commit**
```cmd
git checkout <commit_hash>
ls
```
**Getting back to your branch**
```cmd
git checkout <branch-name>
```
[Return to Index](#index)


## Branching
**Resources:** [**1**](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)  <br> <br>
### View all branches
**To view all branches**, enter the following command:
```cmd
git branch -a
```


### Create new branch
**To create a new branch**, first checkout to the parent branch where the child branch'll be created from.
```cmd
git checkout <branch-name>
```
Then execute following command.
```cmd
git branch <name-of-new-branch>
```
This will create the new branch, but won't switch to the newly created branch. <br> <br>
**To create new branch and immediately auto switching to the newly created branch instead.** <br>
At first checkout to the parent branch where the child branch'll be created from.
```cmd
git checkout <branch-name>
```
Then, execute the following command
```cmd
git branch -b <name-of-new-branch>
```
This will create a branch and will immediately checkout to the newly create branch immediately. <br> <br>
**Note**: Just write branch name using `-` or `_` separated words. **Don't use single or double quotes to name the branch**. <br>


### delete branch
**To delete branch locally:**
To delete a branch **safely**, at first checkout th another branch which is **not** going to be deleted. Then execute the following command.
```cmd
git branch -d <branch-not-to-be-deleted>
```
This deletes the specified branch. This is a “safe” operation in that, Git prevents you from deleting the branch if it has unmerged changes. <br> <br>

**But**, to delete a branch **forcely**, at first checkout th another branch which is **not** going to be deleted. Then execute the following command.
```cmd
git branch -D <branch-to-be-deleted>
```
Force delete the specified branch, even if it has unmerged changes. This is the command to use if you want to permanently throw away all of the commits associated with a particular line of development. <br> <br>

**To delete branch from remote:**
The previous commands will delete a local copy of a branch. The branch may still exist in remote repos. To delete a remote branch execute the following.
```cmd
git push origin --delete <branch-name>
```
or
```cmd
git push origin :<branch-name>
```

### Rename the current branch
- To rename the current branch where you are currently checked out
```cmd
git branch -m <new-name-of-current-branch>
```
- If you are on different branch, then
```cmd
git branch -m <old-name-of-branch> <new-name-of-branch>
```
- If the branch is on remote, delete the old-name remote branch and push the new-name local branch.
```cmd
git push origin :<old-name-of-branch> <new-name-of-branch>
```
- Reset the upstream branch for the new-name local branch. To do this, switch to the branch and then execute the following.
```cmd
git push origin -u <new-name-of-branch>
```
[Return to Index](#index)


## Push an existing repository to server
Usually **origin** is used as **remote name** & **master** is the **default branch** <br>
To push for the first time, add a remote at first. Otherwise skip this command.
```
git remote add <remote_name> <repo_URL>
```
If you have a remote which is already added, then run
```cmd
git push <remote_name> <branch_name>
```
Moreover, to get the remote list
```cmd
git remote show
```
And, to get info about a remote_name
```cmd
git remote show <remote_name>
```
[Return to Index](#index)



## Pull or Fetch a repository from server to PC
The **problem** with **pull** is that, it fetches and merges everything. There can happen merge conflict. So it is safe to use fetch command.
```cmd
git fetch
```
Then, checkout to the branch you want to work with.
```cmd
git checkout <branch-name>
```
Now, reset your-HEAD to the working-branch-HEAD
```cmd
git reset --hard <branch-name>
```
Usually **origin** is used as **remote name** & **master** is the **default branch** <br>
```cmd
git pull <remote_name> <branch_name>
```
[Return to Index](#index)



