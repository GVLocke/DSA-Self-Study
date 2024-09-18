class DynamicArray:
    array = []
    size = 0 # number of indices currently used
    capacity = 0 # total size of the interior array
    
    def __init__(self, capacity: int):
        self.array = [float('-inf')] * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        popped = self.array[self.size - 1]
        self.array[self.size - 1] = float('-inf')
        self.size -= 1
        return popped


    def resize(self) -> None:
        newArray = [float('-inf')] * (self.capacity * 2)
        for i in range(self.size):
            newArray[i] = self.array[i]
        self.capacity *= 2
        self.array = newArray

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity