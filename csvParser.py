'''
############################################################################################
# Csv Parser
# ----------
#
# "Takes a CSV document and converts it to a 2D-Array format."
#
# Copyright 2017 - William Read
#
############################################################################################
'''

# CsvParser Module

class CsvParser:
    ''' Class in which to allow for the parsing of Csv Files, to be in a suitable format to
read in Python. '''
    def __init__(self, csvFile):
        # Defines the output result and where the CSV is stored.
        self.csvResult = []
        self.csvFile = csvFile

        # Determine the csvFile arguement that is parsed is a valid csv document.
        try:
            readCsv = open(self.csvFile,'r')
        except IOError:
            sys.exit("Cannot open: "+self.csvFile)

        # Loops through all the lines in the csv file and adds them to the result
        # in a new array format.
        for row in readCsv:
            fields = row.split(',')
            self.csvResult.append(fields)

        self.csvResult = self.csvResult

    def getCsvParserContents(self):
        ''' Function to allow for retrieval of csv file generated from the initail call of
the class. '''
        return self.csvResult
