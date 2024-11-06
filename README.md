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
Count of actions: 604
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

#### get
Get value
```javascript
["get"]
```
#### set
Set value
```javascript
["set"]
```
#### remove
Delete value
```javascript
["remove"]
```
#### type
Get value type
```javascript
["type"]
```
#### bool
Convert value to boolean
```javascript
["bool"]
```
#### number
Translate value to a number
```javascript
["number"]
```
#### text
Translate value to text
```javascript
["text"]
```
#### list
Translate value into a list
```javascript
["list"]
```
#### alias
Assign an alias to an action
```javascript
["alias"]
```
#### compare
Compare values
```javascript
["compare"]
```

### expression

#### +
Add
```javascript
["+"]
```
#### -
Subtract
```javascript
["-"]
```
#### *
Multiply
```javascript
["*"]
```
#### /
Divide
```javascript
["/"]
```
#### %
Remainder of division
```javascript
["%"]
```
#### **
Elevate
```javascript
["**"]
```
#### !
NOT bitwise operator
```javascript
["!"]
```
#### &
AND bitwise operator
```javascript
["&"]
```
#### |
OR bitwise operator
```javascript
["|"]
```
#### ^
XOR bitwise operator
```javascript
["^"]
```
#### >>
Right shift
```javascript
[">>"]
```
#### <<
Left shift
```javascript
["<<"]
```
#### +=
Add to value
```javascript
["+="]
```
#### -=
Subtract from value
```javascript
["-="]
```
#### *=
Multiply the value
```javascript
["*="]
```
#### /=
Divide the value
```javascript
["/="]
```
#### %=
Residue from dividing the value
```javascript
["%="]
```
#### **=
Increment the value
```javascript
["**="]
```
#### !=
NOT bitwise operator of the value
```javascript
["!="]
```
#### &=
AND bitwise operator of the value
```javascript
["&="]
```
#### |=
OR bitwise operator of the value
```javascript
["|="]
```
#### ^=
XOR bitwise operator of the value
```javascript
["^="]
```
#### >>=
Shift to the right of the value
```javascript
[">>="]
```
#### <<=
Shift to the left of the value
```javascript
["<<="]
```
#### not
Negation (inversion)
```javascript
["not"]
```
#### and
Conjunction (and)
```javascript
["and"]
```
#### or
Disjunction (or)
```javascript
["or"]
```
#### xor
Exclusive disjunction (exclusive or)
```javascript
["xor"]
```
#### in
A value in an array or a name in a dictionary
```javascript
["in"]
```
#### not in
Value not in array or name not in dictionary
```javascript
["not in"]
```
#### is
Value type match
```javascript
["is"]
```
#### not is
Value type mismatch
```javascript
["not is"]
```

### control

#### ?
IF check
```javascript
["?"]
```
#### ??
MATCH check
```javascript
["??"]
```
#### o
FOR, WHILE loop
```javascript
["o"]
```
#### x
Exit loop BREAK
```javascript
["x"]
```
#### >>>
Continue loop CONTINUE
```javascript
[">>>"]
```
#### <<<
Repeat loop iteration
```javascript
["<<<"]
```
#### _
Return action value RETURN
```javascript
["_"]
```
#### .
Print text
```javascript
["."]
```
#### ..
Print text without a new line
```javascript
[".."]
```
#### ...
Enter text
```javascript
["..."]
```
#### action
Execute action
```javascript
["action"]
```
#### action.open
Execute an action from a file
```javascript
["action.open"]
```
#### X
End vapp
```javascript
["X"]
```
#### xx
Error
```javascript
["xx"]
```
#### open
Execute system action
```javascript
["open"]
```
#### shell
Execute a command line command
```javascript
["shell"]
```
#### shell.open
Open a terminal and execute the command
```javascript
["shell.open"]
```
#### code
Execute native code
```javascript
["code"]
```
#### python
Execute Python code
```javascript
["python"]
```
#### compile
Compile code for a specific platform
```javascript
["compile"]
```
#### i
Info logging
```javascript
["i"]
```
#### w
Warning logging
```javascript
["w"]
```
#### e
Error logging
```javascript
["e"]
```
#### d
Debug logging
```javascript
["d"]
```
#### t
Time logging
```javascript
["t"]
```
#### export
Export vapp for selected platforms
```javascript
["export"]
```
#### update
Update script
```javascript
["update"]
```
#### test
Test script
```javascript
["test"]
```
#### help
Display language hint
```javascript
["help"]
```
#### debug
Display debug information
```javascript
["debug"]
```
#### debug.fps
Display FPS
```javascript
["debug.fps"]
```

### text

