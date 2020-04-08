import kinds
from memory import Memory

_normal = "normal"
_compile = "compile"

_def = "def"
_end = "end"

class VM():
    
    def __init__(self):
        self.value_stack = []
        self.run_stack = []

        self.memory = Memory()

        self.primary_words = {}
        self.secondary_words = {}
        self.compile_words = {}

        self.word_buffer = []

        self.comment = 0
        self.state_stack = []
        self.namespace_stack = []

        self.running = True
    
    @property
    def working(self):
        return self.run_stack > 0

    @property
    def namespace(self):
        return ".".join(self.namespace_stack)

    def push_namespace(self, name):
        self.namespace_stack.append(name)

    def pop_namespace(self):
        return self.namespace_stack.pop()

    def spacename(self, name):
        if self.namespace:
            return ".".join([self.namespace, name])
        return name

    def spacevariants(self, name):
        segs = self.namespace.split(".")
        name = str(name)
        # print(segs, name)
        if segs[0]:
            for n in range(len(segs), 0, -1):
                tmp_token = ".".join(segs[0:n]+[name])
                # print(">>", tmp_token)
                if tmp_token in self.secondary_words:
                    return tmp_token
        return name
        #print(">X>",name)


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
        self.value_stack.append(value)

    def pop_value(self):
        return self.value_stack.pop()

    def push_run(self, word):
        self.run_stack.append(word)

    def pop_run(self):
        return self.run_stack.pop()

    def add_primitive(self, name, function):
        self.primary_words[name] = function

    def add_secondary(self, name, words):
        self.secondary_words[name] = list(words)

    def add_compiled(self, name, function):
        self.compile_words[name] = function

    def execute(self, word):
        self.push_run(word)
        self.run()

    def run(self):
        while len(self.run_stack) > 0:
            word = self.pop_run()

            if word == "(":
                self.comment += 1
                return

            elif word == ")":
                self.comment -= 1
                if self.comment < 0:
                    raise Exception("Unbalanced comments")
                return
            
            if self.comment > 0:
                return

            if word == _def:
                self.push_state(_compile)
                if len(self.word_buffer) > 0:
                    self.word_buffer.append(word)
                    return

            if self.state == _compile:
                if word == _end:
                    self.pop_state()
                    if self.state != _compile:
                        self.add_secondary(self.spacename(self.word_buffer[1]), self.word_buffer[2:])
                        self.word_buffer = []
                elif word in self.compile_words:
                    self.compile_words[word](self) 
                else:
                    success, value = kinds.as_whatever(word, False)
                    if success:
                        self.word_buffer.append(value)
                    elif word in self.primary_words:
                        self.word_buffer.append(word)
                    else:
                        sword = self.spacevariants(word)
                        self.word_buffer.append(sword)
            else:
                if (word == _end) and (not (self.state == _compile)):
                    raise Exception('Mismatched end token')
                elif word in self.primary_words:
                    self.primary_words[word](self)
                else:
                    #sword = self.spacevariants(self.spacename(word))
                    sword = self.spacevariants(word)
                    # print(">",sword)
                    if sword in self.secondary_words:
                        for w in self.secondary_words[sword][-1::-1]:
                            self.push_run(w)
                    else:
                        success, value = kinds.as_whatever(word, True)
                        if success:
                            # print(">", value)
                            self.push_value(value)
                        else:
                            raise Exception("Unknown word >{}<".format(word))

    def allot_memory(self, size):
        return self.memory.reserve(size)

    def read_memory(self, index):
        return self.memory[index]

    def write_memory(self, index, data):
        self.memory[index] = data

    def free_memory(self, index, size=1):
        self.memory.clear(index)
