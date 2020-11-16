class ClipList:
    def __init__(self, min=0, max=10):
        self.min = min
        self.max = max

    def __setitem__(self, key, value):
        return

    def __getitem__(self, key):
        return self.record[key]


my_list = ClipList()

my_list.__setitem__(3, 10)
my_list.__getitem__(1)





