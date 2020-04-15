import sys
# from pathlib import Path
import os

from reconn import vm
# from vm import VM
from reconn.util import warn
from reconn.tokenize import make_tokenizer

from reconn.vocabularies import io as rio
from reconn.vocabularies import string as string
from reconn.vocabularies import memory as memory
from reconn.vocabularies import stack as stack
from reconn.vocabularies import logic as logic
from reconn.vocabularies import flow as flow
from reconn.vocabularies import arithmetic as arithmetic
from reconn.vocabularies import file as file


content_roots = [
    os.path.join(os.path.expanduser("~"), ".local/lib/reconn0"),
    os.path.join(os.path.expanduser("~"), "gats/projects/grouped/reconn0"),
]

pip = vm.VM()

core_modules = {}
core_modules["io"] = rio.words
core_modules["string"] = string.words
core_modules["memory"] = memory.words
core_modules["stack"] = stack.words
core_modules["logic"] = logic.words
core_modules["flow"] = flow.words
core_modules["arithmetic"] = arithmetic.words
core_modules["file"] = file.words


def _def(self: vm.VM):
    self.push_state(vm._state_compile)
    pass

def _def_compile(self: vm.VM):
    self.word_buffer.append(vm._def)
    self.push_state(vm._state_hard_compile)

def _end_compile(self: vm.VM):
    self.pop_state()
    if self.state != vm._state_compile:
        self.add_secondary(self.namespace, self.word_buffer[0], self.word_buffer[1:])
        self.word_buffer = []

def _dbg(self: vm.VM):
    print("=== DEBUG ===")
    print("namespace:", self.namespace)
    print("value_stack:",self.value_stack.data)
    print("run_stack:",self.run_stack.data)
    print("state_stack:",self.state_stack)
    print("word_buffer:",self.word_buffer)
    # print("primary_words:",list(self.dictionaries[vm._dict_primary].words.keys()))
    print("secondary_words:",self.dictionaries[vm._dict_secondary].words)
    print("=== END DEBUG ===")

def _words(self: vm.VM):
    print("PRIMARY:", end=" ", flush=True)
    for w in self.dictionaries[vm._dict_primary].words.keys():
        if w[0] == "":
            word = w[1]
        else:
            word = w[0]+"."+w[1]
        print(word, end=" ", flush=True)
    print()

    print("SECONDARY:", end=" ", flush=True)
    for w in self.dictionaries[vm._dict_secondary].words.keys():
        if w[0] == "":
            word = w[1]
        else:
            word = w[0]+"."+w[1]
        print(word, end=" ", flush=True)
    print()

    print("COMPILE:", end=" ", flush=True)
    for w in self.dictionaries[vm._dict_compile].words.keys():
        if w[0] == "":
            word = w[1]
        else:
            word = w[0]+"."+w[1]
        print(word, end=" ", flush=True)
    print()

def _enter(self):
    namespace = self.pop_value()
    self.push_namespace(namespace)

def _leave(self):
    self.pop_namespace()

def _namespace(self):
    self.pop_value(self.namespace)

def _exit(self):
    self.running = False

def _include(self):
    a = self.pop_value()
    tail = a.replace(".", "/")
    if a.startswith("."):
        # raise Exception("unable to include >{}< relative imports not implemented".format(a))
        filepath = os.path.join(os.getcwd(), tail[1:] + ".rcn")
        if os.path.isfile(filepath):
            with open(filepath, "r") as h:
                tokenizer = make_tokenizer(h)
                token_data = tokenizer()
                while token_data[0]:
                    pip.execute(token_data[1])
                    token_data = tokenizer()
            return
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
        words = core_modules[a]
        if len(words) > 0:
            for w in words[0]:
                # tmp = self.spacename(w[0])
                self.add_primary(self.namespace, w[0], w[1])
        if len(words) > 1:
            for w in words[1]:
                # tmp = self.spacename(w[0])
                self.add_compiled(self.namespace, w[0], w[1])
    else:
        raise Exception("no >{}< core module".format(a))

def _do(self):
    word = self.pop_value()
    self.push_run(word)

pip.add_primary("", vm._def, _def)
pip.add_compiled("", vm._def, _def_compile)
pip.add_compiled("", vm._end, _end_compile)

pip.add_primary("", "#debug", _dbg)
pip.add_primary("", "#words", _words)

pip.add_primary("", "#enter", _enter)
pip.add_primary("", "#leave", _leave)
pip.add_primary("", "#namespace", _namespace)

pip.add_primary("", "#exit", _exit)
pip.add_primary("", "#include", _include)
pip.add_primary("", "#use", _use)

pip.add_primary("", "#do", _do)

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
