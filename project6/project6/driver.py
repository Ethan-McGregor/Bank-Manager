from bank import Bank
from tree import BinarySearchTree
from transaction import Transaction


INPUT_FILE = "input.txt"
jollyBanker = Bank(INPUT_FILE)
jollyBanker.executeTransactions()
print(jollyBanker)

#def myFucntion(value):
  #  print(len(value))

#jolly = BinarySearchTree()
#jolly.put(1,"vat")
#jolly.put(3,"cats")
#jolly.put(10,"funny")
#jolly.inOrderTraversal(myFunction)