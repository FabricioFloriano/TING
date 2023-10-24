from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    queue.enqueue({"qtd_linhas": 4})
    assert len(queue.high_priority) == 1
    queue.dequeue()
    assert len(queue.high_priority) == 0
    queue.enqueue({"qtd_linhas": 6})
    assert len(queue.regular_priority) == 1
    queue.enqueue({"qtd_linhas": 4})
    queue.enqueue({"qtd_linhas": 3})
    assert queue.search(1).get("qtd_linhas") == 3
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(-2)