#### lower
Convert text to lower case
```javascript
["lower"]
```
#### upper
Convert text to uppercase
```javascript
["upper"]
```
#### starts
Starts with text
```javascript
["starts"]
```
#### ends
Ends with text
```javascript
["ends"]
```
#### strip
Trim text
```javascript
["strip"]
```
#### strip.start
Trim the beginning of text
```javascript
["strip.start"]
```
#### strip.end
Trim the end of text
```javascript
["strip.end"]
```
#### replace
Replace text
```javascript
["replace"]
```
#### find
Find position in text
```javascript
["find"]
```
#### similar
Compare texts
```javascript
["similar"]
```
#### part
Get a part of text
```javascript
["part"]
```
#### split
Split text
```javascript
["split"]
```
#### join
Join text
```javascript
["join"]
```
#### regex
Find in text using regular expression
```javascript
["regex"]
```
#### regex.replace
Replace text using a regular expression
```javascript
["regex.replace"]
```
#### escape
Escape text
```javascript
["escape"]
```
#### escape.html
Escape HTML text
```javascript
["escape.html"]
```
#### escape.sql
Escape SQL text
```javascript
["escape.sql"]
```
#### escape.url
Escape text URL
```javascript
["escape.url"]
```
#### escape.json
Escape text JSON
```javascript
["escape.json"]
```
#### escape.void
Escape text V O I D
```javascript
["escape.void"]
```
#### unescape
Unescape text
```javascript
["unescape"]
```
#### unescape.html
Unescape HTML text
```javascript
["unescape.html"]
```
#### unescape.sql
Unescape text SQL
```javascript
["unescape.sql"]
```
#### unescape.url
Unescape text URL
```javascript
["unescape.url"]
```
#### unescape.json
Unescape JSON text
```javascript
["unescape.json"]
```
#### unescape.void
Unescape V O I D text
```javascript
["unescape.void"]
```
#### date
Convert text to timestamp, or timestamp to text
```javascript
["date"]
```
#### letters
Number of letters in the text
```javascript
["letters"]
```
#### words
Number of words in the text
```javascript
["words"]
```
#### sentences
Number of sentences in the text
```javascript
["sentences"]
```
#### lines
Number of lines in the text
```javascript
["lines"]
```

### list

#### push
Add to list
```javascript
["push"]
```
#### pop
Extract from the list
```javascript
["pop"]
```
#### reverse
Invert order in the list
```javascript
["reverse"]
```
#### shuffle
Shuffle the list
```javascript
["shuffle"]
```
#### sort
Sort the list
```javascript
["sort"]
```
#### fill
Fill the list
```javascript
["fill"]
```
#### map
Map the list
```javascript
["map"]
```
#### reduce
Reduce the list
```javascript
["reduce"]
```
#### names
Dictionary or list names
```javascript
["names"]
```
#### values
Dictionary values
```javascript
["values"]
```

### math

#### sin
Sine
```javascript
["sin"]
```
#### cos
Cosine
```javascript
["cos"]
```
#### tan
Tangent
```javascript
["tan"]
```
#### sinh
Hyperbolic sine
```javascript
["sinh"]
```
#### cosh
Hyperbolic cosine
```javascript
["cosh"]
```
#### tanh
Hyperbolic tangent
```javascript
["tanh"]
```
#### asin
Arcsine
```javascript
["asin"]
```
#### acos
Arccosine
```javascript
["acos"]
```
#### atan
Arctangent
```javascript
["atan"]
```
#### asinh
Hyperbolic arcsine
```javascript
["asinh"]
```
#### acosh
Hyperbolic arccosine
```javascript
["acosh"]
```
#### atanh
Hyperbolic arctangent
```javascript
["atanh"]
```
#### round
Round a number
```javascript
["round"]
```
#### floor
Round a number down
```javascript
["floor"]
```
#### ceil
Round a number up
```javascript
["ceil"]
```
#### log
Logarithm
```javascript
["log"]
```
#### log.e
Hyperbolic logarithm
```javascript
["log.e"]
```
#### log.n
Natural logarithm
```javascript
["log.n"]
```
#### fa
Factorial
```javascript
["fa"]
```
#### fib
Fibonacci
```javascript
["fib"]
```
#### abs
Absolute value
```javascript
["abs"]
```
#### min
Minimum value
```javascript
["min"]
```
#### max
Maximum value
```javascript
["max"]
```
#### avg
Average value
```javascript
["avg"]
```
#### sum
Sum of values
```javascript
["sum"]
```
#### hex
Hexadecimal value to byte
```javascript
["hex"]
```
#### hex.dec
Hexadecimal value to decimal
```javascript
["hex.dec"]
```
#### bin
Binary value to byte
```javascript
["bin"]
```
#### bin.dec
Binary value to decimal
```javascript
["bin.dec"]
```
#### dec
Decimal value to byte
```javascript
["dec"]
```
#### dec.hex
Decimal value to hexadecimal
```javascript
["dec.hex"]
```
#### dec.bin
Decimal value to binary
```javascript
["dec.bin"]
```
#### rad
Degree to radian
```javascript
["rad"]
```
#### deg
Radian to degree
```javascript
["deg"]
```
#### random
Random value
```javascript
["random"]
```
#### random.reseed
Re-create random seed
```javascript
["random.reseed"]
```
#### random.seed
Get random seed
```javascript
["random.seed"]
```

### time

#### time
Time stamp in microseconds
```javascript
["time"]
```
#### time.ms
Time stamp in milliseconds
```javascript
["time.ms"]
```
#### time.s
Timestamp in seconds
```javascript
["time.s"]
```
#### timer
Set timer
```javascript
["timer"]
```
#### timer.remove
Remove timer
```javascript
["timer.remove"]
```
#### wait
Wait time in seconds
```javascript
["wait"]
```

### crypto

