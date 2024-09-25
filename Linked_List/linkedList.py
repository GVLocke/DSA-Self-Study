from typing import List

class ListNode:
    def __init__(self, value: int, next: 'ListNode' = None) -> None:
        self.value = value
        self.next = next

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
        self.head.next = newHead
        # if the list is empty, we need to make the newHead the tail instead of the dummy node
        if self.head == self.tail:
            self.tail = newHead

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        self.tail.next = newTail
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
        currentNode.next = currentNode.next.next
        return True

    def getValues(self) -> List[int]:
        returnList = []
        currentNode = self.head.next
        while currentNode:
            returnList.append(currentNode.value)
            currentNode = currentNode.next
        return returnList
    
    def addAtIndex(self, index: int, val: int) -> None:
        counter = 0
        currentNode = self.head
        # if the list is empty
        if not currentNode.next:
            if index > 0 or index < 0:
                return
            if index == 0:
                self.head.next = ListNode(val)
                self.tail = self.head.next
                return
        while currentNode.next and counter < index:
            currentNode = currentNode.next
            counter += 1
        if currentNode.next or counter == index:
            newNode = ListNode(val, currentNode.next)
            currentNode.next = newNode
            if currentNode == self.tail:
                self.tail = currentNode.next
            return
        if not currentNode.next and counter < index:
            return 


myList = LinkedList()
myList.addAtIndex(0, 10)
myList.addAtIndex(0, 20)
myList.addAtIndex(1, 30)
print(myList.get(0))