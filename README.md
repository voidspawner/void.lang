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
```js
{
  "run": [
    [".", "Hi World :D"]
  ]
}
```
##### Even simpler
```js
[
  [".", "Hi World :D"]
]
```
##### Multilanguage text
```js
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
```js
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
```js
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
```js
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
```js
[
  ["cloud.file": "/path/to/share"]
]
```
##### Add comments
```js
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
```js
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
```js
[
  ["replace", "Hi World :D", "i", "i!"],
  [".", "{}"],
  "upper",
  [".", "{}"]
]
```
##### Run native code
```js
[
  ["code", "for i in range(10):print(i)"]
]
```
##### Run Python code
```js
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
```js
[".", "Hi World :D"]
```
```
Action name: "."
Action parameters: ["Hi World :D"]
```
#####
```js
["=", "value", 1, "+", 1]
```
```
Action name: "="
Action parameters: ["value", 1, "+", 1]
```
#####
```js
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

```diff
! Get value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["get"]
```
#### set

```diff
! Set value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["set"]
```
#### remove

```diff
! Delete value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["remove"]
```
#### type

```diff
! Get value type
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["type"]
```
#### bool

```diff
! Convert value to boolean
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["bool"]
```
#### number

```diff
! Translate value to a number
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["number"]
```
#### text

```diff
! Translate value to text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["text"]
```
#### list

```diff
! Translate value into a list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["list"]
```
#### alias

```diff
! Assign an alias to an action
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["alias"]
```
#### compare

```diff
! Compare values
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["compare"]
```

### expression

#### +

```diff
! Add
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["+"]
```
#### -

```diff
! Subtract
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["-"]
```
#### *

```diff
! Multiply
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["*"]
```
#### /

```diff
! Divide
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["/"]
```
#### %

```diff
! Remainder of division
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["%"]
```
#### **

```diff
! Elevate
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["**"]
```
#### !

```diff
! NOT bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["!"]
```
#### &

```diff
! AND bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["&"]
```
#### |

```diff
! OR bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["|"]
```
#### ^

```diff
! XOR bitwise operator
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["^"]
```
#### >>

```diff
! Right shift
+ safe・python・js・swift・kotlin・godot・c++
```

```js
[">>"]
```
#### <<

```diff
! Left shift
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["<<"]
```
#### +=

```diff
! Add to value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["+="]
```
#### -=

```diff
! Subtract from value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["-="]
```
#### *=

```diff
! Multiply the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["*="]
```
#### /=

```diff
! Divide the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["/="]
```
#### %=

```diff
! Residue from dividing the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["%="]
```
#### **=

```diff
! Increment the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["**="]
```
#### !=

```diff
! NOT bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["!="]
```
#### &=

```diff
! AND bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["&="]
```
#### |=

```diff
! OR bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["|="]
```
#### ^=

```diff
! XOR bitwise operator of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["^="]
```
#### >>=

```diff
! Shift to the right of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
[">>="]
```
#### <<=

```diff
! Shift to the left of the value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["<<="]
```
#### not

```diff
! Negation (inversion)
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["not"]
```
#### and

```diff
! Conjunction (and)
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["and"]
```
#### or

```diff
! Disjunction (or)
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["or"]
```
#### xor

```diff
! Exclusive disjunction (exclusive or)
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["xor"]
```
#### in

```diff
! A value in an array or a name in a dictionary
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["in"]
```
#### not in

```diff
! Value not in array or name not in dictionary
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["not in"]
```
#### is

```diff
! Value type match
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["is"]
```
#### not is

```diff
! Value type mismatch
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["not is"]
```

### control

#### ?

```diff
! IF check
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["?"]
```
#### ??

```diff
! MATCH check
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["??"]
```
#### o

```diff
! FOR, WHILE loop
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["o"]
```
#### x

```diff
! Exit loop BREAK
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["x"]
```
#### >>>

```diff
! Continue loop CONTINUE
+ safe・python・js・swift・kotlin・godot・c++
```

```js
[">>>"]
```
#### <<<

```diff
! Repeat loop iteration
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["<<<"]
```
#### _

```diff
! Return action value RETURN
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["_"]
```
#### .

```diff
! Print text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["."]
```
#### ..

```diff
! Print text without a new line
+ safe・python・js・swift・kotlin・godot・c++
```

```js
[".."]
```
#### ...

```diff
! Enter text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["..."]
```
#### action

```diff
! Execute action
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["action"]
```
#### action.open

```diff
! Execute an action from a file
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["action.open"]
```
#### X

```diff
! End vapp
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["X"]
```
#### xx

```diff
! Error
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["xx"]
```
#### open

```diff
! Execute system action
+ local・python・js・swift・kotlin・godot・c++
```

```js
["open"]
```
#### shell

```diff
! Execute a command line command
+ local・python・js・swift・kotlin・godot・c++
```

```js
["shell"]
```
#### shell.open

```diff
! Open a terminal and execute the command
+ local・python・js・swift・kotlin・godot・c++
```

```js
["shell.open"]
```
#### code

```diff
! Execute native code
+ local・python・js・swift・kotlin・godot・c++
```

```js
["code"]
```
#### python

```diff
! Execute Python code
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["python"]
```
#### compile

```diff
! Compile code for a specific platform
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["compile"]
```
#### i

```diff
! Info logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["i"]
```
#### w

```diff
! Warning logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["w"]
```
#### e

```diff
! Error logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["e"]
```
#### d

```diff
! Debug logging
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["d"]
```
#### t

```diff
! Time logging
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["t"]
```
#### export

```diff
! Export vapp for selected platforms
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["export"]
```
#### update

```diff
! Update script
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["update"]
```
#### test

```diff
! Test script
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["test"]
```
#### help

```diff
! Display language hint
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["help"]
```
#### debug

```diff
! Display debug information
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["debug"]
```
#### debug.fps

```diff
! Display FPS
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["debug.fps"]
```

### text

#### lower

```diff
! Convert text to lower case
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["lower"]
```
#### upper

```diff
! Convert text to uppercase
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["upper"]
```
#### starts

```diff
! Starts with text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["starts"]
```
#### ends

```diff
! Ends with text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ends"]
```
#### strip