#### encrypt
Encode text
```javascript
["encrypt"]
```
#### decrypt
Decode text
```javascript
["decrypt"]
```
#### hash
Random hash
```javascript
["hash"]
```
#### uuid
Random UUID
```javascript
["uuid"]
```
#### md5
MD5 hash
```javascript
["md5"]
```
#### sha1
SHA1 hash
```javascript
["sha1"]
```
#### sha256
SHA256 hash
```javascript
["sha256"]
```
#### sha512
SHA512 hash
```javascript
["sha512"]
```
#### crc32
CRC32 hash
```javascript
["crc32"]
```
#### base64
Base64 hash
```javascript
["base64"]
```
#### base64.decode
Decode Base64
```javascript
["base64.decode"]
```
#### gzip
Gzip text
```javascript
["gzip"]
```
#### gzip.decode
Decode Gzip
```javascript
["gzip.decode"]
```
#### rsa
Encode text with RSA
```javascript
["rsa"]
```
#### rsa.decode
Decode RSA
```javascript
["rsa.decode"]
```
#### rsa.key.public
Get RSA public key
```javascript
["rsa.key.public"]
```
#### rsa.key.private
Get RSA private key
```javascript
["rsa.key.private"]
```
#### ssl
Encode text with SSL
```javascript
["ssl"]
```
#### ssl.decode
Decode SSL
```javascript
["ssl.decode"]
```
#### ssl.check
Verify SSL
```javascript
["ssl.check"]
```
#### bcrypt
Encode text with Bcrypt
```javascript
["bcrypt"]
```
#### bcrypt.check
Verify Bcrypt
```javascript
["bcrypt.check"]
```

### format

#### void
Encode to V O I D
```javascript
["void"]
```
#### void.decode
Decode V O I D
```javascript
["void.decode"]
```
#### void.read
Read V O I D file
```javascript
["void.read"]
```
#### void.write
Write V O I D file
```javascript
["void.write"]
```
#### json
Encode to JSON
```javascript
["json"]
```
#### json.decode
Decode JSON
```javascript
["json.decode"]
```
#### json.read
Read JSON file
```javascript
["json.read"]
```
#### json.write
Write JSON file
```javascript
["json.write"]
```
#### yaml
Encode YAML
```javascript
["yaml"]
```
#### yaml.decode
Decode YAML
```javascript
["yaml.decode"]
```
#### csv
Encode CSV
```javascript
["csv"]
```
#### csv.decode
Decode CSV
```javascript
["csv.decode"]
```
#### ini
Encode INI
```javascript
["ini"]
```
#### ini.decode
Decode INI
```javascript
["ini.decode"]
```
#### html
Encode HTML
```javascript
["html"]
```
#### html.decode
Decode HTML
```javascript
["html.decode"]
```
#### xml
Encode XML
```javascript
["xml"]
```
#### xml.decode
Decode XML
```javascript
["xml.decode"]
```
#### css
Encode CSS
```javascript
["css"]
```
#### css.decode
Decode CSS
```javascript
["css.decode"]
```

### file

#### file.exists
File exists
```javascript
["file.exists"]
```
#### file.write
Write to file
```javascript
["file.write"]
```
#### file.read
Read file
```javascript
["file.read"]
```
#### file.read.list
Read lines from file
```javascript
["file.read.list"]
```
#### file.remove
Remove file
```javascript
["file.remove"]
```
#### file.move
Move file
```javascript
["file.move"]
```
#### file.copy
Copy file
```javascript
["file.copy"]
```
#### file.rename
Rename file
```javascript
["file.rename"]
```
#### file.info
File information
```javascript
["file.info"]
```
#### file.size
File size
```javascript
["file.size"]
```
#### file.permissions
File permissions
```javascript
["file.permissions"]
```
#### file.readonly
Read-only file
```javascript
["file.readonly"]
```
#### file.hidden
Hidden file
```javascript
["file.hidden"]
```
#### file.modified
File modification time
```javascript
["file.modified"]
```
#### file.sha256
SHA256 file hash
```javascript
["file.sha256"]
```
#### file.crc32
CRC32 file hash
```javascript
["file.crc32"]
```
#### file.base64
Base64 file hash
```javascript
["file.base64"]
```
#### file.zip
Compress a file into a Zip archive
```javascript
["file.zip"]
```
#### file.zip.list
List of files in Zip archive
```javascript
["file.zip.list"]
```
#### file.zip.exists
File exists in Zip archive
```javascript
["file.zip.exists"]
```
#### file.zip.read
Read file from Zip archive
```javascript
["file.zip.read"]
```
#### file.zip.remove
Remove file from Zip archive
```javascript
["file.zip.remove"]
```
#### file.unzip
Extract Zip archive
```javascript
["file.unzip"]
```
#### file.gzip
Compress file with Gzip
```javascript
["file.gzip"]
```
#### file.ungzip
Extract Gzip file
```javascript
["file.ungzip"]
```
#### file.link
Create a symbolic link
```javascript
["file.link"]
```
#### file.link.exists
Symbolic link exists
```javascript
["file.link.exists"]
```
#### file.backup
Backup files
```javascript
["file.backup"]
```
#### dir.exists
Directory exists
```javascript
["dir.exists"]
```
#### dir.create
Create directory
```javascript
["dir.create"]
```
#### dir.copy
Copy directory
```javascript
["dir.copy"]
```
#### dir.move
Move directory
```javascript
["dir.move"]
```
#### dir.rename
Rename directory
```javascript
["dir.rename"]
```
#### dir.remove
Remove directory
```javascript
["dir.remove"]
```
#### dir.list
List of files in a directory
```javascript
["dir.list"]
```
#### dir.clear
Clear directory
```javascript
["dir.clear"]
```
#### dir.info
Directory information
```javascript
["dir.info"]
```
#### dir.size
Directory size
```javascript
["dir.size"]
```
#### dir.permissions
Directory permissions
```javascript
["dir.permissions"]
```
#### dir.readonly
Read-only directory
```javascript
["dir.readonly"]
```
#### dir.hidden
Hidden directory
```javascript
["dir.hidden"]
```
#### dir.modified
Directory modification time
```javascript
["dir.modified"]
```
#### dir.zip
Compress directory
```javascript
["dir.zip"]
```
#### drive.list
List of volumes
```javascript
["drive.list"]
```
#### drive.name
Volume name
```javascript
["drive.name"]
```
#### drive.size
Volume size
```javascript
["drive.size"]
```
#### drive.used
Volume space used
```javascript
["drive.used"]
```
#### drive.free
Volume free space
```javascript
["drive.free"]
```
#### drive.mount
Mount volume
```javascript
["drive.mount"]
```
#### drive.unmount
Unmount volume
```javascript
["drive.unmount"]
```
#### drive.format
Format volume
```javascript
["drive.format"]
```
#### path.drive
Get volume from path
```javascript
["path.drive"]
```
#### path.dir
Get directory from path
```javascript
["path.dir"]
```
#### path.file
Get file from path
```javascript
["path.file"]
```
#### path.name
Get filename from path
```javascript
["path.name"]
```
#### path.extension
Get extension from path
```javascript
["path.extension"]
```
#### path.extension.strip
Trim extension from path
```javascript
["path.extension.strip"]
```

