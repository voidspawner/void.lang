# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **V O I D** or **JSON format**. It is used as a replacement for the standard Bash・CMD・etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one V O I D or JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

> [!IMPORTANT]
> **The project is in the process of development.**

<img src="https://i.imgur.com/kx2UcUh.jpg" width="100%">

> [**About**](#about)・
[**Preinstalled Language**](#preinstalled-language)・
[**Example**](#example)・
[**How to Use**](#how-to-use)・
[**How to Use Game Engine**](#how-to-use-game-engine)・
[**Actions**](#actions)・
[**Progress**](#progress)・
[**Detail**](#detail)・
[**V O I D format**](#v-o-i-d-format)・
[**V O I D os**](#v-o-i-d-os)・
[**V O I D ideology**](#v-o-i-d-ideology)・
[**V O I D work**](#v-o-i-d-work)

## Preinstalled Language

| <p align="center">**Language**</p> | <p align="center">**Engine**</p> | <p align="center">**Web**</p> | <p align="center">**CLI**</p> | <p align="center">**Server**</p> | <p align="center">**Mobile**</p> | <p align="center">**Windows**</p> | <p align="center">**macOS**</p> | <p align="center">**iOS**</p> | <p align="center">**Android**</p> | <p align="center">**Linux**</p> | <p align="center">**Xbox**</p> | <p align="center">**Switch**</p> | <p align="center">**Steam Deck**</p> | <p align="center">**PlayStation**</p> |
| ---------- | ----------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ----------------------- | ----------------------- |
| [**Python**](https://www.python.org/downloads)     | <p align="center">Python</p>        | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| [**JavaScript**](https://nodejs.org/en/download) | <p align="center">NodeJS</p>        | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| [**Swift**](https://www.swift.org/download)      | <p align="center">-</p>             | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| [**Kotlin**](https://developer.android.com/studio)     | <p align="center">-</p>             | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| [**GDScript**](https://godotengine.org/download/windows)   | <p align="center">Godot</p>         | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p>  | <p align="center">+</p> |
| [**C++**](https://www.unrealengine.com/download)        | <p align="center">Unreal Engine</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p>  | <p align="center">+</p> |

## Example
##### Simple
```javascript
{
  "run": [
    [".", "Hi World :D"]
  ]
}
```
##### Even simpler
```javascript
[
  [".", "Hi World :D"]
]
```
##### Multilanguage text
```javascript
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
```javascript
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
```javascript
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
```javascript
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
```javascript
[
  ["cloud.file": "/path/to/share"]
]
```
##### Add comments
```javascript
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
```javascript
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
```javascript
[
  ["replace", "Hi World :D", "i", "i!"],
  [".", "{}"],
  "upper",
  [".", "{}"]
]
```
##### Run native code
```javascript
[
  ["code", "for i in range(10):print(i)"]
]
```
##### Run Python code
```javascript
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

The code is presented as **action name** and **action parameters**.
```javascript
[".", "Hi World :D"]
```
```
Action name: "."
Action parameters: ["Hi World :D"]
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

## Progress
```
Count of actions: 589
```

| **Name**           | **vapp** | **Python** |  **JS**    | **Swift** | **Kotlin** | **GDScript** |  **C++**  |
| -------------- | ---- | ------ | ------ | ----- | ------ | -------- | ----- |
| run            |      |   <p align="center">✔</p>    | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |     <p align="center">✔</p>    | <p align="center">task</p>  |
| value          |      |   <p align="center">✔</p>    | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| expression     |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| control        |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| text           |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| list           |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| math           |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| time           |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| crypto         |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| format         |      |        |        |       |        |          |       |
| ・ json         |      |   <p align="center">✔</p>    | <p align="center">work</p>   | <p align="center">work</p>  |  <p align="center">work</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| ・ yaml         |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| ・ csv          |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| ・ other        | <p align="center">task</p> |  <p align="center">vapp</p>  | <p align="center">vapp</p>   | <p align="center">vapp</p>  |  <p align="center">vapp</p>  |   <p align="center">vapp</p>   | <p align="center">vapp</p>  |
| file           |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| cloud          |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| bot            |      |  <p align="center">task</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">task</p>   | <p align="center">task</p>  |
| request        |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| cookie         |      |  <p align="center">work</p>  | <p align="center">work</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| sql            |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| os             |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| device         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| gps            |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| sensor         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| photo          |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| contacts       |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| calendar       |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| flashlight     |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| health         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| microphone     |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| notification   |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| key            |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| keyboard       |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| mouse          |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| gamepad        |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| clipboard      |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| say            |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| convert        | <p align="center">work</p> |  <p align="center">vapp</p>  | <p align="center">vapp</p>   | <p align="center">vapp</p>  |  <p align="center">vapp</p>  |   <p align="center">vapp</p>   | <p align="center">vapp</p>  |
| video          |      |  <p align="center">task</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| model          |      |  <p align="center">task</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| sound          |      |  <p align="center">task</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| music          |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| volume         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| screen         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| ui             |      |        |        |       |        |          |       |
| ・ graphic      |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| ・ cli          |      |  <p align="center">work</p>  | <p align="center">task</p>   | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| window         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| dialog         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| effect         |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| game           | <p align="center">work</p> |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">vapp</p>  |  <p align="center">vapp</p>  |   <p align="center">vapp</p>   | <p align="center">vapp</p>  |
| vn             | <p align="center">work</p> |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">vapp</p>  |  <p align="center">vapp</p>  |   <p align="center">vapp</p>   | <p align="center">vapp</p>  |
| 2d             |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| 3d             |      |  <p align="center">-</p>     | <p align="center">-</p>      | <p align="center">task</p>  |  <p align="center">task</p>  |   <p align="center">work</p>   | <p align="center">task</p>  |
| ai             |      |  <p align="center">work</p>  | <p align="center">python</p> | <p align="center">task</p>  |  <p align="center">task</p>  |  <p align="center">python</p>  | <p align="center">task</p>  |
| social         | <p align="center">work</p> |  <p align="center">vapp</p>  | <p align="center">vapp</p>   | <p align="center">vapp</p>  |  <p align="center">vapp</p>  |  <p align="center">vapp</p>    | <p align="center">vapp</p>  |
| tech           | wait |  <p align="center">vapp</p>  | <p align="center">vapp</p>   | <p align="center">vapp</p>  |  <p align="center">vapp</p>  |  <p align="center">vapp</p>    | <p align="center">vapp</p>  |

## Detail

### value

#### get ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get value
```javascript
["get"]
```
#### set ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Set value
```javascript
["set"]
```
#### remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Delete value
```javascript
["remove"]
```
#### type ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get value type
```javascript
["type"]
```
#### bool ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Convert value to boolean
```javascript
["bool"]
```
#### number ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Translate value to a number
```javascript
["number"]
```
#### text ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Translate value to text
```javascript
["text"]
```
#### list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Translate value into a list
```javascript
["list"]
```
#### alias ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Assign an alias to an action
```javascript
["alias"]
```
#### compare ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Compare values
```javascript
["compare"]
```

### expression

#### + ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add
```javascript
["+"]
```
#### - ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Subtract
```javascript
["-"]
```
#### * ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Multiply
```javascript
["*"]
```
#### / ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Divide
```javascript
["/"]
```
#### % ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remainder of division
```javascript
["%"]
```
#### ** ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Elevate
```javascript
["**"]
```
#### ! ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
NOT bitwise operator
```javascript
["!"]
```
#### & ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
AND bitwise operator
```javascript
["&"]
```
#### | ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
OR bitwise operator
```javascript
["|"]
```
#### ^ ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
XOR bitwise operator
```javascript
["^"]
```
#### >> ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Right shift
```javascript
[">>"]
```
#### << ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Left shift
```javascript
["<<"]
```
#### += ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add to value
```javascript
["+="]
```
#### -= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Subtract from value
```javascript
["-="]
```
#### *= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Multiply the value
```javascript
["*="]
```
#### /= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Divide the value
```javascript
["/="]
```
#### %= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Residue from dividing the value
```javascript
["%="]
```
#### **= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Increment the value
```javascript
["**="]
```
#### != ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
NOT bitwise operator of the value
```javascript
["!="]
```
#### &= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
AND bitwise operator of the value
```javascript
["&="]
```
#### |= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
OR bitwise operator of the value
```javascript
["|="]
```
#### ^= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
XOR bitwise operator of the value
```javascript
["^="]
```
#### >>= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Shift to the right of the value
```javascript
[">>="]
```
#### <<= ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Shift to the left of the value
```javascript
["<<="]
```
#### not ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Negation (inversion)
```javascript
["not"]
```
#### and ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Conjunction (and)
```javascript
["and"]
```
#### or ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Disjunction (or)
```javascript
["or"]
```
#### xor ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Exclusive disjunction (exclusive or)
```javascript
["xor"]
```
#### in ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
A value in an array or a name in a dictionary
```javascript
["in"]
```
#### not in ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Value not in array or name not in dictionary
```javascript
["not in"]
```
#### is ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Value type match
```javascript
["is"]
```
#### not is ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Value type mismatch
```javascript
["not is"]
```

### control

#### ? ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
IF check
```javascript
["?"]
```
#### ?? ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
MATCH check
```javascript
["??"]
```
#### o ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
FOR, WHILE loop
```javascript
["o"]
```
#### x ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Exit loop BREAK
```javascript
["x"]
```
#### >>> ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Continue loop CONTINUE
```javascript
[">>>"]
```
#### <<< ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Repeat loop iteration
```javascript
["<<<"]
```
#### _ ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Return action value RETURN
```javascript
["_"]
```
#### . ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Print text
```javascript
["."]
```
#### .. ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Print text without a new line
```javascript
[".."]
```
#### ... ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Enter text
```javascript
["..."]
```
#### action ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Execute action
```javascript
["action"]
```
#### action.open ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Execute an action from a file
```javascript
["action.open"]
```
#### X ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
End vapp
```javascript
["X"]
```
#### xx ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Error
```javascript
["xx"]
```
#### open ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Execute system action
```javascript
["open"]
```
#### shell ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Execute a command line command
```javascript
["shell"]
```
#### shell.open ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Open a terminal and execute the command
```javascript
["shell.open"]
```
#### code ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Execute native code
```javascript
["code"]
```
#### python ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Execute Python code
```javascript
["python"]
```
#### compile ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Compile code for a specific platform
```javascript
["compile"]
```
#### i ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Info logging
```javascript
["i"]
```
#### w ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Warning logging
```javascript
["w"]
```
#### e ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Error logging
```javascript
["e"]
```
#### d ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Debug logging
```javascript
["d"]
```
#### t ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Time logging
```javascript
["t"]
```
#### export ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Export vapp for selected platforms
```javascript
["export"]
```
#### update ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Update script
```javascript
["update"]
```
#### test ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Test script
```javascript
["test"]
```
#### help ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Display language hint
```javascript
["help"]
```
#### debug ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Display debug information
```javascript
["debug"]
```
#### debug.fps ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Display FPS
```javascript
["debug.fps"]
```

### text

#### lower ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Convert text to lower case
```javascript
["lower"]
```
#### upper ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Convert text to uppercase
```javascript
["upper"]
```
#### starts ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Starts with text
```javascript
["starts"]
```
#### ends ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Ends with text
```javascript
["ends"]
```
#### strip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Trim text
```javascript
["strip"]
```
#### strip.start ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Trim the beginning of text
```javascript
["strip.start"]
```
#### strip.end ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Trim the end of text
```javascript
["strip.end"]
```
#### replace ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Replace text
```javascript
["replace"]
```
#### find ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Find position in text
```javascript
["find"]
```
#### similar ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Compare texts
```javascript
["similar"]
```
#### part ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get a part of text
```javascript
["part"]
```
#### split ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Split text
```javascript
["split"]
```
#### join ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Join text
```javascript
["join"]
```
#### regex ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Find in text using regular expression
```javascript
["regex"]
```
#### regex.replace ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Replace text using a regular expression
```javascript
["regex.replace"]
```
#### escape ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Escape text
```javascript
["escape"]
```
#### escape.html ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Escape HTML text
```javascript
["escape.html"]
```
#### escape.sql ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Escape SQL text
```javascript
["escape.sql"]
```
#### escape.url ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Escape text URL
```javascript
["escape.url"]
```
#### escape.json ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Escape text JSON
```javascript
["escape.json"]
```
#### escape.void ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Escape text V O I D
```javascript
["escape.void"]
```
#### unescape ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Unescape text
```javascript
["unescape"]
```
#### unescape.html ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Unescape HTML text
```javascript
["unescape.html"]
```
#### unescape.sql ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Unescape text SQL
```javascript
["unescape.sql"]
```
#### unescape.url ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Unescape text URL
```javascript
["unescape.url"]
```
#### unescape.json ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Unescape JSON text
```javascript
["unescape.json"]
```
#### unescape.void ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Unescape V O I D text
```javascript
["unescape.void"]
```
#### date ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Convert text to timestamp, or timestamp to text
```javascript
["date"]
```
#### letters ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Number of letters in the text
```javascript
["letters"]
```
#### words ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Number of words in the text
```javascript
["words"]
```
#### sentences ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Number of sentences in the text
```javascript
["sentences"]
```
#### lines ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Number of lines in the text
```javascript
["lines"]
```

### list

#### push ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add to list
```javascript
["push"]
```
#### pop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Extract from the list
```javascript
["pop"]
```
#### reverse ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Invert order in the list
```javascript
["reverse"]
```
#### shuffle ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Shuffle the list
```javascript
["shuffle"]
```
#### sort ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Sort the list
```javascript
["sort"]
```
#### fill ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Fill the list
```javascript
["fill"]
```
#### map ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Map the list
```javascript
["map"]
```
#### reduce ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Reduce the list
```javascript
["reduce"]
```
#### names ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Dictionary or list names
```javascript
["names"]
```
#### values ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Dictionary values
```javascript
["values"]
```

### math

#### sin ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Sine
```javascript
["sin"]
```
#### cos ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Cosine
```javascript
["cos"]
```
#### tan ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Tangent
```javascript
["tan"]
```
#### sinh ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hyperbolic sine
```javascript
["sinh"]
```
#### cosh ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hyperbolic cosine
```javascript
["cosh"]
```
#### tanh ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hyperbolic tangent
```javascript
["tanh"]
```
#### asin ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Arcsine
```javascript
["asin"]
```
#### acos ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Arccosine
```javascript
["acos"]
```
#### atan ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Arctangent
```javascript
["atan"]
```
#### asinh ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hyperbolic arcsine
```javascript
["asinh"]
```
#### acosh ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hyperbolic arccosine
```javascript
["acosh"]
```
#### atanh ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hyperbolic arctangent
```javascript
["atanh"]
```
#### round ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Round a number
```javascript
["round"]
```
#### floor ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Round a number down
```javascript
["floor"]
```
#### ceil ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Round a number up
```javascript
["ceil"]
```
#### log ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Logarithm
```javascript
["log"]
```
#### log.e ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hyperbolic logarithm
```javascript
["log.e"]
```
#### log.n ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Natural logarithm
```javascript
["log.n"]
```
#### fa ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Factorial
```javascript
["fa"]
```
#### fib ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Fibonacci
```javascript
["fib"]
```
#### abs ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Absolute value
```javascript
["abs"]
```
#### min ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Minimum value
```javascript
["min"]
```
#### max ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Maximum value
```javascript
["max"]
```
#### avg ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Average value
```javascript
["avg"]
```
#### sum ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Sum of values
```javascript
["sum"]
```
#### hex ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hexadecimal value to byte
```javascript
["hex"]
```
#### hex.dec ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hexadecimal value to decimal
```javascript
["hex.dec"]
```
#### bin ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Binary value to byte
```javascript
["bin"]
```
#### bin.dec ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Binary value to decimal
```javascript
["bin.dec"]
```
#### dec ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decimal value to byte
```javascript
["dec"]
```
#### dec.hex ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decimal value to hexadecimal
```javascript
["dec.hex"]
```
#### dec.bin ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decimal value to binary
```javascript
["dec.bin"]
```
#### rad ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Degree to radian
```javascript
["rad"]
```
#### deg ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Radian to degree
```javascript
["deg"]
```
#### random ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Random value
```javascript
["random"]
```
#### random.reseed ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Re-create random seed
```javascript
["random.reseed"]
```
#### random.seed ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get random seed
```javascript
["random.seed"]
```

### time

#### time ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Time stamp in microseconds
```javascript
["time"]
```
#### time.ms ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Time stamp in milliseconds
```javascript
["time.ms"]
```
#### time.s ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Timestamp in seconds
```javascript
["time.s"]
```
#### timer ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Set timer
```javascript
["timer"]
```
#### timer.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remove timer
```javascript
["timer.remove"]
```
#### wait ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Wait time in seconds
```javascript
["wait"]
```

### crypto

#### encrypt ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode text
```javascript
["encrypt"]
```
#### decrypt ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode text
```javascript
["decrypt"]
```
#### hash ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Random hash
```javascript
["hash"]
```
#### uuid ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Random UUID
```javascript
["uuid"]
```
#### md5 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
MD5 hash
```javascript
["md5"]
```
#### sha1 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SHA1 hash
```javascript
["sha1"]
```
#### sha256 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SHA256 hash
```javascript
["sha256"]
```
#### sha512 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SHA512 hash
```javascript
["sha512"]
```
#### crc32 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
CRC32 hash
```javascript
["crc32"]
```
#### base64 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Base64 hash
```javascript
["base64"]
```
#### base64.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode Base64
```javascript
["base64.decode"]
```
#### gzip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Gzip text
```javascript
["gzip"]
```
#### gzip.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode Gzip
```javascript
["gzip.decode"]
```
#### rsa ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode text with RSA
```javascript
["rsa"]
```
#### rsa.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode RSA
```javascript
["rsa.decode"]
```
#### rsa.key.public ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get RSA public key
```javascript
["rsa.key.public"]
```
#### rsa.key.private ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get RSA private key
```javascript
["rsa.key.private"]
```
#### ssl ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode text with SSL
```javascript
["ssl"]
```
#### ssl.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode SSL
```javascript
["ssl.decode"]
```
#### ssl.check ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Verify SSL
```javascript
["ssl.check"]
```
#### bcrypt ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode text with Bcrypt
```javascript
["bcrypt"]
```
#### bcrypt.check ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Verify Bcrypt
```javascript
["bcrypt.check"]
```

### format

#### void ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode to V O I D
```javascript
["void"]
```
#### void.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode V O I D
```javascript
["void.decode"]
```
#### void.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read V O I D file
```javascript
["void.read"]
```
#### void.write ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Write V O I D file
```javascript
["void.write"]
```
#### json ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode to JSON
```javascript
["json"]
```
#### json.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode JSON
```javascript
["json.decode"]
```
#### json.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read JSON file
```javascript
["json.read"]
```
#### json.write ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Write JSON file
```javascript
["json.write"]
```
#### yaml ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode YAML
```javascript
["yaml"]
```
#### yaml.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode YAML
```javascript
["yaml.decode"]
```
#### csv ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode CSV
```javascript
["csv"]
```
#### csv.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode CSV
```javascript
["csv.decode"]
```
#### ini ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode INI
```javascript
["ini"]
```
#### ini.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode INI
```javascript
["ini.decode"]
```
#### html ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode HTML
```javascript
["html"]
```
#### html.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode HTML
```javascript
["html.decode"]
```
#### xml ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode XML
```javascript
["xml"]
```
#### xml.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode XML
```javascript
["xml.decode"]
```
#### css ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Encode CSS
```javascript
["css"]
```
#### css.decode ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Decode CSS
```javascript
["css.decode"]
```

### file

#### file.exists ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File exists
```javascript
["file.exists"]
```
#### file.write ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Write to file
```javascript
["file.write"]
```
#### file.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read file
```javascript
["file.read"]
```
#### file.read.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read lines from file
```javascript
["file.read.list"]
```
#### file.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remove file
```javascript
["file.remove"]
```
#### file.move ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Move file
```javascript
["file.move"]
```
#### file.copy ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Copy file
```javascript
["file.copy"]
```
#### file.rename ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Rename file
```javascript
["file.rename"]
```
#### file.info ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File information
```javascript
["file.info"]
```
#### file.size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File size
```javascript
["file.size"]
```
#### file.permissions ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File permissions
```javascript
["file.permissions"]
```
#### file.readonly ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read-only file
```javascript
["file.readonly"]
```
#### file.hidden ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hidden file
```javascript
["file.hidden"]
```
#### file.modified ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File modification time
```javascript
["file.modified"]
```
#### file.sha256 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SHA256 file hash
```javascript
["file.sha256"]
```
#### file.crc32 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
CRC32 file hash
```javascript
["file.crc32"]
```
#### file.base64 ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Base64 file hash
```javascript
["file.base64"]
```
#### file.zip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Compress a file into a Zip archive
```javascript
["file.zip"]
```
#### file.zip.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
List of files in Zip archive
```javascript
["file.zip.list"]
```
#### file.zip.exists ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File exists in Zip archive
```javascript
["file.zip.exists"]
```
#### file.zip.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read file from Zip archive
```javascript
["file.zip.read"]
```
#### file.zip.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remove file from Zip archive
```javascript
["file.zip.remove"]
```
#### file.unzip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Extract Zip archive
```javascript
["file.unzip"]
```
#### file.gzip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Compress file with Gzip
```javascript
["file.gzip"]
```
#### file.ungzip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Extract Gzip file
```javascript
["file.ungzip"]
```
#### file.link ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create a symbolic link
```javascript
["file.link"]
```
#### file.link.exists ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Symbolic link exists
```javascript
["file.link.exists"]
```
#### file.backup ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Backup files
```javascript
["file.backup"]
```
#### dir.exists ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Directory exists
```javascript
["dir.exists"]
```
#### dir.create ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create directory
```javascript
["dir.create"]
```
#### dir.copy ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Copy directory
```javascript
["dir.copy"]
```
#### dir.move ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Move directory
```javascript
["dir.move"]
```
#### dir.rename ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Rename directory
```javascript
["dir.rename"]
```
#### dir.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remove directory
```javascript
["dir.remove"]
```
#### dir.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
List of files in a directory
```javascript
["dir.list"]
```
#### dir.clear ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Clear directory
```javascript
["dir.clear"]
```
#### dir.info ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Directory information
```javascript
["dir.info"]
```
#### dir.size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Directory size
```javascript
["dir.size"]
```
#### dir.permissions ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Directory permissions
```javascript
["dir.permissions"]
```
#### dir.readonly ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read-only directory
```javascript
["dir.readonly"]
```
#### dir.hidden ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hidden directory
```javascript
["dir.hidden"]
```
#### dir.modified ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Directory modification time
```javascript
["dir.modified"]
```
#### dir.zip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Compress directory
```javascript
["dir.zip"]
```
#### drive.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
List of volumes
```javascript
["drive.list"]
```
#### drive.name ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Volume name
```javascript
["drive.name"]
```
#### drive.size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Volume size
```javascript
["drive.size"]
```
#### drive.used ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Volume space used
```javascript
["drive.used"]
```
#### drive.free ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Volume free space
```javascript
["drive.free"]
```
#### drive.mount ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Mount volume
```javascript
["drive.mount"]
```
#### drive.unmount ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Unmount volume
```javascript
["drive.unmount"]
```
#### drive.format ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Format volume
```javascript
["drive.format"]
```
#### path.drive ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get volume from path
```javascript
["path.drive"]
```
#### path.dir ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get directory from path
```javascript
["path.dir"]
```
#### path.file ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get file from path
```javascript
["path.file"]
```
#### path.name ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get filename from path
```javascript
["path.name"]
```
#### path.extension ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get extension from path
```javascript
["path.extension"]
```
#### path.extension.strip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Trim extension from path
```javascript
["path.extension.strip"]
```

### cloud

#### cloud.file ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File server
```javascript
["cloud.file"]
```
#### cloud.web ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Web server
```javascript
["cloud.web"]
```
#### cloud.api ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
API server
```javascript
["cloud.api"]
```
#### cloud.socket ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Socket server
```javascript
["cloud.socket"]
```
#### cloud.websocket ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Websocket server
```javascript
["cloud.websocket"]
```
#### cloud.mail ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Mail server
```javascript
["cloud.mail"]
```
#### cloud.game ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Game server
```javascript
["cloud.game"]
```
#### cloud.social ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Social server
```javascript
["cloud.social"]
```
#### cloud.live ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Streaming server
```javascript
["cloud.live"]
```

### bot

#### bot.telegram ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Telegram bot
```javascript
["bot.telegram"]
```
#### bot.wechat ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Wechat bot
```javascript
["bot.wechat"]
```
#### bot.x ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
X bot
```javascript
["bot.x"]
```
#### bot.youtube ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
YouTube bot
```javascript
["bot.youtube"]
```
#### bot.tiktok ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
TikTok bot
```javascript
["bot.tiktok"]
```
#### bot.steam ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Steam bot
```javascript
["bot.steam"]
```
#### bot.binance ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Binance bot
```javascript
["bot.binance"]
```
#### bot.ib ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Interactive Brokers bot
```javascript
["bot.ib"]
```

### request

#### request ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Web request
```javascript
["request"]
```
#### request.post ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Post Web request
```javascript
["request.post"]
```
#### request.put ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Put Web request
```javascript
["request.put"]
```
#### request.delete ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Delete Web request
```javascript
["request.delete"]
```
#### request.head ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Head Web request
```javascript
["request.head"]
```

### cookie

#### cookie ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get Web cookies
```javascript
["cookie"]
```
#### cookie.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Delete Web cookies
```javascript
["cookie.remove"]
```

### sql

#### sql ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL query
```javascript
["sql"]
```
#### sql.connect ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Connect to SQL server
```javascript
["sql.connect"]
```
#### sql.disconnet ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Disconnect from SQL server
```javascript
["sql.disconnet"]
```
#### sql.user ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL user
```javascript
["sql.user"]
```
#### sql.user.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL user list
```javascript
["sql.user.list"]
```
#### sql.user.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL remove user
```javascript
["sql.user.remove"]
```
#### sql.db ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL database
```javascript
["sql.db"]
```
#### sql.db.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL database list
```javascript
["sql.db.list"]
```
#### sql.db.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL remove database
```javascript
["sql.db.remove"]
```
#### sql.db.size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL database size
```javascript
["sql.db.size"]
```
#### sql.table ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL table
```javascript
["sql.table"]
```
#### sql.table.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL table list
```javascript
["sql.table.list"]
```
#### sql.table.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL remove table
```javascript
["sql.table.remove"]
```
#### sql.field ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL field
```javascript
["sql.field"]
```
#### sql.field.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL field list
```javascript
["sql.field.list"]
```
#### sql.field.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL remove field
```javascript
["sql.field.remove"]
```
#### sql.index ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL index
```javascript
["sql.index"]
```
#### sql.index.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL index list
```javascript
["sql.index.list"]
```
#### sql.index.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL remove index
```javascript
["sql.index.remove"]
```
#### sql.function ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL function
```javascript
["sql.function"]
```
#### sql.function.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL function list
```javascript
["sql.function.list"]
```
#### sql.function.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL remove function
```javascript
["sql.function.remove"]
```
#### sql.view ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL view
```javascript
["sql.view"]
```
#### sql.view.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL view list
```javascript
["sql.view.list"]
```
#### sql.view.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL remove a view
```javascript
["sql.view.remove"]
```
#### sql.get ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL get one result
```javascript
["sql.get"]
```
#### sql.all ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL get all results
```javascript
["sql.all"]
```
#### sql.cursor ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL cursor
```javascript
["sql.cursor"]
```
#### sql.transaction ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL start transaction
```javascript
["sql.transaction"]
```
#### sql.commit ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL send transaction
```javascript
["sql.commit"]
```
#### sql.rollback ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
SQL cancel transaction
```javascript
["sql.rollback"]
```

### os

#### os.name ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Operating system name
```javascript
["os.name"]
```
#### os.version ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Operating system version
```javascript
["os.version"]
```
#### os.username ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
User name
```javascript
["os.username"]
```
#### os.desktop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it’s desktop
```javascript
["os.desktop"]
```
#### os.mobile ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it’s mobile device
```javascript
["os.mobile"]
```
#### os.web ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it’s Web
```javascript
["os.web"]
```
#### os.windows ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it’s Windows
```javascript
["os.windows"]
```
#### os.macos ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it's macOS
```javascript
["os.macos"]
```
#### os.ios ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it's iOS
```javascript
["os.ios"]
```
#### os.ipados ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it's iPadOS
```javascript
["os.ipados"]
```
#### os.watchos ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it's watchOS
```javascript
["os.watchos"]
```
#### os.tvos ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it's tvOS
```javascript
["os.tvos"]
```
#### os.android ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it's Android
```javascript
["os.android"]
```
#### os.nix ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check that it’s Unix-like
```javascript
["os.nix"]
```

### device

#### cpu.name ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Processor name
```javascript
["cpu.name"]
```
#### cpu.cores ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Number of processor cores
```javascript
["cpu.cores"]
```
#### memory.size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Memory size
```javascript
["memory.size"]
```
#### memory.free ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Memory Free
```javascript
["memory.free"]
```
#### memory.used ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Memory used
```javascript
["memory.used"]
```
#### memory.available ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Memory available
```javascript
["memory.available"]
```

### gps

#### gps ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get GPS coordinates
```javascript
["gps"]
```

### sensor

#### speed ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get speed
```javascript
["speed"]
```
#### tilt ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get tilt
```javascript
["tilt"]
```
#### compass ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get compass direction
```javascript
["compass"]
```
#### motion ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get motion type
```javascript
["motion"]
```

### camera

#### camera ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get camera image
```javascript
["camera"]
```
#### gallery ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get gallery image
```javascript
["gallery"]
```

### contacts

#### contacts ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get contacts
```javascript
["contacts"]
```

### calendar

#### calendar ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get calendar
```javascript
["calendar"]
```

### health

#### health ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get health data
```javascript
["health"]
```

### flashlight

#### flashlight ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Flashlight
```javascript
["flashlight"]
```

### mic

#### mic ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Microphone
```javascript
["mic"]
```

### notification

#### notification ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Receive notifications
```javascript
["notification"]
```
#### notification.token ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Notification token
```javascript
["notification.token"]
```
#### notification.send ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Send notification
```javascript
["notification.send"]
```

### key

#### key ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Assign key action
```javascript
["key"]
```
#### key.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Delete a key action
```javascript
["key.remove"]
```
#### key.press ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Start a key action
```javascript
["key.press"]
```
#### key.enable ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Enable key action
```javascript
["key.enable"]
```
#### key.disable ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Disable key action
```javascript
["key.disable"]
```

### keyboard

#### keyboard ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
On-screen keyboard
```javascript
["keyboard"]
```
#### keyboard.height ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Screen keyboard height
```javascript
["keyboard.height"]
```

### mouse

#### mouse ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Show mouse
```javascript
["mouse"]
```
#### mouse.hide ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hide mouse
```javascript
["mouse.hide"]
```
#### mouse.lock ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Lock mouse
```javascript
["mouse.lock"]
```
#### mouse.capture ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Capture mouse
```javascript
["mouse.capture"]
```
#### mouse.confine ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Limit mouse movement
```javascript
["mouse.confine"]
```
#### mouse.position ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get mouse coordinates
```javascript
["mouse.position"]
```
#### mouse.shape ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Mouse pointer shape
```javascript
["mouse.shape"]
```

### gamepad

#### gamepad.axis ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Gamepad stick deflection
```javascript
["gamepad.axis"]
```
#### gamepad.vibrate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Gamepad vibration
```javascript
["gamepad.vibrate"]
```

### clipboard

#### clipboard ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Clipboard
```javascript
["clipboard"]
```
#### clipboard.clear ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Clear clipboard
```javascript
["clipboard.clear"]
```

### voice

#### voice ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read text with voice
```javascript
["voice"]
```
#### voice.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Voice list
```javascript
["voice.list"]
```
#### voice.stop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Stop text reading
```javascript
["voice.stop"]
```
#### voice.pause ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Pause / continue text reading
```javascript
["voice.pause"]
```

### convert

#### convert ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Convert from one format to another
```javascript
["convert"]
```

### image

#### image ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create image
```javascript
["image"]
```
#### image.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read image from file
```javascript
["image.read"]
```
#### image.write ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Write image to file
```javascript
["image.write"]
```
#### image.size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Resize image
```javascript
["image.size"]
```
#### image.crop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Crop image
```javascript
["image.crop"]
```
#### image.square ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Crop image to square
```javascript
["image.square"]
```
#### image.rotate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Rotate image
```javascript
["image.rotate"]
```
#### image.flip.h ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Reflect image horizontally
```javascript
["image.flip.h"]
```
#### image.flip.v ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Reflect image vertically
```javascript
["image.flip.v"]
```
#### image.tint ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Tint the image
```javascript
["image.tint"]
```
#### image.gray ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Convert image to grayscale
```javascript
["image.gray"]
```
#### image.text ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add text to image
```javascript
["image.text"]
```
#### image.image ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add image to image
```javascript
["image.image"]
```
#### image.draw ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add drawing to image
```javascript
["image.draw"]
```

### video

#### video ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create video
```javascript
["video"]
```
#### video.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read video from file
```javascript
["video.read"]
```
#### video.write ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Write video to file
```javascript
["video.write"]
```
#### video.size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Video size
```javascript
["video.size"]
```
#### video.rate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Video frame rate
```javascript
["video.rate"]
```
#### video.rotate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Rotate video
```javascript
["video.rotate"]
```
#### video.flip.h ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Reflect video horizontally
```javascript
["video.flip.h"]
```
#### video.flip.v ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Reflect video vertically
```javascript
["video.flip.v"]
```
#### video.clip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Video clip
```javascript
["video.clip"]
```
#### video.speed ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Video speed
```javascript
["video.speed"]
```
#### video.reverse ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Change video direction
```javascript
["video.reverse"]
```
#### video.text ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add text to video
```javascript
["video.text"]
```
#### video.image ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add image to video
```javascript
["video.image"]
```
#### video.sound ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add sound to video
```javascript
["video.sound"]
```
#### video.video ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add video to video
```javascript
["video.video"]
```

### model

#### model ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create 3D model
```javascript
["model"]
```
#### model.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read 3D model from file
```javascript
["model.read"]
```
#### model.write ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Write 3D model to file
```javascript
["model.write"]
```
#### model.animate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Animate 3D model
```javascript
["model.animate"]
```
#### model.texture ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Apply texture to 3D model
```javascript
["model.texture"]
```

### sound

#### sound ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create sound
```javascript
["sound"]
```
#### sound.read ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Read sound from file
```javascript
["sound.read"]
```
#### sound.write ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Write sound to file
```javascript
["sound.write"]
```
#### sound.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Current played sounds
```javascript
["sound.list"]
```
#### sound.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remove sound
```javascript
["sound.remove"]
```
#### sound.volume ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Sound volume
```javascript
["sound.volume"]
```
#### sound.speed ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Sound playback speed
```javascript
["sound.speed"]
```
#### sound.clip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Sound clip
```javascript
["sound.clip"]
```
#### sound.sound ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add sound to sound
```javascript
["sound.sound"]
```

### music

#### music ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add music
```javascript
["music"]
```
#### music.stop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Stop music
```javascript
["music.stop"]
```
#### music.pause ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Pause / continue music
```javascript
["music.pause"]
```
#### music.volume ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Music sound volume
```javascript
["music.volume"]
```

### volume

#### volume ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Master volume
```javascript
["volume"]
```

### screen

#### screen.count ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Number of screens
```javascript
["screen.count"]
```
#### screen.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
List of screens
```javascript
["screen.list"]
```
#### screen.info ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Screen information
```javascript
["screen.info"]
```
#### size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Screen size
```javascript
["size"]
```
#### orientation ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Screen orientation
```javascript
["orientation"]
```
#### landscape ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Landscape orientation
```javascript
["landscape"]
```
#### portrait ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Portrait orientation
```javascript
["portrait"]
```
#### rate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Screen frame rate
```javascript
["rate"]
```
#### pixel ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get screen pixel color
```javascript
["pixel"]
```
#### symbol ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Get screen symbol
```javascript
["symbol"]
```
#### dpi ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Dots per inch
```javascript
["dpi"]
```
#### dark ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Dark mode
```javascript
["dark"]
```
#### touch ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Touchscreen
```javascript
["touch"]
```
#### screenshot ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Screenshot
```javascript
["screenshot"]
```
#### screen.record ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Record screen
```javascript
["screen.record"]
```
#### screen.stop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Stop screen recording
```javascript
["screen.stop"]
```

### ui

#### ui ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI element
```javascript
["ui"]
```
#### bg ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Background
```javascript
["bg"]
```
#### show ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Show UI
```javascript
["show"]
```
#### hide ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Hide UI
```javascript
["hide"]
```
#### visible ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI visibility
```javascript
["visible"]
```
#### enable ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Enable UI
```javascript
["enable"]
```
#### disable ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Disable UI
```javascript
["disable"]
```
#### enabled ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check if UI is enabled
```javascript
["enabled"]
```
#### focus ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Move focus to UI
```javascript
["focus"]
```
#### scale ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Scale UI
```javascript
["scale"]
```
#### ui.text ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI text
```javascript
["ui.text"]
```
#### ui.image ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI image
```javascript
["ui.image"]
```
#### ui.button ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI button
```javascript
["ui.button"]
```
#### ui.divider ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI separator
```javascript
["ui.divider"]
```
#### ui.video ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI video
```javascript
["ui.video"]
```
#### ui.select ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI selection
```javascript
["ui.select"]
```
#### ui.switch ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI switch
```javascript
["ui.switch"]
```
#### ui.progress ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI progress bar
```javascript
["ui.progress"]
```
#### ui.slider ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI slider
```javascript
["ui.slider"]
```
#### ui.edit ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI text editor
```javascript
["ui.edit"]
```
#### ui.chart ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI chart
```javascript
["ui.chart"]
```
#### ui.split.h ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI horizontal separator
```javascript
["ui.split.h"]
```
#### ui.split.v ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI vertical separator
```javascript
["ui.split.v"]
```
#### ui.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI list
```javascript
["ui.list"]
```
#### ui.tile ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI tile
```javascript
["ui.tile"]
```
#### ui.color ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI color
```javascript
["ui.color"]
```
#### ui.date ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI date
```javascript
["ui.date"]
```
#### ui.drop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI drop down content
```javascript
["ui.drop"]
```
#### ui.menu ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI menu
```javascript
["ui.menu"]
```
#### ui.menu.context ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
UI context menu
```javascript
["ui.menu.context"]
```

### window

#### window ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create window
```javascript
["window"]
```
#### window.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window list
```javascript
["window.list"]
```
#### window.info ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window information
```javascript
["window.info"]
```
#### title ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window title
```javascript
["title"]
```
#### icon ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window icon
```javascript
["icon"]
```
#### size ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window size
```javascript
["size"]
```
#### size.max ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Maximum window size
```javascript
["size.max"]
```
#### size.min ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Minimum window size
```javascript
["size.min"]
```
#### position ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window position
```javascript
["position"]
```
#### direction ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window text direction
```javascript
["direction"]
```
#### attention ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window attention
```javascript
["attention"]
```
#### top ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Top of all windows
```javascript
["top"]
```
#### foreground ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Foreground window
```javascript
["foreground"]
```
#### unfocusable ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Do not take the focus of the window
```javascript
["unfocusable"]
```
#### unresizable ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Do not resize window
```javascript
["unresizable"]
```
#### center ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Center the window on the screen
```javascript
["center"]
```
#### fullscreen ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Full screen window
```javascript
["fullscreen"]
```
#### drop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drop content to window
```javascript
["drop"]
```
#### border ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window border
```javascript
["border"]
```
#### maximized ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Maximize window
```javascript
["maximized"]
```
#### minimized ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Minimize window
```javascript
["minimized"]
```
#### exclusive ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Make window exclusive
```javascript
["exclusive"]
```
#### vsync ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Vertical window synchronization
```javascript
["vsync"]
```
#### fps ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Window FPS
```javascript
["fps"]
```

### dialog

#### dialog.file ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
File selection
```javascript
["dialog.file"]
```
#### dialog.color ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Color selection
```javascript
["dialog.color"]
```
#### dialog.date ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Date selection
```javascript
["dialog.date"]
```
#### dialog.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Select from list
```javascript
["dialog.list"]
```

### effect

#### effect ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add effect
```javascript
["effect"]
```
#### effect.list ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
List of effects
```javascript
["effect.list"]
```
#### effect.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remove effect
```javascript
["effect.remove"]
```

### game

#### vn ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create visual novel
```javascript
["vn"]
```
#### 2d ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create 2D game
```javascript
["2d"]
```
#### 3d ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create 3D game
```javascript
["3d"]
```
#### menu ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create game menu
```javascript
["menu"]
```
#### say ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Say text
```javascript
["say"]
```
#### say.skip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Skip text
```javascript
["say.skip"]
```
#### route ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Offer to select a root
```javascript
["route"]
```
#### route.remove ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Remove root selection
```javascript
["route.remove"]
```
#### route.check ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Check root
```javascript
["route.check"]
```
#### route.select ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Select root
```javascript
["route.select"]
```
#### route.repeat ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Repeat root selection
```javascript
["route.repeat"]
```
#### route.skip ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Skip root selection
```javascript
["route.skip"]
```
#### character ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create a character
```javascript
["character"]
```
#### come ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Character arrived
```javascript
["come"]
```
#### leave ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Character left
```javascript
["leave"]
```
#### change ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Character changed
```javascript
["change"]
```
#### object ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Add an object to the map
```javascript
["object"]
```
#### shoot ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Character shot
```javascript
["shoot"]
```
#### move ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Character movement
```javascript
["move"]
```
#### jump ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Jump
```javascript
["jump"]
```
#### crouch ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Crouch
```javascript
["crouch"]
```
#### drop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drop
```javascript
["drop"]
```
#### look ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Look around
```javascript
["look"]
```
#### hud ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Interface
```javascript
["hud"]
```
#### hud.map ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Map
```javascript
["hud.map"]
```
#### hud.inventory ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Inventory
```javascript
["hud.inventory"]
```
#### snd ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Spatial sound
```javascript
["snd"]
```
#### light ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Spatial light
```javascript
["light"]
```
#### cam ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Spatial camera
```javascript
["cam"]
```

### ai

#### ai.chat ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Communicate with AI
```javascript
["ai.chat"]
```
#### ai.image ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI image
```javascript
["ai.image"]
```
#### ai.video ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI video
```javascript
["ai.video"]
```
#### ai.music ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI music
```javascript
["ai.music"]
```
#### ai.sound ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI sound
```javascript
["ai.sound"]
```
#### ai.say ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI speech
```javascript
["ai.say"]
```
#### ai.2d ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI 2D asset
```javascript
["ai.2d"]
```
#### ai.3d ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI 3D asset
```javascript
["ai.3d"]
```
#### ai.character ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Create AI character
```javascript
["ai.character"]
```
#### ai.clean ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Clean up image with AI
```javascript
["ai.clean"]
```
#### ai.resize ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Resize image with AI
```javascript
["ai.resize"]
```
#### ai.color ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Colorize image with AI
```javascript
["ai.color"]
```
#### ai.style ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Change image style with AI
```javascript
["ai.style"]
```
#### ai.translate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Translate text with AI
```javascript
["ai.translate"]
```
#### ai.recognize.text ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Recognize text with AI
```javascript
["ai.recognize.text"]
```
#### ai.recognize.image ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Recognize image with AI
```javascript
["ai.recognize.image"]
```
#### ai.recognize.video ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Recognize video with AI
```javascript
["ai.recognize.video"]
```
#### ai.recognize.motion ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Recognize motion with AI
```javascript
["ai.recognize.motion"]
```
#### ai.capture.voice ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Capture voice with AI
```javascript
["ai.capture.voice"]
```
#### ai.capture.face ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Capture facial expressions with AI
```javascript
["ai.capture.face"]
```
#### ai.capture.motion ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Capture motion with AI
```javascript
["ai.capture.motion"]
```

### social

#### social.signin ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Authorization
```javascript
["social.signin"]
```
#### social.signup ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Registration
```javascript
["social.signup"]
```
#### social.signout ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Logout
```javascript
["social.signout"]
```
#### social.restore ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Restore login
```javascript
["social.restore"]
```
#### social ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Social content
```javascript
["social"]
```
#### social.send ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Send content
```javascript
["social.send"]
```
#### social.buy ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Purchase
```javascript
["social.buy"]
```

### tech

#### light.on ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Turn lamp on
```javascript
["light.on"]
```
#### light.off ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Turn lamp off
```javascript
["light.off"]
```
#### power.on ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Power on
```javascript
["power.on"]
```
#### power.off ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Turn power off
```javascript
["power.off"]
```
#### power.timer ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Set timer for power
```javascript
["power.timer"]
```
#### lock.open ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Open the lock
```javascript
["lock.open"]
```
#### lock.close ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Close the lock
```javascript
["lock.close"]
```
#### lock.code ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Set the code on the lock
```javascript
["lock.code"]
```
#### dron.move ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone movement
```javascript
["dron.move"]
```
#### dron.up ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Raise the drone
```javascript
["dron.up"]
```
#### dron.down ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Lower the drone
```javascript
["dron.down"]
```
#### dron.left ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Move the drone to the left
```javascript
["dron.left"]
```
#### dron.right ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Move the drone to the right
```javascript
["dron.right"]
```
#### dron.go ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Move the drone forward
```javascript
["dron.go"]
```
#### dron.stop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Stop drone movement
```javascript
["dron.stop"]
```
#### dron.jump ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Jump the drone
```javascript
["dron.jump"]
```
#### dron.crouch ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Crouch the drone
```javascript
["dron.crouch"]
```
#### dron.open ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Open the drone
```javascript
["dron.open"]
```
#### dron.close ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Close the drone
```javascript
["dron.close"]
```
#### dron.rotate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Turn the drone
```javascript
["dron.rotate"]
```
#### dron.camera ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone camera
```javascript
["dron.camera"]
```
#### dron.camera.rotate ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Rotate drone camera
```javascript
["dron.camera.rotate"]
```
#### dron.camera.on ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Turn drone camera on
```javascript
["dron.camera.on"]
```
#### dron.camera.off ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Turn drone camera off
```javascript
["dron.camera.off"]
```
#### dron.camera.record ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Record drone camera video
```javascript
["dron.camera.record"]
```
#### dron.camera.record.stop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Stop drone camera recording
```javascript
["dron.camera.record.stop"]
```
#### dron.hand.open ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Open the drone arm
```javascript
["dron.hand.open"]
```
#### dron.hand.close ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Close the drone arm
```javascript
["dron.hand.close"]
```
#### dron.hand.move ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone hand movement
```javascript
["dron.hand.move"]
```
#### dron.hand.gesture ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone hand gesture
```javascript
["dron.hand.gesture"]
```
#### dron.sound ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone speaker
```javascript
["dron.sound"]
```
#### dron.volume ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone speaker sound volume
```javascript
["dron.volume"]
```
#### dron.mic ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone microphone
```javascript
["dron.mic"]
```
#### dron.mic.on ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone microphone on
```javascript
["dron.mic.on"]
```
#### dron.mic.off ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone microphone off
```javascript
["dron.mic.off"]
```
#### dron.mic.record ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Drone microphone audio recording
```javascript
["dron.mic.record"]
```
#### dron.mic.record.stop ⌜<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/scroll.svg" width="14" height="14" title="vapp"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/lock.svg" width="14" height="14" title="safe"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/python.svg" width="14" height="14" title="python"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/js.svg" width="14" height="14" title="javascript"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/apple.svg" width="14" height="14" title="swift"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/android.svg" width="14" height="14" title="kotlin"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/gamepad.svg" width="14" height="14" title="godot"> <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/c.svg" width="14" height="14" title="c++">⌟ 
Stop recording drone microphone audio
```javascript
["dron.mic.record.stop"]
```

## V O I D format
**⌜ V O I D format ⌟** is the data format that inherits the best features of [**JSON**](https://en.wikipedia.org/wiki/JSON), [**YAML**](https://en.wikipedia.org/wiki/YAML), [**CSV**](https://en.wikipedia.org/wiki/Comma-separated_values) and [**plain text**](https://en.wikipedia.org/wiki/Plain_text) formats. Makes it easier to write and read data, both by human and by program. The format simplifies data creation by removing the use of unnecessary quotation marks, brackets, colons, commas and other symbols. It is possible to combine **text** and **binary** data.

```
extension
  .void
  .txt
influenced by
  json
  yaml
  csv
  plain text
mime type
  application/void
value type
  text
  number
  boolean
  list
  dictionary
  null
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
```

```
void [1 2 3
.
void.decode "[1 2 3
.
void.write path/to/file.void
void.read path/to/file.void
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
"\n\t\r\b\u1234\"\\"
```

</td>
<td>

```json
"\n\t\r\b\u1234\"\\"
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
h0A
```

</td>
<td>

```json
10
```

</td>
</tr>

<tr>
<td>

```
b1010
```

</td>
<td>

```json
10
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
null
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
null
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
middle dot (·)
  base64 auto decoding
    b64·ViBPIEkgRCBmb3JtYXQ=
  base64 + gzip
    b64·eNoLU/BX8FRwUUjLL8pNLAEAG0QEPA==
  size before binary data
    3·☺☺☺
```

</td>
<td>

```json
{
  "middle dot (·)": {
    "base64 auto decoding": "ViBPIEkgRCBmb3JtYXQ=",
    "base64 + gzip": "eNoLU/BX8FRwUUjLL8pNLAEAG0QEPA==",
    "size before binary data": "\u0001\u0001\u0001"
  }
}
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
  "\n\t\r\b\u1234\"\\"
int
  123 000
float
  1.23
bool
  true
empty
  null
list
  text
  1
  true
  false
  null
dictionary
  name 1
    true
  name 2
    true
code
  [. "Hi World :D
  [= var 123
  [. {var}
base64
  b64·ViBPIEkgRCBmb3JtYXQ=
binary
  3·☺☺☺
```

</td>
<td>

```json
{
  "text": "text",
  "multiline text": "multiline\ntext",
  "text in a line": "textinaline",
  "escape": "\n\t\r\b\u1234\"\\",
  "int": 123000,
  "float": 1.23,
  "bool": true,
  "empty": null,
  "list": ["text", 1, true, false, null],
  "dictionary": {
    "name 1": true,
    "name 2": true
  },
  "code": [
    [".", "Hi World :D"],
    ["=", "var", 123],
    [".", "{var}"]
  ],
  "base64": "ViBPIEkgRCBmb3JtYXQ="
  "binary": "\u0001\u0001\u0001"
}
```

</td>
</tr>

</table>

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create applications and games.

## V O I D ideology
**[⌜V O I D⌟](https://github.com/voidspawner/void.ideology)**  is not only about compact technologies, but also an **ideology** that shows where these technologies are taking us.

## V O I D work
> [!IMPORTANT]
> By adding your code to a repository, you transfer the rights to the uploaded code to the owner of that repository **V O I D spawner**.

Find out current **tasks** and **payment** at [**voidsp.com/task**](https://voidsp.com/task)
