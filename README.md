# Makefiles
compilation of Makefiles for software frameworks.

This repo includes a list of reusable Makefiles for popular languages and frameworks.  You may of course
copy files off this site and edit them to your liking.  

```
curl -o Makefile https://raw.githubusercontent.com/trevorgrayson/Makefiles/master/python/Makefile
```

The Makefiles on this site will be maintained in a way to make it easy to include them dynamically. Consider
putting the following at the start of your `Makefile` to include these resources dynamically.


```
$(shell test -f python.Makefile || curl -o python.Makefile https://raw.githubusercontent.com/trevorgrayson/Makefiles/master/python/Makefile)
include python.Makefile
```


## Goals

* Minimal installation requirements. `make` is installed in most development environments, that's dependency enough.
* Provide targets without library opinions. See previous.
* Don't remove functionality in the name of the previous two goals. If you have a solution, check it in, then remove dependencies if possible.
* Follow reasonable conventions.

## including Makefiles
