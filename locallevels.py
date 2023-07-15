from getpass import getuser

from .level_editor.editor import Editor
from .enums import LevelSettings
from . import decoders
from . import converters


class Level(dict):

    def __init__(self, dict_data: dict):
        super().__init__()
        for key, val in dict_data.items():
            try:
                self.update({LevelSettings(key): val})
            except ValueError:
                self.update({key: val})

    def __setitem__(self, key: LevelSettings | str, val):
        self.update({key: val})

    def to_dict(self):
        level_dict = {}

        for key, val in self.items():
            if type(key) == str:
                level_dict[key] = val
            elif type(key) == LevelSettings:
                level_dict[key.value] = val

        return level_dict

    def get_editor(self):
        return Editor(self[LevelSettings.editor])

    def set_editor(self, editor):
        self[LevelSettings.editor] = editor.to_str()


class LocalLevels(list):

    def __init__(self, file_path=None):
        super().__init__()

        if not file_path:
            self.file_path = f"C:\\Users\\{getuser()}\\AppData\\Local\\GeometryDash\\CCLocalLevels.dat"
        else:
            self.file_path = file_path

        with open(self.file_path, mode="rb") as file:
            bfile = file.read()

        plist = decoders.save_file_decoder(bfile)

        file_dict = converters.str_to_dict(plist)[0]
        levels_dict = file_dict["LLM_01"]
        levels_dict.pop("_isArr")

        self._GAME_BUILD = file_dict.pop("LLM_02")

        for level in levels_dict.values():
            self.append(Level(level))

    def get_level(self, key) -> Level:
        if isinstance(key, int):
            return self[key]
        elif isinstance(key, str):
            for level in self:
                if level[LevelSettings.name] == key:
                    return level
            raise NameError

    def save(self, file_path=None):
        if not file_path:
            path = self.file_path
        else:
            path = self.file_path

        level_dict = {}
        for i, level in enumerate(self):
            level_dict[f"k_{i}"] = level.to_dict()

        plist = f"<?xml version=\"1.0\"?><plist version=\"1.0\" gjver=\"2.0\"><dict><k>LLM_01</k>" \
                f"<d><k>_isArr</k><t />{converters.dict_to_str(level_dict)}</d>" \
                f"<k>LLM_02</k><i>{self._GAME_BUILD}</i></dict></plist>"

        bfile = decoders.save_file_encoder(plist)
        with open(path, "wb") as f:
            f.write(bfile)


if __name__ == '__main__':
    levels = LocalLevels()
    print("Levels opened successful,", len(levels), "levels")