```diff
! Trim text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["strip"]
```
#### strip.start

```diff
! Trim the beginning of text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["strip.start"]
```
#### strip.end

```diff
! Trim the end of text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["strip.end"]
```
#### replace

```diff
! Replace text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["replace"]
```
#### find

```diff
! Find position in text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["find"]
```
#### similar

```diff
! Compare texts
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["similar"]
```
#### part

```diff
! Get a part of text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["part"]
```
#### split

```diff
! Split text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["split"]
```
#### join

```diff
! Join text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["join"]
```
#### regex

```diff
! Find in text using regular expression
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["regex"]
```
#### regex.replace

```diff
! Replace text using a regular expression
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["regex.replace"]
```
#### escape

```diff
! Escape text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["escape"]
```
#### escape.html

```diff
! Escape HTML text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["escape.html"]
```
#### escape.sql

```diff
! Escape SQL text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["escape.sql"]
```
#### escape.url

```diff
! Escape text URL
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["escape.url"]
```
#### escape.json

```diff
! Escape text JSON
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["escape.json"]
```
#### escape.void

```diff
! Escape text V O I D
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["escape.void"]
```
#### unescape

```diff
! Unescape text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["unescape"]
```
#### unescape.html

```diff
! Unescape HTML text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["unescape.html"]
```
#### unescape.sql

```diff
! Unescape text SQL
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["unescape.sql"]
```
#### unescape.url

```diff
! Unescape text URL
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["unescape.url"]
```
#### unescape.json

```diff
! Unescape JSON text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["unescape.json"]
```
#### unescape.void

```diff
! Unescape V O I D text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["unescape.void"]
```
#### date

```diff
! Convert text to timestamp, or timestamp to text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["date"]
```
#### letters

```diff
! Number of letters in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["letters"]
```
#### words

```diff
! Number of words in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["words"]
```
#### sentences

```diff
! Number of sentences in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sentences"]
```
#### lines

```diff
! Number of lines in the text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["lines"]
```

### list

#### push

```diff
! Add to list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["push"]
```
#### pop

```diff
! Extract from the list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["pop"]
```
#### reverse

```diff
! Invert order in the list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["reverse"]
```
#### shuffle

```diff
! Shuffle the list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["shuffle"]
```
#### sort

```diff
! Sort the list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sort"]
```
#### fill

```diff
! Fill the list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["fill"]
```
#### map

```diff
! Map the list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["map"]
```
#### reduce

```diff
! Reduce the list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["reduce"]
```
#### names

```diff
! Dictionary or list names
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["names"]
```
#### values

```diff
! Dictionary values
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["values"]
```

### math

#### sin

```diff
! Sine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sin"]
```
#### cos

```diff
! Cosine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["cos"]
```
#### tan

```diff
! Tangent
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["tan"]
```
#### sinh

```diff
! Hyperbolic sine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sinh"]
```
#### cosh

```diff
! Hyperbolic cosine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["cosh"]
```
#### tanh

```diff
! Hyperbolic tangent
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["tanh"]
```
#### asin

```diff
! Arcsine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["asin"]
```
#### acos

```diff
! Arccosine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["acos"]
```
#### atan

```diff
! Arctangent
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["atan"]
```
#### asinh

```diff
! Hyperbolic arcsine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["asinh"]
```
#### acosh

```diff
! Hyperbolic arccosine
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["acosh"]
```
#### atanh

```diff
! Hyperbolic arctangent
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["atanh"]
```
#### round

```diff
! Round a number
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["round"]
```
#### floor

```diff
! Round a number down
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["floor"]
```
#### ceil

```diff
! Round a number up
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ceil"]
```
#### log

```diff
! Logarithm
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["log"]
```
#### log.e

```diff
! Hyperbolic logarithm
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["log.e"]
```
#### log.n

```diff
! Natural logarithm
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["log.n"]
```
#### fa

```diff
! Factorial
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["fa"]
```
#### fib

```diff
! Fibonacci
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["fib"]
```
#### abs

```diff
! Absolute value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["abs"]
```
#### min

```diff
! Minimum value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["min"]
```
#### max

```diff
! Maximum value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["max"]
```
#### avg

```diff
! Average value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["avg"]
```
#### sum

```diff
! Sum of values
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sum"]
```
#### hex

```diff
! Hexadecimal value to byte
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["hex"]
```
#### hex.dec

```diff
! Hexadecimal value to decimal
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["hex.dec"]
```
#### bin

```diff
! Binary value to byte
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["bin"]
```
#### bin.dec

```diff
! Binary value to decimal
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["bin.dec"]
```
#### dec

```diff
! Decimal value to byte
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["dec"]
```
#### dec.hex

```diff
! Decimal value to hexadecimal
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["dec.hex"]
```
#### dec.bin

```diff
! Decimal value to binary
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["dec.bin"]
```
#### rad

```diff
! Degree to radian
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["rad"]
```
#### deg

```diff
! Radian to degree
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["deg"]
```
#### random

```diff
! Random value
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["random"]
```
#### random.reseed

```diff
! Re-create random seed
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["random.reseed"]
```
#### random.seed

```diff
! Get random seed
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["random.seed"]
```

### time

#### time

```diff
! Time stamp in microseconds
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["time"]
```
#### time.ms

```diff
! Time stamp in milliseconds
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["time.ms"]
```
#### time.s

```diff
! Timestamp in seconds
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["time.s"]
```
#### timer

```diff
! Set timer
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["timer"]
```
#### timer.remove

```diff
! Remove timer
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["timer.remove"]
```
#### wait

```diff
! Wait time in seconds
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["wait"]
```

### crypto

#### encrypt

```diff
! Encode text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["encrypt"]
```
#### decrypt

```diff
! Decode text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["decrypt"]
```
#### hash

```diff
! Random hash
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["hash"]
```
#### uuid

```diff
! Random UUID
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["uuid"]
```
#### md5

```diff
! MD5 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["md5"]
```
#### sha1

```diff
! SHA1 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sha1"]
```
#### sha256

```diff
! SHA256 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sha256"]
```
#### sha512

```diff
! SHA512 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sha512"]
```
#### crc32

