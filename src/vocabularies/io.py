

def _put(self):
    s = self.pop()
    print(str(s), end="")

def _newline(self):
    self.push("\n")

def _putline(self):
    s = self.pop()
    print(str(s), end="\n")

def _printstack(self):
    print(self.stack)

def add_all(self):
    self.add_word("put", _put)
    self.add_word("putline", _putline)
    self.add_word("nl", _newline)
    self.add_word(".s", _printstack)
