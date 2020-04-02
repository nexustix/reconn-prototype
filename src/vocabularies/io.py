

def _put(self):
    s = self.pop_value()
    print(str(s), end="")

def _newline(self):
    self.push_value("\n")

def _putline(self):
    s = self.pop_value()
    print(str(s), end="\n")

def _printstack(self):
    print(self.val_stack)
    print(self.run_stack)
    print(self.state_stack)
    print(self.word_buffer)
    print(self.composite_dict)

def _state(self):
    print("val_stack",self.val_stack)
    print("run_stack",self.run_stack)
    print("state_stack",self.state_stack)
    print("word_buffer",self.word_buffer)
    print("composite_dict",self.composite_dict)

def add_all(self):
    self.add_primitive("puts", _put)
    self.add_primitive("putsnl", _putline)
    self.add_primitive("nl", _newline)
    self.add_primitive(".s", _printstack)
    self.add_primitive(".d", _state)

