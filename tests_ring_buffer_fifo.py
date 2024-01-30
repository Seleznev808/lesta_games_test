import unittest

from ring_buffer_fifo import (
    ListQueue,
    NodeQueue,
    QueueIsEmptyError,
    QueueOverflowError
)


class TestListQueue(unittest.TestCase):
    def setUp(self):
        self.queue = ListQueue(2)
        self.queue.push(1)
        self.queue.push(2)

    def test_push_into_full_queue(self):
        with self.assertRaises(QueueOverflowError):
            self.queue.push(3)

    def test_pop_full_queue(self):
        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)

    def test_pop_empty_queue(self):
        self.queue = ListQueue()
        with self.assertRaises(QueueIsEmptyError):
            self.queue.pop()

    def test_size(self):
        self.assertEqual(self.queue.size(), 2)


class TestNodeQueue(TestListQueue):
    def setUp(self):
        self.queue = NodeQueue(2)
        self.queue.push(1)
        self.queue.push(2)

    def test_pop_empty_queue(self):
        self.queue = NodeQueue()
        with self.assertRaises(QueueIsEmptyError):
            self.queue.pop()


if __name__=='__main__':
    unittest.main()
