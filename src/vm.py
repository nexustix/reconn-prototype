import kinds
from memory import Memory

_normal = "normal"
_compile = "compile"

class VM():

    def __init__(self):
        self.val_stack = []
        self.run_stack = []
        self.primitive_dict = {}
        self.composite_dict = {}
        self.compile_dict = {}
        self.memory = Memory()

        self.state_stack = []
        self.namespace_stack = []
        self.comment = 0
        self.word_buffer = []

    @property
    def namespace(self):
        return ".".join(self.namespace_stack)

    def spacename(self, name):
        if self.namespace:
            return ".".join([self.namespace, name])

    @property
    def state(self):
        if len(self.state_stack) > 0:
            return self.state_stack[-1]
        else:
            return _normal

    def push_state(self, state):
        self.state_stack.append(state)

    def pop_state(self):
        return self.state_stack.pop()

    def push_value(self, value):
        self.val_stack.append(value)

    def pop_value(self):
        return self.val_stack.pop()

    def push_run(self, word):
        self.run_stack.append(word)

    def pop_run(self):
        return self.run_stack.pop()

    def add_primitive(self, name, function):
        self.primitive_dict[name] = function

    def add_composite(self, name, words):
        self.composite_dict[name] = list(words)

    def add_compiled(self, name, function):
        self.compile_dict[name] = function

    def run(self, token):
        # HACK
        success, value = kinds.as_whatever(token, True)
        _, value_fancy = kinds.as_whatever(token, False)
        # print(success, value)

        if value == "(":
            self.comment += 1

        elif value == ")":
            self.comment -= 0
            if self.comment < 0:
                raise Exception("Unbalanced comments")

        if self.comment:
            return

        if value == "def":
            self.push_state(_compile)
            if len(self.word_buffer) > 0:
                self.word_buffer.append("def")
                # print(self.state_stack)
                return

        if self.state == _normal:
            if (success != None):
                self.push_value(value)
            elif token in self.composite_dict:
                for w in self.composite_dict[token]:
                    self.run(w)
            elif token in self.primitive_dict:
                self.push_run(token)
            else:
                raise Exception("Unknown word >{}<".format(token))

        elif self.state == _compile:
            if value in self.compile_dict:
                self.compile_dict[value](self)
            elif value == "end":
                # print("end")
                if not (self.state == _compile):
                   raise Exception('Mismatched "end"')
                self.pop_state()
                # print(self.state_stack)
                if self.state != _compile:
                    self.add_composite(self.word_buffer[1], self.word_buffer[2:])
                    self.word_buffer = []
                else:
                    self.word_buffer.append("end")
            else:
                self.word_buffer.append(value_fancy)

        self._execute()

    def _execute(self):
        while len(self.run_stack) > 0:
            word = self.pop_run()
            # print(word)
            self.primitive_dict[word](self)

    def allot_mem(self, size):
        return self.memory.reserve(size)

    def read_mem(self, index):
        return self.memory[index]

    def write_mem(self, index, data):
        self.memory[index] = data

    def free_mem(self, index, size=1):
        self.memory.clear(index)
            