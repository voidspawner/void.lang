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

#### get
Get value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["get"]
```
#### set
Set value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["set"]
```
#### remove
Delete value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["remove"]
```
#### type
Get value type

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["type"]
```
#### bool
Convert value to boolean

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bool"]
```
#### number
Translate value to a number

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["number"]
```
#### text
Translate value to text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["text"]
```
#### list
Translate value into a list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["list"]
```
#### alias
Assign an alias to an action

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["alias"]
```
#### compare
Compare values

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["compare"]
```

### expression

#### +
Add

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["+"]
```
#### -
Subtract

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["-"]
```
#### *
Multiply

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["*"]
```
#### /
Divide

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["/"]
```
#### %
Remainder of division

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["%"]
```
#### **
Elevate

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["**"]
```
#### !
NOT bitwise operator

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["!"]
```
#### &
AND bitwise operator

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["&"]
```
#### |
OR bitwise operator

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["|"]
```
#### ^
XOR bitwise operator

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["^"]
```
#### >>
Right shift

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
[">>"]
```
#### <<
Left shift

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["<<"]
```
#### +=
Add to value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["+="]
```
#### -=
Subtract from value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["-="]
```
#### *=
Multiply the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["*="]
```
#### /=
Divide the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["/="]
```
#### %=
Residue from dividing the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["%="]
```
#### **=
Increment the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["**="]
```
#### !=
NOT bitwise operator of the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["!="]
```
#### &=
AND bitwise operator of the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["&="]
```
#### |=
OR bitwise operator of the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["|="]
```
#### ^=
XOR bitwise operator of the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["^="]
```
#### >>=
Shift to the right of the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
[">>="]
```
#### <<=
Shift to the left of the value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["<<="]
```
#### not
Negation (inversion)

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["not"]
```
#### and
Conjunction (and)

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["and"]
```
#### or
Disjunction (or)

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["or"]
```
#### xor
Exclusive disjunction (exclusive or)

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["xor"]
```
#### in
A value in an array or a name in a dictionary

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["in"]
```
#### not in
Value not in array or name not in dictionary

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["not in"]
```
#### is
Value type match

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["is"]
```
#### not is
Value type mismatch

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["not is"]
```

### control

