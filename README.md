# V O I D spawner lang

## About
**⌜ V O I D spawner lang ⌟** is a language for rapidly creating applications in the **JSON format**. It is used as a replacement for both the standard Bash/CMD/etc. languages and for writing **UI Applications**, **Servers** and **Games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one JSON file**. Since the **code is presented as data**, applications can be easily automatically generated, updated, installed and launched remotely.

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
| <p align="center">⏳</p> | void.lang.wiki | void.lang description on Wikipedia | <p align="center">1</p> | <p align="center">Late 2023</p> |
| <p align="center">⏳</p> | void.lang.help | void.lang description HTML+JSON file | <p align="center">1</p> | <p align="center">Late 2023</p> |
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
| <p align="center">⏳</p> | void.ai.movie | Movie / anime / animation constructor with void.ai | <p align="center">1</p> | <p align="center">2025</p> |

## Actions

| <p align="center">[Value](#value)</p> | <p align="center">[Control](#control)</p> | <p align="center">[Action](#action)</p> | <p align="center">[Math](#math)</p> | <p align="center">[String](#string)</p> | <p align="center">[Array](#array)</p> | <p align="center">[Time](#time)</p> |
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

##### Zip
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
##### Data
```javascript
[
  [".", "in progress"]
]
```

##### Voice
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

##### Music
```javascript
[
  [".", "in progress"]
]
```

##### Movie
```javascript
[
  [".", "in progress"]
]
```

##### Anime
```javascript
[
  [".", "in progress"]
]
```

##### Animation
```javascript
[
  [".", "in progress"]
]
```
##### Landscape / Object / Furniture / Human / Animal / Plant
```javascript
[
  [".", "in progress"]
]
```
