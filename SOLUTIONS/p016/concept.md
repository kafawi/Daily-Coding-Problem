# e-commerce datastructure

the simplest Implementation is a List. If we have a constant size `N`, we can make the store easy as an array. And we can use a circular buffer for that.

## circular buffer log

```python
class BoundedOrderLog:
    def __init__(self, N):
        self.orders = array of size N
        self.next = 0
        self.size = 0 
        self.N = N

    def record(self, order_id):
        self.orders[self.next] = order_id
        self.next = (self.next + 1) mod self.N
        self.size = min(self.size +1, self.N)

    def get_last(self, i) -> order_id
        assert i < self.size 
        id = (self.next -1 - i) mod self.N
        return self.orders(id)
```

[code](solution.py)
