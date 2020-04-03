import sys

from tokenize import read_token
from vm import VM

import vocabularies.io as rio
import vocabularies.stack as stack
import vocabularies.logic as logic
import vocabularies.flow as flow
import vocabularies.arithmetic as arithmetic

pip = VM()
rio.add_all(pip)
stack.add_all(pip)
logic.add_all(pip)
flow.add_all(pip)
arithmetic.add_all(pip)

pip.add_primitive("concat", arithmetic._add)

def _enter(self):
    namespace = self.pop_value()
    self.push_namespace(namespace)

def _leave(self):
    self.pop_namespace()

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

def _namespace(self):
    self.push_value(self.namespace)

pip.add_primitive("#enter", _enter)
pip.add_primitive("#leave", _leave)
pip.add_primitive("#namespace", _namespace)

pip.add_primitive("get", _get)
pip.add_primitive("set", _set)

pip.add_compiled("allot", _reserve)

#HACK #HACK #HACK
sys.setrecursionlimit(2147483647)
#HACK #HACK #HACK

args = sys.argv[1:]
if len(args) >= 1:
    # print(args[0])
    filename = args[0]

    if filename:
        h = open(filename, "r")
        token_data = read_token(h)

        while token_data[0]:
            #try:
            pip.run(token_data[1])
            #except Exception as e:
            #    print(" <!> " + str(e))
            #    break

            token_data = read_token(h)
else:
    print("Reconn REPL")
    print("Version: #HACK")
    while pip.running:
        token_data = read_token(sys.stdin)
        while token_data[0]:
            try:
                pip.run(token_data[1])
            except Exception as e:
                print(" <!> " + str(e))
                break
            token_data = read_token(sys.stdin)
