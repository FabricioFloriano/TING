from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._my_queue = list()

    def __len__(self):
        return len(self._my_queue)

    def enqueue(self, value):
        return self._my_queue.append(value)

    def dequeue(self):
        return self._my_queue.pop(0)

    def search(self, index):
        if 0 <= index < len(self._my_queue):
            return self._my_queue[index]
        else:
            raise IndexError("Índice Inválido ou Inexistente")
