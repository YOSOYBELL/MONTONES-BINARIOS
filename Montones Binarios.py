import math
import uuid
from random import randint


class Heap:
    # config : True // Max_Heap
    # config : False // Min_heap
    def __init__(self, data=[], config=True):
        self.data = []
        self.config = config
        self.build(data[:])

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * (index + 1)

    def parent(self, index):
        return index // 2 - (1 if index % 2 == 0 else 0)

    def height(self):
        return math.ceil(math.log(len(self.data), 2))

    def __len__(self):
        return len(self.data)

    def insert(self, new):
        self.data.append(new)
        self.build()

    def update(self, old, new):
        self.delete(old)
        self.insert(new)

    def delete(self, to_delete):
        if len(self) == 0:
            raise Exception("El montón está vacio")
        if to_delete not in self.data:
            raise Exception("El elemento no está en el montón")
        self.data.remove(to_delete)
        self.build()

    def build(self, data=[]):
        if data and len(data) > 0 and isinstance(data, list):
            self.data = data
        for index in range(len(self) // 2, -1, -1):
            self.heapify(index)

    def heapify(self, index):
        if self.config:
            self.max_heapify(index)
        else:
            self.min_heapify(index)

    def max_heapify(self, index):
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] < self.data[left_index]:
            largest_index = left_index
        if right_index < len(self) and self.data[largest_index] < self.data[right_index]:
            largest_index = right_index
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.max_heapify(largest_index)

    def peek(self):
        return self.data[0]

    def min_heapify(self, index):
        left_index, right_index, largest_index = self.left(index), self.right(index), index
        if left_index < len(self) and self.data[largest_index] > self.data[left_index]:
            largest_index = left_index                                                              #Si el valor que se encuentra en su anterior es menor, toma su valor
        if right_index < len(self) and self.data[largest_index] > self.data[right_index]:
            largest_index = right_index                                                             #Si el valor que se encuentra en su siguiente es menor, toma su valor
        if largest_index != index:
            self.data[largest_index], self.data[index] = self.data[index], self.data[largest_index]
            self.min_heapify(largest_index)                                                         #se vuelve a llamar la función con el nuevo minimo
        return

    def __str__(self):
        return str(self.data)


class PriorityQueue:
    def __init__(self, data=[], config=True):
        self.data = Heap(data, config)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def enqueue(self, new):
        self.data.insert(new)

    def dequeue(self):
        if len(self) == 0:
            raise Exception("Underflow")
        to_dequeue = self.data.peek()
        self.data.delete(to_dequeue)
        return to_dequeue


class Persona:
    def __init__(self, nombre="", edad=1):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return str({
            "Nombre": self.nombre,
            "Edad": self.edad
        })

    def __lt__(self, other):
        return self.edad < other.edad


MAX_BOUND = 72
MIN_BOUND = 18
SIZE = 10


def heapSort(A):
    pq = PriorityQueue(A)
    result = []
    while len(pq) > 0:
        result = [pq.dequeue()] + result
    return result


def main():
    lst = [Persona(uuid.uuid1(), randint(MIN_BOUND, MAX_BOUND)) for e in range(SIZE)]
    pq = PriorityQueue(lst, False) #config : False // Min_heap
    print(list(map(str, lst)))
    while len(pq) > 0:
        print('Atendiendo al cliente con edad ... ', pq.dequeue())
    print(list(map(str, heapSort(lst))))


main()