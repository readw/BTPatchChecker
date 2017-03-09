'''
############################################################################################
# Router Patch Checker
# --------------------
#
# "Takes CSV input and prints output of formatted strings to display all the routers that
# require a new patch."
#
# Copyright 2017 - William Read
#
############################################################################################
'''

# System Imports
import sys
import csvParser

# Main Application
class Patches:
    ''' Determines whether or not a router needs a patch in order to improve
their services. '''
    def __init__(self, csvContents, patchVersion):
        # Set max version on which to patch.
        self.patchVersion = patchVersion

        # Passes CSV file through all filters returns result.
        self.results = self.compareHost(self.compareAddress(self.checkVersion(self.checkPatched(csvContents))))
        
    def checkPatched(self, results):
        '''Determines if a users system has recieved the current patch'''
        notPatched = []
        for result in results:
            # Checks if the users system has been patched.
            if (result[2].upper() == "NO"):
                # Appends the results of all routers that haven't been patched.
                notPatched.append(result)
        return notPatched

    def checkVersion(self, results):
        '''Takes inputted version from terminal and filters out routers below this version. '''
        patchVersion = []
        for result in results:
            # Determines if the number of patch / csv file is a valid floating value.
            try:
                if (float(result[3]) >= float(self.patchVersion)):
                    # Appends all values less than or greater than the current patch version.
                    patchVersion.append(result)
            except ValueError:
                sys.exit("ERROR: Value found isn't a numerical value.")
        return patchVersion
    
    def compareAddress(self, results):
        ''' Compares to see if the IP addresses are identical, and removes any identical values. '''
        uniqueAddress = []
        for result in results:
            unique = True
            for compare in results:
                # If the comparison value is the same as the result, then ignore it.
                if (compare != result):
                    # Checks to see if the addresses match.
                    if (result[1] == compare[1]):
                        unique = False
                        break
                continue
            if (unique == True):
                # Appends the result to the uniqueHost array if they are unique.
                uniqueAddress.append(result)
        return uniqueAddress

    def compareHost(self, results):
        ''' Compare the hosts of all routers and remove details of all the hosts with duplicate
user names. '''
        uniqueHost = []
        for result in results:
            # Starts by defining the current result as unique
            unique = True
            for compare in results:
                # If the comparison value is the same as the result, then ignore it.
                if (compare != result):
                    # Formats the host names into uppercase, and compares to see if the results
                    # match each other.
                    if (result[0].upper() == compare[0].upper()):
                        unique = False
                        break
                continue
            if (unique == True):
                # Appends the result to the uniqueHost array if they are unique.
                uniqueHost.append(result)
        return uniqueHost
    
    def getRoutersToPatch(self):
        ''' Outputs the formatted results of all the routers needing a patch. 
Possible Formats:
b.example.com (1.1.1.2), OS Version 13 [Behind the other routers so no one sees it]
f.example.com (1.1.1.7), OS Version 12.200'''
        # Iterates through the results and determines the output based on whether notes have been
        # added or not to the router.
        for row in self.results:
            if (row[4] == '' or row[4] == '\r\n'):
                print("{0} ({1}), OS Version {2}\r".format(row[0],row[1],row[3]))
            else:
                print("{0} ({1}), OS Version {2} [{3}]\r".format(row[0],row[1],row[3],row[4].rstrip()))

if __name__ == "__main__":
    # Catches if the user has entered the command in the correct format.
    try:
        csvFileName = sys.argv[1]
        patchVersion = sys.argv[2]
    except Exception:
        sys.exit("ERROR: Make sure format is - 'python routerPatchChecker.py yourfile.csv versionNo'")

    # Creates CSV, Filters CSV and outputs the response of all the routers needing a patch.
    csvContents = csvParser.CsvParser(csvFileName)
    patchUpdates = Patches(csvContents.getCsvParserContents(), patchVersion)
    patchUpdates.getRoutersToPatch()
    
