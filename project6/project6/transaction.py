
class Transaction:

    def __init__(self, line):

        lineSplit = line.split()
        self.__transactionType = lineSplit[0]

        if lineSplit[0] == "O":
            self.__clientFirstName = lineSplit[2]
            self.__clientLastName = lineSplit[1]
            self.__clientId = lineSplit[3]

        elif lineSplit[0] == "D" or lineSplit[0] == "W":
            self.__clientId = lineSplit[1][0:4]
            self.__fundNumber = lineSplit[1][-1]
            self.__amount = lineSplit[2]

        elif lineSplit[0] == "T":
            self.__clientIdFrom = lineSplit[1]
            self.__clientIdTo = lineSplit[3]
            self.__fromFundNumber = lineSplit[1][-1]
            self.__toFundNumber = lineSplit[3][-1]
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

    def getAmount(self):
        return self.__amount

    #Used in transfer
    def getFrom(self):
        return self.__clientIdFrom

    def getTo(self):
        return self.__clientIdTo

    def getFundNumFrom(self):
        return self.__fromFundNumber

    def getFundNumTo(self):
        return self.__toFundNumber

    def getFundNum(self):
        return self.__fundNumber





