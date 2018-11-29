from transaction import Transaction
from client import Client
from tree import BinarySearchTree
import queue

class Bank:

    def __init__(self,fileName):
        self.__fileName = fileName
        self.__clients = BinarySearchTree()
        self.__transactions = None

    def executeTransactions(self):
        self.__transactions = self.makeQueue()
        processQueue()

    def makeQueue(self):
        data = open(self.__fileName)
        self.__transactios = queue()
        for line in data:
            transaction = Transaction(line)
            transactions.put(transaction)

    def processQueue(self):
        while self.__transactions.empty() != True:
            transaction = self.__transactions.get()
            if transaction.getTransactionType() == "O":
                client = Client(transaction.getFirstName(), transaction.getLastName(), transaction.getId())
                self.__clients.put(client)

            elif transaction.getTransactionType() == "D":
                pass
            elif transaction.getTransactionType() == "W":
                pass
            elif transaction.getTransactionType() == "T":
                pass
            else:
                pass
