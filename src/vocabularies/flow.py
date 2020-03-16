

def _if(self):
    no = self.pop()
    yes = self.pop()
    a = self.pop()
    if a:
        self.run_quote(yes)
    else:
        self.run_quote(no)

def _when(self):
    yes = self.pop()
    a = self.pop()
    if a:
        self.run_quote(yes)

def add_all(self):
    self.add_word("if", _if)
    self.add_word("when", _when)
