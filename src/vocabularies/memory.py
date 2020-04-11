def _get(self):
    a = self.pop_value()
    v = self.read_memory(a)
    self.push_value(v)

def _set(self):
    a = self.pop_value()
    b = self.pop_value()
    self.write_memory(a, b)

def _reserve(self):
    a = self.word_buffer.pop()
    i = self.allot_memory(a)
    self.word_buffer.append(i)

def words(prefix=""):
    if prefix:
        prefix = "."+prefix

    return [[
            ("{}get".format(prefix),_get),
            ("{}set".format(prefix), _set),
        ],
        [
            ("{}allot".format(prefix), _reserve),
        ]]
'''
def add_all(self, prefix=""):
    for w in words(prefix):
        self.add_primitive(w[0], w[1])
'''