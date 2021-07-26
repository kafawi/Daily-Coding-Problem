class RandomPicker:
    def __init__(self):
        self.count = 0
        self.choosen = None

    def __call__(self, x):
        from random import random
        self.count += 1
        if random() < 1/self.count:
            self.choosen = x
        return self.choosen
    
    def __get__(self):
        return self.choosen

def test_RandomPicker():
    counts = [0 for _ in range(10)]
    for _ in range(10000):
        picker = RandomPicker() 
        pick = None
        for e in range(10):
            pick = picker(e)
        counts[pick] += 1

    for count in counts:
        assert 1000 - count < 100
    print(counts)
                

if __name__ == "__main__":
    test_RandomPicker()
