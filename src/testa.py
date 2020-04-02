from tokenize import read_token
from vm import VM
# 
# vm = VM()
#from interpreter import Interpreter
import vocabularies.io as rio

pip = VM()
rio.add_all(pip)

# def _testa(self):
#     print("stuff")
# 
# def _cake(self):
#     print("strawberry")


# pip.add_primitive("testa", _testa)
# pip.add_primitive("cake", _cake)
# pip.add_composite("cheese", ["testa","123",'"toast"', "cake"])

# pip.consume_token("def")
# pip.consume_token("toast")
# pip.consume_token("cake")
# pip.consume_token('"cake"')
# pip.consume_token('"cake"')
# pip.consume_token('.s')
# pip.consume_token("end")

# pip.run("testa")
# pip.run("cheese")
# pip.run("toast")

h = open("test.pip", "r")
token_data = read_token(h)

while token_data[0]:
    # print(token_data)
    # pip.consume_token(token_data[1])
    pip.run(token_data[1])
    token_data = read_token(h)