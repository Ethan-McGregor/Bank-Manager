
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

    def deposite(self):
        pass

    def withdraw(self):
        pass