#### ?
IF check

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["?"]
```
#### ??
MATCH check

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["??"]
```
#### o
FOR, WHILE loop

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["o"]
```
#### x
Exit loop BREAK

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["x"]
```
#### >>>
Continue loop CONTINUE

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
[">>>"]
```
#### <<<
Repeat loop iteration

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["<<<"]
```
#### _
Return action value RETURN

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["_"]
```
#### .
Print text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["."]
```
#### ..
Print text without a new line

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
[".."]
```
#### ...
Enter text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["..."]
```
#### action
Execute action

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["action"]
```
#### action.open
Execute an action from a file

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["action.open"]
```
#### X
End vapp

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["X"]
```
#### xx
Error

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["xx"]
```
#### open
Execute system action

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["open"]
```
#### shell
Execute a command line command

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["shell"]
```
#### shell.open
Open a terminal and execute the command

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["shell.open"]
```
#### code
Execute native code

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["code"]
```
#### python
Execute Python code

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["python"]
```
#### compile
Compile code for a specific platform

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["compile"]
```
#### i
Info logging

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["i"]
```
#### w
Warning logging

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["w"]
```
#### e
Error logging

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["e"]
```
#### d
Debug logging

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["d"]
```
#### t
Time logging

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["t"]
```
#### export
Export vapp for selected platforms

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["export"]
```
#### update
Update script

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["update"]
```
#### test
Test script

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["test"]
```
#### help
Display language hint

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["help"]
```
#### debug
Display debug information

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["debug"]
```
#### debug.fps
Display FPS

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["debug.fps"]
```

### text

#### lower
Convert text to lower case

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["lower"]
```
#### upper
Convert text to uppercase

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["upper"]
```
#### starts
Starts with text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["starts"]
```
#### ends
Ends with text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ends"]
```
#### strip
Trim text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["strip"]
```
#### strip.start
Trim the beginning of text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["strip.start"]
```
#### strip.end
Trim the end of text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["strip.end"]
```
#### replace
Replace text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["replace"]
```
#### find
Find position in text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["find"]
```
#### similar
Compare texts

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["similar"]
```
#### part
Get a part of text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["part"]
```
#### split
Split text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["split"]
```
#### join
Join text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["join"]
```
#### regex
Find in text using regular expression

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["regex"]
```
#### regex.replace
Replace text using a regular expression

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["regex.replace"]
```
#### escape
Escape text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["escape"]
```
#### escape.html
Escape HTML text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["escape.html"]
```
#### escape.sql
Escape SQL text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["escape.sql"]
```
#### escape.url
Escape text URL

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["escape.url"]
```
#### escape.json
Escape text JSON

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["escape.json"]
```
#### escape.void
Escape text V O I D

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["escape.void"]
```
#### unescape
Unescape text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["unescape"]
```
#### unescape.html
Unescape HTML text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["unescape.html"]
```
#### unescape.sql
Unescape text SQL

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["unescape.sql"]
```
#### unescape.url
Unescape text URL

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["unescape.url"]
```
#### unescape.json
Unescape JSON text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["unescape.json"]
```
#### unescape.void
Unescape V O I D text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["unescape.void"]
```
#### date
Convert text to timestamp, or timestamp to text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["date"]
```
#### letters
Number of letters in the text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["letters"]
```
#### words
Number of words in the text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["words"]
```
#### sentences
Number of sentences in the text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sentences"]
```
#### lines
Number of lines in the text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["lines"]
```

### list

#### push
Add to list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["push"]
```
#### pop
Extract from the list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["pop"]
```
#### reverse
Invert order in the list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["reverse"]
```
#### shuffle
Shuffle the list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["shuffle"]
```
#### sort
Sort the list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sort"]
```
#### fill
Fill the list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["fill"]
```
#### map
Map the list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["map"]
```
#### reduce
Reduce the list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["reduce"]
```
#### names
Dictionary or list names

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["names"]
```
#### values
Dictionary values

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["values"]
```

### math

#### sin
Sine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sin"]
```
#### cos
Cosine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cos"]
```
#### tan
Tangent

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["tan"]
```
#### sinh
Hyperbolic sine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sinh"]
```
#### cosh
Hyperbolic cosine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cosh"]
```
#### tanh
Hyperbolic tangent

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["tanh"]
```
#### asin
Arcsine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["asin"]
```
#### acos
Arccosine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["acos"]
```
#### atan
Arctangent

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["atan"]
```
#### asinh
Hyperbolic arcsine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["asinh"]
```
#### acosh
Hyperbolic arccosine

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["acosh"]
```
#### atanh
Hyperbolic arctangent

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["atanh"]
```
#### round
Round a number

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["round"]
```
#### floor
Round a number down

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["floor"]
```
#### ceil
Round a number up

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ceil"]
```
#### log
Logarithm

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["log"]
```
#### log.e
Hyperbolic logarithm

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["log.e"]
```
#### log.n
Natural logarithm

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["log.n"]
```
#### fa
Factorial

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["fa"]
```
#### fib
Fibonacci

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["fib"]
```
#### abs
Absolute value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["abs"]
```
#### min
Minimum value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["min"]
```
#### max
Maximum value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["max"]
```
#### avg
Average value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["avg"]
```
#### sum
Sum of values

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sum"]
```
#### hex
Hexadecimal value to byte

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["hex"]
```
#### hex.dec
Hexadecimal value to decimal

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["hex.dec"]
```
#### bin
Binary value to byte

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bin"]
```
#### bin.dec
Binary value to decimal

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bin.dec"]
```
#### dec
Decimal value to byte

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dec"]
```
#### dec.hex
Decimal value to hexadecimal

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dec.hex"]
```
#### dec.bin
Decimal value to binary

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dec.bin"]
```
#### rad
Degree to radian

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["rad"]
```
#### deg
Radian to degree

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["deg"]
```
#### random
Random value

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["random"]
```
#### random.reseed
Re-create random seed

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["random.reseed"]
```
#### random.seed
Get random seed

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["random.seed"]
```

### time

#### time
Time stamp in microseconds

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["time"]
```
#### time.ms
Time stamp in milliseconds

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["time.ms"]
```
#### time.s
Timestamp in seconds

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["time.s"]
```
#### timer
Set timer

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["timer"]
```
#### timer.remove
Remove timer

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["timer.remove"]
```
#### wait
Wait time in seconds

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["wait"]
```

### crypto

