from tokenize import read_token
#from dictionary import Dictionary
from state import State


state = State()

def _puts(self: State):
    s = self.pop()
    print(str(s), end="")

def _newline(self: State):
    print()

def _swap(self: State):
    a = self.pop()
    b = self.pop()
    self.push(a)
    self.push(b)

def _add(self: State):
    a = self.pop()
    b = self.pop()
    self.push(a + b)

def _dup(self: State):
    a = self.pop()
    self.push(a)
    self.push(a)

def _printstack(self: State):
    print()
    print(self.stack)

def _rot(self: State):
    a = self.pop()
    b = self.pop()
    c = self.pop()
    self.push(b)
    self.push(a)
    self.push(c)

def _over(self: State):
    a = self.pop()
    b = self.pop()
    self.push(b)
    self.push(a)
    self.push(b)

def _if(self: State):
    no = self.pop()
    yes = self.pop()
    a = self.pop()
    if a:
        self.run_quote(yes)
    else:
        self.run_quote(no)

def _when(self: State):
    yes = self.pop()
    a = self.pop()
    if a:
        self.run_quote(yes)

"""
def _div(self: State):
    a = self.pop()
    b = self.pop()

    x, rem = divmod(a, b)
    self.push(rem)
    self.push(x)
"""

def _mod(self: State):
    a = self.pop()
    b = self.pop()
    self.push(b % a)


def _drop(self: State):
    self.pop()

def _less_than(self: State):
    a = self.pop()
    b = self.pop()
    if b < a:
        self.push(1)
    else:
        self.push(0)

def _equal(self: State):
    a = self.pop()
    b = self.pop()
    if b == a:
        self.push(1)
    else:
        self.push(0)

def _or(self: State):
    a = self.pop()
    b = self.pop()
    if b or a:
        self.push(1)
    else:
        self.push(0)

def _not(self: State):
    a = self.pop()
    if a:
        self.push(0)
    else:
        self.push(1)


def _ctest(self: State):
    print("YES THIS COMPILE THING DOES STUFF")


def _var(self: State):
    i = self.memory.reserve(1)
    self.wordbuffer.append(i)

def _get(self: State):
    a = self.pop()
    self.push(self.memory[a])

def _set(self: State):
    a = self.pop()
    b = self.pop()
    self.memory[a] = b

def _reserve(self: State):
    a = self.wordbuffer.pop(-1)
    i = self.memory.reserve(a)
    self.wordbuffer.append(i)


state.add_word("puts", _puts)
state.add_word("newline", _newline)

state.add_word("add", _add)
state.add_word("concat", _add)
#state.add_word("div", _div)
state.add_word("%", _mod)

state.add_word("swap", _swap)
state.add_word("dup", _dup)

state.add_word("drop", _drop)
state.add_word("over", _over)
state.add_word("rot", _rot)


state.add_word(".s", _printstack)

state.add_word("if", _if)
state.add_word("when", _when)
state.add_word("<", _less_than)
state.add_word("=", _equal)
state.add_word("or", _or)
state.add_word("not", _not)

#state.add_compile_word("woah", _ctest)
state.add_compile_word("var", _var)
state.add_compile_word("reserve", _reserve)

state.add_word("get", _get)
state.add_word("set", _set)

h = open("test.rcn", "r")
token_data = read_token(h)

while token_data[0]:
    state.consume_token(*token_data)
    token_data = read_token(h)