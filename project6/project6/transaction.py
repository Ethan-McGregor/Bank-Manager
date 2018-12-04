
class Transaction:

    def __init__(self, line):

        lineSplit = line.split()
        self.__transactionType = lineSplit[0]
        self.__error = None
        if lineSplit[0] == "O":
            self.__clientFirstName = lineSplit[2]
            self.__clientLastName = lineSplit[1]
            self.__clientId = lineSplit[3]

        elif lineSplit[0] == "D" or lineSplit[0] == "W":
            self.__clientId = lineSplit[1][0:4]
            self.__fundNumber = lineSplit[1][-1]
            self.__amount = lineSplit[2]

        elif lineSplit[0] == "T":
            self.__clientIdFrom = lineSplit[1][0:4]
            self.__clientIdTo = lineSplit[3][0:4]
            self.__fromFundNumber = lineSplit[1][-1]
            self.__toFundNumber = lineSplit[3][-1]
            self.__amount = lineSplit[2]
        else:
            if len(lineSplit[1]) == 4:
                self.__clientId = lineSplit[1]
                self.__fundNumber = None
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
   
    def makeError(self,error):
        self.__error = error
        return True

    def __str__(self):
        line = ""

        if self.__transactionType == "O":
            line += "Account Opened: " + str(self.__clientFirstName) + " " + str(self.__clientLastName) + ", ID: " + str(self.__clientId)
        elif self.__transactionType == "D":
             line += "Deposite Amount: " + str(self.__amount) + " To fund:" + str(self.__fundNumber) + ", Account ID: " + str(self.__clientId)
        elif self.__transactionType == "W":
            line += "Withtdraw Amount: " + str(self.__amount) + " To fund:" + str(self.__fundNumber) + ", Account ID: " + str(self.__clientId)
        elif self.__transactionType == "H":
            line += "History acess: " + ", Account ID: " + str(self.__clientId)

        if self.__error != None:
            line += "\n\t" + self.__error
        return "\t" + line