#### encrypt
Encode text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["encrypt"]
```
#### decrypt
Decode text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["decrypt"]
```
#### hash
Random hash

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["hash"]
```
#### uuid
Random UUID

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["uuid"]
```
#### md5
MD5 hash

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["md5"]
```
#### sha1
SHA1 hash

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sha1"]
```
#### sha256
SHA256 hash

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sha256"]
```
#### sha512
SHA512 hash

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sha512"]
```
#### crc32
CRC32 hash

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["crc32"]
```
#### base64
Base64 hash

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["base64"]
```
#### base64.decode
Decode Base64

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["base64.decode"]
```
#### gzip
Gzip text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["gzip"]
```
#### gzip.decode
Decode Gzip

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["gzip.decode"]
```
#### rsa
Encode text with RSA

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["rsa"]
```
#### rsa.decode
Decode RSA

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["rsa.decode"]
```
#### rsa.key.public
Get RSA public key

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["rsa.key.public"]
```
#### rsa.key.private
Get RSA private key

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["rsa.key.private"]
```
#### ssl
Encode text with SSL

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ssl"]
```
#### ssl.decode
Decode SSL

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ssl.decode"]
```
#### ssl.check
Verify SSL

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ssl.check"]
```
#### bcrypt
Encode text with Bcrypt

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bcrypt"]
```
#### bcrypt.check
Verify Bcrypt

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bcrypt.check"]
```

### format

#### void
Encode to V O I D

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["void"]
```
#### void.decode
Decode V O I D

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["void.decode"]
```
#### void.read
Read V O I D file

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["void.read"]
```
#### void.write
Write V O I D file

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["void.write"]
```
#### json
Encode to JSON

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["json"]
```
#### json.decode
Decode JSON

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["json.decode"]
```
#### json.read
Read JSON file

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["json.read"]
```
#### json.write
Write JSON file

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["json.write"]
```
#### yaml
Encode YAML

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["yaml"]
```
#### yaml.decode
Decode YAML

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["yaml.decode"]
```
#### csv
Encode CSV

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["csv"]
```
#### csv.decode
Decode CSV

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["csv.decode"]
```
#### ini
Encode INI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ini"]
```
#### ini.decode
Decode INI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ini.decode"]
```
#### html
Encode HTML

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["html"]
```
#### html.decode
Decode HTML

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["html.decode"]
```
#### xml
Encode XML

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["xml"]
```
#### xml.decode
Decode XML

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["xml.decode"]
```
#### css
Encode CSS

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["css"]
```
#### css.decode
Decode CSS

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["css.decode"]
```

### file

