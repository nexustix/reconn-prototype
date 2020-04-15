
class Memory():

    def __init__(self):
        self.buckets = []
        self.next_index = 0
        pass
    
    def allot(self, length):
        self.buckets.append([None]*length)
        self.next_index += 1
        return self.next_index - 1

    def get_at(self, index, offset):
        return self.buckets[index][offset]

    def set_at(self, index, offset, value):
        self.buckets[index][offset] = value

    def get(self, index):
        return self.get_at(index, 0)

    def set(self, index, value):
        self.set_at(index, 0, value)
        

if not ('__memory' in globals()):
    __memory = Memory()


def _allot(self):
    a = int(self.word_buffer.pop())
    i = __memory.allot(a)
    self.word_buffer.append(i)

def _get(self):
    index = self.pop_value()
    value = __memory.get(index)
    self.push_value(value)

def _set(self):
    index = self.pop_value()
    value = self.pop_value()
    __memory.set(index, value)

def _get_at(self):
    index = self.pop_value()
    offset = self.pop_value()
    value = __memory.get_at(index, offset)
    self.push_value(value)


def _set_at(self):
    index = self.pop_value()
    offset = self.pop_value()
    value = self.pop_value()
    __memory.set_at(index, offset, value)



words = [
    [
        ("get", _get),
        ("set", _set),
        ("getat", _get_at),
        ("setat", _set_at),
        # ("", _),
    ],
    [
       ("allot", _allot), 
    ]
]