### cloud

#### cloud.file
File server
```javascript
["cloud.file"]
```
#### cloud.web
Web server
```javascript
["cloud.web"]
```
#### cloud.api
API server
```javascript
["cloud.api"]
```
#### cloud.socket
Socket server
```javascript
["cloud.socket"]
```
#### cloud.websocket
Websocket server
```javascript
["cloud.websocket"]
```
#### cloud.mail
Mail server
```javascript
["cloud.mail"]
```
#### cloud.game
Game server
```javascript
["cloud.game"]
```
#### cloud.social
Social server
```javascript
["cloud.social"]
```
#### cloud.live
Streaming server
```javascript
["cloud.live"]
```

### bot

#### bot.telegram
Telegram bot
```javascript
["bot.telegram"]
```
#### bot.wechat
Wechat bot
```javascript
["bot.wechat"]
```
#### bot.x
X bot
```javascript
["bot.x"]
```
#### bot.youtube
YouTube bot
```javascript
["bot.youtube"]
```
#### bot.tiktok
TikTok bot
```javascript
["bot.tiktok"]
```
#### bot.steam
Steam bot
```javascript
["bot.steam"]
```
#### bot.binance
Binance bot
```javascript
["bot.binance"]
```
#### bot.ib
Interactive Brokers bot
```javascript
["bot.ib"]
```

### request

#### request
Web request
```javascript
["request"]
```
#### request.post
Post Web request
```javascript
["request.post"]
```
#### request.put
Put Web request
```javascript
["request.put"]
```
#### request.delete
Delete Web request
```javascript
["request.delete"]
```
#### request.head
Head Web request
```javascript
["request.head"]
```

### cookie

#### cookie
Get Web cookies
```javascript
["cookie"]
```
#### cookie.remove
Delete Web cookies
```javascript
["cookie.remove"]
```

### sql

#### sql
SQL query
```javascript
["sql"]
```
#### sql.connect
Connect to SQL server
```javascript
["sql.connect"]
```
#### sql.disconnet
Disconnect from SQL server
```javascript
["sql.disconnet"]
```
#### sql.user
SQL user
```javascript
["sql.user"]
```
#### sql.user.list
SQL user list
```javascript
["sql.user.list"]
```
#### sql.user.remove
SQL remove user
```javascript
["sql.user.remove"]
```
#### sql.db
SQL database
```javascript
["sql.db"]
```
#### sql.db.list
SQL database list
```javascript
["sql.db.list"]
```
#### sql.db.remove
SQL remove database
```javascript
["sql.db.remove"]
```
#### sql.db.size
SQL database size
```javascript
["sql.db.size"]
```
#### sql.table
SQL table
```javascript
["sql.table"]
```
#### sql.table.list
SQL table list
```javascript
["sql.table.list"]
```
#### sql.table.remove
SQL remove table
```javascript
["sql.table.remove"]
```
#### sql.field
SQL field
```javascript
["sql.field"]
```
#### sql.field.list
SQL field list
```javascript
["sql.field.list"]
```
#### sql.field.remove
SQL remove field
```javascript
["sql.field.remove"]
```
#### sql.index
SQL index
```javascript
["sql.index"]
```
#### sql.index.list
SQL index list
```javascript
["sql.index.list"]
```
#### sql.index.remove
SQL remove index
```javascript
["sql.index.remove"]
```
#### sql.function
SQL function
```javascript
["sql.function"]
```
#### sql.function.list
SQL function list
```javascript
["sql.function.list"]
```
#### sql.function.remove
SQL remove function
```javascript
["sql.function.remove"]
```
#### sql.view
SQL view
```javascript
["sql.view"]
```
#### sql.view.list
SQL view list
```javascript
["sql.view.list"]
```
#### sql.view.remove
SQL remove a view
```javascript
["sql.view.remove"]
```
#### sql.get
SQL get one result
```javascript
["sql.get"]
```
#### sql.all
SQL get all results
```javascript
["sql.all"]
```
#### sql.cursor
SQL cursor
```javascript
["sql.cursor"]
```
#### sql.transaction
SQL start transaction
```javascript
["sql.transaction"]
```
#### sql.commit
SQL send transaction
```javascript
["sql.commit"]
```
#### sql.rollback
SQL cancel transaction
```javascript
["sql.rollback"]
```

