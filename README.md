# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **JSON format**. It is used as a replacement for the standard Bash/CMD/etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

**The project is in the process of development. Code and description are subject to change and inconsistency.**

<img src="https://i.imgur.com/kx2UcUh.jpg" width="100%">

## Preinstalled Language

- **Python** ⌜CLI App・Web Server・API Server⌟
- **PHP** ⌜CLI App・Web Server・API Server⌟
- **JavaScript** ⌜Web App・Web Server (with NodeJS)・API Server (with NodeJS)・CLI App (with NodeJS)⌟
- **Swift** ⌜macOS App・iOS App・iPadOS App・watchOS App・tvOS App・Linux App・Windows App・Web Server・API Server・Game Native⌟
- **Java** ⌜Android App・Linux App・Windows App・Web Server・API Server・Game Native⌟
- **C#** ⌜Windows App・Web Server・API Server・Game Native⌟

## Game Engine

This is a compiled **V O I D spawner** game for rapidly creating games and applications in **V O I D lang**. It use multiple game engines:

- **Godot Engine**
- **Unreal 5 Engine**
- **V O I D engine**

## Example
##### Simple
```javascript
{
  "run": [
    [".", "Hi World!"]
  ]
}
```
##### Even Simpler
```javascript
[
    [".", "Hi World!"]
]
```
##### Multilanguage Text
```javascript
{
  "run": [
    [".", "{text.hi}!"]
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
##### Web Server
```javascript
{
  "run": [
    ["server.http", {
      "route": [
        ["/", "home"]
      ]
    }]
  ],
  "action": {
    "home": [
      ["=", "response.text", "<h1>Hi World!</h1>"]
    ]
  }
}
```
##### Web Server Simpler
```javascript
{
  "web": {
    "route": [
      ["/", [
        ["=", "response.text", "<h1>Hi World!</h1>"]
      ]]
    ]
  }
}
```
##### Web App with UI
```javascript
{
  "web": {
    "route": [
      ["/", "web.home"]
    ]
  },
  "action": {
    "web": {
      "home": [
        ["ui.title", "{text.hi}"],
        ["ui.content", [
          ["text", {
            "text": "{text.hi}",
            "color": "white",
            "background": "green",
            "size": 20
          }]
        ]]
      ]
    }
  },
  "text": {
    "hi": "Hi World!"
  }
}
```

## How To Use

1. Download **V O I D lang**
2. Create your first app in JSON file
3. Launch app with **V O I D lang**
   ```console
   python python/void.py myfirstapp.json
   php php/void.php myfirstapp.json
   ```

   ##### Or even without JSON file at all
   ```console
   python python/void.py '[[".", "Hi World!"]]'
   ```

   ##### Tip for Linux / macOS: add alias to ~/.bashrc ・ ~/.zshrc ・ ~/.bash_profile
   ```console
   alias void="python /path/to/python/void.py"
   ```

   ##### Tip for Windows: use alias in command line
   ```console
   doskey void=python /path/to/python/void.py
   ```
   ```console
   void myfirstapp.json
   ```

## How To Use Game Engine

1. Buy **V O I D spawner** game on **Steam**
2. Create your first game in **run.json** file
3. Copy the **void.exe** file from the **V O I D spawner** game to the same directory as **run.json** file
4. Sell your game or share with friends

   ##### Run with game engine
   ```console
   void.exe game.json
   ```

   ##### The archive contains run.json and all game files
   ```console
   void.exe game.zip
   ```

   ##### The execution directory contains run.json and all game files or contains run.zip file
   ```console
   void.exe
   ```

   Or you can use the **Exporter** inside the **V O I D spawner** game to export your game to all platforms ⌜**Windows**・**macOS**・**Linux**・**Android**・**iOS**・**Web**・**Xbox**・**Switch**・**PlayStation**⌟

## How To Add Comments
All code is data. So just add the property "description", "//" and so on.
```javascript
{
  "description": "App Description. But you can write more in version",
  "version": {
    "description": "Comment",
    "number": 1,
    "name": "First App"
  },
  "run": [
    [".", "Hi World!"],
    ["//", "This line will be ignored"]
  ]
}
```

## Actions

[Value](#value)・
[Control](#control)・
[Math](#math)・
[Text](#text)・
[List](#list)・
[Time](#time)・
[Format](#format)・
[Crypto](#crypto)・
[File](#file)・
[Dir](#file)・
[Link](#file)・
[Drive](#file)・
[Request](#request)・
[Server](#server)・
[Cache](#cache)・
[DB](#db)・
[Device](#device)・
[UI](#ui)・
[Engine](#v-o-i-d-engine)・
[AI](#v-o-i-d-ai)・
[Voids](#v-o-i-d-voids)・
[Social](#v-o-i-d-social)

The code is presented as **action name** and **action parameters**.
```javascript
[".", "Hi World!"]
```
```
Action name: "."
Action parameters: ["Hi World!"]
```
#####
```javascript
["=", "value", 1, "+", 1]
```
```
Action name: "="
Action parameters: ["value", 1, "+", 1]
```
#####
```javascript
"."
```
```
Action name: "."
Action parameters: []
```

### Value
##### Set
```javascript
["=", "i", 10]
```
##### Get
```javascript
[".", "{i}"]
```
##### Remove
```javascript
["-", "i"]
```
##### Translate
```javascript
{
  "run": [
    [".", "{text.hi}"]
  ],
  "text": {
    "hi": 
      "en": "Hi World",
      "zh": "你好世界"
    }
  }
}
```
##### Alias
```javascript
{
  "alias": {
    "name": "long name"
  },
  "run": [
    ["=", "long name", 123], 
    [".", "{name}"]
  ]
}
```
##### Binary data in Base64 with or without Gzip
```javascript
{
  "data": {
    "image": "H4sIAD22JWYC/+1YezhU6xp..."
  },
  "run": [
    ["file.write", "image.png", "{data.image}"]
  ]
}
```

### Control
##### Action
```javascript
["action", [
  [".", "Hi World"]
]]
```
##### Action list
```javascript
{
  "run": ["action_name"],
  "action": {
    "action_name": [[".", "action from action list"]]
  }
}
```
##### Load action
```javascript
["action.load", "file.json"],
["action.load", "file.json", "action_to_load"],
["action.load", "file.json", ["action 1", "action 2"]],
["action.load", "file.json", "action_to_load", "action_alias"]
```
##### Switch action
```javascript
["vn.say", "Hi"],
["action.switch", "vn"],
["say", "Hi"],
["action.switch", ["vn", "rpg"]],
["action.switch", "vn", "visual novel"],
["visual novel.say", "Hi"],
["action.switch", false]
```

### Math

### Text

### List

### Time

### Format
##### JSON encode
```javascript
["json", {"text": "With tab indent"}],
["json", {"text": "With tab indent"}, true],
["json", {"text": "Short form without indent"}, null],
["json", {"text": "Short form without indent"}, false],
["json", {"text": "With two spaces indent"}, "  "],
["json", {"text": "With two spaces indent"}, 2]
```
##### JSON decode
```javascript
["json.decode", "{\"text\": \"Text to decode\"}"]
```
##### JSON load
```javascript
["json.load", "file.json"]
```
##### JSON save
```javascript
["json.save", "file.json", {"text": "Save with indent"}],
["json.save", "file.json", {"text": "Short form"}, false]
```
##### V O I D format encode
```javascript
["void.encode", {"text": "Text to encode"}],
["void.encode.short", {"text": "Short form without indent and binary to base64 encoding", "binary": "\u0003\u0004\u0005"}],
["void.encode.binary", {"text": "Short form with binary data", "binary": "\u0003\u0004\u0005"}]
```
##### V O I D format decode
```javascript
["void.decode", "|text:Text\\ to\\ decode|"]
```
##### CSV encode
```javascript
["csv", [["Text",1],["With comma separator",2]]],
["csv", [["Text",1],["With tab separator",2]], "\t"]
```
##### CSV decode
```javascript
["csv.decode", "\"Text\",1\n\"With comma separator\",2"],
["csv.decode", "\"Text\"\t1\n\"With tab separator\"\t2", "\t"]
```
##### YAML encode
```javascript
["yaml", {"text": "With tab indent"}],
["yaml", {"text": "Simple form without indent"}, null],
["yaml", {"text": "With two spaces indent"}, 2]
```
##### YAML decode
```javascript
["yaml.decode", "{\"text\": \"Text to decode\"}"]
```
##### HTML encode
```javascript
```
##### HTML decode
```javascript
```
##### XML encode
```javascript
```
##### XML decode
```javascript
```

### Crypto
##### Hash
```javascript
["hash"],
["hash", 32, ["letter", "number", "symbol"]],
["hash", 32, "ABCDEF0123456789"]
```
##### UUID
```javascript
["uuid"]
```
##### MD5
```javascript
["md5", "Text"]
```
##### SHA1
```javascript
["sha1", "Text"]
```
##### SHA256
```javascript
["sha256", "Text"]
```
##### SHA512
```javascript
["sha512", "Text"]
```
##### RSA encode
##### RSA decode
##### RSA check
##### CRC32
##### BASE64 encode
##### BASE64 decode
##### Gzip encode
##### Gzip decode

### File
### Dir
### Link
### Drive

### Request

### Server
##### HTTP
##### HTTPS
##### API
##### Mail
##### Cloud
##### V O I D server

### Cache

##### Set
##### Get
##### Remove
##### List

### DB

### Device
##### Camera
##### Gallery
##### Calendar
##### GPS
##### Compass
##### Speed
##### Tilt
##### Light
##### Health

### UI
##### Text
```javascript
["ui.text", ""]
```
##### Edit
```javascript
["ui.edit", ""]
```
##### Image
```javascript
["ui.image", ""]
```
##### Button
```javascript
["ui.button", ""]
```
##### Slider
```javascript
["ui.slider", ""]
```
##### Progress
```javascript
["ui.progress", ""]
```
##### Switch
```javascript
["ui.switch", ""]
```
##### Drop
```javascript
["ui.drop", ""]
```
##### Menu
##### List
##### Tile
##### Video
##### Sound
##### Draw
##### View

### HTML
##### head
##### script
##### style
##### meta
##### body

## V O I D engine
A game engine for creating 2D and 3D applications and games.

##### Title
```javascript
["title", "App title"]
```
##### Icon
```javascript
["icon", "icon.webp"]
```

#### Background
```javascript
["bg", "image.webp"],
["bg", "sky", "fade"]
```

#### Background animation
```javascript
["bg.animation", "sakura leaves", "fade"],
["bg.animation.speed", 1.2],
["bg.animation.rotate", 10]
```

#### Effect
```javascript
["effect", {
  "name": "speed fade",
  "effect": "fade",
  "speed": 2.1
}]
```

#### Music
```javascript
["music", "chillout.mp3"],
["music", "chillout"],
["music.play"],
["music.stop", "fade"],
["music.pause"]
```

#### Sound
```javascript
["sound", "chillout.mp3"],
["sound", "chillout"],
["sound.play"],
["sound.stop", "fade"],
["sound.pause"]
```

#### Volume
```javascript
["volume", 0.9],
["volume", "90%"],
["music.volume", "10%"],
["music.volume", 0.1],
["sound.volume", "30%"],
["sound.volume", 0.3]
```

#### Window Size
```javascript
["size", 1000, 800]
```

#### Window Position
```javascript
["position", 100, 200]
```

#### Window Attention
```javascript
["attention"]
```

#### Fullscreen
```javascript
["fullscreen"],
["fullscreen", true],
["fullscreen", false]
```

### Visual Novel

#### Say text
```javascript
["vn.say", null, "Text"]
```
#### Character say
```javascript
["vn.say", "character name", "Text"]
```
#### Character come
```javascript
["vn.come", "character name", "left", "fade"]
```
#### Character leave
```javascript
["vn.leave", "character name", "slide left"]
```
#### Character pose
```javascript
["vn.pose", "character name", "shrug"]
```
#### Character emotion
```javascript
["vn.emotion", "character name", "surprise", "fade"]
```
#### Character outfit
```javascript
["vn.outfit", "character name", ["hat", "butterfly tie", "tuxedo"], "fade"]
```
#### Character effect
```javascript
["vn.effect", "character name", "shake"]
```
#### Select route
```javascript
["vn.ask", [
  ["Do something 1", "action 1"],
  ["Do something 2", "action 2"]
]]
```
#### Character
```javascript
["vn.character", {
  "name": "character name",
  "image": {
    "normal": "char_normal",
    "surprise": "char_normal",
    "laugh": "char_laugh"
  },
  "pose": {
    "normal": "char_normal",
    "shrug": "char_shrug"
  },
  "emotion": {
    "normal": "char_emotion_normal",
    "surprise": "char_emotion_surprise",
    "laugh": "char_emotion_laugh"
  },
  "outfit": {
    "hat": {
       "pose": "normal",
       "image": "hat",
       "position": [30, 20],
       "scale": 0.8,
       "rotate": 20
    }
  }
}]
```
#### Textbar
```javascript
["vn.bar", {
  "image": "bar",
  "position": {
    "bottom": 100,
    "left": 0,
    "right": 0
  },
  "height": 100,
  "aspect": "fill",
  "text": {
    "left": 10,
    "right": 10,
    "top": 20,
    "bottom": 20,
    "font": "regular",
    "size": 12,
    "color": white,
    "autoscroll": true
  },
  "button": {
    "save": {
      "image": "icon_save",
      "position": [100, 20]
    },
    "load": {
      "image": "icon_load",
      "position": [140, 20]
    },
    "autoscroll": {
      "image": "icon_autoscroll",
      "position": [180, 20]
    },
    "skip": {
      "image": "icon_skip",
      "position": [220, 20]
    },
    "exit": {
      "image": "icon_exit",
      "position": [260, 20]
    }
  }
}]
```

### RPG

Will be available in 2024.

### Clicker

Will be available in 2024.

### Microsession

Will be available in 2024.

### 2D

Will be available in 2024.

### 3D

Will be available in 2024.

## V O I D engine godot
Utilizes the **Godot Engine** free game engine to create 2D and 3D applications and games.

## V O I D engine unreal
Utilizes the **Unreal Engine 5.4** commercial game engine to create 2D and 3D applications and games.

## V O I D ai
Generate **images・videos・texts・assets**. A limited number of uses are available for free. To use extra **V O I D ai** you can **pay** with **⦵ voids** digital currency.

Will be available in 2024.

## V O I D voids
Digital currency used in the **V O I D ecosystem**.

- Name ```voids```
- Symbol ```⦵```
- Exchange rate ```⦵ 1``` = ```$ 1``` = ```USD₮ 1```

The currency is also a **spawner**. Every month the profit is distributed among the **voids** holders. The number of voids increases proportionally and can be withdrawn to other digital currencies.

## V O I D social

## V O I D format
**[⌜ V O I D format ⌟](https://github.com/voidspawner/void.format)** is the data format that inherits the best features of **JSON**, **YAML**, **CSV** formats. Makes it easier to write and read data, both by human and by program.

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create games and applications.
