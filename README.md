# summer-2020-reproducibility
A repo for learning ways to create reproducible code

# Helper instructions
## Git with RStudio Cloud
To configure your username and email address with RStudio cloud for this project, make sure to enter the following lines at the command line/terminal:
```
git config --global user.email "name@email.com"
git config --global user.name "My Name"
```
Make sure you leave the quotes around your email address and name.

## RStudio git commit messages
On RStudio cloud, git sometimes opens up a `vi/vim` editor for you to enter your commit messages.  If you are in this situation:
- **I want to edit the commit message**:  To do this, click the `insert` button on your keyboard.  Enter your commit message in areas not preceded by the `#` symbol.  Click `esc` to exit the editing mode.
- **I want to save my changes and exit vim**: If you're in editing mode (you clicked the `insert` button on your keyboard), click the `esc` key.  Now, type `:wq!`
- **The commit message is fine - I just want to exit.**: If you're in editing mode (you clicked the `insert` button your keyboard), click the `esc` key.  Now, type `:q`

## Reverting commits
To revert a commit, you can use the command `git revert <SHA>`, where `<SHA>` is the first 5-6 digits of the commit hash that you'd like to "undo".  At the command line, you can find the commit you'd like to revert by typing `git log`.  You can also peruse your commits on GitHub by clicking on the total number of commits in the bar above the main repo code page.

For example, to revert the changes done in commit `50c57856`, type `git revert 50c57856` at the command line.