#### file.exists
File exists

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.exists"]
```
#### file.write
Write to file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.write"]
```
#### file.read
Read file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.read"]
```
#### file.read.list
Read lines from file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.read.list"]
```
#### file.remove
Remove file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.remove"]
```
#### file.move
Move file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.move"]
```
#### file.copy
Copy file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.copy"]
```
#### file.rename
Rename file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.rename"]
```
#### file.info
File information

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.info"]
```
#### file.size
File size

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.size"]
```
#### file.permissions
File permissions

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.permissions"]
```
#### file.readonly
Read-only file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.readonly"]
```
#### file.hidden
Hidden file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.hidden"]
```
#### file.modified
File modification time

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.modified"]
```
#### file.sha256
SHA256 file hash

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.sha256"]
```
#### file.crc32
CRC32 file hash

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.crc32"]
```
#### file.base64
Base64 file hash

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.base64"]
```
#### file.zip
Compress a file into a Zip archive

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.zip"]
```
#### file.zip.list
List of files in Zip archive

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.zip.list"]
```
#### file.zip.exists
File exists in Zip archive

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.zip.exists"]
```
#### file.zip.read
Read file from Zip archive

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.zip.read"]
```
#### file.zip.remove
Remove file from Zip archive

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.zip.remove"]
```
#### file.unzip
Extract Zip archive

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.unzip"]
```
#### file.gzip
Compress file with Gzip

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.gzip"]
```
#### file.ungzip
Extract Gzip file

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.ungzip"]
```
#### file.link
Create a symbolic link

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.link"]
```
#### file.link.exists
Symbolic link exists

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.link.exists"]
```
#### file.backup
Backup files

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["file.backup"]
```
#### dir.exists
Directory exists

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.exists"]
```
#### dir.create
Create directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.create"]
```
#### dir.copy
Copy directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.copy"]
```
#### dir.move
Move directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.move"]
```
#### dir.rename
Rename directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.rename"]
```
#### dir.remove
Remove directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.remove"]
```
#### dir.list
List of files in a directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.list"]
```
#### dir.clear
Clear directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.clear"]
```
#### dir.info
Directory information

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.info"]
```
#### dir.size
Directory size

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.size"]
```
#### dir.permissions
Directory permissions

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.permissions"]
```
#### dir.readonly
Read-only directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.readonly"]
```
#### dir.hidden
Hidden directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.hidden"]
```
#### dir.modified
Directory modification time

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.modified"]
```
#### dir.zip
Compress directory

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dir.zip"]
```
#### drive.list
List of volumes

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.list"]
```
#### drive.name
Volume name

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.name"]
```
#### drive.size
Volume size

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.size"]
```
#### drive.used
Volume space used

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.used"]
```
#### drive.free
Volume free space

⌜ ask・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.free"]
```
#### drive.mount
Mount volume

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.mount"]
```
#### drive.unmount
Unmount volume

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.unmount"]
```
#### drive.format
Format volume

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["drive.format"]
```
#### path.drive
Get volume from path

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["path.drive"]
```
#### path.dir
Get directory from path

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["path.dir"]
```
#### path.file
Get file from path

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["path.file"]
```
#### path.name
Get filename from path

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["path.name"]
```
#### path.extension
Get extension from path

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["path.extension"]
```
#### path.extension.strip
Trim extension from path

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["path.extension.strip"]
```

### cloud

#### cloud.file
File server

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.file"]
```
#### cloud.web
Web server

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.web"]
```
#### cloud.api
API server

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.api"]
```
#### cloud.socket
Socket server

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.socket"]
```
#### cloud.websocket
Websocket server

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.websocket"]
```
#### cloud.mail
Mail server

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.mail"]
```
#### cloud.game
Game server

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.game"]
```
#### cloud.social
Social server

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.social"]
```
#### cloud.live
Streaming server

⌜ local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cloud.live"]
```

### bot

#### bot.telegram
Telegram bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.telegram"]
```
#### bot.wechat
Wechat bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.wechat"]
```
#### bot.x
X bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.x"]
```
#### bot.youtube
YouTube bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.youtube"]
```
#### bot.tiktok
TikTok bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.tiktok"]
```
#### bot.steam
Steam bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.steam"]
```
#### bot.binance
Binance bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.binance"]
```
#### bot.ib
Interactive Brokers bot

⌜ vapp・local・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bot.ib"]
```

### request

#### request
Web request

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["request"]
```
#### request.post
Post Web request

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["request.post"]
```
#### request.put
Put Web request

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["request.put"]
```
#### request.delete
Delete Web request

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["request.delete"]
```
#### request.head
Head Web request

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["request.head"]
```

### cookie

#### cookie
Get Web cookies

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cookie"]
```
#### cookie.remove
Delete Web cookies

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cookie.remove"]
```

### sql

#### sql
SQL query

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql"]
```
#### sql.connect
Connect to SQL server

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.connect"]
```
#### sql.disconnet
Disconnect from SQL server

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.disconnet"]
```
#### sql.user
SQL user

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.user"]
```
#### sql.user.list
SQL user list

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.user.list"]
```
#### sql.user.remove
SQL remove user

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.user.remove"]
```
#### sql.db
SQL database

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.db"]
```
#### sql.db.list
SQL database list

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.db.list"]
```
#### sql.db.remove
SQL remove database

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.db.remove"]
```
#### sql.db.size
SQL database size

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.db.size"]
```
#### sql.table
SQL table

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.table"]
```
#### sql.table.list
SQL table list

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.table.list"]
```
#### sql.table.remove
SQL remove table

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.table.remove"]
```
#### sql.field
SQL field

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.field"]
```
#### sql.field.list
SQL field list

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.field.list"]
```
#### sql.field.remove
SQL remove field

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.field.remove"]
```
#### sql.index
SQL index

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.index"]
```
#### sql.index.list
SQL index list

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.index.list"]
```
#### sql.index.remove
SQL remove index

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.index.remove"]
```
#### sql.function
SQL function

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.function"]
```
#### sql.function.list
SQL function list

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.function.list"]
```
#### sql.function.remove
SQL remove function

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.function.remove"]
```
#### sql.view
SQL view

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.view"]
```
#### sql.view.list
SQL view list

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.view.list"]
```
#### sql.view.remove
SQL remove a view

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.view.remove"]
```
#### sql.get
SQL get one result

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.get"]
```
#### sql.all
SQL get all results

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.all"]
```
#### sql.cursor
SQL cursor

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.cursor"]
```
#### sql.transaction
SQL start transaction

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.transaction"]
```
#### sql.commit
SQL send transaction

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.commit"]
```
#### sql.rollback
SQL cancel transaction

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["sql.rollback"]
```