```diff
! CRC32 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["crc32"]
```
#### base64

```diff
! Base64 hash
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["base64"]
```
#### base64.decode

```diff
! Decode Base64
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["base64.decode"]
```
#### gzip

```diff
! Gzip text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["gzip"]
```
#### gzip.decode

```diff
! Decode Gzip
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["gzip.decode"]
```
#### rsa

```diff
! Encode text with RSA
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["rsa"]
```
#### rsa.decode

```diff
! Decode RSA
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["rsa.decode"]
```
#### rsa.key.public

```diff
! Get RSA public key
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["rsa.key.public"]
```
#### rsa.key.private

```diff
! Get RSA private key
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["rsa.key.private"]
```
#### ssl

```diff
! Encode text with SSL
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ssl"]
```
#### ssl.decode

```diff
! Decode SSL
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ssl.decode"]
```
#### ssl.check

```diff
! Verify SSL
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ssl.check"]
```
#### bcrypt

```diff
! Encode text with Bcrypt
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["bcrypt"]
```
#### bcrypt.check

```diff
! Verify Bcrypt
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["bcrypt.check"]
```

### format

#### void

```diff
! Encode to V O I D
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["void"]
```
#### void.decode

```diff
! Decode V O I D
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["void.decode"]
```
#### void.read

```diff
! Read V O I D file
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["void.read"]
```
#### void.write

```diff
! Write V O I D file
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["void.write"]
```
#### json

```diff
! Encode to JSON
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["json"]
```
#### json.decode

```diff
! Decode JSON
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["json.decode"]
```
#### json.read

```diff
! Read JSON file
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["json.read"]
```
#### json.write

```diff
! Write JSON file
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["json.write"]
```
#### yaml

```diff
! Encode YAML
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["yaml"]
```
#### yaml.decode

```diff
! Decode YAML
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["yaml.decode"]
```
#### csv

```diff
! Encode CSV
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["csv"]
```
#### csv.decode

```diff
! Decode CSV
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["csv.decode"]
```
#### ini

```diff
! Encode INI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ini"]
```
#### ini.decode

```diff
! Decode INI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ini.decode"]
```
#### html

```diff
! Encode HTML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["html"]
```
#### html.decode

```diff
! Decode HTML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["html.decode"]
```
#### xml

```diff
! Encode XML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["xml"]
```
#### xml.decode

```diff
! Decode XML
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["xml.decode"]
```
#### css

```diff
! Encode CSS
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["css"]
```
#### css.decode

```diff
! Decode CSS
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["css.decode"]
```

### file

#### file.exists

```diff
! File exists
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.exists"]
```
#### file.write

```diff
! Write to file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.write"]
```
#### file.read

```diff
! Read file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.read"]
```
#### file.read.list

```diff
! Read lines from file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.read.list"]
```
#### file.remove

```diff
! Remove file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.remove"]
```
#### file.move

```diff
! Move file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.move"]
```
#### file.copy

```diff
! Copy file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.copy"]
```
#### file.rename

```diff
! Rename file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.rename"]
```
#### file.info

```diff
! File information
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.info"]
```
#### file.size

```diff
! File size
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.size"]
```
#### file.permissions

```diff
! File permissions
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.permissions"]
```
#### file.readonly

```diff
! Read-only file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.readonly"]
```
#### file.hidden

```diff
! Hidden file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.hidden"]
```
#### file.modified

```diff
! File modification time
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.modified"]
```
#### file.sha256

```diff
! SHA256 file hash
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.sha256"]
```
#### file.crc32

```diff
! CRC32 file hash
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.crc32"]
```
#### file.base64

```diff
! Base64 file hash
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.base64"]
```
#### file.zip

```diff
! Compress a file into a Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.zip"]
```
#### file.zip.list

```diff
! List of files in Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.zip.list"]
```
#### file.zip.exists

```diff
! File exists in Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.zip.exists"]
```
#### file.zip.read

```diff
! Read file from Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.zip.read"]
```
#### file.zip.remove

```diff
! Remove file from Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.zip.remove"]
```
#### file.unzip

```diff
! Extract Zip archive
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.unzip"]
```
#### file.gzip

```diff
! Compress file with Gzip
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.gzip"]
```
#### file.ungzip

```diff
! Extract Gzip file
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.ungzip"]
```
#### file.link

```diff
! Create a symbolic link
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.link"]
```
#### file.link.exists

```diff
! Symbolic link exists
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.link.exists"]
```
#### file.backup

```diff
! Backup files
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["file.backup"]
```
#### dir.exists

```diff
! Directory exists
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.exists"]
```
#### dir.create

```diff
! Create directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.create"]
```
#### dir.copy

```diff
! Copy directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.copy"]
```
#### dir.move

```diff
! Move directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.move"]
```
#### dir.rename

```diff
! Rename directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.rename"]
```
#### dir.remove

```diff
! Remove directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.remove"]
```
#### dir.list

```diff
! List of files in a directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.list"]
```
#### dir.clear

```diff
! Clear directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.clear"]
```
#### dir.info

```diff
! Directory information
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.info"]
```
#### dir.size

```diff
! Directory size
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.size"]
```
#### dir.permissions

```diff
! Directory permissions
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.permissions"]
```
#### dir.readonly

```diff
! Read-only directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.readonly"]
```
#### dir.hidden

```diff
! Hidden directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.hidden"]
```
#### dir.modified

```diff
! Directory modification time
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.modified"]
```
#### dir.zip

```diff
! Compress directory
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["dir.zip"]
```
#### drive.list

```diff
! List of volumes
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["drive.list"]
```
#### drive.name

```diff
! Volume name
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["drive.name"]
```
#### drive.size

```diff
! Volume size
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["drive.size"]
```
#### drive.used

```diff
! Volume space used
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["drive.used"]
```
#### drive.free

```diff
! Volume free space
+ ask・python・js・swift・kotlin・godot・c++
```

```js
["drive.free"]
```
#### drive.mount

```diff
! Mount volume
+ local・python・js・swift・kotlin・godot・c++
```

```js
["drive.mount"]
```
#### drive.unmount

```diff
! Unmount volume
+ local・python・js・swift・kotlin・godot・c++
```

