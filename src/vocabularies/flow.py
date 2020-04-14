
def _if(self):
    no = self.pop_value()
    yes = self.pop_value()
    a = self.pop_value()

    if a:
        self.push_run(yes)
    else:
        self.push_run(no)

def _when(self):
    yes = self.pop_value()
    a = self.pop_value()
    if a:
        self.push_run(yes)


words = [
    [
        ("if", _if),
        ("when", _when),
    ]]
