from enum import StrEnum


class LevelSettings(StrEnum):

    key_check = "kCEK"
    id = "k1"
    name = "k2"
    description = "k3"
    editor = "k4"
    player_name = "k5"
    official_music = "k8"
    attempts = "k18"
    percent_normal = "k19"
    percent_practice = "k20"
    level_type = "k21"
    replay = "k34"
    jumps = "k36"
    password = "k41"
    server_id = "k42"
    player_music_id = "k45"
    revision = "k46"
    is_editor = "k47"
    objects_count = "k48"
    game_build = "k50"
    coin1 = "k61"
    coin2 = "k62"
    coin3 = "k63"
    difficulty = "k66"
    object_limit = "k69"
    percent_normal2 = "k71"
    unlisted = "k79"
    editor_time = "k80"
    percent_normal3 = "k90"
    cameraX = "kI1"
    cameraY = "kI2"
    zoom = "kI3"
    tab = "kI5"
    tablist = "kI6"
    layer = "kI7"

    def __repr__(self):
        return f"{self.name} <{self.value}>"

    def __str__(self):
        return f"{self.name} <{self.value}>"
