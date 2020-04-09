import sys
from pathlib import Path
import os

from tokenize import make_tokenizer
from vm import VM
from util import warn

import vocabularies.io as rio
import vocabularies.stack as stack
import vocabularies.logic as logic
import vocabularies.flow as flow
import vocabularies.arithmetic as arithmetic

content_roots = [
    str(Path.joinpath(Path.home(), ".local/lib/reconn0")),
    str(Path.joinpath(Path.home(), "gats/projects/grouped/reconn0"))
    ]

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

def _exit(self):
    self.running = False

def _include(self):
    a = self.pop_value()
    tail = a.replace(".", "/")
    if a.startswith("."):
        raise Exception("unable to include >{}< relative imports not implemented".format(a))
    else:
        for path in content_roots:
            filepath = os.path.join(path, tail + ".rcn")
            if os.path.isfile(filepath):
                # print(filepath)
                with open(filepath, "r") as h:
                    tokenizer = make_tokenizer(h)
                    token_data = tokenizer()
                    while token_data[0]:
                        pip.execute(token_data[1])
                        token_data = tokenizer()
                return

    raise Exception("unable to include >{}<".format(a))

pip.add_primitive("#enter", _enter)
pip.add_primitive("#leave", _leave)
pip.add_primitive("#namespace", _namespace)

pip.add_primitive("get", _get)
pip.add_primitive("set", _set)

pip.add_compiled("allot", _reserve)

pip.add_primitive("exit", _exit)
pip.add_primitive("#include", _include)

args = sys.argv[1:]
if len(args) >= 1:
    filename = args[0]

    if filename:
        h = open(filename, "r")
        tokenizer = make_tokenizer(h)
        token_data = tokenizer()

        while token_data[0]:
            pip.execute(token_data[1])
            token_data = tokenizer()
else:
    warn("Reconn REPL")
    warn("Version: #HACK")
    # warn(" OK>", end="", flush=True)
    tokenizer = make_tokenizer(sys.stdin)
    while pip.running:
        token_data = tokenizer()
        while token_data[0] and pip.running:
            try:
                pip.execute(token_data[1])
            except Exception as e:
                warn(" <!> " + str(e))
                break
            if pip.running:
                token_data = tokenizer()
