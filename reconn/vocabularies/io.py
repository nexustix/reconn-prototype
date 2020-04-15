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
    self.push_value(data[0:-1])

def _printstack(self):
    print(self.value_stack.data)

words = [
    [
        ("print", _print),
        ("nl", _newline),
        ("println", _printline),
        ("readline", _readline),
        ("s", _printstack),
        # ("", _),
    ]]