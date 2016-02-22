def createMenu(listOfChoices):
    """
    Description: returns a list of numbered menu options
    Precondition: listOfChoices is a list that indicate menu
             choices
    """
    tmp = "\nMENU\n"
    ct = 1
    for elem in listOfChoices:
        tmp += str(ct)+'. ' + elem + '\n'
        ct += 1
    return tmp