### os

#### os.name
Operating system name
```javascript
["os.name"]
```
#### os.version
Operating system version
```javascript
["os.version"]
```
#### os.username
User name
```javascript
["os.username"]
```
#### os.desktop
Check that it’s desktop
```javascript
["os.desktop"]
```
#### os.mobile
Check that it’s mobile device
```javascript
["os.mobile"]
```
#### os.web
Check that it’s Web
```javascript
["os.web"]
```
#### os.windows
Check that it’s Windows
```javascript
["os.windows"]
```
#### os.macos
Check that it's macOS
```javascript
["os.macos"]
```
#### os.ios
Check that it's iOS
```javascript
["os.ios"]
```
#### os.ipados
Check that it's iPadOS
```javascript
["os.ipados"]
```
#### os.watchos
Check that it's watchOS
```javascript
["os.watchos"]
```
#### os.tvos
Check that it's tvOS
```javascript
["os.tvos"]
```
#### os.android
Check that it's Android
```javascript
["os.android"]
```
#### os.nix
Check that it’s Unix-like
```javascript
["os.nix"]
```

### device

#### cpu.name
Processor name
```javascript
["cpu.name"]
```
#### cpu.cores
Number of processor cores
```javascript
["cpu.cores"]
```
#### memory.size
Memory size
```javascript
["memory.size"]
```
#### memory.free
Memory Free
```javascript
["memory.free"]
```
#### memory.used
Memory used
```javascript
["memory.used"]
```
#### memory.available
Memory available
```javascript
["memory.available"]
```

### gps

#### gps
Get GPS coordinates
```javascript
["gps"]
```

### sensor

#### speed
Get speed
```javascript
["speed"]
```
#### tilt
Get tilt
```javascript
["tilt"]
```
#### compass
Get compass direction
```javascript
["compass"]
```
#### motion
Get motion type
```javascript
["motion"]
```

### camera

#### camera
Get camera image
```javascript
["camera"]
```
#### gallery
Get gallery image
```javascript
["gallery"]
```

### contacts

#### contacts
Get contacts
```javascript
["contacts"]
```

### calendar

#### calendar
Get calendar
```javascript
["calendar"]
```

### health

#### health
Get health data
```javascript
["health"]
```

### flashlight

#### flashlight
Flashlight
```javascript
["flashlight"]
```

### mic

#### mic
Microphone
```javascript
["mic"]
```

### notification

#### notification
Receive notifications
```javascript
["notification"]
```
#### notification.token
Notification token
```javascript
["notification.token"]
```
#### notification.send
Send notification
```javascript
["notification.send"]
```

### key

#### key
Assign key action
```javascript
["key"]
```
#### key.remove
Delete a key action
```javascript
["key.remove"]
```
#### key.press
Start a key action
```javascript
["key.press"]
```
#### key.enable
Enable key action
```javascript
["key.enable"]
```
#### key.disable
Disable key action
```javascript
["key.disable"]
```

### keyboard

#### keyboard
On-screen keyboard
```javascript
["keyboard"]
```
#### keyboard.height
Screen keyboard height
```javascript
["keyboard.height"]
```

### mouse

#### mouse
Show mouse
```javascript
["mouse"]
```
#### mouse.hide
Hide mouse
```javascript
["mouse.hide"]
```
#### mouse.lock
Lock mouse
```javascript
["mouse.lock"]
```
#### mouse.capture
Capture mouse
```javascript
["mouse.capture"]
```
#### mouse.confine
Limit mouse movement
```javascript
["mouse.confine"]
```
#### mouse.position
Get mouse coordinates
```javascript
["mouse.position"]
```
#### mouse.shape
Mouse pointer shape
```javascript
["mouse.shape"]
```

### gamepad

#### gamepad.axis
Gamepad stick deflection
```javascript
["gamepad.axis"]
```
#### gamepad.vibrate
Gamepad vibration
```javascript
["gamepad.vibrate"]
```

### clipboard

#### clipboard
Clipboard
```javascript
["clipboard"]
```
#### clipboard.clear
Clear clipboard
```javascript
["clipboard.clear"]
```

### voice

#### voice
Read text with voice
```javascript
["voice"]
```
#### voice.list
Voice list
```javascript
["voice.list"]
```
#### voice.stop
Stop text reading
```javascript
["voice.stop"]
```
#### voice.pause
Pause / continue text reading
```javascript
["voice.pause"]
```