```js
["drive.unmount"]
```
#### drive.format

```diff
! Format volume
+ local・python・js・swift・kotlin・godot・c++
```

```js
["drive.format"]
```
#### path.drive

```diff
! Get volume from path
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["path.drive"]
```
#### path.dir

```diff
! Get directory from path
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["path.dir"]
```
#### path.file

```diff
! Get file from path
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["path.file"]
```
#### path.name

```diff
! Get filename from path
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["path.name"]
```
#### path.extension

```diff
! Get extension from path
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["path.extension"]
```
#### path.extension.strip

```diff
! Trim extension from path
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["path.extension.strip"]
```

### cloud

#### cloud.file

```diff
! File server
+ local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.file"]
```
#### cloud.web

```diff
! Web server
+ local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.web"]
```
#### cloud.api

```diff
! API server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.api"]
```
#### cloud.socket

```diff
! Socket server
+ local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.socket"]
```
#### cloud.websocket

```diff
! Websocket server
+ local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.websocket"]
```
#### cloud.mail

```diff
! Mail server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.mail"]
```
#### cloud.game

```diff
! Game server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.game"]
```
#### cloud.social

```diff
! Social server
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.social"]
```
#### cloud.live

```diff
! Streaming server
+ local・python・js・swift・kotlin・godot・c++
```

```js
["cloud.live"]
```

### bot

#### bot.telegram

```diff
! Telegram bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.telegram"]
```
#### bot.wechat

```diff
! Wechat bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.wechat"]
```
#### bot.x

```diff
! X bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.x"]
```
#### bot.youtube

```diff
! YouTube bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.youtube"]
```
#### bot.tiktok

```diff
! TikTok bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.tiktok"]
```
#### bot.steam

```diff
! Steam bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.steam"]
```
#### bot.binance

```diff
! Binance bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.binance"]
```
#### bot.ib

```diff
! Interactive Brokers bot
+ vapp・local・python・js・swift・kotlin・godot・c++
```

```js
["bot.ib"]
```

### request

#### request

```diff
! Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["request"]
```
#### request.post

```diff
! Post Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["request.post"]
```
#### request.put

```diff
! Put Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["request.put"]
```
#### request.delete

```diff
! Delete Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["request.delete"]
```
#### request.head

```diff
! Head Web request
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["request.head"]
```

### cookie

#### cookie

```diff
! Get Web cookies
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["cookie"]
```
#### cookie.remove

```diff
! Delete Web cookies
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["cookie.remove"]
```

### sql

#### sql

```diff
! SQL query
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sql"]
```
#### sql.connect

```diff
! Connect to SQL server
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.connect"]
```
#### sql.disconnet

```diff
! Disconnect from SQL server
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.disconnet"]
```
#### sql.user

```diff
! SQL user
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.user"]
```
#### sql.user.list

```diff
! SQL user list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.user.list"]
```
#### sql.user.remove

```diff
! SQL remove user
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.user.remove"]
```
#### sql.db

```diff
! SQL database
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.db"]
```
#### sql.db.list

```diff
! SQL database list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.db.list"]
```
#### sql.db.remove

```diff
! SQL remove database
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.db.remove"]
```
#### sql.db.size

```diff
! SQL database size
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.db.size"]
```
#### sql.table

```diff
! SQL table
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.table"]
```
#### sql.table.list

```diff
! SQL table list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.table.list"]
```
#### sql.table.remove

```diff
! SQL remove table
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.table.remove"]
```
#### sql.field

```diff
! SQL field
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.field"]
```
#### sql.field.list

```diff
! SQL field list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.field.list"]
```
#### sql.field.remove

```diff
! SQL remove field
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.field.remove"]
```
#### sql.index

```diff
! SQL index
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.index"]
```
#### sql.index.list

```diff
! SQL index list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.index.list"]
```
#### sql.index.remove

```diff
! SQL remove index
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.index.remove"]
```
#### sql.function

```diff
! SQL function
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.function"]
```
#### sql.function.list

```diff
! SQL function list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.function.list"]
```
#### sql.function.remove

```diff
! SQL remove function
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.function.remove"]
```
#### sql.view

```diff
! SQL view
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.view"]
```
#### sql.view.list

```diff
! SQL view list
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.view.list"]
```
#### sql.view.remove

```diff
! SQL remove a view
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.view.remove"]
```
#### sql.get

```diff
! SQL get one result
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.get"]
```
#### sql.all

```diff
! SQL get all results
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.all"]
```
#### sql.cursor

```diff
! SQL cursor
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.cursor"]
```
#### sql.transaction

```diff
! SQL start transaction
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.transaction"]
```
#### sql.commit

```diff
! SQL send transaction
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.commit"]
```
#### sql.rollback

```diff
! SQL cancel transaction
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["sql.rollback"]
```

### os

#### os.name

```diff
! Operating system name
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.name"]
```
#### os.version

```diff
! Operating system version
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.version"]
```
#### os.username

```diff
! User name
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.username"]
```
#### os.desktop

```diff
! Check that it’s desktop
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.desktop"]
```
#### os.mobile

```diff
! Check that it’s mobile device
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.mobile"]
```
#### os.web

```diff
! Check that it’s Web
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.web"]
```
#### os.windows

```diff
! Check that it’s Windows
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.windows"]
```
#### os.macos

```diff
! Check that it's macOS
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.macos"]
```
#### os.ios

```diff
! Check that it's iOS
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.ios"]
```
#### os.ipados

```diff
! Check that it's iPadOS
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.ipados"]
```
#### os.watchos

```diff
! Check that it's watchOS
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.watchos"]
```
#### os.tvos

```diff
! Check that it's tvOS
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.tvos"]
```
#### os.android

```diff
! Check that it's Android
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.android"]
```
#### os.nix

```diff
! Check that it’s Unix-like
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["os.nix"]
```

### device

#### cpu.name

```diff
! Processor name
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["cpu.name"]
```
#### cpu.cores

```diff
! Number of processor cores
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["cpu.cores"]
```
#### memory.size

```diff
! Memory size
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["memory.size"]
```
#### memory.free

```diff
! Memory Free
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["memory.free"]
```
#### memory.used

