from .complex_property import ComplexProperty


class HSV(ComplexProperty):

    def __init__(self, str_data):
        hsv = list(map(float, str_data.split("a")))
        self.Hue = int(hsv[0])
        self.Saturation = float(hsv[1])
        self.Brightness = float(hsv[2])
        self.u_range_saturation = bool(hsv[3])
        self.u_range_brightness = bool(hsv[4])

    def to_str(self):
        return f"{self.Hue}a{self.Saturation}a{self.Brightness}a" \
               f"{int(self.u_range_saturation)}a{int(self.u_range_brightness)}"

    def __str__(self):
        return f"{self.Hue}a{self.Saturation}a{self.Brightness}a" \
               f"{int(self.u_range_saturation)}a{int(self.u_range_brightness)}"