### convert

#### convert
Convert from one format to another
```javascript
["convert"]
```

### image

#### image
Create image
```javascript
["image"]
```
#### image.read
Read image from file
```javascript
["image.read"]
```
#### image.write
Write image to file
```javascript
["image.write"]
```
#### image.size
Resize image
```javascript
["image.size"]
```
#### image.crop
Crop image
```javascript
["image.crop"]
```
#### image.square
Crop image to square
```javascript
["image.square"]
```
#### image.rotate
Rotate image
```javascript
["image.rotate"]
```
#### image.flip.h
Reflect image horizontally
```javascript
["image.flip.h"]
```
#### image.flip.v
Reflect image vertically
```javascript
["image.flip.v"]
```
#### image.tint
Tint the image
```javascript
["image.tint"]
```
#### image.gray
Convert image to grayscale
```javascript
["image.gray"]
```
#### image.text
Add text to image
```javascript
["image.text"]
```
#### image.image
Add image to image
```javascript
["image.image"]
```
#### image.draw
Add drawing to image
```javascript
["image.draw"]
```

### video

#### video
Create video
```javascript
["video"]
```
#### video.read
Read video from file
```javascript
["video.read"]
```
#### video.write
Write video to file
```javascript
["video.write"]
```
#### video.size
Video size
```javascript
["video.size"]
```
#### video.rate
Video frame rate
```javascript
["video.rate"]
```
#### video.rotate
Rotate video
```javascript
["video.rotate"]
```
#### video.flip.h
Reflect video horizontally
```javascript
["video.flip.h"]
```
#### video.flip.v
Reflect video vertically
```javascript
["video.flip.v"]
```
#### video.clip
Video clip
```javascript
["video.clip"]
```
#### video.speed
Video speed
```javascript
["video.speed"]
```
#### video.reverse
Change video direction
```javascript
["video.reverse"]
```
#### video.text
Add text to video
```javascript
["video.text"]
```
#### video.image
Add image to video
```javascript
["video.image"]
```
#### video.sound
Add sound to video
```javascript
["video.sound"]
```
#### video.video
Add video to video
```javascript
["video.video"]
```

### model

#### model
Create 3D model
```javascript
["model"]
```
#### model.read
Read 3D model from file
```javascript
["model.read"]
```
#### model.write
Write 3D model to file
```javascript
["model.write"]
```
#### model.animate
Animate 3D model
```javascript
["model.animate"]
```
#### model.texture
Apply texture to 3D model
```javascript
["model.texture"]
```

### sound

#### sound
Create sound
```javascript
["sound"]
```
#### sound.read
Read sound from file
```javascript
["sound.read"]
```
#### sound.write
Write sound to file
```javascript
["sound.write"]
```
#### sound.list
Current played sounds
```javascript
["sound.list"]
```
#### sound.remove
Remove sound
```javascript
["sound.remove"]
```
#### sound.volume
Sound volume
```javascript
["sound.volume"]
```
#### sound.speed
Sound playback speed
```javascript
["sound.speed"]
```
#### sound.clip
Sound clip
```javascript
["sound.clip"]
```
#### sound.sound
Add sound to sound
```javascript
["sound.sound"]
```

### music

#### music
Add music
```javascript
["music"]
```
#### music.stop
Stop music
```javascript
["music.stop"]
```
#### music.pause
Pause / continue music
```javascript
["music.pause"]
```
#### music.volume
Music sound volume
```javascript
["music.volume"]
```

### volume

#### volume
Master volume
```javascript
["volume"]
```

### screen

#### screen.count
Number of screens
```javascript
["screen.count"]
```
#### screen.list
List of screens
```javascript
["screen.list"]
```
#### screen.info
Screen information
```javascript
["screen.info"]
```
#### size
Screen size
```javascript
["size"]
```
#### orientation
Screen orientation
```javascript
["orientation"]
```
#### landscape
Landscape orientation
```javascript
["landscape"]
```
#### portrait
Portrait orientation
```javascript
["portrait"]
```
#### rate
Screen frame rate
```javascript
["rate"]
```
#### pixel
Get screen pixel color
```javascript
["pixel"]
```
#### symbol
Get screen symbol
```javascript
["symbol"]
```
#### dpi
Dots per inch
```javascript
["dpi"]
```
#### dark
Dark mode
```javascript
["dark"]
```
#### touch
Touchscreen
```javascript
["touch"]
```
#### screenshot
Screenshot
```javascript
["screenshot"]
```
#### screen.record
Record screen
```javascript
["screen.record"]
```
#### screen.stop
Stop screen recording
```javascript
["screen.stop"]
```

### ui

