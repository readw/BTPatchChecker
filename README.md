# RouterPatchChecker
### By William Read
Router Patch Checker, to determine if a router needs updating based off of the following criteria:
* The router has not already been patched
* The current version of the router OS is 12 or above
* There are no other routers which share the same IP address
* There are no other routers which share the same hostname

In order to use the application you will need to do the following:
#### Software
Language: Python 2.7 (Developed in Python 2.7.13)
OS: Linux / Unix

#### Instructions
1. Download and extract the repository.

2. Next open up a terminal window in the directory with the 'routerPatchChecker.py'.

3. Enter the command:
> python routerPatchChecker.py sample.csv 12


This will then display all the results to the screen of all routers that require a server patch.

## Notes:
The arguements that follow routerPatchChecker.py represent:
* CSV Name and Location --> enter the directory and name of your csv document.
* Systems Version --> enter the version on which you filter through.