### os

#### os.name
Operating system name

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.name"]
```
#### os.version
Operating system version

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.version"]
```
#### os.username
User name

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.username"]
```
#### os.desktop
Check that it’s desktop

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.desktop"]
```
#### os.mobile
Check that it’s mobile device

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.mobile"]
```
#### os.web
Check that it’s Web

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.web"]
```
#### os.windows
Check that it’s Windows

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.windows"]
```
#### os.macos
Check that it's macOS

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.macos"]
```
#### os.ios
Check that it's iOS

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.ios"]
```
#### os.ipados
Check that it's iPadOS

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.ipados"]
```
#### os.watchos
Check that it's watchOS

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.watchos"]
```
#### os.tvos
Check that it's tvOS

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.tvos"]
```
#### os.android
Check that it's Android

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.android"]
```
#### os.nix
Check that it’s Unix-like

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["os.nix"]
```

### device

#### cpu.name
Processor name

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cpu.name"]
```
#### cpu.cores
Number of processor cores

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["cpu.cores"]
```
#### memory.size
Memory size

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["memory.size"]
```
#### memory.free
Memory Free

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["memory.free"]
```
#### memory.used
Memory used

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["memory.used"]
```
#### memory.available
Memory available

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["memory.available"]
```

### gps

#### gps
Get GPS coordinates

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["gps"]
```

### sensor

#### speed
Get speed

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["speed"]
```
#### tilt
Get tilt

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["tilt"]
```
#### compass
Get compass direction

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["compass"]
```
#### motion
Get motion type

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["motion"]
```

### camera

#### camera
Get camera image

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["camera"]
```
#### gallery
Get gallery image

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["gallery"]
```

### contacts

#### contacts
Get contacts

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["contacts"]
```

### calendar

#### calendar
Get calendar

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["calendar"]
```

### health

#### health
Get health data

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["health"]
```

### flashlight

#### flashlight
Flashlight

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["flashlight"]
```

### mic

#### mic
Microphone

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["mic"]
```

### notification

#### notification
Receive notifications

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["notification"]
```
#### notification.token
Notification token

⌜ ask・swift・kotlin・godot・c++ ⌟

```javascript
["notification.token"]
```
#### notification.send
Send notification

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["notification.send"]
```

### key

#### key
Assign key action

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["key"]
```
#### key.remove
Delete a key action

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["key.remove"]
```
#### key.press
Start a key action

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["key.press"]
```
#### key.enable
Enable key action

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["key.enable"]
```
#### key.disable
Disable key action

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["key.disable"]
```

### keyboard

#### keyboard
On-screen keyboard

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["keyboard"]
```
#### keyboard.height
Screen keyboard height

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["keyboard.height"]
```

### mouse

#### mouse
Show mouse

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["mouse"]
```
#### mouse.hide
Hide mouse

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["mouse.hide"]
```
#### mouse.lock
Lock mouse

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["mouse.lock"]
```
#### mouse.capture
Capture mouse

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["mouse.capture"]
```
#### mouse.confine
Limit mouse movement

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["mouse.confine"]
```
#### mouse.position
Get mouse coordinates

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["mouse.position"]
```
#### mouse.shape
Mouse pointer shape

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["mouse.shape"]
```

### gamepad

#### gamepad.axis
Gamepad stick deflection

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["gamepad.axis"]
```
#### gamepad.vibrate
Gamepad vibration

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["gamepad.vibrate"]
```

### clipboard

#### clipboard
Clipboard

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["clipboard"]
```
#### clipboard.clear
Clear clipboard

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["clipboard.clear"]
```

### voice

#### voice
Read text with voice

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["voice"]
```
#### voice.list
Voice list

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["voice.list"]
```
#### voice.stop
Stop text reading

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["voice.stop"]
```
#### voice.pause
Pause / continue text reading

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["voice.pause"]
```

### convert

#### convert
Convert from one format to another

