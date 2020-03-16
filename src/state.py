
from dictionary import Dictionary
from memory import Memory

_normal = "normal"
_compile = "compile"

def as_number(token):
    try:
        return (True, int(token))
    except ValueError: pass;
    except TypeError: pass;
    return (None, None)

def as_string(token, remove_quotes):
    if type(token) == str and token.startswith('"') and token.endswith('"'):
        if remove_quotes:
            return (True, token[1:-1])
        else:
            return (True, token)
    return (None, None)

def as_quote(token):
    if type(token) == str and token.startswith("'"):
        return (True, token)
    return (None, None)


#HACK
def as_whatever(token, remove_quotes):
    success, v = as_number(token)
    if success:
        return True, v
    
    success, v = as_string(token, remove_quotes)
    if success:
        return True, v

    success, v = as_quote(token)
    if success:
        return True, v
    
    return (None, None)

class State():

    def __init__(self):
        self.comment = 0
        self.main_dict = Dictionary()
        self.compile_dict = Dictionary()
        self.memory = Memory()
        self.stack = []
        self.namespace = "g"
        self.mode = _normal
        self.wordbuffer = []

    def pop(self):
        return self.stack.pop(0)

    def push(self, value):
        #self.stack.append(value)
        self.stack.insert(0, value)

    def consume_token(self, length, token):
        if token == "(":
            self.comment += 1
            return True

        if token == ")":
            self.comment -= 1
            if self.comment < 0:
                raise Exception("unbalanced comments")
            return True

        if not self.comment:
            if self.do_specials(token):
                return

            if token in self.main_dict:
                self.run_word(token)
                return
            
            if self.do_specials(token):
                return

            success, v = as_whatever(token, True)
            if success:
                self.push(v)
                return
            
            raise Exception("unknown token >{}<".format(token))

    def add_word(self, key, value):
        self.main_dict[key] = value

    def add_compile_word(self, key, value):
        self.compile_dict[key] = value


    def run_word(self, key):
        kind, data = self.main_dict[key]

        if kind == "primary":
            data(self)
        else:
            for word in data:
                self.consume_token(None, word)

    def do_specials(self, token):
        if self.mode == _compile:
            if token in self.compile_dict:
                kind, data = self.compile_dict[token]
                data(self)

            elif token == 'end':
                self.mode = _normal
                self.main_dict[self.wordbuffer[0]] = self.wordbuffer[1:]
                self.wordbuffer = []
            else:
                success, v = as_whatever(token, False)
                if success:
                    self.wordbuffer.append(v)
                else:
                    self.wordbuffer.append(token)
            return True

        if token == 'def':
            self.mode = _compile
            return True

    def run_quote(self, value):
        success, v = as_quote(value)
        if success:
            self.run_word(v[1:])
        else:
            raise Exception("Invalid quote >{}<".format(value))