#### ui
UI element
```javascript
["ui"]
```
#### bg
Background
```javascript
["bg"]
```
#### show
Show UI
```javascript
["show"]
```
#### hide
Hide UI
```javascript
["hide"]
```
#### visible
UI visibility
```javascript
["visible"]
```
#### enable
Enable UI
```javascript
["enable"]
```
#### disable
Disable UI
```javascript
["disable"]
```
#### enabled
Check if UI is enabled
```javascript
["enabled"]
```
#### focus
Move focus to UI
```javascript
["focus"]
```
#### scale
Scale UI
```javascript
["scale"]
```
#### ui.text
UI text
```javascript
["ui.text"]
```
#### ui.image
UI image
```javascript
["ui.image"]
```
#### ui.button
UI button
```javascript
["ui.button"]
```
#### ui.divider
UI separator
```javascript
["ui.divider"]
```
#### ui.video
UI video
```javascript
["ui.video"]
```
#### ui.select
UI selection
```javascript
["ui.select"]
```
#### ui.switch
UI switch
```javascript
["ui.switch"]
```
#### ui.progress
UI progress bar
```javascript
["ui.progress"]
```
#### ui.slider
UI slider
```javascript
["ui.slider"]
```
#### ui.edit
UI text editor
```javascript
["ui.edit"]
```
#### ui.chart
UI chart
```javascript
["ui.chart"]
```
#### ui.split.h
UI horizontal separator
```javascript
["ui.split.h"]
```
#### ui.split.v
UI vertical separator
```javascript
["ui.split.v"]
```
#### ui.list
UI list
```javascript
["ui.list"]
```
#### ui.tile
UI tile
```javascript
["ui.tile"]
```
#### ui.color
UI color
```javascript
["ui.color"]
```
#### ui.date
UI date
```javascript
["ui.date"]
```
#### ui.drop
UI drop down content
```javascript
["ui.drop"]
```
#### ui.menu
UI menu
```javascript
["ui.menu"]
```
#### ui.menu.context
UI context menu
```javascript
["ui.menu.context"]
```

### window

#### window
Create window
```javascript
["window"]
```
#### window.list
Window list
```javascript
["window.list"]
```
#### window.info
Window information
```javascript
["window.info"]
```
#### title
Window title
```javascript
["title"]
```
#### icon
Window icon
```javascript
["icon"]
```
#### size
Window size
```javascript
["size"]
```
#### size.max
Maximum window size
```javascript
["size.max"]
```
#### size.min
Minimum window size
```javascript
["size.min"]
```
#### position
Window position
```javascript
["position"]
```
#### direction
Window text direction
```javascript
["direction"]
```
#### attention
Window attention
```javascript
["attention"]
```
#### top
Top of all windows
```javascript
["top"]
```
#### foreground
Foreground window
```javascript
["foreground"]
```
#### unfocusable
Do not take the focus of the window
```javascript
["unfocusable"]
```
#### unresizable
Do not resize window
```javascript
["unresizable"]
```
#### center
Center the window on the screen
```javascript
["center"]
```
#### fullscreen
Full screen window
```javascript
["fullscreen"]
```
#### drop
Drop content to window
```javascript
["drop"]
```
#### border
Window border
```javascript
["border"]
```
#### maximized
Maximize window
```javascript
["maximized"]
```
#### minimized
Minimize window
```javascript
["minimized"]
```
#### exclusive
Make window exclusive
```javascript
["exclusive"]
```
#### vsync
Vertical window synchronization
```javascript
["vsync"]
```
#### fps
Window FPS
```javascript
["fps"]
```

### dialog

#### dialog.file
File selection
```javascript
["dialog.file"]
```
#### dialog.color
Color selection
```javascript
["dialog.color"]
```
#### dialog.date
Date selection
```javascript
["dialog.date"]
```
#### dialog.list
Select from list
```javascript
["dialog.list"]
```

### effect

#### effect
Add effect
```javascript
["effect"]
```
#### effect.list
List of effects
```javascript
["effect.list"]
```
#### effect.remove
Remove effect
```javascript
["effect.remove"]
```

### game

#### vn
Create visual novel
```javascript
["vn"]
```
#### 2d
Create 2D game
```javascript
["2d"]
```
#### 3d
Create 3D game
```javascript
["3d"]
```
#### menu
Create game menu
```javascript
["menu"]
```
#### say
Say text
```javascript
["say"]
```
#### say.skip
Skip text
```javascript
["say.skip"]
```
#### route
Offer to select a root
```javascript
["route"]
```
#### route.remove
Remove root selection
```javascript
["route.remove"]
```
#### route.check
Check root
```javascript
["route.check"]
```
#### route.select
Select root
```javascript
["route.select"]
```
#### route.repeat
Repeat root selection
```javascript
["route.repeat"]
```
#### route.skip
Skip root selection
```javascript
["route.skip"]
```
#### character
Create a character
```javascript
["character"]
```
#### come
Character arrived
```javascript
["come"]
```
#### leave
Character left
```javascript
["leave"]
```
#### change
Character changed
```javascript
["change"]
```
#### object
Add an object to the map
```javascript
["object"]
```
#### shoot
Character shot
```javascript
["shoot"]
```
#### move
Character movement
```javascript
["move"]
```
#### jump
Jump
```javascript
["jump"]
```
#### crouch
Crouch
```javascript
["crouch"]
```
#### drop
Drop
```javascript
["drop"]
```
#### look
Look around
```javascript
["look"]
```
#### hud
Interface
```javascript
["hud"]
```
#### hud.map
Map
```javascript
["hud.map"]
```
#### hud.inventory
Inventory
```javascript
["hud.inventory"]
```
#### snd
Spatial sound
```javascript
["snd"]
```
#### light
Spatial light
```javascript
["light"]
```
#### cam
Spatial camera
```javascript
["cam"]
```

