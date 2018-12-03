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
            if transaction.getTransactionType() == "O":
                client = Client(transaction.getFirstName(), transaction.getLastName(), transaction.getId())
                self.__clients.put(client._Client__id, client)
            elif transaction.getTransactionType() == "D":
                tempClient = self.__clients.get(transaction.getId())
                tempClient.deposite(transaction)
            elif transaction.getTransactionType() == "W":
                tempClient = self.__clients.get(transaction.getId())
                tempClient.withdraw(transaction)
            elif transaction.getTransactionType() == "T":
                self.__transferMoney__(transaction)
            elif transaction.getTransactionType() == "H":
                if len(transaction.getId()) == 4:
                    for history in self.__clients.get(transaction.getId()).getHistory(transaction):
                        print(history)
                elif len(transaction.getId()) == 5:
                     for history in self.__clients.get(transaction.getId()).getFund(transaction.getFundNum(),transaction):
                        print(history)
                else:
                    print("ERROR: Invalid ID")

    def __transferMoney__(self, transaction):
        oppFundNum = [1,0]
        clientFrom = self.__clients.get(transaction.getFrom())
        clientTo = self.__clients.get(transaction.getTo())
        
        #Handles fund 0 and 1 overdraw feature
        if transaction.getFundNumFrom() == "0"  or transaction.getFundNumFrom() == "1":
            test = transaction.getFrom()
            if int(transaction.getAmount()) > clientFrom.getBalance(int(transaction.getFundNumFrom())) and int(transaction.getAmount()) <= clientFrom.getBalance(int(transaction.getFundNumFrom())) + clientFrom.getBalance(int(oppFundNum[int(transaction.getFundNumFrom())])):    
                   transactionDeposite = Transaction("D " + str(clientTo.getId()) + str(transaction.getFundNumTo()) + " " + str(transaction.getAmount()))
                   transactionWithdraw1 = Transaction("W " + str(clientFrom.getId()) + str(transaction.getFundNumFrom()) + " " + str(clientFrom.getBalance(transaction.getFundNumFrom())))
                   transactionWithdraw2 = Transaction("W " + str(clientFrom.getId()) + str(transaction.getFundNumFrom()) + " " + str(int(transaction.getAmount()) - int(clientFrom.getBalance(transaction.getFundNumFrom()))))
                   clientFrom.withdraw(transactionWithdraw1)
                   clientFrom.withdraw(transactionWithdraw2)
                   clientTo.deposite(transactionDeposite)
        #Standard Trasnfer
        else:
            transactionDeposite = Transaction("D " + str(clientTo.getId()) + str(transaction.getFundNumTo()) + " " + str(transaction.getAmount()))
            transactionWithdraw = Transaction("W " + str(clientFrom.getId()) + str(transaction.getFundNumFrom()) + " " + str(transaction.getAmount()))
            clientFrom.withdraw(transactionWithdraw)
            clientTo.deposite(transactionDeposite)

    def __str__(self):
        self.__clients.inOrderTraversal(print)
        return ""

