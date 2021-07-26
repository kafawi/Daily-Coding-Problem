class BoundedOrderLog:
    def __init__(self, N):
        self.orders = [None for _ in range(N)] 
        self.next = 0
        self.size = 0 
        self.N = N

    def record(self, order_id) -> None:
        self.orders[self.next] = order_id
        self.next = (self.next + 1) % self.N
        self.size = min(self.size +1, self.N)

    def get_last(self, i) -> not None:
        assert 0 <= i < self.size 
        idx = (self.next -1 - i) % self.N
        return self.orders[idx]

import unittest

class TestBoundedOrderLog(unittest.TestCase):

    def test_simple_use(self):
        import random
        orders = [random.randint(0,100) for _ in range(10)]
        log = BoundedOrderLog(10)
        for order in orders:
            log.record(order)
        
        for i, order in enumerate(orders):
            i_last = 9 - i
            self.assertEqual(log.get_last(i_last), order)

    def test_record_bound_round_up(self):
        orders = [num for num in range(10)]
        log = BoundedOrderLog(5)
        for order in orders:
            log.record(order)
        
        for i, order in enumerate(orders[5:]):
            i_last = 4 - i
            self.assertEqual(log.get_last(i_last), order)

    def test_get_last_assertion(self):
        log = BoundedOrderLog(1)
        with self.assertRaises(AssertionError):
            log.get_last(0)
        log.record(0)
        self.assertEqual(log.get_last(0), 0)
        with self.assertRaises(AssertionError):
            log.get_last(1)
        log.record(1)
        self.assertEqual(log.get_last(0), 1)
        with self.assertRaises(AssertionError):
            log.get_last(1)

if __name__ == "__main__":
    unittest.main()
    

