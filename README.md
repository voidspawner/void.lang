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
The language was created for my own needs, so as not to write the same code repeatedly. Several versions for PHP and Python languages were created. Now I bring the code to the form that can be published. There are plans to integrate **Social Networks and Trading Platforms API, convert Videos, Images and Music, create Games and work with AI**.

I make changes every day. Later, a social network will be launched, the entire work process will be transferred there.

| Progress | Description | Version |
| --- | --- | --- |
| <p align="center">✅</p> | void.lang.python | <p align="center">Beta |
| <p align="center">✅</p> | void.lang.php | <p align="center">Beta</p> |
| <p align="center">▶️</p> | Language description on GitHub | <p align="center">1</p> |
| <p align="center">▶️</p> | void.web | <p align="center">1</p> |
| <p align="center">▶️</p> | void.lang.python | <p align="center">1</p> |
| <p align="center">⏳</p> | void.lang.php | <p align="center">1</p> |
| <p align="center">⏳</p> | void.lang.js | <p align="center">1</p> |
| <p align="center">⏳</p> | void.lang.swift | <p align="center">1</p> |
| <p align="center">⏳</p> | void.lang.java | <p align="center">1</p> |
| <p align="center">⏳</p> | void.lang.cs | <p align="center">1</p> |

## Actions

| [Value](#value) | [Control](#control) | [Math](#math) | [String](#string) | [Array](#array) |
| --- | --- | --- | --- | --- |
| [Format](#format) | [Crypto](#crypto) | [File](#file) | [URL](#url) | [Server](#server) |
| [Cache](#cache) | [CLI](#cli) | [UI](#ui) | [DB](#db) | [Device](#device) |
| [Social](#social) | [Trade](#trade) | [Game](#game) | [AI](#ai) | |

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
  ["=", "value", 1, "+", 1, "*", 2],
  ["[=", "name.arr", [1, 2, 3]],
  ["=", "rnd", ["random", 1, 100]],
  ["=", "name.dict", {"rnd": "{rnd}"}],
  ["=", "name.escaped", {"rnd": "{rnd}"}, true],
  ["[=", "{name.text}.escaped.arr", ["{rnd}"], true],
  [".", "{i}"],
  [".", "{name.subname}"],
  [".", "{name}"],
  [".", "{value}"],
  [".", "{name.arr}"],
  [".", "{rnd}"],
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

##### For / Repeat / While
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

### Math

### String

### Array

### Format
##### JSON
##### CSV
##### YAML
##### INI
##### Image
##### Video
##### Sound

### Crypto

### File
##### File
##### Dir
##### Link
##### Volume

### URL

### Server
##### Web
##### API
##### Socket
##### Mail
##### Cloud
##### Game

### Cache
##### File
##### Memory

### CLI

### UI

### DB
##### JSON
##### MySQL

### Device

### Social
##### YouTube
##### TikTok
##### Twitter
##### Facebook
##### Instagram
##### Weibo
##### Telegram
##### WhatsApp
##### WeChat

### Trade
##### Yahoo! Finance
##### Interactive Brokers
##### Binance

### Game
##### Visual Novel
##### RPG
##### Platformer
##### Shooter
##### 3D
##### 2D
##### 2.5D

### AI
