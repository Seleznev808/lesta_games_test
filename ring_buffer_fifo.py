import timeit


class QueueOverflowError(Exception):
    """Исключение при переполнении очереди."""

    pass


class QueueIsEmptyError(Exception):
    """Исключение при попытке извлечь элемент из пустой очереди."""

    pass


class ListQueue:
    """Реализация циклического буфера FIFO с помощью списка
    на примере очереди ограниченной длины.
    """

    def __init__(self, max_size=0):
        self.__list_elements = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    @property
    def is_empty(self):
        return self.__size == 0

    @property
    def is_full(self):
        return self.__size == self.__max_size

    def push(self, value):
        if self.is_full:
            raise QueueOverflowError('Очередь переполнена')
        self.__list_elements[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def pop(self):
        if self.is_empty:
            raise QueueIsEmptyError('В очереди нет элементов')
        extracted_element = self.__list_elements[self.__head]
        self.__list_elements[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return extracted_element

    def size(self):
        return self.__size


class NodeQueue:
    """Реализация циклического буфера FIFO с помощью связного списка
    на примере очереди ограниченной длины.
    """

    def __init__(self, max_size=0):
        self.__max_size = max_size
        self.__head = None
        self.__tail = None
        self.__size = 0

    @property
    def is_empty(self):
        return self.__size == 0

    @property
    def is_full(self):
        return self.__size == self.__max_size

    def push(self, value):
        if self.is_full:
            raise QueueOverflowError('Очередь переполнена')
        new_node = Node(value)
        if self.is_empty:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def pop(self):
        if self.is_empty:
            raise QueueIsEmptyError('В очереди нет элементов')
        extracted_element = self.__head.value
        self.__head = self.__head.next
        self.__size -= 1
        return extracted_element

    def size(self):
        return self.__size


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


list_queue = ListQueue(1000)
node_queue = NodeQueue(1000)

if __name__=='__main__':
    number_of_measurements = 100

    print('Время добавления элемента в циклический буфер')
    print('на основе списка:')
    for _ in range(5):
        print(timeit.timeit('list_queue.push(1)', number=number_of_measurements, setup='from __main__ import list_queue'))
    print('-' * 100)
    print('на основе связного списка:')
    for _ in range(5):
        print(timeit.timeit('node_queue.push(1)', number=number_of_measurements, setup='from __main__ import node_queue'))

    print('-' * 100)

    print('Время извлечения элемента из циклического буфера')
    print('на основе списка:')
    for _ in range(5):
        print(timeit.timeit('list_queue.pop()', number=number_of_measurements, setup='from __main__ import list_queue'))
    print('-' * 100)
    print('на основе связного списка:')
    for _ in range(5):
        print(timeit.timeit('node_queue.pop()', number=number_of_measurements, setup='from __main__ import node_queue'))
