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
import vocabularies.string as string
import vocabularies.memory as memory

content_roots = [
    str(Path.joinpath(Path.home(), ".local/lib/reconn0")),
    str(Path.joinpath(Path.home(), "gats/projects/grouped/reconn0"))
    ]

pip = VM()

core_modules = {}

core_modules["io"] = rio.words
core_modules["stack"] = stack.words
# core_modules["logic"] = logic.words
core_modules["flow"] = flow.words
# core_modules["math"] = arithmetic.words
core_modules["string"] = string.words
core_modules["memory"] = memory.words

pip.add_primitive("concat", arithmetic._add)

def _enter(self):
    namespace = self.pop_value()
    self.push_namespace(namespace)

def _leave(self):
    self.pop_namespace()

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
                with open(filepath, "r") as h:
                    tokenizer = make_tokenizer(h)
                    token_data = tokenizer()
                    while token_data[0]:
                        pip.execute(token_data[1])
                        token_data = tokenizer()
                return

    raise Exception("unable to include >{}<".format(a))

def _use(self):
    a = self.pop_value()
    if a in core_modules:
        words = core_modules[a]()
        for w in words[0]:
            tmp = self.spacename(w[0])
            self.add_primitive(tmp, w[1])
        for w in words[1]:
            tmp = self.spacename(w[0])
            self.add_compiled(tmp, w[1])
    else:
        raise Exception("no >{}< core module".format(a))

pip.add_primitive("#enter", _enter)
pip.add_primitive("#leave", _leave)
pip.add_primitive("#namespace", _namespace)

pip.add_primitive("#exit", _exit)
pip.add_primitive("#include", _include)
pip.add_primitive("#use", _use)

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