### ai

#### ai.chat
Communicate with AI
```javascript
["ai.chat"]
```
#### ai.image
Create AI image
```javascript
["ai.image"]
```
#### ai.video
Create AI video
```javascript
["ai.video"]
```
#### ai.music
Create AI music
```javascript
["ai.music"]
```
#### ai.sound
Create AI sound
```javascript
["ai.sound"]
```
#### ai.say
Create AI speech
```javascript
["ai.say"]
```
#### ai.2d
Create AI 2D asset
```javascript
["ai.2d"]
```
#### ai.3d
Create AI 3D asset
```javascript
["ai.3d"]
```
#### ai.character
Create AI character
```javascript
["ai.character"]
```
#### ai.clean
Clean up image with AI
```javascript
["ai.clean"]
```
#### ai.resize
Resize image with AI
```javascript
["ai.resize"]
```
#### ai.color
Colorize image with AI
```javascript
["ai.color"]
```
#### ai.style
Change image style with AI
```javascript
["ai.style"]
```
#### ai.translate
Translate text with AI
```javascript
["ai.translate"]
```
#### ai.recognize.text
Recognize text with AI
```javascript
["ai.recognize.text"]
```
#### ai.recognize.image
Recognize image with AI
```javascript
["ai.recognize.image"]
```
#### ai.recognize.video
Recognize video with AI
```javascript
["ai.recognize.video"]
```
#### ai.recognize.motion
Recognize motion with AI
```javascript
["ai.recognize.motion"]
```
#### ai.capture.voice
Capture voice with AI
```javascript
["ai.capture.voice"]
```
#### ai.capture.face
Capture facial expressions with AI
```javascript
["ai.capture.face"]
```
#### ai.capture.motion
Capture motion with AI
```javascript
["ai.capture.motion"]
```

### social

#### social.signin
Authorization
```javascript
["social.signin"]
```
#### social.signup
Registration
```javascript
["social.signup"]
```
#### social.signout
Logout
```javascript
["social.signout"]
```
#### social.restore
Restore login
```javascript
["social.restore"]
```
#### social
Social content
```javascript
["social"]
```
#### social.send
Send content
```javascript
["social.send"]
```
#### social.buy
Purchase
```javascript
["social.buy"]
```

### tech

#### light.on
Turn lamp on
```javascript
["light.on"]
```
#### light.off
Turn lamp off
```javascript
["light.off"]
```
#### power.on
Power on
```javascript
["power.on"]
```
#### power.off
Turn power off
```javascript
["power.off"]
```
#### power.timer
Set timer for power
```javascript
["power.timer"]
```
#### lock.open
Open the lock
```javascript
["lock.open"]
```
#### lock.close
Close the lock
```javascript
["lock.close"]
```
#### lock.code
Set the code on the lock
```javascript
["lock.code"]
```
#### dron.move
Drone movement
```javascript
["dron.move"]
```
#### dron.up
Raise the drone
```javascript
["dron.up"]
```
#### dron.down
Lower the drone
```javascript
["dron.down"]
```
#### dron.left
Move the drone to the left
```javascript
["dron.left"]
```
#### dron.right
Move the drone to the right
```javascript
["dron.right"]
```
#### dron.go
Move the drone forward
```javascript
["dron.go"]
```
#### dron.stop
Stop drone movement
```javascript
["dron.stop"]
```
#### dron.jump
Jump the drone
```javascript
["dron.jump"]
```
#### dron.crouch
Crouch the drone
```javascript
["dron.crouch"]
```
#### dron.open
Open the drone
```javascript
["dron.open"]
```
#### dron.close
Close the drone
```javascript
["dron.close"]
```
#### dron.rotate
Turn the drone
```javascript
["dron.rotate"]
```
#### dron.camera
Drone camera
```javascript
["dron.camera"]
```
#### dron.camera.rotate
Rotate drone camera
```javascript
["dron.camera.rotate"]
```
#### dron.camera.on
Turn drone camera on
```javascript
["dron.camera.on"]
```
#### dron.camera.off
Turn drone camera off
```javascript
["dron.camera.off"]
```
#### dron.camera.record
Record drone camera video
```javascript
["dron.camera.record"]
```
#### dron.camera.record.stop
Stop drone camera recording
```javascript
["dron.camera.record.stop"]
```
#### dron.hand.open
Open the drone arm
```javascript
["dron.hand.open"]
```
#### dron.hand.close
Close the drone arm
```javascript
["dron.hand.close"]
```
#### dron.hand.move
Drone hand movement
```javascript
["dron.hand.move"]
```
#### dron.hand.gesture
Drone hand gesture
```javascript
["dron.hand.gesture"]
```
#### dron.sound
Drone speaker
```javascript
["dron.sound"]
```
#### dron.volume
Drone speaker sound volume
```javascript
["dron.volume"]
```
#### dron.mic
Drone microphone
```javascript
["dron.mic"]
```
#### dron.mic.on
Drone microphone on
```javascript
["dron.mic.on"]
```
#### dron.mic.off
Drone microphone off
```javascript
["dron.mic.off"]
```
#### dron.mic.record
Drone microphone audio recording
```javascript
["dron.mic.record"]
```
#### dron.mic.record.stop
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
