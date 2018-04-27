# Git Commands<br>
Git is a Version Controlling System (VCS), used to manage projects. To manage your PROJECT with **Git**, enter the following Commands as your need.<br><br>
For full Documentation on Git Visit [**Here**](https://git-scm.com/docs/) and [**Here**](https://github.com/tiimgreen/github-cheat-sheet/blob/master/README.md#styled-git-log) <br><br>
If you speak **Bengali**, you can visit [**Here**](https://www.youtube.com/watch?v=M2a7OQX8te4&index=1&list=PLoR56CteKZnC0lBlHdnVnq0J3yDhgbi9w) .



## Index: 
- [Git Initialize](#git-initialize) <br>
- [Adding File or Directory to git](#adding-file-or-directory-to-git) <br>
- [Status of Git](#status-of-git) <br>
- [Configuring Git](#configuring-git) <br>
- [Git Commit](#git-commit) <br>
- [Commit Count](#commit-count) <br>
- [Viewing the Commit History](#viewing-the-commit-history)
- [Go back to previous commit](#go-back-to-previous-commit) <br>



## Git Initialize
**Command:** 
```cmd
git init
```
In a whole Project Directory, **git is to be initialized only once**, and obviously this is the first Command inside a Project Directory.<br><br>
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
git commit -m dirname
```
Or
```cmd
git commit -m path/to/dirname
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
[**Watch this awesome Documentation to get clear concept**](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History) <br><br>
[Return to Index](#index)



## Go back to Previous Commit
**To view the files' content at a commit**
```cmd
git show <commit_hash>
```
**To view the Whole Project State at a commit**
```cmd
git checkout <commit_hash>
ls
```
**Getting back to last commit, i.e. to master branch**
```cmd
git checkout master
```
[Return to Index](#index)





