class CounterComponent:
    def __init__(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
