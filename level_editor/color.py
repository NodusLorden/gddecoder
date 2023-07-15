from .complex_property import ComplexProperty
from .HSV import HSV
from .. import components


class Color:

    def __init__(self):
        self.red = 255
        self.green = 255
        self.blue = 255
        self.red2 = 255
        self.green2 = 255
        self.blue2 = 255
        self.blending = False
        self.opacity = 1
        self.player_color = -1
        self.k18 = 0
        self.k8 = 1
        self.k15 = 1
        self.other = {}

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue and\
            self.red2 == other.red2 and self.green2 == other.green2 and self.blue2 == other.blue2 and \
            self.blending == other.blending and self.opacity == other.opacity and self.k18 == other.k18 and\
            self.k8 == other.k8 and self.k15 == other.k15

    @classmethod
    def load_color(cls, str_data):
        color_id = None
        color = cls()
        for key, val in components.keyval(str_data.split("_")):
            match key:
                case "1":
                    color.red = int(val)
                case "2":
                    color.green = int(val)
                case "3":
                    color.blue = int(val)
                case "11":
                    color.red2 = int(val)
                case "12":
                    color.green2 = int(val)
                case "13":
                    color.blue2 = int(val)
                case "4":
                    color.player_color = int(val)
                case "5":
                    color.blending = bool(val)
                case "6":
                    color_id = int(val)
                case "7":
                    color.opacity = float(val)
                case "9":
                    color.target_channel_id = int(val)
                case "10":
                    color.color_HSV = HSV(val)
                case "17":
                    color.copy_opacity = bool(val)
                case "18":
                    color.k18 = val
                case "8":
                    color.k8 = val
                case "15":
                    color.k15 = val
                case other:
                    color.other["k" + other] = val

        if color_id is None:
            raise AttributeError
        return color, color_id

    def get_str(self, color_id):
        str_data_list = []
        for key, val in self.other.items():

            if type(val) == bool:
                val = str(int(val))
            elif isinstance(val, ComplexProperty):
                val = val.to_str()
            elif type(val) != str:
                val = str(val)

            if type(key) != str:
                key = str(key)

            str_data_list += [key[1:], val]

        str_data_list += [
            "1", self.red,
            "2", self.green,
            "3", self.blue,
            "11", self.red2,
            "12", self.green2,
            "13", self.blue2,
            "4", self.player_color,
            "6", color_id + 1,
            "5", self.blending,
            "7", self.opacity
        ] + \
        ["9", self.target_channel_id] if hasattr(self, "target_channel_id") else [] +\
        ["10", self.color_HSV.to_str()] if hasattr(self, "color_HSV") else [] +\
        ["17", self.copy_opacity] if hasattr(self, "copy_opacity") else [] +\
        [
            "18", self.k18,
            "8", self.k8,
            "15", self.k15,
        ]


        return "_".join(str_data_list)

    def __str__(self):
        return f"R: {self.red}, G: {self.green}, B: {self.blue}, Opacity: {self.opacity}, Blending: {self.blending}"

    def __repr__(self):
        return f"R: {self.red}, G: {self.green}, B: {self.blue}, Opacity: {self.opacity}, Blending: {self.blending}"


class Colors(list, ComplexProperty):

    def __init__(self):
        super().__init__()
        for _ in range(1, 1012):
            self.append(Color())

    def load_color(self, color_str):
        color, i = Color.load_color(color_str)
        self[i - 1] = color

    def to_str(self):
        void_color = Color()
        colors = []
        for i, color in enumerate(self):
            if color == void_color and i < 999:
                continue
            colors.append(color.get_str(i))
        return "|".join(colors)
