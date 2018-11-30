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
                clientFrom = self.__clients.get(transaction.getFrom())
                clientTo = self.__clients.get(transaction.getTo())
                
                if fund == 0  and transaction.getAmount() > clientFrom.getBalance(transaction.getFundNumFrom()):
                    pass
                elif fund == 1 and transaction.getAmount() > clientFrom.getBalance(transaction.getFundNumTo()):
                    pass
                else:
                    pass

