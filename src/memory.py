
class Memory():

    def __init__(self):
        self.data = {}
        self.counter = 1
        self.step = 1 # 2 for crude out of bounds detection

    def _new(self):
        self.data[self.counter] = 0
        self.counter += self.step
        return self.counter - self.step

    def reserve(self, amount=1):
        if amount == 1:
            return self._new()
        else:
            first = self.counter
            for i in range(amount):
                self._new()
            return first

    def clear(self, key):
        del self.data[key]

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            raise Exception("Memory access violation")
