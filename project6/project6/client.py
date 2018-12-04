from fund import Fund

class Client:

    def __init__(self, firstName = None, lastName = None, id = None):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__id = id
        self.__funds = self.__createFunds__()
        self.__history = []
    
    def deposite(self, transaction):
        fund = transaction.getFundNum()
        self.__funds[int(fund)].deposite(transaction)
        self.__history.append(transaction)

    def withdraw(self, transaction):
        fund = transaction.getFundNum()
        self.__funds[int(fund)].withdraw(transaction)
        self.__history.append(transaction)

    def __createFunds__(self):
        FUND_NAMES = ["Money Market","Prime Money Market","Long-Term Bond","Short-Term Bond","500 Index Fund","Capital Value Fund","Growth Equity Fund","Growth Index Fund","Value Fund","Value Stock Index"]
        funds = []
        for i in range(len(FUND_NAMES)):
            funds.append(Fund(FUND_NAMES[i], i))
        return funds

    def getBalance(self, fundNum):
        return self.__funds[int(fundNum)].getBalance()

    def getId(self):
        return self.__id

    def getHistory(self):
        return self.__history

    def addHistory(self,transaction):
        self.__history.append(transaction)

    def getFund(self,fundNum,transaction):
        return self.__funds[int(fundNum)]

    def __str__(self):
        line = "First Name: " + str(self.__firstName) + ", Last Name: " + str(self.__lastName) + ", Account ID: " + str(self.__id)
        for each in self.__funds:
            line += "\n\t" + each.toString()
        line += "\n"
        return line

    



   

        


