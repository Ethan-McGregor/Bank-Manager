from node import Node
class BinarySearchTree:

    def __init__(self):
        self.__root = None
        self.__size = 0

    def getCount(self):
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def get(self, key):
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                return currentNode.getValue()
            elif currentNode.getKey() > key:
                currentNode = currentNode.getLeftChild()
            else:
                currentNode = currentNode.getRightChild()
        return None

    def __getItem__(self, key):
        return self.get(key)

    def put(self, key, value):
        if self.isEmpty():
            self.__root  = Node(key, value)
            self.__size += 1
            return
        currentNode = self.__root
        while currentNode != None:
            if currentNode.getKey() == key:
                currentNode.setValue(value)
                return
            elif currentNode.getKey() > key:
                if currentNode.getLeftChild() == None:
                    newNode = Node(key, value)
                    currentNode.setLeftChild(newNode)
                    break
                else:
                    currentNode = currentNode.getLeftChild()
            else:
                if currentNode.getRightChild() == None:
                    newNode = Node(key, value)
                    currentNode.setRightChild(newNode)
                    break
                else:
                    currentNode = currentNode.getRightChild()
        self.__size += 1

    def __setItem__(self, key, data):
        self.put(key, data)

    def inOrderTraversal(self, func):
        self.__inOrderTraversalRec(self.__root, func)

    def __inOrderTraversalRec__(self, theNode, func):
        self.__inOrderTraversalRec__(theNode.getLeftChild(), func)
        func(theNode.getValue())
        self.inOrderTraversal(theNode.getRightChild(), func)



