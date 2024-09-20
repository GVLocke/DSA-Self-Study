from typing import List

class ListNode:
    def __init__(self, value: int, next: 'ListNode' = None) -> None:
        self.value = value
        self.next = next
    
    def setNext(self, next: 'ListNode') -> None:
        self.next = next
    
    def setValue(self, value: int) -> None:
        self.value = value

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        counter = 0
        currentNode = self.head.next
        # if the list is empty
        if currentNode == None:
            return -1
        while currentNode.next and counter < index:
            currentNode = currentNode.next
            counter += 1
        return currentNode.value if counter == index else -1

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val, self.head.next)
        self.head.setNext(newHead)
        # if the list is empty, we need to make the newHead the tail instead of the dummy node
        if self.head == self.tail:
            self.tail = newHead

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        self.tail.setNext(newTail)
        self.tail = newTail

    def remove(self, index: int) -> bool:
        counter = 0
        currentNode = self.head
        # if the list is empty
        if currentNode.next == None:
            return False
        while currentNode.next and counter < index:
            currentNode = currentNode.next
            counter += 1
        if not currentNode.next:
            return False
        if self.tail == currentNode.next:
            self.tail = currentNode
        currentNode.setNext(currentNode.next.next)
        return True

    def getValues(self) -> List[int]:
        returnList = []
        currentNode = self.head.next
        while currentNode:
            returnList.append(currentNode.value)
            currentNode = currentNode.next
        return returnList

myList = LinkedList()
myList.get(0)