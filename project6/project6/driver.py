from bank import Bank
from tree import BinarySearchTree
from transaction import Transaction


INPUT_FILE = "input.txt"
jollyBanker = Bank(INPUT_FILE)
jollyBanker.executeTransactions()
print(jollyBanker)

# tree = BinarySearchTree()
# tree.put(1,2)
# print("test")
# print(jollyBanker)