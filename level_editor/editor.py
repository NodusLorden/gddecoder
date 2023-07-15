from .level_enums import EditorSettings, PlayerSpeed
from .complex_property import ComplexProperty
from .color import Colors
from .blocks import Block, Blocks
from .. import decoders
from .. import components


class Editor(dict):

    def __init__(self, str_data=""):
        super().__init__()

        self.blocks = Blocks()
        self.colors = Colors()
        self[EditorSettings.music_offset] = 0.0
        self[EditorSettings.background] = 0
        self[EditorSettings.ground] = 0
        self[EditorSettings.game_mode] = 0
        self[EditorSettings.mini] = False
        self[EditorSettings.dual] = False
        self[EditorSettings.player_speed] = PlayerSpeed(0)
        self[EditorSettings.two_player_mode] = False

        if not str_data:
            return

        data = decoders.editor_decoder(str_data)
        level_properties, blocks_str = data.split(";", 1)

        self.load_properties(level_properties)
        self.load_blocks(blocks_str)

    def load_properties(self, level_properties):
        for key, val in components.keyval(level_properties.split(",")):
            try:
                data_key = EditorSettings(key)

                match data_key:
                    case EditorSettings.colors:
                        self.load_colors(val)
                        continue
                    case _:
                        val_data = val

            except ValueError:
                data_key = key
                val_data = val

            self.update({data_key: val_data})

    def load_blocks(self, blocks_str):
        set(map(lambda block: self.blocks.append(Block(block)), blocks_str.split(";")[:-1]))

    def load_colors(self, colors_str):
        set(map(lambda color: self.colors.load_color(color), colors_str.split("|")[:-1]))

    def to_str(self):
        str_data_list = ["kS38", self.colors.to_str()]

        for key, val in self.items():

            if type(val) == bool:
                val_data = str(int(val))
            elif isinstance(val, ComplexProperty):
                val_data = val.to_str()
            else:
                val_data = str(val)

            if type(key) == EditorSettings:
                data_key = str(key.value)
            elif type(key) == str:
                data_key = key
            else:
                raise TypeError

            str_data_list += [data_key, val_data]

        str_data = ",".join(str_data_list) + ";" + self.blocks.to_str() + ";"
        return decoders.editor_encoder(str_data)

    def __str__(self):
        return f"Blocks count: {len(self.blocks)}"

    def __repr__(self):
        return f"Blocks count: {len(self.blocks)}"
