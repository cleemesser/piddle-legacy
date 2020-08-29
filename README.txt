
[Eds NOTES: Legacy code:
I believe this was actively worked on in the 2000s using python 2 and various back end graphics libraries at the time. I'm preserving it here for reference. Joe Strout was the lead for the project with collaborators. It is reference in Andy Robinson's book by O'Reiley]


To install, type:

        python setup.py install

This should create a sub-directory, "piddle", where python modules are
installed for your system by default.  

To test, change to the "(topdirectory)/src/piddle" directory.  From a command prompt, type:

   python piddletest.py

This will give a text menu of options to try. 


On Mac OS, you have to go through a bit more effort to supply
command-line arguments to the setup script:

Option 1 (as described by Tom Loredo):
-------------------------------------
I can't vouch that Piddle has been updated to work properly this way
on the Mac, but what you should try is to drop the "setup.py" file
on the *Interpreter* (not the IDE), and when a command window pops
up, type in "build" (to build the package in the current directory)
or "install" (to build it and copy it to your site-packages directory
so it is accessible elsewhere).  As long as Piddle doesn't do something
out of the ordinary, this should work on a Mac (though if Piddle builds
C extensions, you'll need to have a copy of Codewarrior somewhere
on your drive, and if you don't have the newest version check the
MacPython page for info on what to change to get compatibility with
old Codewarrior).


Option 2:
--------
 * hit option-double-click on the script's icon (or option-drop it
   onto the Python interpreter's icon)

 * press the ``Set unix-style command line'' button

 * set the ``Keep stdio window open on termination'' if you're
   interested in seeing the output of the setup script (which is
   usually voluminous and often useful)

 * when the command-line dialog pops up, enter ``install'' (you
   can, of course, enter any Distutils command-line as described in
   this document or in Distributing Python Modules: just leave off
   the initial python setup.py and you'll be fine)





$Id$