⌜ vapp・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["convert"]
```

### image

#### image
Create image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image"]
```
#### image.read
Read image from file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.read"]
```
#### image.write
Write image to file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.write"]
```
#### image.size
Resize image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.size"]
```
#### image.crop
Crop image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.crop"]
```
#### image.square
Crop image to square

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.square"]
```
#### image.rotate
Rotate image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.rotate"]
```
#### image.flip.h
Reflect image horizontally

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.flip.h"]
```
#### image.flip.v
Reflect image vertically

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.flip.v"]
```
#### image.tint
Tint the image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.tint"]
```
#### image.gray
Convert image to grayscale

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.gray"]
```
#### image.text
Add text to image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.text"]
```
#### image.image
Add image to image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.image"]
```
#### image.draw
Add drawing to image

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["image.draw"]
```

### video

#### video
Create video

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video"]
```
#### video.read
Read video from file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.read"]
```
#### video.write
Write video to file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.write"]
```
#### video.size
Video size

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.size"]
```
#### video.rate
Video frame rate

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.rate"]
```
#### video.rotate
Rotate video

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.rotate"]
```
#### video.flip.h
Reflect video horizontally

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.flip.h"]
```
#### video.flip.v
Reflect video vertically

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.flip.v"]
```
#### video.clip
Video clip

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.clip"]
```
#### video.speed
Video speed

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.speed"]
```
#### video.reverse
Change video direction

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.reverse"]
```
#### video.text
Add text to video

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.text"]
```
#### video.image
Add image to video

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.image"]
```
#### video.sound
Add sound to video

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.sound"]
```
#### video.video
Add video to video

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["video.video"]
```

### model

#### model
Create 3D model

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["model"]
```
#### model.read
Read 3D model from file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["model.read"]
```
#### model.write
Write 3D model to file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["model.write"]
```
#### model.animate
Animate 3D model

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["model.animate"]
```
#### model.texture
Apply texture to 3D model

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["model.texture"]
```

### sound

#### sound
Create sound

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound"]
```
#### sound.read
Read sound from file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.read"]
```
#### sound.write
Write sound to file

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.write"]
```
#### sound.list
Current played sounds

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.list"]
```
#### sound.remove
Remove sound

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.remove"]
```
#### sound.volume
Sound volume

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.volume"]
```
#### sound.speed
Sound playback speed

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.speed"]
```
#### sound.clip
Sound clip

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.clip"]
```
#### sound.sound
Add sound to sound

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["sound.sound"]
```

### music

#### music
Add music

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["music"]
```
#### music.stop
Stop music

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["music.stop"]
```
#### music.pause
Pause / continue music

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["music.pause"]
```
#### music.volume
Music sound volume

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["music.volume"]
```

### volume

#### volume
Master volume

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["volume"]
```

### screen

#### screen.count
Number of screens

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["screen.count"]
```
#### screen.list
List of screens

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["screen.list"]
```
#### screen.info
Screen information

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["screen.info"]
```
#### size
Screen size

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["size"]
```
#### orientation
Screen orientation

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["orientation"]
```
#### landscape
Landscape orientation

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["landscape"]
```
#### portrait
Portrait orientation

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["portrait"]
```
#### rate
Screen frame rate

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["rate"]
```
#### pixel
Get screen pixel color

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["pixel"]
```
#### symbol
Get screen symbol

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["symbol"]
```
#### dpi
Dots per inch

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["dpi"]
```
#### dark
Dark mode

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["dark"]
```
#### touch
Touchscreen

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["touch"]
```
#### screenshot
Screenshot

⌜ safe・swift・kotlin・godot・c++ ⌟

```javascript
["screenshot"]
```
#### screen.record
Record screen

⌜ safe・swift・kotlin・godot・c++ ⌟

```javascript
["screen.record"]
```
#### screen.stop
Stop screen recording

⌜ safe・swift・kotlin・godot・c++ ⌟

```javascript
["screen.stop"]
```

### ui

