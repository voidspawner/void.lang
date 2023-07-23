# V O I D spawner lang

## About
**⌜ V O I D spawner lang ⌟** is a language for rapidly creating applications in the **JSON format**. It is used as a replacement for both the standard Bash/CMD/etc. languages and for writing **UI Applications**, **Servers** and **Games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

<img src="https://i.imgur.com/kx2UcUh.jpg" width="100%">

## Preinstalled Language

- **Python** ⌜CLI App・Web Server・API Server・Game (with Godot)⌟
- **PHP** ⌜CLI App・Web Server・API Server・Game (with Godot)⌟
- **JS** ⌜Web App・Web Server (with NodeJS)・API Server (with NodeJS)・CLI App (with NodeJS)⌟
- **Swift** ⌜macOS App・iOS App・iPadOS App・watchOS App・tvOS App・Linux App・Windows App・Web Server・API Server・Game (with Godot)・Game (with UE5)・Game Native⌟
- **Java** ⌜Android App・Linux App・Windows App・Web Server・API Server・Game (with Godot)・Game (with UE5)・Game Native⌟
- **C#** ⌜Windows App・Web Server・API Server・Game (with Godot)・Game (with UE5)・Game Native⌟

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

   ##### Tip for *nix (add to ~/.bashrc | ~/.zshrc | ~/.bash_profile)
   ```console
   alias void="python3 /path/to/python/void.py"
   ```
   ```console
   void myfirstapp.json
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
| <p align="center">✅</p> | void.lang.github | void.lang description on GitHub | <p align="center">1</p> | <p align="center">Jul 2023</p> |
| <p align="center">▶️</p> | void.web | Social web application | <p align="center">1</p> | <p align="center">Sep 2023</p> |
| <p align="center">▶️</p> | void.lang.python | void.lang in Python language | <p align="center">1</p> | <p align="center">Aug 2023</p> |
| <p align="center">▶️</p> | void.lang.js | void.lang in JavaScript language | <p align="center">1</p> | <p align="center">Sep 2023</p> |
| <p align="center">▶️</p> | void.lang.swift | void.lang in Swift language | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">▶️</p> | void.lang.java | void.lang in Java language | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">▶️</p> | void.lang.php | void.lang in PHP language | <p align="center">1</p> | <p align="center">Sep 2023</p> |
| <p align="center">▶️</p> | void.lang.help | void.lang description HTML+JSON file | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">▶️</p> | void.app | Social mobile and desktop application | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">▶️</p> | void.game | Games constructor | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">▶️</p> | void.ai | Multipurpose AI | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">▶️</p> | void.voids | Digital currency | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.lang.wiki | void.lang description on Wikipedia | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">⏳</p> | void.lang.cs | void.lang in C# language | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.parts | Robot parts and components | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.blade | void.ai generated social media content | <p align="center">1</p> | <p align="center">2024</p> |
| <p align="center">⏳</p> | void.ai.movie | Movie / anime / animation constructor with void.ai | <p align="center">1</p> | <p align="center">2025</p> |
| <p align="center">⏳</p> | void.booster | Space rocket to deliver cargo<br>to orbit and other planets, operated by void.ai | <p align="center">1</p> | <p align="center">2040</p> |
| <p align="center">⏳</p> | void.spawner | ??? | <p align="center">1</p> | <p align="center">2100</p> |

## Actions

| <p align="center">[Value](#value)</p> | <p align="center">[Control](#control)</p> | <p align="center">[Action](#action)</p> | <p align="center">[Math](#math)</p> | <p align="center">[Text](#text)</p> | <p align="center">[Array](#array)</p> | <p align="center">[Time](#time)</p> |
| --- | --- | --- | --- | --- | --- | --- |
| <p align="center">[Format](#format)</p> | <p align="center">[Crypto](#crypto)</p> | <p align="center">[File](#file)</p> | <p align="center">[URL](#url)</p> | <p align="center">[Server](#server)</p> | <p align="center">[Cache](#cache)</p> | <p align="center">[CLI](#cli)</p> |
| <p align="center">[UI](#ui)</p> | <p align="center">[DB](#db)</p> | <p align="center">[Device](#device)</p> | <p align="center">[Social](#social)</p> | <p align="center">[Trade](#trade)</p> | <p align="center">[Game](#game)</p> | <p align="center">[AI](#ai)</p> |

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
  ["url", "google.com", [
    [".", "Response code: {code}"],
    [".", "{text}"]
  ]]
]
```
```
Action name: "url"
Action parameters: ["google.com", [
                     [".", "Response code: {code}"],
                     [".", "{text}"]
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
  [".", "{i}"]
]
```
```javascript
[
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
##### Types

The types are similar to JSON types. Minor changes only in the names. **Text** instead of **String**. And **Dictionary** instead of **Object**.

```javascript
[
  ["=", "text", "text\r\n\t\"\\\/\b\f\u30AB"],
  ["=", "number", 1],
  ["=", "number", -1.2],
  ["=", "number", 1e+10],
  ["=", "boolean", true],
  ["=", "boolean", false],
  ["=", "null", null],
  ["=", "array", [1, 2, 3]],
  ["=", "dictionary", {
    "name1": "value1",
    "name2": "value2"
  }],

  ["=", "number", ["num", "-1.234"]],
  ["=", "number", ["num", "100_000"]],
  ["=", "number", ["num", "100'000"]],
  ["=", "number", ["num", "100,000,000"]],
  ["=", "number", ["num", "123'456,34", ",", "'"]],
  ["=", "number", ["num", "1e10"]],
  ["=", "number", ["num", "1m"]],
  ["=", "number", ["num", "1kb"]],
  ["=", "number", ["num", "1G"]],
  ["=", "boolean", ["bool", null]],
  ["=", "boolean", ["bool", 1]],
  ["=", "boolean", ["bool", "yes"]],
  ["=", "text", ["text", "{number}"]],
  ["=", "text", "", "+", "{number}"],
  ["=", "array", ["{number}"]]
]
```
```javascript
[
  ["=", "type", ["type", "Text"]],
  [".", "{type}"]
]
```

##### Expression
```javascript
[
  ["=", "expression", {
    "+": [1, "+", 1],
    "-": [3, "-", 1],
    "*": [2, "*", 2],
    "/": [4, "/", 2],
    "%": [5, "%", 2],
    "~": ["2", "~", 8],
    "=": ["1", "=", 1],
    "!=": ["1", "!=", 2],
    ">=": ["2", ">=", 1],
    "<=": ["2", "<=", 3],
    ">": ["2", ">", 1],
    "<": ["2", "<", 3],
    "&&": [true, "&&", false],
    "||": [true, "||", false],
    "!.boolean": ["!", true],
    "!.number": ["!", 0],
    "&": [2, "&", 1],
    "|": [2, "|", 1],
    "^": [2, "^", 3],
    ">>": [2, ">>", 1],
    "<<": ["1", "<<", 1],
    "in.array": [2, "<>", [1, 2, 3]],
    "!in.array": [2, "><", [1, 2, 3]],
    "in.dict": [2, "<>", {1: 0, 2: 0, 3: 0}],
    "!in.dict": [2, "><", {1: 0, 2: 0, 3: 0}]
  }],
  [".", "{expression}"]
]
```

##### Set with Change 
```javascript
[
  ["=", "value", {
    "++": 1,
    "--": 2,
    "+=": 1,
    "-=": 1,
    "*=": 2,
    "/=": 4,
    "%=": 5,
    "~=": 2,
    "!=.boolean": true,
    "!=.number": 0,
    "&=": 2,
    "|=": 2,
    "^=": 3,
    ">>=": 2,
    "<<=": 1,
  }],
  ["++", "value.++"],
  ["--", "value.--"],
  ["+=", "value.+=", 1],
  ["-=", "value.-=", 1],
  ["*=", "value.*=", 2],
  ["/=", "value./=", 2],
  ["%=", "value.%=", 2],
  ["~=", "value.~=", 8],
  ["!=", "value.!=.boolean"],
  ["!=", "value.!=.number"],
  ["&=", "value.&=", 1],
  ["|=", "value.|=", 1],
  ["^=", "value.^=", 1],
  [">>=", "value.>>=", 1],
  ["<<=", "value.<<=", 1],
  [".", "{value}"]
]
```

##### Set with Check
```javascript
[
  ["=", "list", ["text", 12, true]]
  [":", [
    ["value1", "text"],
    ["value2", "number"],
    ["value3", "boolean"]
  ], "{list}"]
  [".", "{value1} {value2} {value3}"],

  ["?", [[":", [
    ["value1", "text"],
    ["value2", "number"],
    ["value3", "boolean"]
  ], "{list}", true]], [
    [".", "Values checked"]
  ]],

  ["=", "dict", {
    "value1": "text",
    "value2": 12,
    "value3": true
  }],
  ["?", [[":", [
    ["value1", "text"],
    ["value2", "number"],
    ["value3", "boolean"]
  ], "{dict}", true]], [
    [".", "Values checked"]
  ]]
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
    ["++", "i"]
  ]],

  ["=", "i", 0],
  ["...", ["fps", 10], [
    [".", "{i}"],
    ["++", "i"],
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
        ["code", "number", false, 500],
        ["message", "text"]
      ]],
      [".", "Override error | code : {code} | message : {message}"],
      ["X", "{code}"]
    ]
  }
}
```

##### Print / Println / Echo
```javascript
[
  ["=", "---", "text"],
  [".", "Print this {---} with newline"],
  [".", "Print this {---} without newline", true],
  [".", [1, 2, 3, true, null, "{---}"]],
  [".", {
    "name1": "value",
    "name2": "{---}"
  }]
]
```

##### Log / Notification
```javascript
{
  "notification": {
    "info": [
      {
        "path": "./app.log",
        "text": "{date} {time} : {message}",
        "size": "1m",
        "count": 5,
        "zip": true
      },
      {
        "path": "./log.json",
        "data": {
          "date": "{date}",
          "time": "{time}",
          "message": "{message}"
        },
        "count": 100000
      },
      {
        "db": "log",
        "table": "info",
        "user": "log",
        "password": "",
        "data": {
          "date": "{date}",
          "time": "{time}",
          "message": "{message}"
        },
        "count": 100000
      },
      {
        "mail": "log@site.com",
        "title": "Log",
        "text": "{date} {time} : {message}",
      }
    ],
    "me": [
      {
        "sms": "+123456789",
        "text": "{date} {time} : {message}",
      },
      {
        "telegram": "+123456789",
        "text": "{date} {time} : {message}",
      }
    ]
  },
  "run": [
    ["..", "app started"],
    ["..", "app started", "me"]
  ]
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

##### Code / Eval
```javascript
[
  ["code", "print('Print on Python')"]
]
```

### Action
##### Run
```javascript
[
  ["action", ".", "text"],
  ["action", ".", ["text"]],
  ["action", [
    [".", "text"],
    [".", "text"]
  ]],
  ["action", "=", "i", 1, "+", 1],
  ["action", "=", ["n", 1, "+", 1]],
  [".", "{i}"],
  [".", "{n}"]
]
```

##### Create
```javascript
{
  "run": [
    ["=", "sum1", ["sum", 1, 4]],
    ["=", "sum2", ["sum", 1, 4, 5, 6]],
    [".", "{sum1}"],
    [".", "{sum2}"]
  ],
  "action": {
    "sum": [
      [":", [
        ["number1", "number", true],
        ["number2", "number", true],
        ["other", ["number", "..."], false]
      ]],
      ["=", "result", "{number1}", "+", "{number2}"],
      ["...", ["number", "{other}"], [
        ["+=", "result", "{number}"]
      ]],
      ["->", "{result}"]
    ]
  }
}
```

##### List
```javascript
[
  [".", "List actions"],
  ["action.list"]

  ["=", "list", ["action.list", true]],
  [".", "{list}"]
]
```

##### Search
```javascript
[
  [".", "Search actions locally and remotely"],
  ["action.search", "pdf"],

  ["=", "search", ["action.search", "pdf", true]],
  [".", "{search}"]
]
```

##### Update / Install
```javascript
[
  [".", "Update actions"],
  ["action.get"],

  [".", "Update / install specified actions"],
  ["action.get", ["void.lang.action.math", "void.lang.action.format"]],

  [".", "Update / install specified actions without notification"],
  ["action.get", ["void.lang.action.math", "void.lang.action.format"], true]
]
```

##### Remove
```javascript
[
  [".", "Remove specified actions"],
  ["action.remove", ["void.lang.action.format.pdf", "void.lang.action.format.xls"]],

  [".", "Remove specified actions without notification"],
  ["action.remove", "void.lang.action.format.pdf", true]
]
```

##### Test
```javascript
[
  [".", "Run all tests"],
  ["action.test"],

  [".", "Run tests on specified actions"],
  ["action.test", "sin"],
  ["action.test", ["sin", "cos", "tan"]],
  ["action.test", "void.lang.action.math"],

  ["=", "test", ["action.test", "cos", true]],
  ["?", "{test}", [
    [".", "Test : ok"]
  ], [
    [".", "Test : failed"]
  ]]
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
    "log.ln": ["log", 3],
    "log.log10": ["log", 3, 10],
    "log.log2": ["log", 3, 2],
    "abs": ["abs", -10],
    "min": ["min", 1, 10, 2, 5, -2],
    "max": ["max", 1, 10, 2, 5, -2],
    "random.0-1": ["random"],
    "random.0-100": ["random", 100],
    "random.10-100": ["random", 10, 100],
    "average": ["average", 1, 5, 7, 3],
    "average.array": ["average", [1, 5, 7, 3]],
    "factorial": ["factorial", 10],
    "convert.dec->hex": ["convert", "dec", "hex", 10],
    "convert.dec->oct": ["convert", "dec", "oct", 10],
    "convert.dec->bin": ["convert", "dec", "bin", 10],
    "convert.hex->dec": ["convert", "hex", "dec", "A0"],
    "convert.grad->rad": ["convert", "grad", "rad", 180]
  }],
  [".", "{math}"]
]
```

### Text
```javascript
[
  ["=", "text", {
    "upper": ["upper", "text"],
    "lower": ["lower", "Text"],
    "date.date": ["date", null, "00.00.0000"],
    "date.time": ["date", null, "00:00"],
    "date.datetime from timestamp": ["date", 123456, "Y-m-d H:i:s"],
    "split": ["split", "a b c", " "],
    "join": ["join", [1, 2, 3], "/"],
    "trim.both": ["trim", " text "],
    "trim.start": ["trim.start", ". . . text ", ". "],
    "trim.end": ["trim.end", "text ", " "],
    "search": ["search", "text", "x"],
    "count.array": ["count", [1, 2, 3]],
    "count.letters": ["count", "text"],
    "pad.spaces": ["pad", "Text", 10],
    "pad.start": ["pad.start", "Text", 10, "."],
    "pad.center": ["pad.center", "Text", 10, "."],
    "convert.charset": ["convert", null, "utf16", "text"],
    "replace": ["replace", "text", "x", "*"],
    "regex.search": ["regex", "text", "/[x]/"],
    "regex.replace": ["regex", "text", "/[x]/", "*"],
    "escape.html": ["escape.html", "<div></div>"],
    "escape.json": ["escape.json", "text\n"],
    "escape.url": ["escape.url", "text="],
    "escape.sql": ["escape.sql", "text'"],
    "sarts": ["starts", "text", "t"],
    "ends": ["ends", "text", "t"],
    "search": ["search", "text", "e"],
    "part": ["text", 1, 2]
  }],
  [".", "{text}"]
]
```

### Array
```javascript
[
  ["=", "array", {
    "add": [[1, 2, 3], "+" 4],
    "add.to position": ["add", [1, 2, 3], 4, 2],
    "add.first": ["add", [1, 2, 3], 4, 0],
    "add.last": ["add", [1, 2, 3], 4, -1],
    "merge.array": [[1, 2, 3], "+", [4, 5, 6]],
    "merge.dict": [{"name1": "value1"}, "+", {"name2": "value2"}],
    "remove.index": ["-", [1, 2, 3], 1],
    "remove.first": ["-", [1, 2, 3], 0],
    "remove.last": ["-", [1, 2, 3], -1],
    "remove.and extract": ["-", [1, 2, 3], -1, true],
    "shuffle": ["shuffle", [1, 2, 3]],
    "reverse": ["reverse", [1, 2, 3]],
    "part": ["part", [1, 2, 3, 4, 5], 1, 2],
    "unique": ["unique", [1, 2, 2, 3, 1, 2, 5]],
    "search": ["search", [1, 2, 3], 2],
    "search.dict": ["search", {"name1": "value1", "name2": "value2"}, "value2"],
    "names": ["names", {"name1": "value1", "name2": "value2"}],
    "values": ["values", {"name1": "value1", "name2": "value2"}],
    "map.simple": ["map", [1, 2, 3], null, ["{value}", "+", 1]],
    "map.complex": ["map", [1, 2, 3], "val", [
      ["=", "{result}", "{val}", "+", 1],
      ["->", "{result}"]
    ]],
    "filter.simple": ["filter", [1, 2, 3], "i", ["{i}", ">", 2]],
    "filter.complex": ["filter", [1, 2, 3], null, [
      ["?", ["{value}", ">", 2], [
        ["->", "{value}"]
      ]]
    ]],
    "reduce.simple": ["reduce", [1, 2, 5, 7, 3], null, ["{first}", ">", "{second}"]],
    "reduce.complex": ["reduce", [1, 2, 5, 7, 3], ["a", "b"], [
      ["?", ["{a}", ">", "{b}"], [
        ["->", "{a}"]
      ], [
        ["->", "{b}"]
      ]]
    ]],
    "flat": ["flat", [1, 2, [3, 4, [5]]]]
  }],
  [".", "{array}"]
]
```

### Time
##### Wait
```javascript
[
  ["wait", 1000],
  [".", "After waiting 1 second"]
]
```

##### Timer
```javascript
[
  ["timer", 10000, [
    [".", "After waiting 10 seconds"]
  ]],

  ["timer", 1000, [
    [".", "Repeat every 1 second"]
  ], true],

  ["timer", ["8:00", "mon"], [
    [".", "Every Monday at 8:00"]
  ], true, "monday alarm"],

  [".", ["timer.list"]],

  ["timer.remove", "monday alarm"],
  ["timer.clear"]
]
```

##### Speed / Stopwatch
```javascript
[
  ["speed.start", "db load remotely"],
  ["wait", 1000],
  ["speed.check", "db load remotely"],
  ["wait", 2000],
  ["speed.check", "db load remotely", "wait more"],
  [".", "{speed.db load remotely.list}"],
  [".", "{speed.db load remotely.total}"],
  [".", "{speed.db load remotely.last}"],
  [".", "{speed.db load remotely.start}"],
  [".", "{speed.db load remotely.wait more}"],
  ["speed.stop", "db load remotely"]
]
```

### Format
##### JSON
```javascript
[
  ["=", "data", [1, 2, 3, null, {"name": "value"}]],

  ["=", "json", ["json.encode", "{data}", true]],
  ["=", "data", ["json.decode", "{json}"]],

  [".", "Write JSON pretty"],
  ["json.write", "./file.json", "{data}", true],

  ["=", "data", ["json.read", "./file.json"]],
  [".", "{data}"],

  [".", "Check data"],
  ["=", "result", ["json.check", "./file.json"]],
  ["?", ["{result}", "!=", true], [
    [".", "{result}"]
  ], [
    [".", "ok"]
  ]]
]
```
```javascript
{
  "json": {
    "pretty": true
  },
  "run": [
    [".", "Write JSON pretty by default"],
    ["json.write", "./file.json", [1,2,3,null,{"name": "value"}]]
  ]
}
```

##### CSV
```javascript
[
  ["=", "data", [
    [1, 2, "text1"],
    [3, 4, "text2"]
  ]],

  ["=", "csv", ["csv.encode", "{data}", null, ";"]],
  ["=", "data", ["csv.decode", "{csv}", null, ";"]],

  [".", "Write with header. Separator ';'"],
  ["csv.write", "./file.csv", "{data}", ["header1", "header2", "header3"], ";"],

  ["=", "data", [
    {
      "header1": 1,
      "header2": 2,
      "header3": "Text1"
    },
    {
      "header1": 3,
      "header2": 4,
      "header3": "Text2"
    }
  ]],
  [".", "Ignore header"],
  ["csv.write", "./file.csv", "{data}", true],

  [".", "Write with header"],
  ["csv.write", "./file.csv", "{data}"],

  [".", "Read data and ignore header. Separator ','. Read data as array"],
  ["=", "data", ["csv.read", "./file.csv", true, ","]],
  [".", "{data}"],

  [".", "Read data as dictionary"],
  ["=", "data", ["csv.read", "./file.csv", null, null, true]],
  [".", "{data}"]
]
```
```javascript
{
  "csv": {
    "separator": ';'
  },
  "run": [
    [".", "Read data with separator ';' by default"],
    ["=", "data", ["csv.read", "./file.csv"]],
    [".", "{data}"]
  ]
}
```

##### YAML
YAML is more advanced format than JSON. Has a simplified syntax and more elegant, but has more rules.
```javascript
[
  ["=", "data", {
    "name1": "value1",
    "name2": "value2",
    "name3": [1,2,3],
    "name4": {
      "name5": true,
      "name6": null
    }
  }],

  ["=", "yaml", ["yaml.encode", "{data}"]],
  ["=", "data", ["yaml.decode", "{yaml}"]],

  [".", "Write pretty by default"],
  ["yaml.write", "./file.yaml", "{data}"],

  [".", "Write compact"],
  ["yaml.write", "./file.yaml", "{data}", false],

  ["=", "data", ["yaml.read", "./file.yaml"]],
  [".", "{data}"]
]
```
```javascript
{
  "yaml": {
    "pretty": false
  },
  "run": [
    [".", "Write compact by default"],
    ["yaml.write", "./file.yaml", [1, 2, 3, {"name": "value"}]]
  ]
}
```

##### INI
```javascript
[
  ["=", "data", {
    "section1": {
      "name1": "value1",
      "name2": "value2"
    },
    "section2": {
      "name3": [1,2,3]
    }
  }],

  [".", "Encode ini with array separator ','"],
  ["=", "ini", ["ini.encode", "{data}", ","]],
  ["=", "data", ["ini.decode", "{ini}", ","]],
  
  ["ini.write", "./file.ini", "{data}", ","],
  ["=", "data", ["ini.read", "./file.ini", ","]],
  [".", "{data}"]
]
```

##### HTML
```javascript
[
  ["=", "html", ["html.encode", [
    ["doctype", "html"],
    ["html", {"lang": "en"}],
    ["head", [
      ["meta", {"charset": "utf-8"}],
      ["meta", {"name": "viewport", "content": {"width": "device-width", "initial-scale": 1}}],
      ["meta", {"name": "description", "content": "description text"}],
      ["meta", {"name": "keywords", "content"=["keyword1", "keyword2", "keyword3"]}],
      ["meta", {"name": "author", "content": "author name"}],
      ["comment", "comment text"],
      ["link", {"href": "../css/style.css", "rel": "stylesheet"}],
      ["icon", "/favicons/favicon_bash.png"],
      ["script", "../js/script.js"]
    ]],
    ["body", [
      ["div", {"class": "content"}, [
        "..."
      ]]
    ]]
  ]]],
  ["=", "html", ["html.decode", "{html}"]],
  [".", "{html}"],

  ["html.write", "./file.html", "{html}],
  ["=", "html", ["html.read", "./file.html"]],
  [".", "{html}"]
]
```

##### Image
```javascript
[
  [".", "in progress : will be available in late 2023"],

  ["convert", "./image.jpg", "./image.png"],
  ["convert", "./image.png", "./image.jpg", {
    "quality": 0.9,
    "progressive": true
  }],

  ["image", [
    ["load", "./image.png"],
    ["resize", {"width": 1080}],
    ["rectangle", {"x": 10, "y": 10, "width": 200, "height": 40, "color": "c2f542"}],
    ["text", "Text on image", {
      "size": 20,
      "font": "Arial",
      "bold": true,
      "color": "white"
    }],
    ["save", "./image.jpg", {"quality": 0.9}]
  ]]
]
```

##### Video
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Sound
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

### Crypto
```javascript
[
  ["=", "crypto", {
    "hash": ["hash", 10],
    "hash.numbers": ["hash", 10, ["number"]],
    "hash.letters": ["hash", 10, ["letter"]],
    "hash.number+symbols": ["hash", 10, ["number", "*.-", "#", "%"]],
    "uuid": ["uuid"],
    "md5": ["md5", "text"],
    "sha1": ["sha1", "text"],
    "sha256": ["sha256", "text"],
    "sha512": ["sha512", "text"],
    "crc32": ["crc32", "text"],
    "base64.encode": ["base64.encode", "text"],
    "gzip.encode": ["gzip.encode", "text"],
    "ssl.encode": ["ssl.encode", "text", "aes-128-ctr", "passphrase"],
    "bcrypt.encode": ["bcrypt.encode", "text", 10]
  }],
  ["+=", "crypto", {
    "base64.decode": ["base64.encode", "{crypto.base64.encode}"],
    "gzip.decode": ["gzip.decode", "{crypto.gzip.encode}"],
    "ssl.decode": ["ssl.decode", "{crypto.ssl.encode.text}","{crypto.ssl.encode.cypher}", "passphrase", "{crypto.ssl.encode.vector}"],
    "bcrypt.check": ["bcrypt.check", "text", "{bcrypt.encode}"]
  }],

  ["=", "crypto.rsa.key", ["rsa.key", 512]],
  ["=", "rsa", ["rsa.encode", "text", "{crypto.rsa.key.public}"]],
  ["=", "crypto.rsa", ["rsa.decode", "{rsa}", "{crypto.rsa.key.private}"]],
    
  [".", "{crypto}"]
]
```

### File
##### File
```javascript
[
  ["file.write", "./file.txt", "Text"],
  ["file.write", "./file.txt", "Text", {
    "append": true,
    "lock": true,
    "owner": "user",
    "chmod": 777,
    "date": {
      "create": "2100/01/01",
      "update": "2100/01/01"
    },
    "encode": "utf8"
  }],
  ["file.write", "./file.json", ["write array as JSON", 1, 2, 3]],
  ["file.write", "./file.json.gz", ["write array as JSON and gzip", 1, 2, 3]],
  ["file.write", "./file.csv", [["Write as CSV", 1, 2, 3], ["Text", 3, 4, 5]]],

  ["=", "text", ["file.read", "file.txt"]],
  ["=", "text", ["file.read", "file.txt"], {
    "lock": true,
    "encode", "utf8"
  }],
  ["=", "json", ["file.read", "file.json", {
    "format": "json"
  }]],
  ["=", "json", ["file.read", "file.json.gz", {
    "format": "auto"
  }],

  ["=", "info", ["file.info", "file.txt"]],
  [".", "Size: {info.size} | Chmod: {info.chmod} | Owner: {info.owner} | Created: {info.created.date}"],
  [".", "{info}"],
  ["file.info", "file.txt", {
    "chmod": 777,
    "date": {
      "create": "2100/01/01"
    }
  }],

  ["?", [["file.exists", "file.txt"]], [
    [".", "file exists"]
  ], [
    [".", "file not exists"]
  ]],

  ["file.copy", "file.txt", "newfile.txt"],
  ["file.duplicate", "file.txt"],
  ["file.duplicate", "file.txt", "file3.txt"],
  ["file.move", "file2.txt", "new/dir"],
  ["file.move", "file3.txt", "new/dir", {
    "name": "file2.txt",
    "overwrite": true
  }],

  ["file.remove", "file.txt"]
]
```

##### Dir
```javascript
[
  ["dir.create", "new/dir/path"],
  ["?", [["dir.exists", "new/dir"]], [
    [".", "Dir exists"]
  ], [
    [".", "Dir not exists"]
  ]],

  ["=", ["dir.info", "new"]],
  ["dir.info", "new", {
    "owner": "user",
    "chmod": 777,
    "recursive": true
  }],

  ["file.write", "new/dir/file.txt", "text"],
  ["=", "size", ["dir.size", "new"]],
  [".", "Size recursive: {size}"],

  ["=", "size", ["dir.size", "new", false]],
  [".", "Size one dir only: {size}"],

  ["=", "path", ["dir.path"]],
  [".", "Current dir: {path}"],

  ["=", "list", ["dir.list", "new"]],
  [".", "{list}"],
  ["=", "list", ["dir.list", "new", {
    "recursive": true,
    "size": true,
    "chmod": true,
    "owner": true,
    "file": true,
    "dir": true,
    "link": true
  }]],
  [".", "{list}"],

  ["dir.copy", "new/dir", "new", {
    "name": "dir2",
    "overwrite": true
  }],
  ["dir.duplicate", "new/dir"],
  ["dir.duplicate", "new/dir", "dir4"],
  ["dir.move", "new/dir4", "new/dir", {
    "overwrite": true
  }],

  ["dir.rename", "new/dir", "dir5"],

  ["dir.change", "new"],
  ["=", "path", ["dir.path"]],
  [".", "Changed dir: {path}"],
  ["dir.change", ".."],

  ["dir.remove", "new"]
]
```

##### Link
```javascript
[
  ["file.create", "file.txt", "text"],
  ["dir.create", "./dir"],

  ["link.create", "./file.txt", "./file2.txt"],
  ["link.create", "./dir", "./dir2"],

  ["=", "info", ["link.info", "file2.txt"],
  [".", "{info}"],

  ["=", "info", ["link.info", "dir2"],
  [".", "{info}"],

  ["link.info", "file2.txt", {
    "owner": "user",
    "chmod": 777
  }],

  ["?", [["link.exists", "file2.txt"]], [
    [".", "link exists"]
  ], [
    [".", "link not exists"]
  ]],

  ["link.copy", "file2.txt", "./file3.txt"],
  ["link.duplicate", "file2.txt"],
  ["link.duplicate", "file2.txt", "file4.txt"],

  ["link.rename", "./file2.txt", "file22.txt"],
  ["link.move", "file22.txt", "./file2.txt"],

  ["link.remove", "file2.txt"],
  ["link.remove", "dir2"]
]
```

##### Volume
```javascript
[
  ["=", "current", ["volume.current"]],
  [".", "{current}"],
  ["volume.change", "/Volumes/ssd"],

  ["=", "info", ["volume.info"]],
  ["=", "info", ["volume.info", "/Volumes/flash"]],
  [".", "Path: {info.path} | Name: {info.name} | Size: {info.size} | Free: {info.free} | Used: {info.used}"],

  ["=", "size", ["volume.size"]],
  [".", "Size: {size}"],
  ["=", "free", ["volume.free", "/Volumes/ssd"]],
  [".", "Free: {free}"],

  ["=", "list", ["volume.list"]],
  [".", "{list}"],

  ["volume.rename", "/Volumes/flash", "/Volumes/backup"],
  ["volume.eject", "/Volumes/ssd"]
]
```

##### Zip
```javascript
[
  ["zip.create", "file.zip", "./dir", {
    "compress": 0.5
  }],
  ["zip.add", "file.zip", "file.txt"],
  ["zip.remove", "file.zip", "file.txt"],
  ["=", "list", ["zip.list", "file.zip"]],
  [".", "{list}"],
  ["=", "info", ["zip.info", "file.zip"]],
  [".", "{info}"],
  ["zip.extract", "file.zip", "./dir2"],

  ["gzip.create", "file.gz", "file.txt"],
  ["gzip.extract", "file.gz", "./dir3"],
  ["=", "info", ["gzip.info", "file.gz"]],
  [".", "{info}"],

  ["tar.create", "file.tar", "./dir"],
  ["tar.create", "file.tar.gz", "./dir"],
  ["tar.add", "file.tar", "file.txt"],
  ["tar.remove", "file.tar", "file.txt"],
  ["=", "list", ["tar.list", "file.tar"]],
  [".", "{list}"],
  ["=", "info", ["tar.info", "file.tar"]],
  [".", "{info}"],

  ["=", "list", ["rar.list", "file.rar"]],
  [".", "{list}"],
  ["=", "info", ["rar.info", "file.rar"]],
  [".", "{info}"],
  ["rar.extract", "./file.rar", "./dir4"]
]
```

### URL
```javascript
[
  ["=", "text", ["url", "http://google.com"]],
  [".", "{text}"],

  ["url", "google.com", [
    [".", "Response code: {code}"],
    [".", "{text}"]
  ]],

  ["url", "google.com", [
    [".", "Response code: {code}"],
    [".", "{text}"]
  ], [
    [".", "Error | Code: {code}"],
    [".", "{response.code}"],
    [".", "{response.text}"],
    [".", "{response.header}"]
  ]],

  ["url", "site.com", {
    "post": {
      "name1": "value1",
      "name2": "value2"
    },
    "header": {
      "name1": "value1",
      "name2": "value2"
    },
    "cookie": {
      "name1": {
        "text": "value1",
        "domain": "/",
        "expire": "10d"
      },
      "name2": "value2"
    }
  }, [
    [".", "{response.text}"]
  ]],

  ["url", "site.com", {
    "scheme": "https",
    "path": ["user", "article"],
    "get": {
      "id": 1234
    },
    "method": "delete"
  }, [
    [".", "Article [https://site.com/user/article?id=1234] deleted"]
  ]]
]
```

### Server
##### Web
```javascript
[
  ["server.web", {
    "route": [
      ["/", "home"]
    ]
  }]
```
```javascript
[
  ["server.web", {
    "route": [
      ["/", [
        ["=", "response.text", "<h1>Text</h1>"],
        ["=", "response.code", 200],
        ["response.redirect", "/article/permanent.redirect", true],
        ["response.content", "<h1>text"</h1>],
        ["response.code", 200],
        ["response.header", "name1", "value1"],
        ["response.header", {
          "name1": "value1",
          "name2": "value2"
        }],
        ["response.cookie", "name", "value", "1d", "/"],
        ["response.cookie", {
          "name1": {
            "value": "value1",
            "expire": "1d",
            "domain": "/"
          },
          "name2": "value2"
        }]
      ]]
    ]
  }]
]
```
```javascript
{
  "web": {
    "host": "domain.com",
    "port": 443,
    "https": true,
    "ssl": {
      "certificate": "...",
      "protocol": "tls"
    },
    "route": [
      ["/", "home"],
      ["/article", "delete", "article.delete"],
      ["/article", "post", "article.send"]
    ]
  }
}
```
##### API
```javascript
[
  ["server.api", {
    "host": "api.domain.com",
    "port": 8080,
    "format": "json",
    "pretty": false,
    "route": [
      ["/", "api.list"],
      ["/article", "api.article.list"],
      ["/article", {
        "path": [
          ["id", "int", true]
        ]
      }, "api.article.get"],
      ["/article/send", "post", "api.article.send"],
      ["/article/delete", "api.article.delete"]
    ]
  }]
]
```
```javascript
{
  "api": {
    "host": "api.domain.com",
    "port": 8080,
    "route": [
      ["/", "api.list"],
      ["/article", "api.article.list"]
    ]
  }
}
```

##### Socket
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Mail
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Cloud
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Game
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

### Cache
```javascript
{
  "cache": {
    "file": "./cache",
    "memory": "memory"
  },
  "run": [
    ["=", "cache", ["cache.get", "file", "name", "default"]],
    [".", "{cache}"],

    ["cache.set", "file", "name", "value"],

    ["=", "list", ["cache.list", "file"]],
    [".", "{list}"],

    ["=", "info", ["cache.info", "file", "name"]],
    [".", "{info}"],

    ["cache.remove", "file", "name"],
    ["cache.clear"],

    ["cache.set", "memory", "name", "value"],
    ["cache.remove", "memory", "name"],

    ["=", "cache.file.data.name", "value"],
    ["-", "cache.file.data.name"],

    ["=", "cache.memory.data.name", "value"],
    [".", "{cache.memory.data.name}"],
    ["-", "cache.memory.data.name"]
  ]
}
```

### CLI
```javascript
[
  ["cli", {
    "title": "App Title",
    "help": true,
    "command": [
      ["get", "app.get", "Get data"],
      ["set", "app.set", "Set data with params", [
        ["text", "Text description, required", "text", true],
        ["count", "Count, default: 1", "number", false, 1]
      ]]
    ]
  }]
]
```
```javascript
{
  "cli": {
    "title": "App Title",
    "command": [
      [null, "app.home", "Without command"],
      ["get", "app.get", "Get data"]
    ]
  }
}
```

### UI
```javascript
[
  ["ui", [
    ["title", "App Title"],
    ["text", "Text", {
      "size": 20,
      "font": "Arial",
      "bold": 300,
      "color": "green"
    }],
    ["button", "Press", {
      "size": 10,
      "background": "blue",
      "color": "white"
    }, [
    ]]
  ]]
]
```

### DB
##### JSON
```javascript
{
  "db": {
    "json1": {
      "path": "./db.json"
    }
  },
  "run": [
    ["json.db.set", "json1", "data", [1, 2, 3]],
    ["=", "value", ["json.db.get", "data.1"]],
    [".", "{value}"],
  
    ["json.db.remove", "data"],
  
    ["=", "db.json1.data.name", {
      "name1": [1, 2, 3],
      "name2": "value2",
      "name3": "value3",
      "name4": 1,
      "name5": [
        {"a": 1, "b": 1},
        {"a": 1, "b": 2},
        {"a": 2, "b": 1},
        {"a": 2, "b": 2},
        {"a": 3, "b": 3}
      ]
    }],
    ["=", "value", "{db.json1.data.name.name4}"],
    [".", "{value}"],

    ["-", "db.json1.data.name.name3"]
  ]
}
```

##### MySQL
```javascript
{
  "db": {
    "sql1": {
      "server": "local",
      "user": "guest",
      "password": null
    }
  },
  "run": [
    ["sql.open", "sql1"],
    ["sql.open", "sql1", {
      "server": "server.com",
      "port": 3306,
      "user": "backup",
      "password": "HMB2vm2xjd",
      "database": "db1"
    }],
    ["sql.query", "sql1", "SELECT * FROM table1"],
    ["sql.list", "sql1", "table1"],
    ["sql.db.open", "sql1", "db2"],
  
    ["=", "row", ["sql.fetch.one", "sql1", "table1"]],
    [".", "{row}"],
  
    ["=", "list", ["sql.fetch.all", "sql1", "table1", ["[name]", "=", "value"], 10, 100]],
    [".", "{list}"],
  
    ["sql.close", "database"]
  ]
]
```

### Device
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

### Social
##### YouTube
```javascript
[
  [".", "in progress : will be available in late 2023"],

  ["youtube.download", "https://www.youtube.com/watch?v=y6120QOlsfU", "./", 720],
  ["youtube.download", "https://www.youtube.com/watch?v=y6120QOlsfU", "./", 1080],
  ["youtube.download", "https://www.youtube.com/watch?v=y6120QOlsfU", "./", "hd"],

  ["=", "info", ["youtube.info", "y6120QOlsfU"]],
  [".", "video info : {info}"],

  ["=", "info", ["youtube.info", "https://www.youtube.com/channel/UCvxu4st8jt0Li69hAh_nqQg"]],
  ["=", "info", ["youtube.info", "darude"]],
  [".", "channel info : {info}],

  ["=", "videos", ["youtube.videos", "darude"]],
  ["=", "videos", ["youtube.videos", "https://www.youtube.com/channel/UCvxu4st8jt0Li69hAh_nqQg"],
  ["=", "videos", ["youtube.videos", "https://www.youtube.com/playlist?list=PLD8GFRgnUxHbI-ZbQIJCS2Q1kJ86I0caG"]],

  ["=", "shorts", ["youtube.shorts", "darude"]],
  ["=", "streams", ["youtube.streams", "darude"]],
  ["=", "playslists", ["youtube.playslists", "darude"]],
  ["=", "releases", ["youtube.playslists", "darude"]],
  ["=", "channels", ["youtube.channels", "darude"]],
  ["=", "community", ["youtube.community", "darude"]],

  ["youtube.upload", "./movie.mp4", {
    "title": "Title",
    "description": "Description"    
  }],

  ["youtube.edit", "y6120QOlsfU", {
    "title": "New Title",
    "description": "New Description"
  }]
]
```

##### TikTok
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Twitter
```javascript
[
  [".", "in progress : will be available in late 2023"]

  ["twitter.send", "New tweet"],
  ["twitter.send", "New tweet", "https://twitter.com/ABCDEF/status/ABCDEF"],
  ["twitter.send", {
    "text": "tweet",
    "image": "./image.jpg"
  }],
  ["twitter.send", {
    "text": "tweet",
    "video": "./video.mp4",
    "location": "Kuala Lumpur"
  }],

  ["=", "tweets", ["twitter.tweets", "https://twitter.com/ABCDEF"]],
  [".", "{tweets}"],

  ["=", "search", ["twitter.search", "keywords"]],
  [".", "{search}"]
]
```

##### Facebook
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Instagram
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Weibo
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### Telegram
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### WhatsApp
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### WeChat
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

### Trade
##### Yahoo! Finance
```javascript
[
  [".", "in progress : will be available in late 2023"],

  [".", "Gathering tickers by 3 lettters"],
  ["=", "tickers", ["yahoo.tickers", 3]],
  [".", "{tickers}"],

  ["=", "info", ["yahoo.info", "aapl"]],
  [".", "{info}"],

  ["=", "history", ["yahoo.history", "aapl", "1y", "1m"]],
  [".", "{history}"],

  ["=", "price", ["yahoo.price", "aapl"]],
  [".", "{price}"],

  ["=", "options", ["yahoo.options", "aapl"]],
  [".", "{options}"],

  ["=", "history", ["yahoo.history", "AAPL230721C00192500", "1y", "1m"]],
  [".", "{history}"]
]
```

##### Interactive Brokers
```javascript
[
  [".", "in progress : will be available in late 2023"],

  ["=", "tickers", ["ib.tickers"]],
  [".", "{tickers}"],

  ["=", "info", ["ib.info", "aapl"]],
  [".", "{info}"],

  ["=", "price", ["ib.price", "aapl"]],
  [".", "{price}"],

  ["=", "history", ["ib.history", "aapl", "1y", "1m"]],
  [".", "{history}"],

  ["=", "price", ["ib.price", "aapl"]],
  [".", "{price}"],

  ["=", "options", ["ib.options", "aapl"]],
  [".", "{options}"],

  ["ib.buy", "aapl", 1],
  ["ib.buy", "AAPL230721C00192500", 1],
  ["ib.sell", "aapl", 1],
  ["ib.sell", "AAPL230721C00192500", 1],

  ["=", "portfolio", ["ib.portfolio"]],
  [".", "{portfolio}"]
]
```

##### Binance
```javascript
[
  [".", "in progress : will be available in late 2023"],

  ["=", "coins", ["binance.coins", 3]],
  [".", "{coins}"],

  ["=", "pairs", ["binance.pairs", "eth"]],
  [".", "{pairs}"],
  
  ["=", "info", ["binance.info", "eth"]],
  [".", "{info}"],

  ["=", "history", ["binance.history", "eth", "usdt", "1y", "1m"]],
  [".", "{history}"],

  ["=", "price", ["binance.price", "eth", "usdt"]],
  [".", "{price}"],

  [".", "Buy ETH with USDT"],
  ["binance.buy", "eth", "usdt", 1],

  ["=", "wallet", ["binance.wallet"]],
  [".", "wallet"]
]
```

### Game
##### Visual Novel
```javascript
[
  [".", "in progress : will be available in late 2023"]
]
```

##### RPG
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

##### Platformer
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

##### Shooter
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

##### 3D
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

##### 2D
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

##### 2.5D
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

### AI
##### Data
```javascript
[
   [".", "in progress : will be available in 2024"]
]
```

##### Voice
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

##### Image
```javascript
[
  [".", "in progress : will be available in 2024"]
]
```

##### Video
```javascript
[
  [".", "in progress : will be available in 2025"]
]
```

##### Sound
```javascript
[
  [".", "in progress : will be available in 2025"]
]
```

##### Music
```javascript
[
  [".", "in progress : will be available in 2025"]
]
```

##### Movie
```javascript
[
  [".", "in progress : will be available in 2025"]
]
```

##### Anime
```javascript
[
  [".", "in progress : will be available in 2025"]
]
```

##### Animation
```javascript
[
  [".", "in progress : will be available in 2025"]
]
```
##### Landscape / Object / Furniture / Human / Animal / Plant
```javascript
[
  [".", "in progress : will be available in 2025"]
]
```

## AI
To use **void.ai**, you will need to pay for a **subscription** (limited number of uses per day) or **pay** with voids digital currency.

But the fact is that the currency is also a **spawner**. Every month the profit is distributed among the **voids** holders. The number of voids increases proportionally and can be withdrawn to other digital currencies.

Will be available in 2024.
