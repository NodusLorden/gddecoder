from .complex_property import ComplexProperty
from .level_enums import Easing, Comparison
from .groups import Groups
from .HSV import HSV
from .level_enums import BlockSettings
from .. import components


class Block(dict):

    def __init__(self, data):

        if type(data) == Block:
            super().__init__(data)
            return

        super().__init__()
        if type(data) == dict:
            data = data
        elif type(data) == str:
            data = components.keyval(data.split(","))
        else:
            raise TypeError

        for key, val in data:

            try:
                data_key = BlockSettings(int(key))

                match data_key:
                    case BlockSettings.groups:
                        val_data = Groups(val)
                    case BlockSettings.color_1_hsv_values:
                        val_data = HSV(val)
                    case BlockSettings.color_2_hsv_values:
                        val_data = HSV(val)
                    case BlockSettings.comparison:
                        val_data = Comparison(int(val))
                    case BlockSettings.easing:
                        val_data = Easing(int(val))
                    case BlockSettings.copied_color_hsv_values:
                        val_data = HSV(val)
                    case _:
                        val_data = val

            except ValueError:
                data_key = key
                val_data = val

            if type(val_data) == str:
                try:
                    val_data = int(val_data)
                except ValueError:
                    try:
                        val_data = float(val_data)
                    except ValueError:
                        pass

            self.update({data_key: val_data})

    def __setitem__(self, key: BlockSettings | str, val):
        self.update({key: val})

    def __getitem__(self, key):
        if key not in self:
            return False
        return self.get(key)

    def to_str(self):
        block_list = []

        for key, val in self.items():
            if type(key) == int:
                data_key = str(key)
            elif type(key) == BlockSettings:
                data_key = str(key.value)
            else:
                raise TypeError

            if isinstance(val, ComplexProperty):
                val_data = val.to_str()
            else:
                val_data = str(val)

            block_list += [data_key, val_data]

        return ",".join(block_list)

    def __str__(self):
        block_list = []

        for key, val in self.items():
            if type(key) == BlockSettings:
                block_list += [f"{key.name} = {val}"]
            elif type(key) == str:
                block_list += [f"{key} = {val}"]

        return "; ".join(block_list)

    def __repr__(self):
        block_list = []

        for key, val in self.items():
            block_list += [f"{str(key)} = {val}"]

        return " | ".join(block_list)


class Blocks(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_str(self):
        str_data = []
        for block in self:
            str_data.append(block.to_str())
        return ";".join(str_data)

    def add(self, block: Block):
        self.insert(0, block)

    def __str__(self):
        return "Block list"
