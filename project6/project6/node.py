
class Node:

    def __init__(self, key, value=None):
        self.__key = key
        self.__value = value
        self.__leftChild = None
        self.__rightChild = None

    def getKey(self):
        return self.__key

    def setKey(self, key):
        pass

    def getValue(self):
        return self.__value

    def setValue(self, value):
        self.__value = value

    def getLeftChild(self):
        return self.__leftChild

    def setLeftChild(self, childNode):
        self.__leftChild = childNode

    def getRightChild(self):
        return self.__rightChild

    def setRightChild(self, childNode):
        self.__rightChild = childNode

    def isLeaf(self):
        return self.getLeftChild() == None and self.getRightChild() == None

