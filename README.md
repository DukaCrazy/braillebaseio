# Braille Base IO
Reader for JSON, XML, and CSV formats.

## Input Examples
JSON example:
```json
[
    {
        "letter": "a",
        "braille": "⠁,⠁",
        "pattern": 0
    },
    {
        "letter": "b",
        "braille": "⠟,⠟,⠟",
        "pattern": 0
    }
]
```
XML example:
```xml
<?xml version="1.0" encoding="utf-8"?>
<braille_append>
    <item>
        <letter>a</letter>
        <braille>⠁,⠁</braille>
        <pattern>0</pattern>
    </item>

    <item>
        <letter>b</letter>
        <braille>⠟,⠟,⠟</braille>
        <pattern>0</pattern>
    </item>
</braille_append>
```
CSV example:
```csv
a,"⠁,⠁",0
b,"⠟,⠟,⠟",0
```
## Output Example

[('a', ['⠁', '⠁'], 0), ('b', ['⠟', '⠟', '⠟'], 0)]

<img src="./img/logo.png" alt="Logo" width="500" height="493">


