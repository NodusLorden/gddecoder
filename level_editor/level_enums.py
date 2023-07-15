from enum import IntEnum, StrEnum


class ColorsSettings():



    def __str__(self):
        return f"{self.name} <{self.value}>"

    def __repr__(self):
        return f"{self.name} <{self.value}>"


class EditorSettings(StrEnum):

    colors = "kS38"
    music_offset = "kA13"
    background = "kA6"
    ground = "kA7"
    fonts = "kA18"
    game_mode = "kA2"
    mini = "kA3"
    dual = "kA8"
    player_speed = "kA4"
    two_player_mode = "kA10"
    flip_gravity = "kA11"

    def __str__(self):
        return f"{self.name} <{self.value}>"

    def __repr__(self):
        return f"{self.name} <{self.value}>"


class PlayerSpeed(IntEnum):
    default = 0
    slow = 1
    double = 2
    triple = 3
    quadruple = 4

    def __str__(self):
        return f"{self.name} <{self.value}>"


class GameModes(IntEnum):
    cube = 0
    ship = 1
    boll = 2
    ufo = 3
    wave = 4
    robot = 5

    def __str__(self):
        return f"{self.name} <{self.value}>"


class BlockSettings(IntEnum):
    id = 1
    x = 2
    y = 3
    x_flipped = 4
    y_flipped = 5
    rotation = 6
    red = 7
    green = 8
    blue = 9
    time = 10
    touch_triggered = 11
    secret_coin_id = 12
    portal_checked = 13
    tint_ground = 14
    player_color_1 = 15
    player_color_2 = 16
    blending = 17
    editor_layer_1 = 20
    color_1 = 21
    color_2 = 22
    color_id = 23
    z_layer = 24
    z_order = 25
    move_x = 28
    move_y = 29
    easing = 30
    text = 31
    scale = 32
    group_parent = 34
    opacity = 35
    is_active_trigger = 36
    color_1_hsv_enabled = 41
    color_2_hsv_enabled = 42
    color_1_hsv_values = 43
    color_2_hsv_values = 44
    fade_in_time = 45
    hold_time = 46
    fade_out_time = 47
    pulse_mode = 48
    copied_color_hsv_values = 49
    copied_color_id = 50
    target_group_id = 51
    pulse_type = 52
    tp_portal_distance = 54
    activate_group = 56
    groups = 57
    lock_to_player_x = 58
    lock_y = 59
    copy_opacity = 60
    editor_layer_2 = 61
    spawn_triggered = 62
    spawn_duration = 63
    do_not_fade = 64
    main_only = 65
    detail_only = 66
    do_not_enter = 67
    degrees = 68
    times_360 = 69
    lock_object_rotation = 70
    follow_target_pos_center_id = 71
    x_mod = 72
    y_mod = 73
    strength = 75
    animation_id = 76
    count = 77
    subtract_count = 78
    pickup_mode = 79
    block_a_id = 80
    hold_mode = 81
    toggle_mode = 82
    interval = 84
    easing_rate = 85
    exclusive = 86
    multi_trigger = 87
    comparison = 88
    dual_mode = 89
    speed = 90
    follow_delay = 91
    offset_y = 92
    trigger_on_exit = 93
    dynamic_block = 94
    block_b_id = 95
    glow_disabled = 96
    custom_rotation_speed = 97
    disable_rotation = 98
    multi_activate = 99
    use_target_enabled = 100
    target_pos_coordinates = 101
    editor_disable = 102
    high_detail = 103
    max_speed = 105
    randomize_start = 106
    animation_speed = 107
    grouping = 108

    def __str__(self):
        return f"{self.name} <{self.value}>"

    def __repr__(self):
        return f"{self.name} <{self.value}>"


class Easing(IntEnum):

    Ease_in_out: int = 1
    Ease_in: int = 2
    Ease_out: int = 3
    Elastic_in_out: int = 4
    Elastic_in: int = 5
    Elastic_out: int = 6
    Bounce_in_out: int = 7
    Bounce_in: int = 8
    Bounce_out: int = 9
    Exponential_in_out: int = 10
    Exponential_in: int = 11
    Exponential_out: int = 12
    Sine_in_out: int = 13
    Sine_in: int = 14
    Sine_out: int = 15
    Back_in_out: int = 16
    Back_in: int = 17
    Back_out: int = 18

    def __str__(self):
        return f"{self.name} <{self.value}>"


class Comparison(IntEnum):

    Equals: int = 0
    Larger: int = 1
    Smaller: int = 2

    def __str__(self):
        return f"{self.name} <{self.value}>"
