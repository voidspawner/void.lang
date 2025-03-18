# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **[V O I D](#v-o-i-d-format)** or **[JSON](https://en.wikipedia.org/wiki/JSON)** format. It is used as a replacement for the standard **``Bash``**・**``CMD``**・etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one ``V O I D`` or ``JSON`` file**. Since the **code is presented as data**, applications can be easily generated with **``AI``**, updated, installed and launched remotely.

> [!IMPORTANT]
> **The project is in the process of development.**

  <img src="https://github.com/voidspawner/voidspawner.github.io/blob/main/site/image/logo.jpg" width="100%">

> [**About**](#about)・
[**Preinstalled Language**](#preinstalled-language)・
[**Example**](#example)・
[**How to Use**](#how-to-use)・
[**How to Use Game Engine**](#how-to-use-game-engine)・
[**Actions**](#actions)・
[**V O I D format**](#v-o-i-d-format)・
[**V O I D db**](#v-o-i-d-db)・
[**V O I D ai**](#v-o-i-d-ai)・
[**V O I D game**](#v-o-i-d-game)・
[**V O I D social**](#v-o-i-d-social)・
[**V O I D os**](#v-o-i-d-os)・
[**V O I D tech**](#v-o-i-d-tech)・
[**V O I D ideology**](#v-o-i-d-ideology)・
[**V O I D license**](#v-o-i-d-license)・
[**V O I D task**](#v-o-i-d-task)

## Preinstalled Language

| Language                                                 | Engine                              | Web                     | CLI                     | Server                  | Mobile                  | Windows                 | macOS                   | Linux                   | iOS                     | Android                 | Xbox                    | Switch                  | PlayStation             | Steam Deck              |
| -------------------------------------------------------- | ----------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| [**Python**](https://www.python.org/downloads)           | <p align="center">Python</p>        | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> |
| [**JavaScript**](https://nodejs.org/en/download)         | <p align="center">NodeJS</p>        | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> |
| [**Swift**](https://www.swift.org/download)              | <p align="center">-</p>             | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> |
| [**Kotlin**](https://developer.android.com/studio)       | <p align="center">-</p>             | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> |
| [**GDScript**](https://godotengine.org/download/windows) | <p align="center">Godot</p>         | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> |
| [**C++**](https://www.unrealengine.com/download)         | <p align="center">Unreal Engine</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> |

## Example
##### Simple
```json
{
  "run": [
    [".", "Hi World :D"]
  ]
}
```
##### Even simpler
```json
[
  [".", "Hi World :D"]
]
```
##### Multilanguage text
```json
{
  "run": [
    [".", "{text.hi} :D"]
  ],
  "text": {
    "hi": {
      "en": "Hi World",
      "zh": "你好世界",
      "fr": "Bonjour le monde",
      "es": "Hola Mundo",
      "pt": "Olá Mundo",
      "it": "Ciao mondo",
      "de": "Hallo Welt",
      "jp": "こんにちは世界",
      "ru": "Привет, мир",
      "ar": "مرحبا بالعالم",
      "hi": "हैलो वर्ल्ड"
    }
  }
}
```
##### Web server
```json
{
  "run": [
    ["cloud.web", {
      "route": [
        ["/", "home"]
      ]
    }]
  ],
  "action": {
    "home": [
      ["response", "<h1>Hi World 😄</h1>"]
    ]
  }
}
```
##### Web server simpler
```json
[
  ["cloud.web": {
    "route": [
      ["/", [
        ["response", "<h1>Hi World 😄</h1>"]
      ]]
    ]
  }]
]
```
##### Web app with UI
```json
{
  "run": [
    ["cloud.web": {
      "route": [
        ["/", [
          ["title", "{text.hi}"],
          ["text", "{text.hi}", {
            "color": "white",
            "background": "green",
            "size": 20
          }]
        ]]
      ]
    }]
  ],
  "text": {
    "hi": "Hi World 😄"
  }
}
```
##### File sharing
```json
[
  ["cloud.file": "/path/to/share"]
]
```
##### Add comments
```json
{
  "description": "All code is data. So just add the property 'description', '//' and so on",
  "version": {
    "description": "Version description",
    "number": 1,
    "name": "First"
  },
  "run": [
    [".", "Hi World :D"]
  ]
}
```
##### Use loop and conditions
```json
[
  ["=", "word", "Hi World :D"],
  ["o", "letter", "{word}", [
    ["?", ["{letter}", "=", "i"], [
      ["..", "i!"]
    ], [
      ["..", "{letter}"]
    ]]
  ]]
]
```
##### Get the last result without using variables
```json
[
  ["replace", "Hi World :D", "i", "i!"],
  [".", "{}"],
  "upper",
  "."
]
```
##### Run native code
```json
[
  ["code", "for i in range(10):print(i)"]
]
```
##### Import into your project
```python
exec(open('void.py').read())
encrypted = void.encrypt('Hi World :D')
print(void.decrypt(encrypted.text, encrypted.key))
```

## How to Use

1. Download **V O I D lang**
2. Create your first vapp (V O I D app) in **``run.json``** or other JSON file
3. Launch vapp with **V O I D lang**
 
```console
python void.py vapp.json
```

**Alternative**

```console
python void.py vapp.void
```
```console
python void.py app.py
```
```console
python void.py "['.', 'Hi World :D']"
```

> [!TIP]
> **Linux・macOS**: Add alias to **``~/.bashrc``** ・ **``~/.zshrc``** ・ **``~/.bash_profile``** (macOS)
> ```console
> alias void="python /path/to/void.py"
> ```
> 
> **Windows**: Use alias in command line
> ```console
> doskey void=python /path/to/void.py
> ```
> ```console
> void vapp.json
> ```
> 
> **Swift・Kotlin・C++**: Embed the **vapp** in the source code and compile it into an executable
> ```console
> swiftc void.swift
> ```
> ```console
> kotlinc void.kt
> ```
> ```console
> clang++ void.cpp -o void.exe
> ```

## How to Use Game Engine

1. Buy **V O I D spawner** game on **Steam**
2. Create your first game in **``run.json``** file
3. Copy the **void.exe** file from the **V O I D spawner** game to the same directory as **``run.json``** file
4. Sell your game or share with friends

> [!NOTE]
> **Run with game engine**
> ```console
> void.exe game.json
> ```
>
> **The archive contains ``run.json`` and all game files**
> ```console
> void.exe game.zip
> ```
>
> **The execution directory contains ``run.json`` and all game files or contains ``run.zip`` file**
> ```console
> void.exe
> ```
>
> You can use the **Exporter** inside the **V O I D spawner** game to export your game to all platforms ⌜**Windows**・**macOS**・**Linux**・**Android**・**iOS**・**Web**・**Xbox**・**Switch**・**PlayStation**⌟

**Alternative**

1. Download **V O I D lang**
2. Import **``void.gd``**・**``void.cpp``** into the **Godot**・**Unreal Engine**
3. Create your first game in **``run.json``** file
4. Export the game in the engine itself to the available platforms
5. Sell your game or share with friends

## Actions

> Count **``591``**
>
> [!NOTE]
> **Use Help to display a description of the action**
>
> ```json
> ["help"],
> ["help", "upper"]
> 
> ```console
> python void.py help
> python void.py help upper
> ```
 
## V O I D format
**⌜ V O I D format ⌟** is the data format that inherits the best features of [**JSON**](https://en.wikipedia.org/wiki/JSON), [**YAML**](https://en.wikipedia.org/wiki/YAML), [**CSV**](https://en.wikipedia.org/wiki/Comma-separated_values) and [**plain text**](https://en.wikipedia.org/wiki/Plain_text) formats. Makes it easier to write and read data, both by human and by program. The format simplifies data creation by removing the use of unnecessary quotation marks, brackets, colons, commas and other symbols. It is possible to combine **text** and **binary** data.

```
extension
    .void
    .txt
mime type
    application/void
influenced by
    json
    yaml
    csv
    python
    assembly
    plain text
container
    settings
    text
    code
    data
    image
    video
    sound
    3d
    subtitles
    font
    file
value type
    text
    number
    boolean
    list
    dictionary
    none
    binary
indent
    tab
        \t
separator
    space
        " "
newline
    line feed
        \n
code
    encode
        [void.encode [1 2 3]]
    decode
        [void.decode "[1 2 3]"]
    write
        [file path/to/file.void [1 2 3]]
    read
        [file path/to/file.void]
    compress
        [file.void path/to/file]
        [dir.void path/to/dir]
    decompress
        [file.unvoid path/to/file.void]
    encrypt
        [file.void path/to/file key]
        [dir.void path/to/dir key]
    decrypt
        [file.unvoid path/to/file.void key]
```

<table>
<tr>
<th align="center"><img width="441" height="1"><p>V O I D format</p></th>
<th align="center"><img width="441" height="1"><p>JSON</p></th>
</tr>

<tr>
<td>

```
text
```

</td>
<td>

```json
"text"
```

</td>
</tr>

<tr>
<td>

```
text with space
```
```
"text with space"
```
```
text\ with\ space
```

</td>
<td>

```json
"text with space"
```

</td>
</tr>

<tr>
<td>

```
"
    multiline
    text
```

</td>
<td>

```json
"multiline\ntext"
```

</td>
</tr>

<tr>
<td>

```
'
    text
    in
    a
    line
```

</td>
<td>

```json
"textinaline"
```

</td>
</tr>

<tr>
<td>

```
c:\Users\name\Desktop
```

</td>
<td>

```json
"c:\\Users\\name\\Desktop"
```

</td>
</tr>

<tr>
<td>

```
"\t\n\r\"\\"
```

</td>
<td>

```json
"\t\n\r\"\\"
```

</td>
</tr>

<tr>
<td>

```
123
```

</td>
<td>

```json
123
```

</td>
</tr>

<tr>
<td>

```
-123
```

</td>
<td>

```json
-123
```

</td>
</tr>

<tr>
<td>

```
0.123
```

</td>
<td>

```json
0.123
```

</td>
</tr>

<tr>
<td>

```
100_000
```

```
100 000
```

</td>
<td>

```json
100000
```

</td>
</tr>

<tr>
<td>

```
true
```

</td>
<td>

```json
true
```

</td>
</tr>

<tr>
<td>

```
false
```

</td>
<td>

```json
false
```

</td>
</tr>

<tr>
<td>

```
none
```

</td>
<td>

```json
null
```

</td>
</tr>

<tr>
<td>

```
1
text
true
false
none
```

</td>
<td>

```json
[
  1,
  "text",
  true,
  false,
  null
]
```

</td>
</tr>

<tr>
<td>

```
[
    [1 12.34 Name]
    [2 56.78 Other\ name]
]
```

```
[
    [1 12.34 Name
    [2 56.78 "Other name
```

```
[]
    1 12.34 Name
    2 56.78 "Other name
```

</td>
<td>

```json
[
    [1, 12.34, "Name"],
    [2, 56.78, "Other name"]
]
```

</td>
</tr>

<tr>
<td>

```
name
    text
other name
    123
```

</td>
<td>

```json
{
    "name": "text",
    "other name": 123
}
```

</td>
</tr>

<tr>
<td>

```
[name:text other\ name:123
```

</td>
<td>

```json
{"name": "text", "other name": 123}
```

</td>
</tr>

<tr>
<td>

```
[
    name
        text

    other name
        123
```

</td>
<td>

```json
[
    {
        "name": "text"
    },
    {
        "other name": 123
    }
]
```

</td>
</tr>

<tr>
<td>

```
text
    text
multiline text
    "
        multiline
        text
text in a line
    '
        text
        in
        a
        line
escape
    "\t\n\r\"\\"
int
    123 000
float
    1.23
bool
    true
empty
    none
list
    text
    1
    true
    false
    none
short list
    [text 1 true false none]
dictionary
    name 1
        true
    name 2
        true
code
    []
        . "Hi World :D
        = var 123
        . {var}
base64
    *
        ViBPIEkgRCBmb3JtYXQ=
base64 + gzip
    *
        eNoLU/BX8FRwUUjLL8pNLAEAG0QEPA==
base64 short
    *ViBPIEkgRCBmb3JtYXQ=
binary
    *
        3
        <00 01 02>
binary short
   *3*<00 01 02>
binary in hex
    *
        56 20 4F 20 49
        20 44 20 66 6F
        72 6D 61 74
binary in bin
    *
        0000 1000 1111 0001
```

</td>
<td>

```json
{
    "text": "text",
    "multiline text": "multiline\ntext",
    "text in a line": "textinaline",
    "escape": "\t\n\r\"\\",
    "int": 123000,
    "float": 1.23,
    "bool": true,
    "empty": null,
    "list": [
        "text",
        1,
        true,
        false,
        null
    ],
    "short list": ["text", 1, true, false, null],
    "dictionary": {
        "name 1": true,
        "name 2": true
    },
    "code": [
        [".", "Hi World :D"],
        ["=", "var", 123],
        [".", "{var}"]
    ],
    "base64": "need to convert",
    "base64 + gzip": "need to convert",
    "base64 short": "need to convert",
    "binary": "impossible",
    "binary short": "impossible",
    "binary in hex": "need to convert",
    "binary in bin": "need to convert"
}
```

</td>
</tr>

</table>

> [!TIP]
> Use **V O I D format [highlighting 📃](https://github.com/voidspawner/voidspawner.github.io/blob/main/site/settings/void.sublime-syntax)** for **[Sublime Text](https://sublimetext.com)**.
>
> ``Tools`` → ``Developer`` → ``New Syntax…`` → ``Copy · Paste`` → ``Save as void.sublime-syntax``
>
> You can change the **color scheme** to alternate sections.
> 
> ``Preferences`` → ``Customize Color Scheme``
>
> ```json
> {
>   "rules":
>	  [
>	    {
>	      "scope": "variable.void.odd",
>	      "foreground": "hsl(185, 100%, 50%)"
>	    },
>	    {
>	      "scope": "variable.void.even",
>	      "foreground": "hsl(185, 100%, 80%)"
>	    }
>	  ]
> }
> ```

## V O I D db
A database that uses **``V O I D``** · **``JSON``** · **``CSV``** files for storage directly. Data is **cached**, **indexed** and **saved** automatically. **Easy access** to data without the need to create complex constructs.

> ``data.json``
> ```json
> {
>   "name": {
>     "subname": "value"
>   },
>   "list": [
>     {
>       "index": 1,
>       "value": 1
>     },
>     {
>       "index": 2,
>       "value": 2
>     }
>   ]
> }
> ```
>
> ```
> . {data.json/name.subname}
> . {data.json/list.index.2.value}
> = data.json/list.index.2.value 3
>```

> ``data.csv``
> ```csv
> index,text,value
> 1,text 1,value 1
> 5,text 5,value 5
> ```
>
> ```
> . {data.csv/index.5.value}
> . {data.csv/1.value}
> = data.csv/index.5.value 3
>```

## V O I D ai
**[Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)** that makes it easier to work with data. Third-party AI is currently connected.

> **ChatGPT**
>
> ```
> chat "radius of the Earth"
> chat "tell me a story"
> chat "translate to portuguese: Hi world :D"
> translate "嗨，世界 :D"
> translate "Hi world :D" portuguese
> image "playing cats on the lawn" cats.jpg
> recognize "what's in the lower left corner?" cats.jpg
> code "python mouse movement simulation"
> ```
>
> **Stable Diffusion**
>
> ```
> image "playing cats on the lawn" cats.jpg
> video "playing cats on the lawn" cats.mp4
> fix "remove the cat in the center and add more grass" cats.jpg cats-edited.jpg
> recolor dogs.jpg dogs-colorized.jpg
> restyle "cyberpunk" cats.jpg cats-cyberpunk.jpg
> restyle "Van Gogh" cats.jpg cats-vangogh.jpg
> nobg cats.jpg cats-without-background.png
> 2x cats.jpg cats-resize-2x.jpg
> 4x cats.jpg cats-resize-4x.jpg
> reface man.jpg child.jpg man-to-child.jpg
> asset.character "a girl in a tight space suit without a helmet smiles welcomingly" girl.jpg
> asset.pixel "brick walls 32x32" wall.png
> ```
> 
> **TRELLIS**
>
> ```
> asset.3d "a white cat sits on a stack of books" cat.glb
> ```
> 
> **Voice Cloning**
>
> ```
> say "Hi world :D"
> voice
> voice duck duck-voice.mp3
> voice duck
> say "Hi world :D"
> revoice my-voice.mp3 talk.mp3 my-talk.mp3
> revoice duck talk.mp3 duck-talk.mp3
> ```
> 
> **speechrecognition**
>
> ```
> voice.text
> voice.text talk.mp3
> voice.text video.mp4
> ```
> 
> **gTTS**
>
> ```
> say "Hi world :D"
> voice
> voice name
> ```
> 
> **DeepL**
>
> ```
> translate "你好，世界 :D"
> ```

Work is underway to develop a custom AI that will run on a **[V O I D chip](https://github.com/voidspawner/void.tech#chip)**.

## V O I D game
**[⌜V O I D game⌟](https://voidspawner.github.io)** is a game that creates an **infinite** number of games, v-apps and content.

## V O I D social
**⌜ V O I D social ⌟** is a social network where you can **quickly** and **easily** communicate without words with people all over the world.

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create applications and games.

## V O I D tech
**[⌜ V O I D tech ⌟](https://github.com/voidspawner/void.tech)** are combinable devices controlled by **[V O I D ai](#v-o-i-d-ai)** for creating **individual** stand-alone productions, as well as creating individual products with **unique designs** and in the required quantities.

## V O I D ideology
**[⌜V O I D⌟](https://github.com/voidspawner/void.ideology)**  is not only about compact technologies, but also an **ideology** that shows where these technologies are taking us.

## V O I D license
**⌜ V O I D license ⌟** is a license to distribute digital content and goods. Expressed in a single sentence:

> **DO WHAT YOU WANT**

You can use it in both **private** and **open source**, embed it in **free** or **paid** products. **Modify**. Create your **own solutions** based on it. **No need to specify the author**.

## V O I D task
> [!IMPORTANT]
> By adding your code to the repository, you are publishing it under the **V O I D licence**.

Find out current **tasks** and **payment** at [**V O I D task**](https://github.com/voidspawner/void.task)
