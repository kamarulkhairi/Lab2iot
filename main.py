class SimpleCounter:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def clear(self):
        self._count = 0

    def get_value(self):
        return print(self._count)


my_counter = SimpleCounter()
my_counter.get_value()
my_counter.increment()
my_counter.increment()
my_counter.get_value()
my_counter.clear()
my_counter.get_value()
