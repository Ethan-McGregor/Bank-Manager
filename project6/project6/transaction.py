
class Transaction:

    def __init__(self, line):

        lineSplit = line.split()
        self.__transactionType = lineSplit[0]

        if lineSplit[0] == "O":
            self.__clientFirstName = lineSplit[2]
            self.__clientLastName = lineSplit[1]
            self.__clientId = lineSplit[3]

        elif lineSplit[0] == "D" or lineSplit[0] == "W":
            self.__clientId = lineSplit[2][0:4]
            self.__fundNumber = lineSplit[2][-1]
            self.__amount = lineSplit[1]

        elif lineSplit[0] == "T":
            self.__clientId1 = lineSplit[1]
            self.__clientId2 = lineSplit[3]
            self.__amount = lineSplit[2]
        else:
            if len(lineSplit[1]) == 4:
                self.__clientId = lineSplit[1]
            else:
                self.__clientId =lineSplit[1][0:4]
                self.__fundNumber = lineSplit[1][-1]

    def getTransactionType(self):
        return self.__transactionType

    def getFirstName(self):
        return self.__clientFirstName

    def getLastName(self):
        return self.__clientLastName

    def getId(self):
        return self.__clientId


