
class Fund:

    def __init__(self,fundName, fundNum):
        self.__fundName = fundName
        self.__fundNum = fundNum
        self.__balance = 0
        self.__history = []

    def getFundName(self):
        return self.__fundName

    def getBalance(self):
        return self.__balance

    def getHistory(self):
        return self.__history

    def addHistory(self, transaction):
        self.__history.append(transaction)

    def deposite(self, transaction):
        amount = transaction.getAmount()
        self.__balance += int(amount)
        self.__history.append(transaction)

    def withdraw(self, transaction):
        amount = transaction.getAmount()
        if int(amount) > self.__balance:
            error = "ERROR: Cannot withdraw $" + str(amount)+ " from: " + self.__fundName + ", Balance is: " + str(self.__balance)
            print(error)
            transaction.makeError(error)
        else:

            self.__balance -= int(amount)
        self.__history.append(transaction)

    def toString(self):
        line = ""
        line += "Fund: " + str(self.__fundName) + ", Balance: " + str(self.__balance)
        return line