```diff
! Memory used
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["memory.used"]
```
#### memory.available

```diff
! Memory available
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["memory.available"]
```

### gps

#### gps

```diff
! Get GPS coordinates
+ ask・swift・kotlin・godot・c++
```

```js
["gps"]
```

### sensor

#### speed

```diff
! Get speed
+ ask・swift・kotlin・godot・c++
```

```js
["speed"]
```
#### tilt

```diff
! Get tilt
+ ask・swift・kotlin・godot・c++
```

```js
["tilt"]
```
#### compass

```diff
! Get compass direction
+ ask・swift・kotlin・godot・c++
```

```js
["compass"]
```
#### motion

```diff
! Get motion type
+ ask・swift・kotlin・godot・c++
```

```js
["motion"]
```

### camera

#### camera

```diff
! Get camera image
+ ask・swift・kotlin・godot・c++
```

```js
["camera"]
```
#### gallery

```diff
! Get gallery image
+ ask・swift・kotlin・godot・c++
```

```js
["gallery"]
```

### contacts

#### contacts

```diff
! Get contacts
+ ask・swift・kotlin・godot・c++
```

```js
["contacts"]
```

### calendar

#### calendar

```diff
! Get calendar
+ ask・swift・kotlin・godot・c++
```

```js
["calendar"]
```

### health

#### health

```diff
! Get health data
+ ask・swift・kotlin・godot・c++
```

```js
["health"]
```

### flashlight

#### flashlight

```diff
! Flashlight
+ ask・swift・kotlin・godot・c++
```

```js
["flashlight"]
```

### mic

#### mic

```diff
! Microphone
+ ask・swift・kotlin・godot・c++
```

```js
["mic"]
```

### notification

#### notification

```diff
! Receive notifications
+ ask・swift・kotlin・godot・c++
```

```js
["notification"]
```
#### notification.token

```diff
! Notification token
+ ask・swift・kotlin・godot・c++
```

```js
["notification.token"]
```
#### notification.send

```diff
! Send notification
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["notification.send"]
```

### key

#### key

```diff
! Assign key action
+ safe・js・swift・kotlin・godot・c++
```

```js
["key"]
```
#### key.remove

```diff
! Delete a key action
+ safe・js・swift・kotlin・godot・c++
```

```js
["key.remove"]
```
#### key.press

```diff
! Start a key action
+ safe・js・swift・kotlin・godot・c++
```

```js
["key.press"]
```
#### key.enable

```diff
! Enable key action
+ safe・js・swift・kotlin・godot・c++
```

```js
["key.enable"]
```
#### key.disable

```diff
! Disable key action
+ safe・js・swift・kotlin・godot・c++
```

```js
["key.disable"]
```

### keyboard

#### keyboard

```diff
! On-screen keyboard
+ safe・js・swift・kotlin・godot・c++
```

```js
["keyboard"]
```
#### keyboard.height

```diff
! Screen keyboard height
+ safe・js・swift・kotlin・godot・c++
```

```js
["keyboard.height"]
```

### mouse

#### mouse

```diff
! Show mouse
+ safe・js・swift・kotlin・godot・c++
```

```js
["mouse"]
```
#### mouse.hide

```diff
! Hide mouse
+ safe・js・swift・kotlin・godot・c++
```

```js
["mouse.hide"]
```
#### mouse.lock

```diff
! Lock mouse
+ safe・js・swift・kotlin・godot・c++
```

```js
["mouse.lock"]
```
#### mouse.capture

```diff
! Capture mouse
+ safe・js・swift・kotlin・godot・c++
```

```js
["mouse.capture"]
```
#### mouse.confine

```diff
! Limit mouse movement
+ safe・js・swift・kotlin・godot・c++
```

```js
["mouse.confine"]
```
#### mouse.position

```diff
! Get mouse coordinates
+ safe・js・swift・kotlin・godot・c++
```

```js
["mouse.position"]
```
#### mouse.shape

```diff
! Mouse pointer shape
+ safe・js・swift・kotlin・godot・c++
```

```js
["mouse.shape"]
```

### gamepad

#### gamepad.axis

```diff
! Gamepad stick deflection
+ safe・js・swift・kotlin・godot・c++
```

```js
["gamepad.axis"]
```
#### gamepad.vibrate

```diff
! Gamepad vibration
+ safe・js・swift・kotlin・godot・c++
```

```js
["gamepad.vibrate"]
```

### clipboard

#### clipboard

```diff
! Clipboard
+ safe・js・swift・kotlin・godot・c++
```

```js
["clipboard"]
```
#### clipboard.clear

```diff
! Clear clipboard
+ safe・js・swift・kotlin・godot・c++
```

```js
["clipboard.clear"]
```

### voice

#### voice

```diff
! Read text with voice
+ safe・js・swift・kotlin・godot・c++
```

```js
["voice"]
```
#### voice.list

```diff
! Voice list
+ safe・js・swift・kotlin・godot・c++
```

```js
["voice.list"]
```
#### voice.stop

```diff
! Stop text reading
+ safe・js・swift・kotlin・godot・c++
```

```js
["voice.stop"]
```
#### voice.pause

```diff
! Pause / continue text reading
+ safe・js・swift・kotlin・godot・c++
```

```js
["voice.pause"]
```

### convert

#### convert

```diff
! Convert from one format to another
+ vapp・python・js・swift・kotlin・godot・c++
```

```js
["convert"]
```

### image

#### image

```diff
! Create image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image"]
```
#### image.read

```diff
! Read image from file
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.read"]
```
#### image.write

```diff
! Write image to file
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.write"]
```
#### image.size

```diff
! Resize image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.size"]
```
#### image.crop

```diff
! Crop image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.crop"]
```
#### image.square

```diff
! Crop image to square
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.square"]
```
#### image.rotate

```diff
! Rotate image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.rotate"]
```
#### image.flip.h

```diff
! Reflect image horizontally
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.flip.h"]
```
#### image.flip.v

```diff
! Reflect image vertically
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.flip.v"]
```
#### image.tint

```diff
! Tint the image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.tint"]
```
#### image.gray

```diff
! Convert image to grayscale
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.gray"]
```
#### image.text

```diff
! Add text to image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.text"]
```
#### image.image

