from queue import Empty
from queue import Full

class ArrayDeque:
    def __init__(self,N=10):
        self._data = [None] * N
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._data)
    

    def first(self):
        ''' Return the value stored at the front of the Deque '''
        if self.is_empty():
            raise Empty("Queue is Empty")
        return self._data[self._front]
        #pass

    def last(self):
        ''' Return the value stored at the last of the Deque '''
        if self.is_empty():
            raise Empty("Queue is Empty")
        loc = (self._front + self._size - 1) % len(self._data)
        ans = self._data[loc]
        return ans

        #pass

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans
        #pass

    def add_last(self, e):
        if self._size == len(self._data):
            raise Full("Full Deque Exception")
        loc = (self._front + self._size) % len(self._data)
        self._data[loc] = e
        self._size += 1
        #pass


    def add_first(self, e):
        if self._size == len(self._data):
            raise Full("Full Deque Exception")
        loc = (self._front - 1) % len(self._data)
        self._data[loc] = e
        self._front = (self._front - 1) % len(self._data)
        self._size += 1
        #pass

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is Empty")
        loc = (self._front + self._size - 1) % len(self._data)
        ans = self._data[loc]
        self._data[loc] = None
        self._size -= 1
        return ans
        #pass

    def __str__(self):
        return str(self._data)

def main():
    # Empty Queue, size 10.
    deque = ArrayDeque()

    # Add 0, 1, 2, 3 following FIFO.
    for i in range(4):
        deque.add_first(i)
    print(deque)  # [None, None, None, None, None, None, 3, 2, 1, 0]

    # Add 4, 5, 6, 7 following LIFO.
    for j in range(4):
        deque.add_last(j + 4)
    print(deque)  # [4, 5, 6, 7, None, None, 3, 2, 1, 0]

    # Remove first one
    print(deque.delete_first()) # 3

    # Remove last one
    print(deque.delete_last()) # 7


if __name__ == '__main__':
    main()
