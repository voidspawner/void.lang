# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **[V O I D](#v-o-i-d-format)** or **[JSON](https://en.wikipedia.org/wiki/JSON)** format. It is used as a replacement for the standard ``Bash``・``CMD``・etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one ``V O I D`` or ``JSON`` file**. Since the **code is presented as data**, applications can be easily generated with **``AI``**, updated, installed and launched remotely.

> [!IMPORTANT]
> **The project is in the process of development.**

<img src="https://github.com/voidspawner/void.ideology/blob/main/asset/image/logo.jpg" width="100%">

> [**About**](#about)・
[**Preinstalled Language**](#preinstalled-language)・
[**Example**](#example)・
[**How to Use**](#how-to-use)・
[**How to Use Game Engine**](#how-to-use-game-engine)・
[**Actions**](#actions)・
[**V O I D format**](#v-o-i-d-format)・
[**V O I D db**](#v-o-i-d-db)・
[**V O I D ai**](#v-o-i-d-ai)・
[**V O I D license**](#v-o-i-d-license)・
[**V O I D os**](#v-o-i-d-os)・
[**V O I D tech**](#v-o-i-d-tech)・
[**V O I D ideology**](#v-o-i-d-ideology)・
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
  ["native", "for i in range(10):print(i)"]
]
```
##### Run Python code
```json
[
  ["python", "for i in range(10):print(i)"]
]
```
##### Import void.py
```python
# crypto.py
exec(open('void.py').read())
encrypted = void.encrypt('Hi World :D')
print(void.decrypt(encrypted.text, encrypted.key))
```

## How to Use

1. Download **V O I D lang**
2. Create your first vapp (V O I D app) in **run.json** or other JSON file
3. Launch vapp with **V O I D lang**
 
```console
python void.py vapp.json
```

> [!TIP]
> **Tip for Linux・macOS**: Add alias to ~/.bashrc ・ ~/.zshrc ・ ~/.bash_profile (macOS)
> ```console
> alias void="python /path/to/void.py"
> ```
> 
> **Tip for Windows**: use alias in command line
> ```console
> doskey void=python /path/to/void.py
> ```
> ```console
> void vapp.json
> ```
> 
> **Tip for Swift・Kotlin・C++**: embed the vapp in the source code and compile it into an executable
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
2. Create your first game in **run.json** file
3. Copy the **void.exe** file from the **V O I D spawner** game to the same directory as **run.json** file
4. Sell your game or share with friends

> [!NOTE]
> **Run with game engine**
> ```console
> void.exe game.json
> ```
>
> **The archive contains run.json and all game files**
> ```console
> void.exe game.zip
> ```
>
> **The execution directory contains run.json and all game files or contains run.zip file**
> ```console
> void.exe
> ```
>
> You can use the **Exporter** inside the **V O I D spawner** game to export your game to all platforms ⌜**Windows**・**macOS**・**Linux**・**Android**・**iOS**・**Web**・**Xbox**・**Switch**・**PlayStation**⌟

**Alternative**

1. Download **V O I D lang**
2. Import **void.gd**・**void.cpp** into the **Godot**・**Unreal Engine**
3. Create your first game in **run.json** file
4. Export the game in the engine itself to the available platforms
5. Sell your game or share with friends

## Actions

> [**value**](#value)・
[**expression**](#expression)・
[**control**](#control)・
[**text**](#text)・
[**list**](#list)・
[**math**](#math)・
[**time**](#time)・
[**crypto**](#crypto)・
[**format**](#format)・
[**file**](#file)・
[**cloud**](#cloud)・
[**bot**](#bot)・
[**request**](#request)・
[**cookie**](#cookie)・
[**sql**](#sql)・
[**os**](#os)・
[**device**](#device)・
[**gps**](#gps)・
[**sensor**](#sensor)・
[**photo**](#photo)・
[**contacts**](#contacts)・
[**calendar**](#calendar)・
[**flashlight**](#flashlight)・
[**health**](#health)・
[**microphone**](#microphone)・
[**notification**](#notification)・
[**key**](#key)・
[**keyboard**](#keyboard)・
[**mouse**](#mouse)・
[**gamepad**](#gamepad)・
[**clipboard**](#clipboard)・
[**say**](#say)・
[**convert**](#convert)・
[**image**](#image)・
[**video**](#video)・
[**model**](#model)・
[**sound**](#sound)・
[**music**](#music)・
[**volume**](#volume)・
[**screen**](#screen)・
[**ui**](#ui)・
[**window**](#window)・
[**dialog**](#dialog)・
[**effect**](#effect)・
[**game**](#game)・
[**vn**](#vn)・
[**2d**](#2d)・
[**3d**](#3d)・
[**ai**](#ai)・
[**social**](#social)・
[**tech**](#tech)

> Count of actions **``591``**

The code is presented as **action name** and **action parameters**.

> ```json
> [".", "Hi World :D"]
> ```
> 
> Action name **``"."``**
> 
> Action parameters **``["Hi World :D"]``**

> ```json
> ["=", "value", 1, "+", 1]
> ```
> 
> Action name **``"="``**
> 
> Action parameters **``["value", 1, "+", 1]``**

> ```json
> "."
> ```
> 
> Action name **``"."``**
> 
> Action parameters **``[]``**

####

> **``vapp``** code created as an action
> 
> **``safe``** can be used in a social network
> 
> **``local``** can be used in self-starting
> 
> **``ask``** ask permission before use

### value

#### get

```diff
! Get value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["get"]
```
#### set

```diff
! Set value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["set"]
```
#### remove

```diff
! Delete value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["remove"]
```
#### type

```diff
! Get value type
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["type"]
```
#### bool

```diff
! Convert value to boolean
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["bool"]
```
#### number

```diff
! Translate value to a number
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["number"]
```
#### text

```diff
! Translate value to text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["text"]
```
#### list

```diff
! Translate value into a list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["list"]
```
#### alias

```diff
! Assign an alias to an action
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["alias"]
```

### expression

#### +

```diff
! Add
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["+"]
```
#### -

```diff
! Subtract
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["-"]
```
#### *

```diff
! Multiply
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["*"]
```
#### /

```diff
! Divide
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["/"]
```
#### %

```diff
! Remainder of division
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["%"]
```
#### **

```diff
! Elevate
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["**"]
```
#### !

```diff
! NOT bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["!"]
```
#### &

```diff
! AND bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["&"]
```
#### |

```diff
! OR bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["|"]
```
#### ^

```diff
! XOR bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["^"]
```
#### >>

```diff
! Right shift
+ safe・python・js・swift・kotlin・godot・c++
```

```json
[">>"]
```
#### <<

```diff
! Left shift
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["<<"]
```
#### +=

```diff
! Add to value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["+="]
```
#### -=

```diff
! Subtract from value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["-="]
```
#### *=

```diff
! Multiply the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["*="]
```
#### /=

```diff
! Divide the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["/="]
```
#### %=

```diff
! Residue from dividing the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["%="]
```
#### **=

```diff
! Increment the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["**="]
```
#### !=

```diff
! NOT bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["!="]
```
#### &=

```diff
! AND bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["&="]
```
#### |=

```diff
! OR bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["|="]
```
#### ^=

```diff
! XOR bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["^="]
```
#### >>=

```diff
! Shift to the right of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
[">>="]
```
#### <<=

```diff
! Shift to the left of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["<<="]
```
#### not

```diff
! Negation (not)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["not"]
```
#### and

```diff
! Conjunction (and)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["and"]
```
#### or

```diff
! Disjunction (or)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["or"]
```
#### xor

```diff
! Exclusive disjunction (exclusive or)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["xor"]
```
#### in

```diff
! A value in an array or a name in a dictionary
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["in"]
```
#### not in

```diff
! Value not in array or name not in dictionary
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["not in"]
```
#### is

```diff
! Value type match
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["is"]
```
#### not is

```diff
! Value type mismatch
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["not is"]
```

### control

#### ?

```diff
! Check an expression for truth (IF)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["?"]
```
#### ??

```diff
! Multiple expression check (MATCH, SWITCH)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["??"]
```
#### o

```diff
! Loop (FOR, WHILE)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["o"]
```
#### x

```diff
! Exit loop (BREAK)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["x"]
```
#### >>>

```diff
! Continue loop (CONTINUE)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
[">>>"]
```
#### <<<

```diff
! Repeat loop iteration
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["<<<"]
```
#### _

```diff
! Return action value (RETURN)
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["_"]
```
#### .

```diff
! Print text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["."]
```
#### ..

```diff
! Print text without a new line
+ safe・python・js・swift・kotlin・godot・c++
```

```json
[".."]
```
#### ...

```diff
! Enter text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["..."]
```
#### action

```diff
! Execute action
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["action"]
```
#### action.open

```diff
! Execute an action from a file
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["action.open"]
```
#### X

```diff
! End vapp
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["X"]
```
#### xx

```diff
! Error
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["xx"]
```
#### open

```diff
! Execute system action
+ local・python・js・swift・kotlin・godot・c++
```

```json
["open"]
```
#### shell

```diff
! Execute a command line command
+ local・python・js・swift・kotlin・godot・c++
```

```json
["shell"]
```
#### shell.open

```diff
! Open a terminal and execute the command
+ local・python・js・swift・kotlin・godot・c++
```

```json
["shell.open"]
```
#### code

```diff
! Execute native code
+ local・python・js・swift・kotlin・godot・c++
```

```json
["code"]
```
#### python

```diff
! Execute Python code
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["python"]
```
#### compile

```diff
! Compile code for a specific platform
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["compile"]
```
#### i

```diff
! Info logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["i"]
```
#### w

```diff
! Warning logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["w"]
```
#### e

```diff
! Error logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["e"]
```
#### d

```diff
! Debug logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["d"]
```
#### t

```diff
! Time logging
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["t"]
```
#### export

```diff
! Export vapp for selected platforms
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["export"]
```
#### update

```diff
! Update script
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["update"]
```
#### test

```diff
! Test script
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["test"]
```
#### help

```diff
! Display language hint
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["help"]
```
#### debug

```diff
! Display debug information
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["debug"]
```
#### debug.fps

```diff
! Display FPS
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["debug.fps"]
```

### text

#### lower

```diff
! Convert text to lower case
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["lower"]
```
#### upper

```diff
! Convert text to uppercase
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["upper"]
```
#### starts

```diff
! Starts with text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["starts"]
```
#### ends

```diff
! Ends with text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ends"]
```
#### strip

```diff
! Trim text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["strip"]
```
#### strip.start

```diff
! Trim the beginning of text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["strip.start"]
```
#### strip.end

```diff
! Trim the end of text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["strip.end"]
```
#### replace

```diff
! Replace text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["replace"]
```
#### find

```diff
! Find position in text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["find"]
```
#### similar

```diff
! Compare texts
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["similar"]
```
#### part

```diff
! Get a part of text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["part"]
```
#### split

```diff
! Split text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["split"]
```
#### join

```diff
! Join text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["join"]
```
#### regex

```diff
! Find in text using regular expression
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["regex"]
```
#### regex.replace

```diff
! Replace text using a regular expression
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["regex.replace"]
```
#### escape

```diff
! Escape text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["escape"]
```
#### escape.html

```diff
! Escape HTML text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["escape.html"]
```
#### escape.sql

```diff
! Escape SQL text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["escape.sql"]
```
#### escape.url

```diff
! Escape text URL
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["escape.url"]
```
#### escape.json

```diff
! Escape text JSON
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["escape.json"]
```
#### escape.void

```diff
! Escape text V O I D
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["escape.void"]
```
#### unescape

```diff
! Unescape text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["unescape"]
```
#### unescape.html

```diff
! Unescape HTML text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["unescape.html"]
```
#### unescape.sql

```diff
! Unescape text SQL
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["unescape.sql"]
```
#### unescape.url

```diff
! Unescape text URL
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["unescape.url"]
```
#### unescape.json

```diff
! Unescape JSON text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["unescape.json"]
```
#### unescape.void

```diff
! Unescape V O I D text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["unescape.void"]
```
#### date

```diff
! Convert text to timestamp, or timestamp to text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["date"]
```
#### letters

```diff
! Number of letters in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["letters"]
```
#### words

```diff
! Number of words in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["words"]
```
#### sentences

```diff
! Number of sentences in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sentences"]
```
#### lines

```diff
! Number of lines in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["lines"]
```

### list

#### push

```diff
! Add to list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["push"]
```
#### pop

```diff
! Extract from the list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["pop"]
```
#### reverse

```diff
! Invert order in the list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["reverse"]
```
#### shuffle

```diff
! Shuffle the list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["shuffle"]
```
#### sort

```diff
! Sort the list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sort"]
```
#### fill

```diff
! Fill the list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["fill"]
```
#### map

```diff
! Map the list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["map"]
```
#### reduce

```diff
! Reduce the list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["reduce"]
```
#### names

```diff
! Dictionary or list names
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["names"]
```
#### values

```diff
! Dictionary values
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["values"]
```

### math

#### sin

```diff
! Sine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sin"]
```
#### cos

```diff
! Cosine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["cos"]
```
#### tan

```diff
! Tangent
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["tan"]
```
#### sinh

```diff
! Hyperbolic sine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sinh"]
```
#### cosh

```diff
! Hyperbolic cosine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["cosh"]
```
#### tanh

```diff
! Hyperbolic tangent
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["tanh"]
```
#### asin

```diff
! Arcsine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["asin"]
```
#### acos

```diff
! Arccosine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["acos"]
```
#### atan

```diff
! Arctangent
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["atan"]
```
#### asinh

```diff
! Hyperbolic arcsine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["asinh"]
```
#### acosh

```diff
! Hyperbolic arccosine
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["acosh"]
```
#### atanh

```diff
! Hyperbolic arctangent
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["atanh"]
```
#### round

```diff
! Round a number
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["round"]
```
#### floor

```diff
! Round a number down
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["floor"]
```
#### ceil

```diff
! Round a number up
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ceil"]
```
#### log

```diff
! Logarithm
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["log"]
```
#### log.e

```diff
! Hyperbolic logarithm
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["log.e"]
```
#### log.n

```diff
! Natural logarithm
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["log.n"]
```
#### fa

```diff
! Factorial
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["fa"]
```
#### fib

```diff
! Fibonacci
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["fib"]
```
#### abs

```diff
! Absolute value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["abs"]
```
#### min

```diff
! Minimum value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["min"]
```
#### max

```diff
! Maximum value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["max"]
```
#### avg

```diff
! Average value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["avg"]
```
#### sum

```diff
! Sum of values
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sum"]
```
#### hex

```diff
! Hexadecimal value to byte
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["hex"]
```
#### hex.dec

```diff
! Hexadecimal value to decimal
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["hex.dec"]
```
#### bin

```diff
! Binary value to byte
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["bin"]
```
#### bin.dec

```diff
! Binary value to decimal
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["bin.dec"]
```
#### dec

```diff
! Decimal value to byte
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["dec"]
```
#### dec.hex

```diff
! Decimal value to hexadecimal
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["dec.hex"]
```
#### dec.bin

```diff
! Decimal value to binary
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["dec.bin"]
```
#### rad

```diff
! Degree to radian
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["rad"]
```
#### deg

```diff
! Radian to degree
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["deg"]
```
#### random

```diff
! Random value
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["random"]
```
#### random.reseed

```diff
! Re-create random seed
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["random.reseed"]
```
#### random.seed

```diff
! Get random seed
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["random.seed"]
```

### time

#### time

```diff
! Time stamp in microseconds
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["time"]
```
#### time.ms

```diff
! Time stamp in milliseconds
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["time.ms"]
```
#### time.s

```diff
! Timestamp in seconds
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["time.s"]
```
#### timer

```diff
! Set timer
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["timer"]
```
#### timer.remove

```diff
! Remove timer
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["timer.remove"]
```
#### wait

```diff
! Wait time in seconds
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["wait"]
```

### crypto

#### encrypt

```diff
! Encode text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["encrypt"]
```
#### decrypt

```diff
! Decode text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["decrypt"]
```
#### hash

```diff
! Get a numeric hash of the text or a random hash
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["hash"]
```
#### uuid

```diff
! Random UUID
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["uuid"]
```
#### md5

```diff
! MD5 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["md5"]
```
#### sha1

```diff
! SHA1 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sha1"]
```
#### sha256

```diff
! SHA256 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sha256"]
```
#### sha512

```diff
! SHA512 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sha512"]
```
#### crc32

```diff
! CRC32 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["crc32"]
```
#### base64

```diff
! Base64 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["base64"]
```
#### base64.decode

```diff
! Decode Base64
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["base64.decode"]
```
#### gzip

```diff
! Gzip text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["gzip"]
```
#### gzip.decode

```diff
! Decode Gzip
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["gzip.decode"]
```
#### rsa

```diff
! Encode text with RSA
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["rsa"]
```
#### rsa.decode

```diff
! Decode RSA
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["rsa.decode"]
```
#### rsa.key.public

```diff
! Get RSA public key
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["rsa.key.public"]
```
#### rsa.key.private

```diff
! Get RSA private key
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["rsa.key.private"]
```
#### ssl

```diff
! Encode text with SSL
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ssl"]
```
#### ssl.decode

```diff
! Decode SSL
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ssl.decode"]
```
#### ssl.check

```diff
! Verify SSL
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ssl.check"]
```
#### bcrypt

```diff
! Encode text with Bcrypt
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["bcrypt"]
```
#### bcrypt.check

```diff
! Verify Bcrypt
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["bcrypt.check"]
```

### format

#### void

```diff
! Encode to V O I D
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["void"]
```
#### void.decode

```diff
! Decode V O I D
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["void.decode"]
```
#### void.read

```diff
! Read V O I D file
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["void.read"]
```
#### void.write

```diff
! Write V O I D file
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["void.write"]
```
#### json

```diff
! Encode to JSON
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["json"]
```
#### json.decode

```diff
! Decode JSON
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["json.decode"]
```
#### json.read

```diff
! Read JSON file
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["json.read"]
```
#### json.write

```diff
! Write JSON file
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["json.write"]
```
#### yaml

```diff
! Encode YAML
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["yaml"]
```
#### yaml.decode

```diff
! Decode YAML
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["yaml.decode"]
```
#### csv

```diff
! Encode CSV
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["csv"]
```
#### csv.decode

```diff
! Decode CSV
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["csv.decode"]
```
#### ini

```diff
! Encode INI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ini"]
```
#### ini.decode

```diff
! Decode INI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ini.decode"]
```
#### html

```diff
! Encode HTML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["html"]
```
#### html.decode

```diff
! Decode HTML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["html.decode"]
```
#### xml

```diff
! Encode XML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["xml"]
```
#### xml.decode

```diff
! Decode XML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["xml.decode"]
```
#### css

```diff
! Encode CSS
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["css"]
```
#### css.decode

```diff
! Decode CSS
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["css.decode"]
```

### file

#### file.exists

```diff
! File exists
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.exists"]
```
#### file.write

```diff
! Write to file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.write"]
```
#### file.read

```diff
! Read file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.read"]
```
#### file.read.list

```diff
! Read lines from file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.read.list"]
```
#### file.remove

```diff
! Remove file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.remove"]
```
#### file.move

```diff
! Move file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.move"]
```
#### file.copy

```diff
! Copy file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.copy"]
```
#### file.rename

```diff
! Rename file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.rename"]
```
#### file.info

```diff
! File information
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.info"]
```
#### file.size

```diff
! File size
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.size"]
```
#### file.permissions

```diff
! File permissions
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.permissions"]
```
#### file.readonly

```diff
! Read-only file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.readonly"]
```
#### file.hidden

```diff
! Hidden file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.hidden"]
```
#### file.modified

```diff
! File modification time
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.modified"]
```
#### file.sha256

```diff
! SHA256 file hash
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.sha256"]
```
#### file.crc32

```diff
! CRC32 file hash
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.crc32"]
```
#### file.base64

```diff
! Base64 file hash
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.base64"]
```
#### file.zip

```diff
! Compress a file into a Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.zip"]
```
#### file.zip.list

```diff
! List of files in Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.zip.list"]
```
#### file.zip.exists

```diff
! File exists in Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.zip.exists"]
```
#### file.zip.read

```diff
! Read file from Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.zip.read"]
```
#### file.zip.remove

```diff
! Remove file from Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.zip.remove"]
```
#### file.unzip

```diff
! Extract Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.unzip"]
```
#### file.gzip

```diff
! Compress file with Gzip
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.gzip"]
```
#### file.ungzip

```diff
! Extract Gzip file
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.ungzip"]
```
#### file.link

```diff
! Create a symbolic link
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.link"]
```
#### file.link.exists

```diff
! Symbolic link exists
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.link.exists"]
```
#### file.backup

```diff
! Backup files
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.backup"]
```
#### file.compare

```diff
! Compare files
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["file.compare"]
```
#### dir.exists

```diff
! Directory exists
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.exists"]
```
#### dir.create

```diff
! Create directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.create"]
```
#### dir.copy

```diff
! Copy directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.copy"]
```
#### dir.move

```diff
! Move directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.move"]
```
#### dir.rename

```diff
! Rename directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.rename"]
```
#### dir.remove

```diff
! Remove directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.remove"]
```
#### dir.list

```diff
! List of files in a directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.list"]
```
#### dir.clear

```diff
! Clear directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.clear"]
```
#### dir.info

```diff
! Directory information
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.info"]
```
#### dir.size

```diff
! Directory size
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.size"]
```
#### dir.permissions

```diff
! Directory permissions
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.permissions"]
```
#### dir.readonly

```diff
! Read-only directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.readonly"]
```
#### dir.hidden

```diff
! Hidden directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.hidden"]
```
#### dir.modified

```diff
! Directory modification time
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.modified"]
```
#### dir.zip

```diff
! Compress directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.zip"]
```
#### dir.backup

```diff
! Backup directory
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.backup"]
```
#### dir.compare

```diff
! Compare directories
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["dir.compare"]
```
#### drive.list

```diff
! List of volumes
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["drive.list"]
```
#### drive.name

```diff
! Volume name
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["drive.name"]
```
#### drive.size

```diff
! Volume size
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["drive.size"]
```
#### drive.used

```diff
! Volume space used
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["drive.used"]
```
#### drive.free

```diff
! Volume free space
+ ask・python・js・swift・kotlin・godot・c++
```

```json
["drive.free"]
```
#### drive.mount

```diff
! Mount volume
+ local・python・js・swift・kotlin・godot・c++
```

```json
["drive.mount"]
```
#### drive.unmount

```diff
! Unmount volume
+ local・python・js・swift・kotlin・godot・c++
```

```json
["drive.unmount"]
```
#### drive.format

```diff
! Format volume
+ local・python・js・swift・kotlin・godot・c++
```

```json
["drive.format"]
```
#### path.drive

```diff
! Get volume from path
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["path.drive"]
```
#### path.dir

```diff
! Get directory from path
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["path.dir"]
```
#### path.file

```diff
! Get file from path
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["path.file"]
```
#### path.name

```diff
! Get filename from path
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["path.name"]
```
#### path.extension

```diff
! Get extension from path
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["path.extension"]
```
#### path.extension.strip

```diff
! Trim extension from path
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["path.extension.strip"]
```

### cloud

#### cloud.file

```diff
! File server
+ local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.file"]
```
#### cloud.web

```diff
! Web server
+ local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.web"]
```
#### cloud.api

```diff
! API server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.api"]
```
#### cloud.socket

```diff
! Socket server
+ local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.socket"]
```
#### cloud.websocket

```diff
! Websocket server
+ local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.websocket"]
```
#### cloud.mail

```diff
! Mail server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.mail"]
```
#### cloud.game

```diff
! Game server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.game"]
```
#### cloud.social

```diff
! Social server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.social"]
```
#### cloud.live

```diff
! Streaming server
+ local・python・js・swift・kotlin・godot・c++
```

```json
["cloud.live"]
```

### bot

#### bot.telegram

```diff
! Telegram bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.telegram"]
```
#### bot.wechat

```diff
! Wechat bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.wechat"]
```
#### bot.x

```diff
! X bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.x"]
```
#### bot.youtube

```diff
! YouTube bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.youtube"]
```
#### bot.tiktok

```diff
! TikTok bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.tiktok"]
```
#### bot.steam

```diff
! Steam bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.steam"]
```
#### bot.binance

```diff
! Binance bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.binance"]
```
#### bot.ib

```diff
! Interactive Brokers bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```json
["bot.ib"]
```

### request

#### request

```diff
! Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["request"]
```
#### request.post

```diff
! Post Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["request.post"]
```
#### request.put

```diff
! Put Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["request.put"]
```
#### request.delete

```diff
! Delete Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["request.delete"]
```
#### request.head

```diff
! Head Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["request.head"]
```

### cookie

#### cookie

```diff
! Get Web cookies
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["cookie"]
```
#### cookie.remove

```diff
! Delete Web cookies
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["cookie.remove"]
```

### sql

#### sql

```diff
! SQL query
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sql"]
```
#### sql.connect

```diff
! Connect to SQL server
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.connect"]
```
#### sql.disconnet

```diff
! Disconnect from SQL server
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.disconnet"]
```
#### sql.user

```diff
! SQL user
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.user"]
```
#### sql.user.list

```diff
! SQL user list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.user.list"]
```
#### sql.user.remove

```diff
! SQL remove user
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.user.remove"]
```
#### sql.db

```diff
! SQL database
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.db"]
```
#### sql.db.list

```diff
! SQL database list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.db.list"]
```
#### sql.db.remove

```diff
! SQL remove database
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.db.remove"]
```
#### sql.db.size

```diff
! SQL database size
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.db.size"]
```
#### sql.table

```diff
! SQL table
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.table"]
```
#### sql.table.list

```diff
! SQL table list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.table.list"]
```
#### sql.table.remove

```diff
! SQL remove table
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.table.remove"]
```
#### sql.field

```diff
! SQL field
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.field"]
```
#### sql.field.list

```diff
! SQL field list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.field.list"]
```
#### sql.field.remove

```diff
! SQL remove field
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.field.remove"]
```
#### sql.index

```diff
! SQL index
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.index"]
```
#### sql.index.list

```diff
! SQL index list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.index.list"]
```
#### sql.index.remove

```diff
! SQL remove index
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.index.remove"]
```
#### sql.function

```diff
! SQL function
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.function"]
```
#### sql.function.list

```diff
! SQL function list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.function.list"]
```
#### sql.function.remove

```diff
! SQL remove function
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.function.remove"]
```
#### sql.view

```diff
! SQL view
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.view"]
```
#### sql.view.list

```diff
! SQL view list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.view.list"]
```
#### sql.view.remove

```diff
! SQL remove a view
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.view.remove"]
```
#### sql.get

```diff
! SQL get one result
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.get"]
```
#### sql.all

```diff
! SQL get all results
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.all"]
```
#### sql.cursor

```diff
! SQL cursor
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.cursor"]
```
#### sql.transaction

```diff
! SQL start transaction
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.transaction"]
```
#### sql.commit

```diff
! SQL send transaction
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.commit"]
```
#### sql.rollback

```diff
! SQL cancel transaction
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["sql.rollback"]
```

### os

#### os.name

```diff
! Operating system name
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.name"]
```
#### os.version

```diff
! Operating system version
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.version"]
```
#### os.username

```diff
! User name
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.username"]
```
#### os.desktop

```diff
! Check that it’s desktop
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.desktop"]
```
#### os.mobile

```diff
! Check that it’s mobile device
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.mobile"]
```
#### os.web

```diff
! Check that it’s Web
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.web"]
```
#### os.windows

```diff
! Check that it’s Windows
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.windows"]
```
#### os.macos

```diff
! Check that it's macOS
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.macos"]
```
#### os.ios

```diff
! Check that it's iOS
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.ios"]
```
#### os.ipados

```diff
! Check that it's iPadOS
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.ipados"]
```
#### os.watchos

```diff
! Check that it's watchOS
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.watchos"]
```
#### os.tvos

```diff
! Check that it's tvOS
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.tvos"]
```
#### os.android

```diff
! Check that it's Android
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.android"]
```
#### os.nix

```diff
! Check that it’s Unix-like
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["os.nix"]
```

### device

#### cpu.name

```diff
! Processor name
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["cpu.name"]
```
#### cpu.cores

```diff
! Number of processor cores
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["cpu.cores"]
```
#### memory.size

```diff
! Memory size
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["memory.size"]
```
#### memory.free

```diff
! Memory Free
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["memory.free"]
```
#### memory.used

```diff
! Memory used
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["memory.used"]
```
#### memory.available

```diff
! Memory available
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["memory.available"]
```

### gps

#### gps

```diff
! Get GPS coordinates
+ ask・swift・kotlin・godot・c++
```

```json
["gps"]
```

### sensor

#### speed

```diff
! Get speed
+ ask・swift・kotlin・godot・c++
```

```json
["speed"]
```
#### tilt

```diff
! Get tilt
+ ask・swift・kotlin・godot・c++
```

```json
["tilt"]
```
#### compass

```diff
! Get compass direction
+ ask・swift・kotlin・godot・c++
```

```json
["compass"]
```
#### motion

```diff
! Get motion type
+ ask・swift・kotlin・godot・c++
```

```json
["motion"]
```

### camera

#### camera

```diff
! Get camera image
+ ask・swift・kotlin・godot・c++
```

```json
["camera"]
```
#### gallery

```diff
! Get gallery image
+ ask・swift・kotlin・godot・c++
```

```json
["gallery"]
```

### contacts

#### contacts

```diff
! Get contacts
+ ask・swift・kotlin・godot・c++
```

```json
["contacts"]
```

### calendar

#### calendar

```diff
! Get calendar
+ ask・swift・kotlin・godot・c++
```

```json
["calendar"]
```

### health

#### health

```diff
! Get health data
+ ask・swift・kotlin・godot・c++
```

```json
["health"]
```

### flashlight

#### flashlight

```diff
! Flashlight
+ ask・swift・kotlin・godot・c++
```

```json
["flashlight"]
```

### mic

#### mic

```diff
! Microphone
+ ask・swift・kotlin・godot・c++
```

```json
["mic"]
```

### notification

#### notification

```diff
! Receive notifications
+ ask・swift・kotlin・godot・c++
```

```json
["notification"]
```
#### notification.token

```diff
! Notification token
+ ask・swift・kotlin・godot・c++
```

```json
["notification.token"]
```
#### notification.send

```diff
! Send notification
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["notification.send"]
```

### key

#### key

```diff
! Assign key action
+ safe・js・swift・kotlin・godot・c++
```

```json
["key"]
```
#### key.remove

```diff
! Delete a key action
+ safe・js・swift・kotlin・godot・c++
```

```json
["key.remove"]
```
#### key.press

```diff
! Start a key action
+ safe・js・swift・kotlin・godot・c++
```

```json
["key.press"]
```
#### key.enable

```diff
! Enable key action
+ safe・js・swift・kotlin・godot・c++
```

```json
["key.enable"]
```
#### key.disable

```diff
! Disable key action
+ safe・js・swift・kotlin・godot・c++
```

```json
["key.disable"]
```

### keyboard

#### keyboard

```diff
! On-screen keyboard
+ safe・js・swift・kotlin・godot・c++
```

```json
["keyboard"]
```
#### keyboard.height

```diff
! Screen keyboard height
+ safe・js・swift・kotlin・godot・c++
```

```json
["keyboard.height"]
```

### mouse

#### mouse

```diff
! Show mouse
+ safe・js・swift・kotlin・godot・c++
```

```json
["mouse"]
```
#### mouse.hide

```diff
! Hide mouse
+ safe・js・swift・kotlin・godot・c++
```

```json
["mouse.hide"]
```
#### mouse.lock

```diff
! Lock mouse
+ safe・js・swift・kotlin・godot・c++
```

```json
["mouse.lock"]
```
#### mouse.capture

```diff
! Capture mouse
+ safe・js・swift・kotlin・godot・c++
```

```json
["mouse.capture"]
```
#### mouse.confine

```diff
! Limit mouse movement
+ safe・js・swift・kotlin・godot・c++
```

```json
["mouse.confine"]
```
#### mouse.position

```diff
! Get mouse coordinates
+ safe・js・swift・kotlin・godot・c++
```

```json
["mouse.position"]
```
#### mouse.shape

```diff
! Mouse pointer shape
+ safe・js・swift・kotlin・godot・c++
```

```json
["mouse.shape"]
```

### gamepad

#### gamepad.axis

```diff
! Gamepad stick deflection
+ safe・js・swift・kotlin・godot・c++
```

```json
["gamepad.axis"]
```
#### gamepad.vibrate

```diff
! Gamepad vibration
+ safe・js・swift・kotlin・godot・c++
```

```json
["gamepad.vibrate"]
```

### clipboard

#### clipboard

```diff
! Clipboard
+ safe・js・swift・kotlin・godot・c++
```

```json
["clipboard"]
```
#### clipboard.clear

```diff
! Clear clipboard
+ safe・js・swift・kotlin・godot・c++
```

```json
["clipboard.clear"]
```

### voice

#### voice

```diff
! Read text with voice
+ safe・js・swift・kotlin・godot・c++
```

```json
["voice"]
```
#### voice.list

```diff
! Voice list
+ safe・js・swift・kotlin・godot・c++
```

```json
["voice.list"]
```
#### voice.stop

```diff
! Stop text reading
+ safe・js・swift・kotlin・godot・c++
```

```json
["voice.stop"]
```
#### voice.pause

```diff
! Pause / continue text reading
+ safe・js・swift・kotlin・godot・c++
```

```json
["voice.pause"]
```

### convert

#### convert

```diff
! Convert from one format to another
+ vapp・python・js・swift・kotlin・godot・c++
```

```json
["convert"]
```

### image

#### image

```diff
! Create image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image"]
```
#### image.read

```diff
! Read image from file
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.read"]
```
#### image.write

```diff
! Write image to file
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.write"]
```
#### image.size

```diff
! Resize image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.size"]
```
#### image.crop

```diff
! Crop image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.crop"]
```
#### image.square

```diff
! Crop image to square
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.square"]
```
#### image.rotate

```diff
! Rotate image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.rotate"]
```
#### image.flip.h

```diff
! Reflect image horizontally
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.flip.h"]
```
#### image.flip.v

```diff
! Reflect image vertically
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.flip.v"]
```
#### image.tint

```diff
! Tint the image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.tint"]
```
#### image.gray

```diff
! Convert image to grayscale
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.gray"]
```
#### image.text

```diff
! Add text to image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.text"]
```
#### image.image

```diff
! Add image to image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.image"]
```
#### image.draw

```diff
! Add drawing to image
+ safe・js・swift・kotlin・godot・c++
```

```json
["image.draw"]
```

### video

#### video

```diff
! Create video
+ safe・js・swift・kotlin・godot・c++
```

```json
["video"]
```
#### video.read

```diff
! Read video from file
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.read"]
```
#### video.write

```diff
! Write video to file
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.write"]
```
#### video.size

```diff
! Video size
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.size"]
```
#### video.rate

```diff
! Video frame rate
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.rate"]
```
#### video.rotate

```diff
! Rotate video
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.rotate"]
```
#### video.flip.h

```diff
! Reflect video horizontally
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.flip.h"]
```
#### video.flip.v

```diff
! Reflect video vertically
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.flip.v"]
```
#### video.clip

```diff
! Video clip
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.clip"]
```
#### video.speed

```diff
! Video speed
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.speed"]
```
#### video.reverse

```diff
! Change video direction
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.reverse"]
```
#### video.text

```diff
! Add text to video
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.text"]
```
#### video.image

```diff
! Add image to video
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.image"]
```
#### video.sound

```diff
! Add sound to video
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.sound"]
```
#### video.video

```diff
! Add video to video
+ safe・js・swift・kotlin・godot・c++
```

```json
["video.video"]
```

### model

#### model

```diff
! Create 3D model
+ safe・js・swift・kotlin・godot・c++
```

```json
["model"]
```
#### model.read

```diff
! Read 3D model from file
+ safe・js・swift・kotlin・godot・c++
```

```json
["model.read"]
```
#### model.write

```diff
! Write 3D model to file
+ safe・js・swift・kotlin・godot・c++
```

```json
["model.write"]
```
#### model.animate

```diff
! Animate 3D model
+ safe・js・swift・kotlin・godot・c++
```

```json
["model.animate"]
```
#### model.texture

```diff
! Apply texture to 3D model
+ safe・js・swift・kotlin・godot・c++
```

```json
["model.texture"]
```

### sound

#### sound

```diff
! Create sound
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound"]
```
#### sound.read

```diff
! Read sound from file
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.read"]
```
#### sound.write

```diff
! Write sound to file
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.write"]
```
#### sound.list

```diff
! Current played sounds
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.list"]
```
#### sound.remove

```diff
! Remove sound
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.remove"]
```
#### sound.volume

```diff
! Sound volume
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.volume"]
```
#### sound.speed

```diff
! Sound playback speed
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.speed"]
```
#### sound.clip

```diff
! Sound clip
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.clip"]
```
#### sound.sound

```diff
! Add sound to sound
+ safe・js・swift・kotlin・godot・c++
```

```json
["sound.sound"]
```

### music

#### music

```diff
! Add music
+ safe・js・swift・kotlin・godot・c++
```

```json
["music"]
```
#### music.stop

```diff
! Stop music
+ safe・js・swift・kotlin・godot・c++
```

```json
["music.stop"]
```
#### music.pause

```diff
! Pause / continue music
+ safe・js・swift・kotlin・godot・c++
```

```json
["music.pause"]
```
#### music.volume

```diff
! Music sound volume
+ safe・js・swift・kotlin・godot・c++
```

```json
["music.volume"]
```

### volume

#### volume

```diff
! Master volume
+ safe・js・swift・kotlin・godot・c++
```

```json
["volume"]
```

### screen

#### screen.count

```diff
! Number of screens
+ safe・js・swift・kotlin・godot・c++
```

```json
["screen.count"]
```
#### screen.list

```diff
! List of screens
+ safe・js・swift・kotlin・godot・c++
```

```json
["screen.list"]
```
#### screen.info

```diff
! Screen information
+ safe・js・swift・kotlin・godot・c++
```

```json
["screen.info"]
```
#### size

```diff
! Screen size
+ safe・js・swift・kotlin・godot・c++
```

```json
["size"]
```
#### orientation

```diff
! Screen orientation
+ safe・js・swift・kotlin・godot・c++
```

```json
["orientation"]
```
#### landscape

```diff
! Landscape orientation
+ safe・js・swift・kotlin・godot・c++
```

```json
["landscape"]
```
#### portrait

```diff
! Portrait orientation
+ safe・js・swift・kotlin・godot・c++
```

```json
["portrait"]
```
#### rate

```diff
! Screen frame rate
+ safe・js・swift・kotlin・godot・c++
```

```json
["rate"]
```
#### pixel

```diff
! Get screen pixel color
+ safe・js・swift・kotlin・godot・c++
```

```json
["pixel"]
```
#### symbol

```diff
! Get screen symbol
+ safe・js・swift・kotlin・godot・c++
```

```json
["symbol"]
```
#### dpi

```diff
! Dots per inch
+ safe・js・swift・kotlin・godot・c++
```

```json
["dpi"]
```
#### dark

```diff
! Dark mode
+ safe・js・swift・kotlin・godot・c++
```

```json
["dark"]
```
#### touch

```diff
! Touchscreen
+ safe・js・swift・kotlin・godot・c++
```

```json
["touch"]
```
#### screenshot

```diff
! Screenshot
+ safe・swift・kotlin・godot・c++
```

```json
["screenshot"]
```
#### screen.record

```diff
! Record screen
+ safe・swift・kotlin・godot・c++
```

```json
["screen.record"]
```
#### screen.stop

```diff
! Stop screen recording
+ safe・swift・kotlin・godot・c++
```

```json
["screen.stop"]
```

### ui

#### ui

```diff
! UI element
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui"]
```
#### bg

```diff
! Background
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["bg"]
```
#### show

```diff
! Show UI
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["show"]
```
#### hide

```diff
! Hide UI
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["hide"]
```
#### visible

```diff
! UI visibility
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["visible"]
```
#### enable

```diff
! Enable UI
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["enable"]
```
#### disable

```diff
! Disable UI
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["disable"]
```
#### enabled

```diff
! Check if UI is enabled
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["enabled"]
```
#### focus

```diff
! Move focus to UI
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["focus"]
```
#### scale

```diff
! Scale UI
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["scale"]
```
#### ui.text

```diff
! UI text
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.text"]
```
#### ui.image

```diff
! UI image
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.image"]
```
#### ui.button

```diff
! UI button
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.button"]
```
#### ui.divider

```diff
! UI separator
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.divider"]
```
#### ui.video

```diff
! UI video
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.video"]
```
#### ui.select

```diff
! UI selection
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.select"]
```
#### ui.switch

```diff
! UI switch
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.switch"]
```
#### ui.progress

```diff
! UI progress bar
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.progress"]
```
#### ui.slider

```diff
! UI slider
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.slider"]
```
#### ui.edit

```diff
! UI text editor
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.edit"]
```
#### ui.chart

```diff
! UI chart
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.chart"]
```
#### ui.split.h

```diff
! UI horizontal separator
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.split.h"]
```
#### ui.split.v

```diff
! UI vertical separator
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.split.v"]
```
#### ui.list

```diff
! UI list
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.list"]
```
#### ui.tile

```diff
! UI tile
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.tile"]
```
#### ui.color

```diff
! UI color
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.color"]
```
#### ui.date

```diff
! UI date
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.date"]
```
#### ui.drop

```diff
! UI drop down content
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.drop"]
```
#### ui.menu

```diff
! UI menu
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.menu"]
```
#### ui.menu.context

```diff
! UI context menu
+ safe・python・js・swift・kotlin・godot・c++
```

```json
["ui.menu.context"]
```

### window

#### window

```diff
! Create window
+ safe・js・swift・kotlin・godot・c++
```

```json
["window"]
```
#### window.list

```diff
! Window list
+ safe・js・swift・kotlin・godot・c++
```

```json
["window.list"]
```
#### window.info

```diff
! Window information
+ safe・js・swift・kotlin・godot・c++
```

```json
["window.info"]
```
#### title

```diff
! Window title
+ safe・js・swift・kotlin・godot・c++
```

```json
["title"]
```
#### icon

```diff
! Window icon
+ safe・js・swift・kotlin・godot・c++
```

```json
["icon"]
```
#### size

```diff
! Window size
+ safe・js・swift・kotlin・godot・c++
```

```json
["size"]
```
#### size.max

```diff
! Maximum window size
+ safe・js・swift・kotlin・godot・c++
```

```json
["size.max"]
```
#### size.min

```diff
! Minimum window size
+ safe・js・swift・kotlin・godot・c++
```

```json
["size.min"]
```
#### position

```diff
! Window position
+ safe・js・swift・kotlin・godot・c++
```

```json
["position"]
```
#### direction

```diff
! Window text direction
+ safe・js・swift・kotlin・godot・c++
```

```json
["direction"]
```
#### attention

```diff
! Window attention
+ safe・js・swift・kotlin・godot・c++
```

```json
["attention"]
```
#### top

```diff
! Top of all windows
+ safe・js・swift・kotlin・godot・c++
```

```json
["top"]
```
#### foreground

```diff
! Foreground window
+ safe・js・swift・kotlin・godot・c++
```

```json
["foreground"]
```
#### unfocusable

```diff
! Do not take the focus of the window
+ safe・js・swift・kotlin・godot・c++
```

```json
["unfocusable"]
```
#### unresizable

```diff
! Do not resize window
+ safe・js・swift・kotlin・godot・c++
```

```json
["unresizable"]
```
#### center

```diff
! Center the window on the screen
+ safe・js・swift・kotlin・godot・c++
```

```json
["center"]
```
#### fullscreen

```diff
! Full screen window
+ safe・js・swift・kotlin・godot・c++
```

```json
["fullscreen"]
```
#### drop

```diff
! Drop content to window
+ safe・js・swift・kotlin・godot・c++
```

```json
["drop"]
```
#### border

```diff
! Window border
+ safe・js・swift・kotlin・godot・c++
```

```json
["border"]
```
#### maximized

```diff
! Maximize window
+ safe・js・swift・kotlin・godot・c++
```

```json
["maximized"]
```
#### minimized

```diff
! Minimize window
+ safe・js・swift・kotlin・godot・c++
```

```json
["minimized"]
```
#### exclusive

```diff
! Make window exclusive
+ safe・js・swift・kotlin・godot・c++
```

```json
["exclusive"]
```
#### vsync

```diff
! Vertical window synchronization
+ safe・js・swift・kotlin・godot・c++
```

```json
["vsync"]
```
#### fps

```diff
! Window FPS
+ safe・js・swift・kotlin・godot・c++
```

```json
["fps"]
```

### dialog

#### dialog.file

```diff
! File selection
+ safe・js・swift・kotlin・godot・c++
```

```json
["dialog.file"]
```
#### dialog.color

```diff
! Color selection
+ safe・js・swift・kotlin・godot・c++
```

```json
["dialog.color"]
```
#### dialog.date

```diff
! Date selection
+ safe・js・swift・kotlin・godot・c++
```

```json
["dialog.date"]
```
#### dialog.list

```diff
! Select from list
+ safe・js・swift・kotlin・godot・c++
```

```json
["dialog.list"]
```

### effect

#### effect

```diff
! Add effect
+ safe・js・swift・kotlin・godot・c++
```

```json
["effect"]
```
#### effect.list

```diff
! List of effects
+ safe・js・swift・kotlin・godot・c++
```

```json
["effect.list"]
```
#### effect.remove

```diff
! Remove effect
+ safe・js・swift・kotlin・godot・c++
```

```json
["effect.remove"]
```

### game

#### vn

```diff
! Create visual novel
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["vn"]
```
#### 2d

```diff
! Create 2D game
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["2d"]
```
#### 3d

```diff
! Create 3D game
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["3d"]
```
#### menu

```diff
! Create game menu
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["menu"]
```
#### say

```diff
! Say text
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["say"]
```
#### say.skip

```diff
! Skip text
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["say.skip"]
```
#### route

```diff
! Offer to select a root
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["route"]
```
#### route.remove

```diff
! Remove root selection
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["route.remove"]
```
#### route.check

```diff
! Check root
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["route.check"]
```
#### route.select

```diff
! Select root
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["route.select"]
```
#### route.repeat

```diff
! Repeat root selection
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["route.repeat"]
```
#### route.skip

```diff
! Skip root selection
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["route.skip"]
```
#### character

```diff
! Create a character
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["character"]
```
#### come

```diff
! Character arrived
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["come"]
```
#### leave

```diff
! Character left
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["leave"]
```
#### change

```diff
! Character changed
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["change"]
```
#### object

```diff
! Add an object to the map
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["object"]
```
#### shoot

```diff
! Character shot
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["shoot"]
```
#### move

```diff
! Character movement
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["move"]
```
#### jump

```diff
! Jump
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["jump"]
```
#### crouch

```diff
! Crouch
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["crouch"]
```
#### drop

```diff
! Drop
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["drop"]
```
#### look

```diff
! Look around
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["look"]
```
#### hud

```diff
! Interface
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["hud"]
```
#### hud.map

```diff
! Map
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["hud.map"]
```
#### hud.inventory

```diff
! Inventory
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["hud.inventory"]
```
#### snd

```diff
! Spatial sound
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["snd"]
```
#### light

```diff
! Spatial light
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["light"]
```
#### cam

```diff
! Spatial camera
+ vapp・safe・js・swift・kotlin・godot・c++
```

```json
["cam"]
```

### ai

#### ai.chat

```diff
! Communicate with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.chat"]
```
#### ai.image

```diff
! Create AI image
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.image"]
```
#### ai.video

```diff
! Create AI video
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.video"]
```
#### ai.music

```diff
! Create AI music
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.music"]
```
#### ai.sound

```diff
! Create AI sound
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.sound"]
```
#### ai.say

```diff
! Create AI speech
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.say"]
```
#### ai.2d

```diff
! Create AI 2D asset
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.2d"]
```
#### ai.3d

```diff
! Create AI 3D asset
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.3d"]
```
#### ai.character

```diff
! Create AI character
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.character"]
```
#### ai.clean

```diff
! Clean up image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.clean"]
```
#### ai.resize

```diff
! Resize image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.resize"]
```
#### ai.color

```diff
! Colorize image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.color"]
```
#### ai.style

```diff
! Change image style with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.style"]
```
#### ai.translate

```diff
! Translate text with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.translate"]
```
#### ai.recognize.text

```diff
! Recognize text with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.recognize.text"]
```
#### ai.recognize.image

```diff
! Recognize image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.recognize.image"]
```
#### ai.recognize.video

```diff
! Recognize video with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.recognize.video"]
```
#### ai.recognize.motion

```diff
! Recognize motion with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.recognize.motion"]
```
#### ai.capture.voice

```diff
! Capture voice with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.capture.voice"]
```
#### ai.capture.face

```diff
! Capture facial expressions with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.capture.face"]
```
#### ai.capture.motion

```diff
! Capture motion with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["ai.capture.motion"]
```

### social

#### social.signin

```diff
! Authorization
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["social.signin"]
```
#### social.signup

```diff
! Registration
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["social.signup"]
```
#### social.signout

```diff
! Logout
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["social.signout"]
```
#### social.restore

```diff
! Restore login
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["social.restore"]
```
#### social

```diff
! Social content
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["social"]
```
#### social.send

```diff
! Send content
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["social.send"]
```
#### social.buy

```diff
! Purchase
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["social.buy"]
```

### tech

#### light.on

```diff
! Turn lamp on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["light.on"]
```
#### light.off

```diff
! Turn lamp off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["light.off"]
```
#### power.on

```diff
! Power on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["power.on"]
```
#### power.off

```diff
! Turn power off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["power.off"]
```
#### power.timer

```diff
! Set timer for power
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["power.timer"]
```
#### lock.open

```diff
! Open the lock
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["lock.open"]
```
#### lock.close

```diff
! Close the lock
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["lock.close"]
```
#### lock.code

```diff
! Set the code on the lock
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["lock.code"]
```
#### dron.move

```diff
! Drone movement
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.move"]
```
#### dron.up

```diff
! Raise the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.up"]
```
#### dron.down

```diff
! Lower the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.down"]
```
#### dron.left

```diff
! Move the drone to the left
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.left"]
```
#### dron.right

```diff
! Move the drone to the right
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.right"]
```
#### dron.go

```diff
! Move the drone forward
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.go"]
```
#### dron.stop

```diff
! Stop drone movement
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.stop"]
```
#### dron.jump

```diff
! Jump the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.jump"]
```
#### dron.crouch

```diff
! Crouch the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.crouch"]
```
#### dron.open

```diff
! Open the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.open"]
```
#### dron.close

```diff
! Close the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.close"]
```
#### dron.rotate

```diff
! Turn the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.rotate"]
```
#### dron.camera

```diff
! Drone camera
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.camera"]
```
#### dron.camera.rotate

```diff
! Rotate drone camera
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.camera.rotate"]
```
#### dron.camera.on

```diff
! Turn drone camera on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.camera.on"]
```
#### dron.camera.off

```diff
! Turn drone camera off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.camera.off"]
```
#### dron.camera.record

```diff
! Record drone camera video
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.camera.record"]
```
#### dron.camera.record.stop

```diff
! Stop drone camera recording
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.camera.record.stop"]
```
#### dron.hand.open

```diff
! Open the drone arm
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.hand.open"]
```
#### dron.hand.close

```diff
! Close the drone arm
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.hand.close"]
```
#### dron.hand.move

```diff
! Drone hand movement
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.hand.move"]
```
#### dron.hand.gesture

```diff
! Drone hand gesture
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.hand.gesture"]
```
#### dron.sound

```diff
! Drone speaker
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.sound"]
```
#### dron.volume

```diff
! Drone speaker sound volume
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.volume"]
```
#### dron.mic

```diff
! Drone microphone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.mic"]
```
#### dron.mic.on

```diff
! Drone microphone on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.mic.on"]
```
#### dron.mic.off

```diff
! Drone microphone off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.mic.off"]
```
#### dron.mic.record

```diff
! Drone microphone audio recording
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.mic.record"]
```
#### dron.mic.record.stop

```diff
! Stop recording drone microphone audio
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```json
["dron.mic.record.stop"]
```

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
        [void [1 2 3]]
        .
    decode
        [void.decode "[1 2 3]"]
        .
    write
        [void.write path/to/file.void [1 2 3]]
        .
    read
        [void.read path/to/file.void]
        .
    compress
        [file.void path/to/file]
        [dir.void path/to/dir]
    decompress
        [unvoid path/to/file.void]
        .
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
binary
    *
        3
        <00 01 02>
binary jpeg
    *
        jpeg
        <FF D8 FF E0 00…>
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
    "binary": "impossible",
    "binary jpeg": "impossible",
    "binary in hex": "need to convert",
    "binary in bin": "need to convert"
}
```

</td>
</tr>

</table>

> [!TIP]
> Use **V O I D format [highlighting 📃](https://raw.githubusercontent.com/voidspawner/void.ideology/refs/heads/main/asset/settings/void.sublime-syntax)** for **[Sublime Text](https://sublimetext.com)**.
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
>```

> ``data.csv``
> ```csv
> index,text,value
> 1,text 1,value 1
> 2,text 2,value 2
> ```
>
> ```
> . {data.csv/index.2.value}
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

## V O I D license
**⌜ V O I D license ⌟** is a license to distribute digital content and goods. Expressed in a single sentence:

> **DO WHAT YOU WANT**

You can use it in both **private** and **open source**, embed it in **free** or **paid** products. **Modify**. Create your **own solutions** based on it. **No need to specify the author**.

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create applications and games.

## V O I D tech
**[⌜ V O I D tech ⌟](https://github.com/voidspawner/void.tech)** is combinable devices controlled by **V O I D ai** to perform **home**, **business**, **industrial** purposes and **teaching children** to interact with technology.

## V O I D ideology
**[⌜V O I D⌟](https://github.com/voidspawner/void.ideology)**  is not only about compact technologies, but also an **ideology** that shows where these technologies are taking us.

## V O I D task
> [!IMPORTANT]
> By adding your code to the repository, you are publishing it under the **V O I D licence**.

Find out current **tasks** and **payment** at [**V O I D task**](https://github.com/voidspawner/void.task)
