
def _if(self):
    no = self.pop_value()
    yes = self.pop_value()
    a = self.pop_value()

    # print(yes, no)
    if a:
        # self.run(yes)
        self.push_run(yes)
    else:
        # self.run(no)
        self.push_run(no)

def _when(self):
    yes = self.pop_value()
    a = self.pop_value()
    # print(">",yes, "<")
    if a:
        # self.run(yes)
        self.push_run(yes)

#def add_all(self):
#    self.add_primitive("if", _if)
#    self.add_primitive("when", _when)

def words(prefix=""):
    if prefix:
        prefix = prefix+"."

    return [[
        ("{}if".format(prefix), _if),
        ("{}when".format(prefix), _when),
        ],[]]
