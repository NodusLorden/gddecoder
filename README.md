# gddecoder
Lib for work this Geometry Dash levels


## Start
```py
from gddecoder import *

levels = LocalLevels()
```
If you need to work with a save file that is not in the standard path
```py
levels = LocalLevels("path/to/file/CCLocalLevels.dat")
```
`LocalLevels` is list of levels, to get the level, use the `levels.get_level()` method or standard list syntax `levels[n]`.

```py
level1 = levels.get_level(10)
level2 = levels.get_level("first level")
level3 = level[10]
```

`levels[n]` don't support levels names, ~~level["first level"]~~.

## Change levels
Level is `dict`. To refer to a key in a level, you can use the name of the key that matches the name of the key in the game's save file, or use the `LevelSettings` enum.

```py
level["k2"] = "test level"
level[LevelSettings.objects_count] = 800
```

### Some programs

Print names of all levels:
```py
from  gddecoder import *


levels = LocalLevels()

for lvl in levels:
    print(lvl[LevelSettings.name])
```

Counting the total number of jumps in levels:
```py
from gddecoder import *


levels = LocalLevels()

jumps = 0

for lvl in levels:

    # test because the level may not have jumps
    if LevelSettings.jumps in lvl:
        jumps += lvl[LevelSettings.jumps]

print(jumps)
```

## Editor

Level has method `get_editor`, it return Editor object.
```py
editor = level.get_editor()
```

Editor object has attribute `blocks` and `colors`. Other properties are stored as in a dictionary. Use `EditorSettings` enum or game key.
```py
# set 2 player mode
editor[EditorSettings.two_player_mode] = True
# get 20 block in level
blocks = editor.blocks[19]
# get bg Color
color_bg = editor.colors[1000]
```

## Blocks

Blocks are also dictionaries. Use `BlockSettings` enum.
```py
block = editor.blocks[9]
block[BlockSettings.x] = 30
block[BlockSettings.y] = 15
```

### Add block
```py
editor.blocks.add(Block(
    {
        BlockSettings.id: 1,
        BlockSettings.x: 15,
        BlockSettings.y: 15,
    }
))
```

### Block duplication
```py
editor.blocks.add(Block(
    editor.blocks[9]
))
```

### Set groups
`Groups` is set.
```py
block = editor.blocks[9]
block[BlockSettings.groups] = Groups([1, 2, 10])
```
```py
block[BlockSettings.groups].add(14)
```
```py
block[BlockSettings.groups].pop(10)
```

### Colors
The block stores only the color channel of the block as an int. To change a color, you need to change the corresponding color in `editor.colors` and then assign it to the block.


## Save
Save to standart path:
```py
level.set_editor(editor)
levels.save()
```
For other path:
```py
level.set_editor(editor)
levels.save("other/path/file.dat")
```