```diff
! Add image to image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.image"]
```
#### image.draw

```diff
! Add drawing to image
+ safe・js・swift・kotlin・godot・c++
```

```js
["image.draw"]
```

### video

#### video

```diff
! Create video
+ safe・js・swift・kotlin・godot・c++
```

```js
["video"]
```
#### video.read

```diff
! Read video from file
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.read"]
```
#### video.write

```diff
! Write video to file
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.write"]
```
#### video.size

```diff
! Video size
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.size"]
```
#### video.rate

```diff
! Video frame rate
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.rate"]
```
#### video.rotate

```diff
! Rotate video
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.rotate"]
```
#### video.flip.h

```diff
! Reflect video horizontally
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.flip.h"]
```
#### video.flip.v

```diff
! Reflect video vertically
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.flip.v"]
```
#### video.clip

```diff
! Video clip
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.clip"]
```
#### video.speed

```diff
! Video speed
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.speed"]
```
#### video.reverse

```diff
! Change video direction
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.reverse"]
```
#### video.text

```diff
! Add text to video
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.text"]
```
#### video.image

```diff
! Add image to video
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.image"]
```
#### video.sound

```diff
! Add sound to video
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.sound"]
```
#### video.video

```diff
! Add video to video
+ safe・js・swift・kotlin・godot・c++
```

```js
["video.video"]
```

### model

#### model

```diff
! Create 3D model
+ safe・js・swift・kotlin・godot・c++
```

```js
["model"]
```
#### model.read

```diff
! Read 3D model from file
+ safe・js・swift・kotlin・godot・c++
```

```js
["model.read"]
```
#### model.write

```diff
! Write 3D model to file
+ safe・js・swift・kotlin・godot・c++
```

```js
["model.write"]
```
#### model.animate

```diff
! Animate 3D model
+ safe・js・swift・kotlin・godot・c++
```

```js
["model.animate"]
```
#### model.texture

```diff
! Apply texture to 3D model
+ safe・js・swift・kotlin・godot・c++
```

```js
["model.texture"]
```

### sound

#### sound

```diff
! Create sound
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound"]
```
#### sound.read

```diff
! Read sound from file
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.read"]
```
#### sound.write

```diff
! Write sound to file
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.write"]
```
#### sound.list

```diff
! Current played sounds
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.list"]
```
#### sound.remove

```diff
! Remove sound
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.remove"]
```
#### sound.volume

```diff
! Sound volume
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.volume"]
```
#### sound.speed

```diff
! Sound playback speed
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.speed"]
```
#### sound.clip

```diff
! Sound clip
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.clip"]
```
#### sound.sound

```diff
! Add sound to sound
+ safe・js・swift・kotlin・godot・c++
```

```js
["sound.sound"]
```

### music

#### music

```diff
! Add music
+ safe・js・swift・kotlin・godot・c++
```

```js
["music"]
```
#### music.stop

```diff
! Stop music
+ safe・js・swift・kotlin・godot・c++
```

```js
["music.stop"]
```
#### music.pause

```diff
! Pause / continue music
+ safe・js・swift・kotlin・godot・c++
```

```js
["music.pause"]
```
#### music.volume

```diff
! Music sound volume
+ safe・js・swift・kotlin・godot・c++
```

```js
["music.volume"]
```

### volume

#### volume

```diff
! Master volume
+ safe・js・swift・kotlin・godot・c++
```

```js
["volume"]
```

### screen

#### screen.count

```diff
! Number of screens
+ safe・js・swift・kotlin・godot・c++
```

```js
["screen.count"]
```
#### screen.list

```diff
! List of screens
+ safe・js・swift・kotlin・godot・c++
```

```js
["screen.list"]
```
#### screen.info

```diff
! Screen information
+ safe・js・swift・kotlin・godot・c++
```

```js
["screen.info"]
```
#### size

```diff
! Screen size
+ safe・js・swift・kotlin・godot・c++
```

```js
["size"]
```
#### orientation

```diff
! Screen orientation
+ safe・js・swift・kotlin・godot・c++
```

```js
["orientation"]
```
#### landscape

```diff
! Landscape orientation
+ safe・js・swift・kotlin・godot・c++
```

```js
["landscape"]
```
#### portrait

```diff
! Portrait orientation
+ safe・js・swift・kotlin・godot・c++
```

```js
["portrait"]
```
#### rate

```diff
! Screen frame rate
+ safe・js・swift・kotlin・godot・c++
```

```js
["rate"]
```
#### pixel

```diff
! Get screen pixel color
+ safe・js・swift・kotlin・godot・c++
```

```js
["pixel"]
```
#### symbol

```diff
! Get screen symbol
+ safe・js・swift・kotlin・godot・c++
```

```js
["symbol"]
```
#### dpi

```diff
! Dots per inch
+ safe・js・swift・kotlin・godot・c++
```

```js
["dpi"]
```
#### dark

```diff
! Dark mode
+ safe・js・swift・kotlin・godot・c++
```

```js
["dark"]
```
#### touch

```diff
! Touchscreen
+ safe・js・swift・kotlin・godot・c++
```

```js
["touch"]
```
#### screenshot

```diff
! Screenshot
+ safe・swift・kotlin・godot・c++
```

```js
["screenshot"]
```
#### screen.record

```diff
! Record screen
+ safe・swift・kotlin・godot・c++
```

```js
["screen.record"]
```
#### screen.stop

```diff
! Stop screen recording
+ safe・swift・kotlin・godot・c++
```

```js
["screen.stop"]
```

### ui

#### ui

```diff
! UI element
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui"]
```
#### bg

```diff
! Background
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["bg"]
```
#### show

```diff
! Show UI
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["show"]
```
#### hide

```diff
! Hide UI
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["hide"]
```
#### visible

```diff
! UI visibility
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["visible"]
```
#### enable

```diff
! Enable UI
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["enable"]
```
#### disable

```diff
! Disable UI
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["disable"]
```
#### enabled

```diff
! Check if UI is enabled
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["enabled"]
```
#### focus

```diff
! Move focus to UI
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["focus"]
```
#### scale

```diff
! Scale UI
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["scale"]
```
#### ui.text

