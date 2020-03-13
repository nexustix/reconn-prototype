

class Dictionary():

    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        if key in self.data:
            kind, value = self.data[key]
            if kind == "primary" or kind == "secondary":
                return kind, value
            else:
                raise Exception("Entry >{}< has invalid type >{}<".format(str(key), str(kind)))
        else:
            raise Exception("Tried to acces invalid word >{}<".format(str(key)))

    def __setitem__(self, key, value):
        if callable(value):
            self.data[key] = ("primary", value)
        else:
            if type(value) == str:
                raise Exception("Tried to create secondary by using string instead of list >{}<".format(str(value)))
            else:
                self.data[key] = ("secondary", tuple(value))

    def __contains__(self, key):
        return key in self.data



if __name__ == "__main__":
    d = Dictionary()

    def testa():
        psss

    d["print"] = testa
    #d["print"] = "test"
    #print(d["toast"])