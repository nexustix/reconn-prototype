from tokenize import read_token
#from dictionary import Dictionary
from state import State


import vocabularies.arithmetic as arithmetic
import vocabularies.flow as flow
import vocabularies.io as rio
import vocabularies.logic as logic
import vocabularies.stack as stack


state = State()

arithmetic.add_all(state)
flow.add_all(state)
rio.add_all(state)
logic.add_all(state)
stack.add_all(state)

state.add_word("concat", arithmetic._add)

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
    self.wordbuffer.insert(-1, i)



state.add_compile_word("var", _var)
state.add_compile_word("alloc", _reserve)

state.add_word("get", _get)
state.add_word("set", _set)

h = open("test.rcn", "r")
token_data = read_token(h)

while token_data[0]:
    state.consume_token(*token_data)
    token_data = read_token(h)
