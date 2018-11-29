from fund import Fund
class Client:

    def __init__(self,firstName = None,lastName = None,id = None):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__id = id
        self.__funds = self.__createFunds__()
        self.__history = []

    def deposite(self, fund, amount):
        self.__funds[int(fund)].deposite(amount)

    def withdraw(self, fund, amount):
        self.__funds[int(fund)].withdraw(amount)

    def transfer():
        pass

    def __createFunds__(self):
        FUND_NAMES = ["Money Market","Prime Money Market","Long-Term Bond","Short-Term Bond","500 Index Fund","Capital Value Fund","Growth Equity Fund","Growth Index Fund","Value Fund","Value Stock Index"]
        funds = []
        for i in range(len(FUND_NAMES)):
            funds.append(Fund(FUND_NAMES[i], i))
        return funds

    def getBalance(self, fundNum):
        return self.__funds[fundNum].getBalance()


   

        


