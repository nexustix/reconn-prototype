from tokenize import read_token
#from dictionary import Dictionary
from state import State


state = State()

def _puts(self: State):
    s = self.pop()
    print(s, end="")

def _newline(self: State):
    print()

def _swap(self: State):
    self.stack[0], self.stack[1] = self.stack[1], self.stack[0]

state.add_word("puts", _puts)
state.add_word("newline", _newline)
state.add_word("swap", _swap)

h = open("test.rcn", "r")
token_data = read_token(h)

while token_data[0]:
    state.consume_token(*token_data)
    token_data = read_token(h)

'''
main_dict = Dictionary()

h = open("test.rcn", "r")

token_data = read_token(h)
comment = 0

stack = []


def as_number(token):
    try:
        return (True, int(token_data))
    except ValueError: pass;
    except TypeError: pass;
    return (None, None)

def as_string(token):
    if type(token) == str and token.startswith('"') and token.endswith('"'):
        return (True, token[1:-1])
    return (None, None)

while token_data[0]:
    len, token = token_data
    if token == "(":
        comment += 1
    elif token == ")":
        comment -= 1
        if comment < 0:
            raise Exception("unbalanced comments")
    elif not comment:
        # run token_data
        if token in main_dict:
            print("doing >{}<".format(token_data[1]))
        else:
            success, n = as_number(token)
            if success:
                stack.append(n)
            else:
                success, s = as_string(token)
                if success:
                    stack.append(s)
                else:
                    raise Exception("unknown token >{}<".format(token))
    print(stack)
    token_data = read_token(h)
'''