#### ui
UI element

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui"]
```
#### bg
Background

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["bg"]
```
#### show
Show UI

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["show"]
```
#### hide
Hide UI

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["hide"]
```
#### visible
UI visibility

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["visible"]
```
#### enable
Enable UI

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["enable"]
```
#### disable
Disable UI

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["disable"]
```
#### enabled
Check if UI is enabled

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["enabled"]
```
#### focus
Move focus to UI

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["focus"]
```
#### scale
Scale UI

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["scale"]
```
#### ui.text
UI text

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.text"]
```
#### ui.image
UI image

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.image"]
```
#### ui.button
UI button

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.button"]
```
#### ui.divider
UI separator

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.divider"]
```
#### ui.video
UI video

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.video"]
```
#### ui.select
UI selection

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.select"]
```
#### ui.switch
UI switch

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.switch"]
```
#### ui.progress
UI progress bar

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.progress"]
```
#### ui.slider
UI slider

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.slider"]
```
#### ui.edit
UI text editor

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.edit"]
```
#### ui.chart
UI chart

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.chart"]
```
#### ui.split.h
UI horizontal separator

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.split.h"]
```
#### ui.split.v
UI vertical separator

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.split.v"]
```
#### ui.list
UI list

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.list"]
```
#### ui.tile
UI tile

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.tile"]
```
#### ui.color
UI color

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.color"]
```
#### ui.date
UI date

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.date"]
```
#### ui.drop
UI drop down content

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.drop"]
```
#### ui.menu
UI menu

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.menu"]
```
#### ui.menu.context
UI context menu

⌜ safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ui.menu.context"]
```

### window

#### window
Create window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["window"]
```
#### window.list
Window list

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["window.list"]
```
#### window.info
Window information

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["window.info"]
```
#### title
Window title

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["title"]
```
#### icon
Window icon

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["icon"]
```
#### size
Window size

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["size"]
```
#### size.max
Maximum window size

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["size.max"]
```
#### size.min
Minimum window size

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["size.min"]
```
#### position
Window position

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["position"]
```
#### direction
Window text direction

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["direction"]
```
#### attention
Window attention

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["attention"]
```
#### top
Top of all windows

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["top"]
```
#### foreground
Foreground window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["foreground"]
```
#### unfocusable
Do not take the focus of the window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["unfocusable"]
```
#### unresizable
Do not resize window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["unresizable"]
```
#### center
Center the window on the screen

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["center"]
```
#### fullscreen
Full screen window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["fullscreen"]
```
#### drop
Drop content to window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["drop"]
```
#### border
Window border

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["border"]
```
#### maximized
Maximize window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["maximized"]
```
#### minimized
Minimize window

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["minimized"]
```
#### exclusive
Make window exclusive

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["exclusive"]
```
#### vsync
Vertical window synchronization

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["vsync"]
```
#### fps
Window FPS

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["fps"]
```

### dialog

#### dialog.file
File selection

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["dialog.file"]
```
#### dialog.color
Color selection

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["dialog.color"]
```
#### dialog.date
Date selection

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["dialog.date"]
```
#### dialog.list
Select from list

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["dialog.list"]
```

### effect

#### effect
Add effect

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["effect"]
```
#### effect.list
List of effects

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["effect.list"]
```
#### effect.remove
Remove effect

⌜ safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["effect.remove"]
```

### game

#### vn
Create visual novel

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["vn"]
```
#### 2d
Create 2D game

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["2d"]
```
#### 3d
Create 3D game

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["3d"]
```
#### menu
Create game menu

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["menu"]
```
#### say
Say text

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["say"]
```
#### say.skip
Skip text

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["say.skip"]
```
#### route
Offer to select a root

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["route"]
```
#### route.remove
Remove root selection

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["route.remove"]
```
#### route.check
Check root

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["route.check"]
```
#### route.select
Select root

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["route.select"]
```
#### route.repeat
Repeat root selection

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["route.repeat"]
```
#### route.skip
Skip root selection

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["route.skip"]
```
#### character
Create a character

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["character"]
```
#### come
Character arrived

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["come"]
```
#### leave
Character left

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["leave"]
```
#### change
Character changed

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["change"]
```
#### object
Add an object to the map

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["object"]
```
#### shoot
Character shot

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["shoot"]
```
#### move
Character movement

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["move"]
```
#### jump
Jump

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["jump"]
```
#### crouch
Crouch

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["crouch"]
```
#### drop
Drop

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["drop"]
```
#### look
Look around

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["look"]
```
#### hud
Interface

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["hud"]
```
#### hud.map
Map

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["hud.map"]
```
#### hud.inventory
Inventory

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["hud.inventory"]
```
#### snd
Spatial sound

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["snd"]
```
#### light
Spatial light

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["light"]
```
#### cam
Spatial camera

⌜ vapp・safe・js・swift・kotlin・godot・c++ ⌟

```javascript
["cam"]
```

### ai

#### ai.chat
Communicate with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.chat"]
```
#### ai.image
Create AI image

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.image"]
```
#### ai.video
Create AI video

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.video"]
```
#### ai.music
Create AI music

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.music"]
```
#### ai.sound
Create AI sound

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.sound"]
```
#### ai.say
Create AI speech

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.say"]
```
#### ai.2d
Create AI 2D asset

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.2d"]
```
#### ai.3d
Create AI 3D asset

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.3d"]
```
#### ai.character
Create AI character

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.character"]
```
#### ai.clean
Clean up image with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.clean"]
```
#### ai.resize
Resize image with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.resize"]
```
#### ai.color
Colorize image with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.color"]
```
#### ai.style
Change image style with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.style"]
```
#### ai.translate
Translate text with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.translate"]
```
#### ai.recognize.text
Recognize text with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.recognize.text"]
```
#### ai.recognize.image
Recognize image with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.recognize.image"]
```
#### ai.recognize.video
Recognize video with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.recognize.video"]
```
#### ai.recognize.motion
Recognize motion with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.recognize.motion"]
```
#### ai.capture.voice
Capture voice with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.capture.voice"]
```
#### ai.capture.face
Capture facial expressions with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.capture.face"]
```
#### ai.capture.motion
Capture motion with AI

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["ai.capture.motion"]
```