```diff
! UI text
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.text"]
```
#### ui.image

```diff
! UI image
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.image"]
```
#### ui.button

```diff
! UI button
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.button"]
```
#### ui.divider

```diff
! UI separator
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.divider"]
```
#### ui.video

```diff
! UI video
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.video"]
```
#### ui.select

```diff
! UI selection
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.select"]
```
#### ui.switch

```diff
! UI switch
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.switch"]
```
#### ui.progress

```diff
! UI progress bar
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.progress"]
```
#### ui.slider

```diff
! UI slider
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.slider"]
```
#### ui.edit

```diff
! UI text editor
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.edit"]
```
#### ui.chart

```diff
! UI chart
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.chart"]
```
#### ui.split.h

```diff
! UI horizontal separator
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.split.h"]
```
#### ui.split.v

```diff
! UI vertical separator
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.split.v"]
```
#### ui.list

```diff
! UI list
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.list"]
```
#### ui.tile

```diff
! UI tile
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.tile"]
```
#### ui.color

```diff
! UI color
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.color"]
```
#### ui.date

```diff
! UI date
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.date"]
```
#### ui.drop

```diff
! UI drop down content
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.drop"]
```
#### ui.menu

```diff
! UI menu
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.menu"]
```
#### ui.menu.context

```diff
! UI context menu
+ safe・python・js・swift・kotlin・godot・c++
```

```js
["ui.menu.context"]
```

### window

#### window

```diff
! Create window
+ safe・js・swift・kotlin・godot・c++
```

```js
["window"]
```
#### window.list

```diff
! Window list
+ safe・js・swift・kotlin・godot・c++
```

```js
["window.list"]
```
#### window.info

```diff
! Window information
+ safe・js・swift・kotlin・godot・c++
```

```js
["window.info"]
```
#### title

```diff
! Window title
+ safe・js・swift・kotlin・godot・c++
```

```js
["title"]
```
#### icon

```diff
! Window icon
+ safe・js・swift・kotlin・godot・c++
```

```js
["icon"]
```
#### size

```diff
! Window size
+ safe・js・swift・kotlin・godot・c++
```

```js
["size"]
```
#### size.max

```diff
! Maximum window size
+ safe・js・swift・kotlin・godot・c++
```

```js
["size.max"]
```
#### size.min

```diff
! Minimum window size
+ safe・js・swift・kotlin・godot・c++
```

```js
["size.min"]
```
#### position

```diff
! Window position
+ safe・js・swift・kotlin・godot・c++
```

```js
["position"]
```
#### direction

```diff
! Window text direction
+ safe・js・swift・kotlin・godot・c++
```

```js
["direction"]
```
#### attention

```diff
! Window attention
+ safe・js・swift・kotlin・godot・c++
```

```js
["attention"]
```
#### top

```diff
! Top of all windows
+ safe・js・swift・kotlin・godot・c++
```

```js
["top"]
```
#### foreground

```diff
! Foreground window
+ safe・js・swift・kotlin・godot・c++
```

```js
["foreground"]
```
#### unfocusable

```diff
! Do not take the focus of the window
+ safe・js・swift・kotlin・godot・c++
```

```js
["unfocusable"]
```
#### unresizable

```diff
! Do not resize window
+ safe・js・swift・kotlin・godot・c++
```

```js
["unresizable"]
```
#### center

```diff
! Center the window on the screen
+ safe・js・swift・kotlin・godot・c++
```

```js
["center"]
```
#### fullscreen

```diff
! Full screen window
+ safe・js・swift・kotlin・godot・c++
```

```js
["fullscreen"]
```
#### drop

```diff
! Drop content to window
+ safe・js・swift・kotlin・godot・c++
```

```js
["drop"]
```
#### border

```diff
! Window border
+ safe・js・swift・kotlin・godot・c++
```

```js
["border"]
```
#### maximized

```diff
! Maximize window
+ safe・js・swift・kotlin・godot・c++
```

```js
["maximized"]
```
#### minimized

```diff
! Minimize window
+ safe・js・swift・kotlin・godot・c++
```

```js
["minimized"]
```
#### exclusive

```diff
! Make window exclusive
+ safe・js・swift・kotlin・godot・c++
```

```js
["exclusive"]
```
#### vsync

```diff
! Vertical window synchronization
+ safe・js・swift・kotlin・godot・c++
```

```js
["vsync"]
```
#### fps

```diff
! Window FPS
+ safe・js・swift・kotlin・godot・c++
```

```js
["fps"]
```

### dialog

#### dialog.file

```diff
! File selection
+ safe・js・swift・kotlin・godot・c++
```

```js
["dialog.file"]
```
#### dialog.color

```diff
! Color selection
+ safe・js・swift・kotlin・godot・c++
```

```js
["dialog.color"]
```
#### dialog.date

```diff
! Date selection
+ safe・js・swift・kotlin・godot・c++
```

```js
["dialog.date"]
```
#### dialog.list

```diff
! Select from list
+ safe・js・swift・kotlin・godot・c++
```

```js
["dialog.list"]
```

### effect

#### effect

```diff
! Add effect
+ safe・js・swift・kotlin・godot・c++
```

```js
["effect"]
```
#### effect.list

```diff
! List of effects
+ safe・js・swift・kotlin・godot・c++
```

```js
["effect.list"]
```
#### effect.remove

```diff
! Remove effect
+ safe・js・swift・kotlin・godot・c++
```

```js
["effect.remove"]
```

### game

#### vn

```diff
! Create visual novel
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["vn"]
```
#### 2d

```diff
! Create 2D game
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["2d"]
```
#### 3d

```diff
! Create 3D game
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["3d"]
```
#### menu

```diff
! Create game menu
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["menu"]
```
#### say

```diff
! Say text
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["say"]
```
#### say.skip

```diff
! Skip text
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["say.skip"]
```
#### route

```diff
! Offer to select a root
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["route"]
```
#### route.remove

```diff
! Remove root selection
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["route.remove"]
```
#### route.check

```diff
! Check root
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["route.check"]
```
#### route.select

```diff
! Select root
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["route.select"]
```
#### route.repeat

```diff
! Repeat root selection
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["route.repeat"]
```
#### route.skip

