# Makefiles
compilation of Makefiles for software frameworks.

This repo includes a list of reusable Makefiles for popular languages and frameworks.  You may of course
copy files off this site and edit them to your liking.  The Makefiles on this site will be maintained in a 
way to make it easy to include them dynamically.  It is a goal of this project to give developers 
functionality without requiring installation of extra libraries.

## including Makefiles

Put the following at the start of your `Makefile` to include these resources dynamically.

e.g.

```
$(shell curl -o python.Makefile https://raw.githubusercontent.com/trevorgrayson/Makefiles/master/python/Makefile)
include python.Makefile
```