### social

#### social.signin
Authorization

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["social.signin"]
```
#### social.signup
Registration

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["social.signup"]
```
#### social.signout
Logout

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["social.signout"]
```
#### social.restore
Restore login

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["social.restore"]
```
#### social
Social content

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["social"]
```
#### social.send
Send content

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["social.send"]
```
#### social.buy
Purchase

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["social.buy"]
```

### tech

#### light.on
Turn lamp on

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["light.on"]
```
#### light.off
Turn lamp off

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["light.off"]
```
#### power.on
Power on

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["power.on"]
```
#### power.off
Turn power off

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["power.off"]
```
#### power.timer
Set timer for power

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["power.timer"]
```
#### lock.open
Open the lock

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["lock.open"]
```
#### lock.close
Close the lock

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["lock.close"]
```
#### lock.code
Set the code on the lock

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["lock.code"]
```
#### dron.move
Drone movement

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.move"]
```
#### dron.up
Raise the drone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.up"]
```
#### dron.down
Lower the drone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.down"]
```
#### dron.left
Move the drone to the left

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.left"]
```
#### dron.right
Move the drone to the right

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.right"]
```
#### dron.go
Move the drone forward

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.go"]
```
#### dron.stop
Stop drone movement

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.stop"]
```
#### dron.jump
Jump the drone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.jump"]
```
#### dron.crouch
Crouch the drone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.crouch"]
```
#### dron.open
Open the drone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.open"]
```
#### dron.close
Close the drone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.close"]
```
#### dron.rotate
Turn the drone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.rotate"]
```
#### dron.camera
Drone camera

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.camera"]
```
#### dron.camera.rotate
Rotate drone camera

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.camera.rotate"]
```
#### dron.camera.on
Turn drone camera on

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.camera.on"]
```
#### dron.camera.off
Turn drone camera off

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.camera.off"]
```
#### dron.camera.record
Record drone camera video

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.camera.record"]
```
#### dron.camera.record.stop
Stop drone camera recording

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.camera.record.stop"]
```
#### dron.hand.open
Open the drone arm

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.hand.open"]
```
#### dron.hand.close
Close the drone arm

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.hand.close"]
```
#### dron.hand.move
Drone hand movement

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.hand.move"]
```
#### dron.hand.gesture
Drone hand gesture

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.hand.gesture"]
```
#### dron.sound
Drone speaker

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.sound"]
```
#### dron.volume
Drone speaker sound volume

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.volume"]
```
#### dron.mic
Drone microphone

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.mic"]
```
#### dron.mic.on
Drone microphone on

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.mic.on"]
```
#### dron.mic.off
Drone microphone off

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.mic.off"]
```
#### dron.mic.record
Drone microphone audio recording

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

```javascript
["dron.mic.record"]
```
#### dron.mic.record.stop
Stop recording drone microphone audio

⌜ vapp・safe・python・js・swift・kotlin・godot・c++ ⌟

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
