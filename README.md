# V O I D spawner lang

## About
**⌜ V O I D spawner lang ⌟** is a language for rapidly creating applications in the **JSON format**. It is used as a replacement for both the standard Bash/CMD/etc. languages and for writing **UI Applications**, **Servers** and **Games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one JSON file**. Since the **code is presented as data**, applications can be easily automatically generated, updated, installed and launched remotely.

<img src="https://i.imgur.com/gMwOOh9.jpg" width="100%">

## Preinstalled Language

- **Python** ⌜CLI App | Web Server | API Server | Game (with Godot)⌟
- **PHP** ⌜CLI App | Web Server | API Server | Game (with Godot)⌟
- **JS** ⌜Web App | Web Server (with NodeJS) | API Server (with NodeJS) | CLI App (with NodeJS)⌟
- **Swift** ⌜macOS App | iOS App | iPadOS App | watchOS App | tvOS App | Linux App | Windows App | Web Server | API Server | Game (with Godot) | Game (with UE5) | Game Native⌟
- **Java** ⌜Android App | Linux App | Windows App | Web Server | API Server | Game (with Godot) | Game (with UE5) | Game Native⌟
- **C#** ⌜Windows App | Web Server | API Server | Game (with Godot) | Game (with UE5) | Game Native⌟

## Example
##### Simple
```javascript
{
  "run": [
    [".", "Hello World!"]
  ]
}
```
##### Even Simpler
```javascript
[
    [".", "Hello World!"]
]
```
##### Multilanguage Text
```javascript
{
  "run": [
    [".", "{void.text.hello}!"]
  ],
  "text": {
    "void.text.hello": {
      "en": "Hello World",
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
      ["=", "response.text", "<h1>Hello World!</h1>"]
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
        ["=", "response.text", "<h1>Hello World!</h1>"]
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
      ["/", "web.home"],
      ["/hello", "web.hello"]
    ]
  },
  "action": {
    "web": {
      "home": [
        ["ui.title", "{void.text.hello}"],
        ["ui.content", [
          ["button", "{void.text.hello}", [
            ["go", "/hello"]
          ], {
            "color": "white",
            "background": "blue",
            "size": 20
          }]
        ]]
      ],
      "hello": [
        ["ui.title", "{void.text.hello}"],
        ["ui.content", [
          ["text", "{void.text.hello}", {
            "color": "white",
            "background": "green",
            "size": 20
          }]
        ]]
      ]
    }
  },
  "text": {
    "void.text.hello": "Hello World!"
  }
}
```

## How To Use

1. Download **void.lang**
2. Create your first app in JSON file
3. Launch app with **void.lang**
   ```console
   python3 python/void.py myfirstapp.json
   php php/void.php myfirstapp.json
   ```

   ##### Or Even Without JSON File At All
   ```console
   python3 python/void.py '[[".", "Hello World!"]]'
   ```

## How To Add Comments
All code is data. So just add the property "description", "//" and so on.
```javascript
{
  "description": "App Description. But you can write more in version",
  "version": {
    "number": 1,
    "name": "First App"
  },
  "run": [
    [".", "Hello World!"],
    ["//", "This line will be ignored"]
  ]
}
```

## When Will It Be Available
The language was created for my own needs, so as not to write the same code repeatedly. Several versions for PHP and Python languages were created. Now I bring the code to the form that can be published. There are plans to integrate **Social Networks and Trading Platforms API, convert Videos, Images and Music, create Games and work with AI**. And we need to find people who can make it happen.

Changes are made every day. Later, a social network will be launched, the entire work process will be transferred there.

| Progress | Name | Description | Version | Date |
| --- | --- | --- | --- | --- |
| <p align="center">✅</p> | void.lang.python | void.lang in Python language | <p align="center">Beta | <p align="center">2022</p> |
| <p align="center">✅</p> | void.lang.php | void.lang in PHP language | <p align="center">Beta</p> | <p align="center">2022</p> |
| <p align="center">✅</p> | void.web | Social web application | <p align="center">Beta</p> | <p align="center">2022</p> |
| <p align="center">▶️</p> | void.lang.github | void.lang description on GitHub | <p align="center">1</p> | <p align="center">Aug 2023</p> |
| <p align="center">▶️</p> | void.web | Social web application | <p align="center">1</p> | <p align="center">Sep 2023</p> |
| <p align="center">▶️</p> | void.lang.python | void.lang in Python language | <p align="center">1</p> | <p align="center">Aug 2023</p> |
| <p align="center">⏳</p> | void.lang.php | void.lang in PHP language | <p align="center">1</p> | <p align="center">Sep 2023</p> |
| <p align="center">⏳</p> | void.lang.js | void.lang in JavaScript language | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">⏳</p> | void.lang.swift | void.lang in Swift language | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">⏳</p> | void.lang.java | void.lang in Java language | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.lang.cs | void.lang in C# language | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.app | Social mobile and desktop application | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">⏳</p> | void.game | Games constructor | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">⏳</p> | void.ai | Multipurpose AI | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.parts | Robot parts and components | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.voids | Digital currency | <p align="center">1</p> | <p align="center">2024</p> |

