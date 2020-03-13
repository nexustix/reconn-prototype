
from dictionary import Dictionary

_normal = "normal"
_compile = "compile"

def as_number(token):
    try:
        return (True, int(token))
    except ValueError: pass;
    except TypeError: pass;
    return (None, None)

def as_string(token):
    if type(token) == str and token.startswith('"') and token.endswith('"'):
        return (True, token[1:-1])
    return (None, None)

class State():

    def __init__(self):
        self.comment = 0
        self.main_dict = Dictionary()
        self.stack = []
        self.namespace = "g"
        self.mode = _normal
        self.wordbuffer = []

    def pop(self):
        return self.stack.pop(-1)

    def consume_token(self, length, token):
        if self.do_specials(token):
            return

        #HACK
        elif not self.comment:
            if token in self.main_dict:
                self.run_word(token)
                return
            
            if self.do_specials(token):
                return

            success, n = as_number(token)
            if success:
                self.stack.append(n)
                return
            
            success, s = as_string(token)
            if success:
                self.stack.append(s)
                return
            
            raise Exception("unknown token >{}<".format(token))

    def add_word(self, key, value):
        self.main_dict[key] = value

    def run_word(self, key):
        kind, data = self.main_dict[key]

        if kind == "primary":
            data(self)
        else:
            for word in data:
                #self.run_word(word)
                self.consume_token(None, word)

    def do_specials(self, token):
        #print(">",token)
        if self.mode == _compile:
            if token == ';':
                #print("- end compile")
                self.mode = _normal
                self.main_dict[self.wordbuffer[0]] = self.wordbuffer[1:]
                self.wordbuffer = []
            else:
                #print("- add word")
                self.wordbuffer.append(token)
            return True

        if token == ':':
            #print("- start compile")
            self.mode = _compile
            return True

        if token == "(":
            self.comment += 1
            return True

        if token == ")":
            self.comment -= 1
            if self.comment < 0:
                raise Exception("unbalanced comments")
            return True