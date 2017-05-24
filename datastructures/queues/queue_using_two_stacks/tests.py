
import unittest

from .a_queue import AQueue

class TestAQueue(unittest.TestCase):

    def test_enqueue_dequeue_one_val(self):
        
        v1 = 1
        
        a_queue = AQueue()

        a_queue.enqueue(v1)
        v_out = a_queue.dequeue()

        self.assertEqual(v1, v_out)


    def test_enqueue_dequeue_two_vals(self):

        values = [ 0, 1 ]

        a_queue = AQueue()

        for val in values:
            a_queue.enqueue(val)

        values_out = [ a_queue.dequeue(), a_queue.dequeue() ]

        self.assertSequenceEqual(values, values_out)


    def test_front_of_queue(self):

        v1 = 1

        a_queue = AQueue()

        a_queue.enqueue(v1)
        v_out = a_queue.get_front()

        self.assertEqual(v1, v_out)

        # check value is still in the queue
        v_out = a_queue.dequeue()
        self.assertEqual(v1, v_out)
        
