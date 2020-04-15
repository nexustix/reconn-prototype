from reconn import kinds
from reconn.util import warn

from reconn.dictionary import Dictionary
from reconn.stack import Stack

_dict_primary = 0
_dict_secondary = 1
_dict_compile = 2

_state_normal = "normal"
_state_compile = "compile"
_state_hard_compile = "hard"

_def = "def"
_end = "end"

class VM():

    def __init__(self):
        self.run_stack = Stack()
        self.value_stack = Stack()
        self.state_stack = []
        self.namespace_stack = []

        self.dictionaries = [
            Dictionary(),
            Dictionary(),
            Dictionary()
        ]

        self.word_buffer = []
        self.comment = 0

        self.running = True

    @property
    def namespace(self):
        return ".".join(self.namespace_stack)

    def push_namespace(self, name):
        self.namespace_stack.append(name)

    def pop_namespace(self):
        if len(self.namespace_stack) > 0:
            return self.namespace_stack.pop()
        else:
            raise Exception("can't leave namespace, you aren't inside a namespace")


    def spacename(self, word):
        if self.namespace:
            combo = self.namespace + "." + str(word)
            segs = combo.split(".")
        else:
            segs = str(word).split(".")

        if len(segs) > 1:
            head = segs[-1]
            tail = ".".join(segs[:-1])
            return (tail, head)
        else:
            return ("",segs[-1])

    @property
    def state(self):
        if len(self.state_stack) > 0:
            return self.state_stack[-1]
        else:
            return _state_normal

    def push_state(self, state):
        self.state_stack.append(state)

    def pop_state(self):
        return self.state_stack.pop()

    def execute(self, word):
        self.run_stack.push(word)
        self.run()

    def execute_all(self, words, ok=False):
        for word in words:
            self.execute(word)
        if ok:
            warn(" OK>", end="", flush=True)

    def do(self, word):
        #wkey = (self.namespace, word)
        wkey = self.spacename(word)
        # print(wkey)
        if self.state == _state_compile:
            if wkey in self.dictionaries[_dict_compile]:
                self.dictionaries[_dict_compile][wkey](self)
                return True

        elif self.state == _state_normal:
            if wkey in self.dictionaries[_dict_primary]:
                self.dictionaries[_dict_primary][wkey](self)
                return True
            elif wkey in self.dictionaries[_dict_secondary]:
                for w in self.dictionaries[_dict_secondary][wkey][-1::-1]:
                    self.run_stack.push(w)   
                return True
            else:
                success, value = kinds.as_whatever(word, True)
                if success:
                    self.value_stack.push(value)
                    return True

        return False
        
    def run(self):
        while len(self.run_stack) > 0:
            word = self.run_stack.pop()
           
            if word == "(": self.comment += 1; return
            if word == ")": 
                self.comment -= 1
                if self.comment < 0: raise Exception("Unbalanced comments")
                return
            if self.comment > 0: return

            if self.state == _state_compile:
                if not self.do(word):
                    success, value = kinds.as_whatever(word, False)
                    if success:
                        self.word_buffer.append(value)
                    else:
                        self.word_buffer.append(word)

            elif self.state == _state_hard_compile:
                self.word_buffer.append(word)
                if word == _end:
                    self.pop_state()

            elif self.state == _state_normal:
                if not self.do(word):
                    raise Exception("Unknown word >{}<".format(word))

    def add_primary(self, namespace, name, function ):
        self.dictionaries[_dict_primary][(namespace, name)] = function

    def add_secondary(self, namespace, name, words):
        self.dictionaries[_dict_secondary][(namespace, name)] = words

    def add_compiled(self, namespace, name, function):
        self.dictionaries[_dict_compile][(namespace, name)] = function

    def push_value(self, value):
        self.value_stack.push(value)

    def pop_value(self):
        return self.value_stack.pop()

    def push_run(self, value):
        self.run_stack.push(value)

    def pop_run(self):
        return self.run_stack.pop()