## Actions

| [Value](#value) | [Control](#control) | [Math](#math) | [String](#string) | [Array](#array) | [Format](#format) | [Crypto](#crypto) |
| --- | --- | --- | --- | --- | --- | --- |
| [File](#file) | [URL](#url) | [Server](#server) | [Cache](#cache) | [CLI](#cli) | [UI](#ui) | [DB](#db) |
| [Device](#device) | [Social](#social) | [Trade](#trade) | [Game](#game) | [AI](#ai) | | |

The code is presented as **action name** and **action parameters**.
```javascript
[
    [".", "Hello World!"]
]
```
```
Action name: "."
Action parameters: ["Hello World!"]
```

```javascript
[
    ["=", "value", 1, "+", 1]
]
```
```
Action name: "="
Action parameters: ["value", 1, "+", 1]
```

```javascript
[
    ["url", "http://sitename.com", {
      "post": {
        "name1": "value1",
        "name2": "value2"
      },
      "header": {
        "header1": "value1"
      }
    }, [
      [".", "OK : {code}"]
    ]]
]
```
```
Action name: "url"
Action parameters: ["http://sitename.com", {
                     "post": {
                       "name1": "value1",
                       "name2": "value2"
                     },
                     "header": {
                       "header1": "value1"
                     }
                   }, [
                     [".", "OK : {code}"]
                   ]]
```
```javascript
[
  "."
]
```
```
Action name: "."
Action parameters: []
```

### Value
##### Set / Get
```javascript
[
  ["=", "i", 10],
  ["=", "name.subname", 10],
  ["=", "name.text", "name"],
  ["=", "expression", 1, "+", 1, "*", [4, "+", 1]],
  ["=", "random", ["random", 1, 100]],
  ["=", "{name.text}.expression.array", [1, 2, [1, "+", 2]]],
  ["=", "{name.text}.expression.dict", {
    "value1": [1, "+", 1],
    "value2": ["cos", 2],
    "value3": "{value}",
    "array": [1, 2, 3],
    "random": "{random}"
  }],
  ["[=", "name.nonexpression.array", [1, "+", 2, "{random}"]],
  ["[=", "name.nonexpression.dict", {
    "{name}": [1, "+", "{random}"]
  }],
  ["[]=", "name.totallescaped.array", [1, "+", 2, "{random}"]],
  ["[]=", "name.totallescaped.dict", {
    "{name}": [1, "+", "{random}"]
  }],
  [".", "{i}"],
  [".", "{expression}"],
  [".", "{random}"],
  [".", "{name.subname}"],
  [".", "{name}"]
]
```
##### Remove
```javascript
[
  ["=", "dict", {"name1": "value1", "name2": "value2"}],
  ["=", "i", 10],
  ["-", "dict.name1"],
  ["-", "i"],
  [".", "{dict}"],
  [".", "{i}"]
]
```

### Control
##### If / Switch
```javascript
[
  ["=", "i", 10],
  ["?", ["{i}", ">=", 10], [
    [".", "True"]
  ], [
    [".", "False"]
  ]],

  ["?=", "n", ["{i}", "<", 10], true, false],
  [".", "{n}"],

  ["??", "{i}", [
    [1, [
      [".", 1]
    ]],
    [[2, 10], [
      [".", "From 2 to 10"]
    ]],
    ["?", ["{i}", "=", 100], [
      [".", 100]
    ]]
  ], [
    [".", "default"]
  ]]
]
```

##### For / Foreach / While
```javascript
[
  ["...", ["value", 1, 10], [
    [".", "{value}"]
  ]],

  ["...", ["value", 10], [
    [".", "{value}"]
  ]],

  ["...", ["value", 1, 10, 0.1], [
    [".", "{value}"]
  ]],

  ["...", ["letter", "text"], [
    [".", "{letter}"]
  ]],

  ["...", ["value", [1, 2, 3, 5]], [
    [".", "{value}"]
  ]],

  ["...", ["index", "value", {"name1": 1, "name2": 2}], [
    [".", "{index} : {value}"]
  ]],

  ["=", "dict",  {"name1": 1, "name2": 2}],
  ["...", ["index", "value", "{dict}"], [
    [".", "{index} : {value}"]
  ]],

  ["...", ["time", 1000], [
    [".", "repeat 1 sec"],
  ]],

  ["=", "i", 0],
  ["...", ["?", ["{i}", "<", 100]], [
    [".", "{i}"],
    ["++=", "i"]
  ]],

  ["=", "i", 0],
  ["...", ["fps", 10], [
    [".", "{i}"],
    ["++=", "i"],
    ["?", ["i", ">", 100], ["x"]]
  ]],

  ["...", true, [
    [".", "infinite"]
  ]]
]
```

##### Continue / Break / Repeat
```javascript
[
  ["...", ["i", 10], [
    ["?", ["{i}", "%", 2], [
      [".", "continue on {i}"],
      ">>>"
    ]],
    ["?", ["{i}", "=", 7], [
      [".", "break on {i}"],
      "x"
    ]],
    ["?", ["{i}", "=", 5], [
      [".", "repeat 3 times on {i}"],
      ["<<<", 3]
    ]]
  ]]
]
```

##### Exit
```javascript
[
  ["X", 1, "Exit with code 1"]
]
```

##### Error
```javascript
[
  ["xx", 500, "Error happens", {"data": "value"}]
]
```
```javascript
{
  "action": {
    "xx": [
      [":", [
        ["code", "number"],
        ["message", "text"]
      ]],
      [".", "Override error | code : {code} | message : {message}"],
      "X"
    ]
  }
}
```

##### Shell
```javascript
[
  ["shell", "whoami", true],
  ["=", "name", ["shell", "whoami"]],
  [".", "{name}"]
]
```

### Math
```javascript
[
  ["=", "math", {
    "sin": ["sin", 3],
    "cos": ["cos", 3],
    "tan": ["tan", 3],
    "sinh": ["sinh", 3],
    "cosh": ["cosh", 3],
    "tanh": ["tanh", 3],
    "asin": ["asin", 0.5],
    "acos": ["acos", 0.5],
    "atan": ["atan", 0.5],
    "asinh": ["asinh", 3],
    "acosh": ["acosh", 3],
    "atanh": ["atanh", 0.5],
    "round": ["round", 2.546, 2],
    "floor": ["floor", 2.546, 2],
    "ceil": ["ceil", 2.542, 2],
    "ln": ["log", 3],
    "log10": ["log", 3, 10],
    "log2": ["log", 3, 2],
    "abs": ["abs, -10]
  }],
  [".", "{math}"]
]
```

### String
```javascript
[
  [".", "in progress"]
]
```

### Array
```javascript
[
  [".", "in progress"]
]
```

### Format
##### JSON
```javascript
[
  [".", "in progress"]
]
```

##### CSV
```javascript
[
  [".", "in progress"]
]
```

##### YAML
```javascript
[
  [".", "in progress"]
]
```

##### INI
```javascript
[
  [".", "in progress"]
]
```

##### Image
```javascript
[
  [".", "in progress"]
]
```

##### Video
```javascript
[
  [".", "in progress"]
]
```

##### Sound
```javascript
[
  [".", "in progress"]
]
```

### Crypto
```javascript
[
  [".", "in progress"]
]
```

### File
##### File
```javascript
[
  [".", "in progress"]
]
```

##### Dir
```javascript
[
  [".", "in progress"]
]
```

##### Link
```javascript
[
  [".", "in progress"]
]
```

##### Volume
```javascript
[
  [".", "in progress"]
]
```

### URL
```javascript
[
  [".", "in progress"]
]
```

### Server
##### Web
```javascript
[
  [".", "in progress"]
]
```

##### API
```javascript
[
  [".", "in progress"]
]
```

##### Socket
```javascript
[
  [".", "in progress"]
]
```

##### Mail
```javascript
[
  [".", "in progress"]
]
```

##### Cloud
```javascript
[
  [".", "in progress"]
]
```

##### Game
```javascript
[
  [".", "in progress"]
]
```

### Cache
##### File
```javascript
[
  [".", "in progress"]
]
```

##### Memory
```javascript
[
  [".", "in progress"]
]
```

### CLI
```javascript
[
  [".", "in progress"]
]
```

### UI
```javascript
[
  [".", "in progress"]
]
```

### DB
##### JSON
```javascript
[
  [".", "in progress"]
]
```

##### MySQL
```javascript
[
  [".", "in progress"]
]
```

### Device
```javascript
[
  [".", "in progress"]
]
```

### Social
##### YouTube
```javascript
[
  [".", "in progress"]
]
```

##### TikTok
```javascript
[
  [".", "in progress"]
]
```

##### Twitter
```javascript
[
  [".", "in progress"]
]
```

##### Facebook
```javascript
[
  [".", "in progress"]
]
```

##### Instagram
```javascript
[
  [".", "in progress"]
]
```

##### Weibo
```javascript
[
  [".", "in progress"]
]
```

##### Telegram
```javascript
[
  [".", "in progress"]
]
```

##### WhatsApp
```javascript
[
  [".", "in progress"]
]
```

##### WeChat
```javascript
[
  [".", "in progress"]
]
```

### Trade
##### Yahoo! Finance
```javascript
[
  [".", "in progress"]
]
```

##### Interactive Brokers
```javascript
[
  [".", "in progress"]
]
```

##### Binance
```javascript
[
  [".", "in progress"]
]
```

### Game
##### Visual Novel
```javascript
[
  [".", "in progress"]
]
```

##### RPG
```javascript
[
  [".", "in progress"]
]
```

##### Platformer
```javascript
[
  [".", "in progress"]
]
```

##### Shooter
```javascript
[
  [".", "in progress"]
]
```

##### 3D
```javascript
[
  [".", "in progress"]
]
```

##### 2D
```javascript
[
  [".", "in progress"]
]
```

##### 2.5D
```javascript
[
  [".", "in progress"]
]
```

### AI
```javascript
[
  [".", "in progress"]
]
```