```diff
! Skip root selection
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["route.skip"]
```
#### character

```diff
! Create a character
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["character"]
```
#### come

```diff
! Character arrived
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["come"]
```
#### leave

```diff
! Character left
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["leave"]
```
#### change

```diff
! Character changed
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["change"]
```
#### object

```diff
! Add an object to the map
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["object"]
```
#### shoot

```diff
! Character shot
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["shoot"]
```
#### move

```diff
! Character movement
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["move"]
```
#### jump

```diff
! Jump
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["jump"]
```
#### crouch

```diff
! Crouch
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["crouch"]
```
#### drop

```diff
! Drop
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["drop"]
```
#### look

```diff
! Look around
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["look"]
```
#### hud

```diff
! Interface
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["hud"]
```
#### hud.map

```diff
! Map
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["hud.map"]
```
#### hud.inventory

```diff
! Inventory
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["hud.inventory"]
```
#### snd

```diff
! Spatial sound
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["snd"]
```
#### light

```diff
! Spatial light
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["light"]
```
#### cam

```diff
! Spatial camera
+ vapp・safe・js・swift・kotlin・godot・c++
```

```js
["cam"]
```

### ai

#### ai.chat

```diff
! Communicate with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.chat"]
```
#### ai.image

```diff
! Create AI image
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.image"]
```
#### ai.video

```diff
! Create AI video
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.video"]
```
#### ai.music

```diff
! Create AI music
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.music"]
```
#### ai.sound

```diff
! Create AI sound
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.sound"]
```
#### ai.say

```diff
! Create AI speech
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.say"]
```
#### ai.2d

```diff
! Create AI 2D asset
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.2d"]
```
#### ai.3d

```diff
! Create AI 3D asset
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.3d"]
```
#### ai.character

```diff
! Create AI character
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.character"]
```
#### ai.clean

```diff
! Clean up image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.clean"]
```
#### ai.resize

```diff
! Resize image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.resize"]
```
#### ai.color

```diff
! Colorize image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.color"]
```
#### ai.style

```diff
! Change image style with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.style"]
```
#### ai.translate

```diff
! Translate text with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.translate"]
```
#### ai.recognize.text

```diff
! Recognize text with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.recognize.text"]
```
#### ai.recognize.image

```diff
! Recognize image with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.recognize.image"]
```
#### ai.recognize.video

```diff
! Recognize video with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.recognize.video"]
```
#### ai.recognize.motion

```diff
! Recognize motion with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.recognize.motion"]
```
#### ai.capture.voice

```diff
! Capture voice with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.capture.voice"]
```
#### ai.capture.face

```diff
! Capture facial expressions with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.capture.face"]
```
#### ai.capture.motion

```diff
! Capture motion with AI
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["ai.capture.motion"]
```

### social

#### social.signin

```diff
! Authorization
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["social.signin"]
```
#### social.signup

```diff
! Registration
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["social.signup"]
```
#### social.signout

```diff
! Logout
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["social.signout"]
```
#### social.restore

```diff
! Restore login
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["social.restore"]
```
#### social

```diff
! Social content
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["social"]
```
#### social.send

```diff
! Send content
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["social.send"]
```
#### social.buy

```diff
! Purchase
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["social.buy"]
```

### tech

#### light.on

```diff
! Turn lamp on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["light.on"]
```
#### light.off

```diff
! Turn lamp off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["light.off"]
```
#### power.on

```diff
! Power on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["power.on"]
```
#### power.off

```diff
! Turn power off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["power.off"]
```
#### power.timer

```diff
! Set timer for power
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["power.timer"]
```
#### lock.open

```diff
! Open the lock
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["lock.open"]
```
#### lock.close

```diff
! Close the lock
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["lock.close"]
```
#### lock.code

```diff
! Set the code on the lock
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["lock.code"]
```
#### dron.move

```diff
! Drone movement
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.move"]
```
#### dron.up

```diff
! Raise the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.up"]
```
#### dron.down

```diff
! Lower the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.down"]
```
#### dron.left

```diff
! Move the drone to the left
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.left"]
```
#### dron.right

```diff
! Move the drone to the right
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.right"]
```
#### dron.go

```diff
! Move the drone forward
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.go"]
```
#### dron.stop

```diff
! Stop drone movement
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.stop"]
```
#### dron.jump

```diff
! Jump the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.jump"]
```
#### dron.crouch

```diff
! Crouch the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.crouch"]
```
#### dron.open

```diff
! Open the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.open"]
```
#### dron.close

```diff
! Close the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.close"]
```
#### dron.rotate

```diff
! Turn the drone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.rotate"]
```
#### dron.camera

```diff
! Drone camera
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.camera"]
```
#### dron.camera.rotate

```diff
! Rotate drone camera
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.camera.rotate"]
```
#### dron.camera.on

```diff
! Turn drone camera on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.camera.on"]
```
#### dron.camera.off

```diff
! Turn drone camera off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.camera.off"]
```
#### dron.camera.record

```diff
! Record drone camera video
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.camera.record"]
```
#### dron.camera.record.stop

```diff
! Stop drone camera recording
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.camera.record.stop"]
```
#### dron.hand.open

```diff
! Open the drone arm
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.hand.open"]
```
#### dron.hand.close

```diff
! Close the drone arm
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.hand.close"]
```
#### dron.hand.move

```diff
! Drone hand movement
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.hand.move"]
```
#### dron.hand.gesture

```diff
! Drone hand gesture
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.hand.gesture"]
```
#### dron.sound

```diff
! Drone speaker
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.sound"]
```
#### dron.volume

```diff
! Drone speaker sound volume
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.volume"]
```
#### dron.mic

```diff
! Drone microphone
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.mic"]
```
#### dron.mic.on

```diff
! Drone microphone on
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.mic.on"]
```
#### dron.mic.off

```diff
! Drone microphone off
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.mic.off"]
```
#### dron.mic.record

```diff
! Drone microphone audio recording
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
["dron.mic.record"]
```
#### dron.mic.record.stop

```diff
! Stop recording drone microphone audio
+ vapp・safe・python・js・swift・kotlin・godot・c++
```

```js
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
