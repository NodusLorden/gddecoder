from .complex_property import ComplexProperty


class Groups(set, ComplexProperty):

    def __init__(self, data):
        if type(data) == str:
            super().__init__()
            for group in data.split("."):
                self.add(int(group))
        elif type(data) == int:
            super().__init__()
            self.add(data)
        else:
            super().__init__(data)

    def to_str(self):
        return ".".join(map(str, self))
