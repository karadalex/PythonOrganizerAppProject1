# Functions for converting a textfile to a single string or a list which has as elements the lines as strings:


def textFileToString(textFile):
    text = open(textFile, "r")
    string = ""
    for line in text:
        string += line
    text.close()
    return string

def textFileToListWithStrings(textFile):
    text = open(textFile, "r")
    listOfTextLinesStrings = []
    for line in text:
        listOfTextLinesStrings.append(line)
    text.close()
    return listOfTextLinesStrings
