# summer-2020-reproducibility
A repo for learning ways to create reproducible code

## Helper instructions
To revert a commit, you can use the command `git revert <SHA>`, where `<SHA>` is the first 5-6 digits of the commit hash that you'd like to "undo".  At the command line, you can find the commit you'd like to revert by typing `git log`.  You can also peruse your commits on GitHub by clicking on the total number of commits in the bar above the main repo code page.

For example, to revert the changes done in commit `50c57856`, type `git revert 50c57856` at the command line.
