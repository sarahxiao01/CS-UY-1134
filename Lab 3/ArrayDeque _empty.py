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
       ''' Return the value stored at the front of the queue '''
        if self.is_empty():
            raise Empty("Queue is Empty")
        pass

    def last(self):
        if self.is_empty():
            raise Empty("Queue is Empty")

        pass

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        pass

    def add_last(self, e):
        if self._size == len(self._data):
            raise Full("Full Queue Exception")
        ''' Insert e at the end of the queue '''
        pass


    def add_first(self, e):
        pass

    def delete_last(self):
         pass

    def __str__(self):
        return "Incomplete!! Change this."

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
