from reconn.vm import VM

class HandleStore():

    def __init__(self):
        self.handles = {}
        pass

    def open(self, filename, mode="r"):
        self.handles[filename] = open(filename, mode=mode)

    def _valid(self, filename):
        if filename:
            return True
        else:
            raise Exception("no such handle >{}<".format(filename))

    def read(self, filename, length):
        if self._valid(filename):
            return self.handles[filename].read(length)

    def readln(self, filename):
        if self._valid(filename):
            return self.handles[filename].readline()
        
    def write(self, filename, data):
        if self._valid(filename):
            return self.handles[filename].write(data)

    def close(self, filename):
        if self._valid(filename):
            self.handles[filename].close()

if not ('__handlestore' in globals()):
    __handlestore = HandleStore()

# def _open(self: VM):
#     target = self.pop_value()
#     __handlestore.open(target)

def _open(self: VM):
    mode = self.pop_value()
    target = self.pop_value()
    __handlestore.open(target, mode)

def _read(self: VM):
    length = self.pop_value()
    target = self.pop_value()
    data = __handlestore.read(target, length)
    self.push_value(data)

def _readln(self: VM):
    target = self.pop_value()
    data = __handlestore.readln(target)
    self.push_value(data)

def _write(self: VM):
    target = self.pop_value()
    data = self.pop_value()
    __handlestore.write(target, data)

def _close(self: VM):
    target = self.pop_value()
    __handlestore.close(target)


words = [
    [
        ("open", _open),
        ("close", _close),
        ("read", _read),
        ("readln", _readln),
        ("write", _write),
        # ("", _),
    ]]