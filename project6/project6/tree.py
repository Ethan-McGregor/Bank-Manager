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
        if theNode == None:
            return
        self.__inOrderTraversalRec__(theNode.getLeftChild(), func)
        func(theNode.getValue())
        self.inOrderTraversal(theNode.getRightChild(), func)

    def remove(self,key):
        if self.__root == None:
            return None
        if self.__root.getKey() == key:
            self.__size -= 1
            if self.__root.getLeftChild() == None:
                self.__root = self.__root.getRightChild()
            if self.__root.getLeftChild() == None:
                self.__root = self.__root.getLeftChild()
            else:
                replaceNode = self.__getAndRemoveRightSmall(self.__root)
                self.__root.setKey(replaceNode.getKey())
                self.__root.setValue(replaceNode.getValue())
                return
        else:
            currentNode = self.__root
            while currentNode != None:
                if currentNode.getleftChild() and currentNode.getLeftChild().getKey() == key:
                    foundNode = currentNode.getLeftChild()
                    if foundNode.isLeaf():
                        currentNode.setLeftChild(None)
                    elif foundNode.getLeftChild() == None:
                        currentNode.setLeftChild(foundNode.getRightChild())
                    elif foundNode.getRightChild() == None:
                        currentNode.setLeftChild(foundNode.getLeftChild())
                    else:
                        replaceNode = self.__getAndRemoveRightSmall(currentNode)
                        foundNode.setKey(replaceNode.getKey())
                        foundNode.setValue(replaceNode.getValue())
                    self.__size -= 1

                    break
                elif currentNode.getRightChild() and currentNode.getRightChild().getKey() == key:
                    pass
                elif currentNode.getKey() > key:
                    currentNode = currentNode.getLeftChild()
                else:
                    currentNode = currentNode.getRightChild()