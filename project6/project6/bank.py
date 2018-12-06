from transaction import Transaction
from client import Client
from tree import BinarySearchTree
import queue

class Bank:

    def __init__(self,fileName):
        self.__fileName = fileName
        self.__clients = BinarySearchTree()
        self.__transactions = self.makeQueue()

    def executeTransactions(self):
        self.__transactions = self.makeQueue()
        self.processQueue()

    def makeQueue(self):
        data = open(self.__fileName)
        transactionQueue = queue.Queue()
        for line in data:
            transaction = Transaction(line)
            transactionQueue.put(transaction)
        return transactionQueue
   
    def processQueue(self):
        while self.__transactions.empty() != True:
            transaction = self.__transactions.get()
            checkError = self.__checkIdError__(transaction)
            if transaction.getTransactionType() == "O":
                if  checkError == "":
                    client = Client(transaction.getFirstName(), transaction.getLastName(), transaction.getId())
                    self.__clients.put(client._Client__id, client)
                else:
                    print(checkError)
            elif transaction.getTransactionType() == "D":
                if checkError == "":
                    tempClient = self.__clients.get(transaction.getId())
                    tempClient.deposite(transaction)
                else:
                    print(checkError)
            elif transaction.getTransactionType() == "W":
                if checkError == "":
                    tempClient = self.__clients.get(transaction.getId())
                    tempClient.withdraw(transaction)
                else:
                    print(checkError)
            elif transaction.getTransactionType() == "T":
                self.__transferMoney__(transaction)
            elif transaction.getTransactionType() == "H":
                if checkError == "":
                    if transaction.getFundNum() == None:
                        print("\nTransaction history for Clinet #" + str(transaction.getId()))
                        if len(self.__clients.get(transaction.getId()).getHistory()) == 0:
                            print("\tNo transaction history")
                        else:
                            for history in self.__clients.get(transaction.getId()).getHistory():
                                print(history)
                        self.__clients.get(transaction.getId()).addHistory(transaction)
                    elif transaction.getFundNum() != None:
                         print("\nTransaction history for Clinet #" + str(transaction.getId()) + ", Fund #" + str(transaction.getFundNum()))
                         if len(self.__clients.get(transaction.getId()).getFund(transaction.getFundNum(),transaction).getHistory()) == 0:
                            print("\tNo transaction history")
                         else:
                            for history in self.__clients.get(transaction.getId()).getFund(transaction.getFundNum(),transaction).getHistory():
                                print(history)
                         self.__clients.get(transaction.getId()).getFund(transaction.getFundNum(),transaction).addHistory(transaction)
                else:
                    print(checkError)
    def __transferMoney__(self, transaction):
        clientFrom = self.__clients.get(transaction.getFrom())
        clientTo = self.__clients.get(transaction.getTo())
        error = ""
        if self.__clients.get(transaction.getFrom()) == None :
            error += "ERROR: Transfer failed clinet #" + str(transaction.getFrom()) + " does not exsist"
        if self.__clients.get(transaction.getTo()) == None:
            error += "ERROR: Transfer failed clinet #" + str(transaction.getTo()) + " does not exsist"
        if error == "":
            transactionDeposite = Transaction("D " + str(clientTo.getId()) + str(transaction.getFundNumTo()) + " " + str(transaction.getAmount()))
            transactionWithdraw = Transaction("W " + str(clientFrom.getId()) + str(transaction.getFundNumFrom()) + " " + str(transaction.getAmount()))
            clientFrom.withdraw(transactionWithdraw)
            clientTo.deposite(transactionDeposite)
        else:
            print(error)

    def __checkIdError__(self, transaction):
        error = ""
        if transaction.getId() != None and len(transaction.getId()) != 4:
            error += "ERROR: ID improper length"
        elif transaction.getTransactionType() == "O" and self.__clients.get(transaction.getId()) != None:
            error += "ERROR: ID already in use"
        elif transaction.getTransactionType() == "H" and self.__clients.get(transaction.getId()) == None:
            error += "ERROR: Cannot print history, client #"+ str(transaction.getId()) + " does not exist"
        return error

    def __str__(self):
        print("\n***Printing all client accounts***")
        self.__clients.inOrderTraversal(print)
        return ""

