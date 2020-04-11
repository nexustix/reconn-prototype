import sys

def _print(self):
    s = self.pop_value()
    print(s, end="", flush=True)

def _newline(self):
    self.push_value("\n")

def _printline(self):
    s = self.pop_value()
    print(s, end="\n", flush=True)

def _readline(self):
    data = sys.stdin.readline()
    # print(type(data), data)
    self.push_value(data[0:-1])

def _printstack(self):
    print(self.value_stack)

def _state(self):
    print("=== DEBUG ===")
    print("namespace:", self.namespace)
    print("value_stack:",self.value_stack)
    print("run_stack:",self.run_stack)
    print("state_stack:",self.state_stack)
    print("word_buffer:",self.word_buffer)
    print("primary_words:",list(self.primary_words.keys()))
    print("secondary_words:",self.secondary_words)
    print("=== END DEBUG ===")

# def add_all(self):
#     self.add_primitive("print", _put)
#     self.add_primitive("println", _putline)
#     self.add_primitive("nl", _newline)
#     self.add_primitive(".s", _printstack)
#     self.add_primitive(".d", _state)


def words(prefix=""):
    if prefix:
        prefix = prefix+"."
    return [[
        ("{}print".format(prefix), _print),
        ("{}println".format(prefix), _printline),
        ("{}readln".format(prefix), _readline),
        ("{}nl".format(prefix), _newline),
        ("{}.s".format(prefix), _printstack),
        ("{}.d".format(prefix), _state)
        ],[]]
