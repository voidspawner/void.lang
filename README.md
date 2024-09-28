# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **V O I D** or **JSON format**. It is used as a replacement for the standard Bash・CMD・etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one V O I D or JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

**The project is in the process of development.**

<img src="https://i.imgur.com/kx2UcUh.jpg" width="100%">

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
```python
# crypto.py
encrypted = void.encrypt('Hi World :D')
print(void.decrypt(encrypted.text, encrypted.key))
```
```javascript
[
  ["file.read", "crypto.py"],
  "code"
]
```

## How to Use

1. Download **V O I D lang**
2. Create your first vapp (V O I D app) in **run.json** or other JSON file
3. Launch vapp with **V O I D lang**
   ```console
   python void.py vapp.json
   ```

   ##### Tip for Linux・macOS: add alias to ~/.bashrc ・ ~/.zshrc ・ ~/.bash_profile (macOS)
   ```console
   alias void="python /path/to/void.py"
   ```

   ##### Tip for Windows: use alias in command line
   ```console
   doskey void=python /path/to/void.py
   ```
   ```console
   void vapp.json
   ```

   ##### Tip for Swift・Kotlin・C++: embed the vapp in it and compile it into an executable
   ```console
   swiftc void.swift
   ```
   ```console
   kotlinc void.kt
   ```
   ```console
   clang++ void.cpp -o void.exe
   ```


## How to Use Game Engine

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

   You can use the **Exporter** inside the **V O I D spawner** game to export your game to all platforms ⌜**Windows**・**macOS**・**Linux**・**Android**・**iOS**・**Web**・**Xbox**・**Switch**・**PlayStation**⌟

Alternative:

1. Download **V O I D lang**
2. Import **void.gd**・**void.cpp** into the **Godot**・**Unreal Engine**
3. Create your first game in **run.json** file
4. Export the game to available platforms
5. Sell your game or share with friends

## Actions

[value](#value)・
[expression](#expression)・
[control](#control)・
[text](#text)・
[list](#list)・
[math](#math)・
[time](#time)・
[crypto](#crypto)・
[format](#format)・
[file](#file)・
[cloud](#cloud)・
[bot](#bot)・
[request](#request)・
[cookie](#cookie)・
[sql](#sql)・
[os](#os)・
[device](#device)・
[gps](#gps)・
[sensor](#sensor)・
[photo](#photo)・
[contacts](#contacts)・
[calendar](#calendar)・
[flashlight](#flashlight)・
[health](#health)・
[microphone](#microphone)・
[notification](#notification)・
[key](#key)・
[keyboard](#keyboard)・
[mouse](#mouse)・
[gamepad](#gamepad)・
[clipboard](#clipboard)・
[say](#say)・
[convert](#convert)・
[image](#image)・
[video](#video)・
[model](#model)・
[sound](#sound)・
[music](#music)・
[volume](#volume)・
[screen](#screen)・
[ui](#ui)・
[window](#window)・
[dialog](#dialog)・
[effect](#effect)・
[game](#game)・
[vn](#vn)・
[2d](#2d)・
[3d](#3d)・
[ai](#ai)・
[social](#social)・
[tech](#tech)

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

```
Count of actions: 604
```

## Detail

### value

#### get
```javascript
["get"]
```
#### set
```javascript
["set"]
```
#### remove
```javascript
["remove"]
```
#### type
```javascript
["type"]
```
#### bool
```javascript
["bool"]
```
#### number
```javascript
["number"]
```
#### text
```javascript
["text"]
```
#### list
```javascript
["list"]
```
#### alias
```javascript
["alias"]
```
### expression

#### +
```javascript
["+"]
```
#### -
```javascript
["-"]
```
#### *
```javascript
["*"]
```
#### /
```javascript
["/"]
```
#### //
```javascript
["//"]
```
#### %
```javascript
["%"]
```
#### **
```javascript
["**"]
```
#### !
```javascript
["!"]
```
#### &
```javascript
["&"]
```
#### |
```javascript
["|"]
```
#### ^
```javascript
["^"]
```
#### >>
```javascript
[">>"]
```
#### <<
```javascript
["<<"]
```
#### +=
```javascript
["+="]
```
#### -=
```javascript
["-="]
```
#### *=
```javascript
["*="]
```
#### /=
```javascript
["/="]
```
#### //=
```javascript
["//="]
```
#### %=
```javascript
["%="]
```
#### **=
```javascript
["**="]
```
#### !=
```javascript
["!="]
```
#### &=
```javascript
["&="]
```
#### |=
```javascript
["|="]
```
#### ^=
```javascript
["^="]
```
#### >>=
```javascript
[">>="]
```
#### <<=
```javascript
["<<="]
```
#### and
```javascript
["and"]
```
#### or
```javascript
["or"]
```
#### xor
```javascript
["xor"]
```
#### not
```javascript
["not"]
```
#### in
```javascript
["in"]
```
#### not in
```javascript
["not in"]
```
#### is
```javascript
["is"]
```
#### not is
```javascript
["not is"]
```
### control

#### ?
```javascript
["?"]
```
#### ??
```javascript
["??"]
```
#### o
```javascript
["o"]
```
#### x
```javascript
["x"]
```
#### >>>
```javascript
[">>>"]
```
#### <<<
```javascript
["<<<"]
```
#### _
```javascript
["_"]
```
#### .
```javascript
["."]
```
#### ..
```javascript
[".."]
```
#### action
```javascript
["action"]
```
#### action.open
```javascript
["action.open"]
```
#### X
```javascript
["X"]
```
#### xx
```javascript
["xx"]
```
#### open
```javascript
["open"]
```
#### shell
```javascript
["shell"]
```
#### shell.open
```javascript
["shell.open"]
```
#### code
```javascript
["code"]
```
#### code.python
```javascript
["code.python"]
```
#### i
```javascript
["i"]
```
#### w
```javascript
["w"]
```
#### e
```javascript
["e"]
```
#### d
```javascript
["d"]
```
#### t
```javascript
["t"]
```
#### export
```javascript
["export"]
```
#### update
```javascript
["update"]
```
#### test
```javascript
["test"]
```
### text

#### lower
```javascript
["lower"]
```
#### upper
```javascript
["upper"]
```
#### starts
```javascript
["starts"]
```
#### ends
```javascript
["ends"]
```
#### strip
```javascript
["strip"]
```
#### strip.begin
```javascript
["strip.begin"]
```
#### strip.end
```javascript
["strip.end"]
```
#### replace
```javascript
["replace"]
```
#### find
```javascript
["find"]
```
#### similar
```javascript
["similar"]
```
#### part
```javascript
["part"]
```
#### split
```javascript
["split"]
```
#### join
```javascript
["join"]
```
#### regex
```javascript
["regex"]
```
#### regex.replace
```javascript
["regex.replace"]
```
#### escape
```javascript
["escape"]
```
#### escape.html
```javascript
["escape.html"]
```
#### escape.sql
```javascript
["escape.sql"]
```
#### escape.url
```javascript
["escape.url"]
```
#### escape.json
```javascript
["escape.json"]
```
#### escape.void
```javascript
["escape.void"]
```
#### unescape
```javascript
["unescape"]
```
#### unescape.html
```javascript
["unescape.html"]
```
#### unescape.sql
```javascript
["unescape.sql"]
```
#### unescape.url
```javascript
["unescape.url"]
```
#### unescape.json
```javascript
["unescape.json"]
```
#### unescape.void
```javascript
["unescape.void"]
```
#### num
```javascript
["num"]
```
#### pad
```javascript
["pad"]
```
#### date
```javascript
["date"]
```
#### letters
```javascript
["letters"]
```
#### words
```javascript
["words"]
```
#### sentences
```javascript
["sentences"]
```
#### lines
```javascript
["lines"]
```
### list

#### push
```javascript
["push"]
```
#### pop
```javascript
["pop"]
```
#### insert
```javascript
["insert"]
```
#### reverse
```javascript
["reverse"]
```
#### shuffle
```javascript
["shuffle"]
```
#### sort
```javascript
["sort"]
```
#### map
```javascript
["map"]
```
#### reduce
```javascript
["reduce"]
```
#### names
```javascript
["names"]
```
#### values
```javascript
["values"]
```
#### clear
```javascript
["clear"]
```
### math

#### sin
```javascript
["sin"]
```
#### cos
```javascript
["cos"]
```
#### tan
```javascript
["tan"]
```
#### sinh
```javascript
["sinh"]
```
#### cosh
```javascript
["cosh"]
```
#### tanh
```javascript
["tanh"]
```
#### asin
```javascript
["asin"]
```
#### acos
```javascript
["acos"]
```
#### atan
```javascript
["atan"]
```
#### asinh
```javascript
["asinh"]
```
#### acosh
```javascript
["acosh"]
```
#### atanh
```javascript
["atanh"]
```
#### round
```javascript
["round"]
```
#### floor
```javascript
["floor"]
```
#### ceil
```javascript
["ceil"]
```
#### log
```javascript
["log"]
```
#### pow
```javascript
["pow"]
```
#### fac
```javascript
["fac"]
```
#### fib
```javascript
["fib"]
```
#### abs
```javascript
["abs"]
```
#### min
```javascript
["min"]
```
#### max
```javascript
["max"]
```
#### avg
```javascript
["avg"]
```
#### sum
```javascript
["sum"]
```
#### hex
```javascript
["hex"]
```
#### bin
```javascript
["bin"]
```
#### dec
```javascript
["dec"]
```
#### rad
```javascript
["rad"]
```
#### deg
```javascript
["deg"]
```
#### random
```javascript
["random"]
```
#### random.reseed
```javascript
["random.reseed"]
```
#### random.seed
```javascript
["random.seed"]
```
### time

#### time
```javascript
["time"]
```
#### time.ms
```javascript
["time.ms"]
```
#### time.s
```javascript
["time.s"]
```
#### timer
```javascript
["timer"]
```
#### timer.remove
```javascript
["timer.remove"]
```
#### timepast
```javascript
["timepast"]
```
#### wait
```javascript
["wait"]
```
### crypto

#### encrypt
```javascript
["encrypt"]
```
#### decrypt
```javascript
["decrypt"]
```
#### hash
```javascript
["hash"]
```
#### uuid
```javascript
["uuid"]
```
#### md5
```javascript
["md5"]
```
#### sha1
```javascript
["sha1"]
```
#### sha256
```javascript
["sha256"]
```
#### sha512
```javascript
["sha512"]
```
#### crc32
```javascript
["crc32"]
```
#### base64
```javascript
["base64"]
```
#### base64.decode
```javascript
["base64.decode"]
```
#### gzip
```javascript
["gzip"]
```
#### gzip.decode
```javascript
["gzip.decode"]
```
#### rsa
```javascript
["rsa"]
```
#### rsa.decode
```javascript
["rsa.decode"]
```
#### rsa.key.public
```javascript
["rsa.key.public"]
```
#### rsa.key.private
```javascript
["rsa.key.private"]
```
#### ssl
```javascript
["ssl"]
```
#### ssl.decode
```javascript
["ssl.decode"]
```
#### ssl.check
```javascript
["ssl.check"]
```
#### bcrypt
```javascript
["bcrypt"]
```
#### bcrypt.check
```javascript
["bcrypt.check"]
```
### format

#### void
```javascript
["void"]
```
#### void.decode
```javascript
["void.decode"]
```
#### void.read
```javascript
["void.read"]
```
#### void.write
```javascript
["void.write"]
```
#### json
```javascript
["json"]
```
#### json.decode
```javascript
["json.decode"]
```
#### json.read
```javascript
["json.read"]
```
#### json.write
```javascript
["json.write"]
```
#### yaml
```javascript
["yaml"]
```
#### yaml.decode
```javascript
["yaml.decode"]
```
#### csv
```javascript
["csv"]
```
#### csv.decode
```javascript
["csv.decode"]
```
#### ini
```javascript
["ini"]
```
#### ini.decode
```javascript
["ini.decode"]
```
#### html
```javascript
["html"]
```
#### html.decode
```javascript
["html.decode"]
```
#### xml
```javascript
["xml"]
```
#### xml.decode
```javascript
["xml.decode"]
```
#### css
```javascript
["css"]
```
#### css.decode
```javascript
["css.decode"]
```
#### robots
```javascript
["robots"]
```
#### sitemap
```javascript
["sitemap"]
```
### file

#### file.exists
```javascript
["file.exists"]
```
#### file.write
```javascript
["file.write"]
```
#### file.read
```javascript
["file.read"]
```
#### file.remove
```javascript
["file.remove"]
```
#### file.move
```javascript
["file.move"]
```
#### file.copy
```javascript
["file.copy"]
```
#### file.rename
```javascript
["file.rename"]
```
#### file.info
```javascript
["file.info"]
```
#### file.size
```javascript
["file.size"]
```
#### file.permissions
```javascript
["file.permissions"]
```
#### file.readonly
```javascript
["file.readonly"]
```
#### file.hidden
```javascript
["file.hidden"]
```
#### file.modified
```javascript
["file.modified"]
```
#### file.sha256
```javascript
["file.sha256"]
```
#### file.crc32
```javascript
["file.crc32"]
```
#### file.base64
```javascript
["file.base64"]
```
#### file.zip
```javascript
["file.zip"]
```
#### file.zip.list
```javascript
["file.zip.list"]
```
#### file.zip.exists
```javascript
["file.zip.exists"]
```
#### file.zip.read
```javascript
["file.zip.read"]
```
#### file.zip.remove
```javascript
["file.zip.remove"]
```
#### file.unzip
```javascript
["file.unzip"]
```
#### file.gzip
```javascript
["file.gzip"]
```
#### file.ungzip
```javascript
["file.ungzip"]
```
#### file.link
```javascript
["file.link"]
```
#### file.link.exists
```javascript
["file.link.exists"]
```
#### file.backup
```javascript
["file.backup"]
```
#### dir.exists
```javascript
["dir.exists"]
```
#### dir.create
```javascript
["dir.create"]
```
#### dir.copy
```javascript
["dir.copy"]
```
#### dir.move
```javascript
["dir.move"]
```
#### dir.rename
```javascript
["dir.rename"]
```
#### dir.remove
```javascript
["dir.remove"]
```
#### dir.list
```javascript
["dir.list"]
```
#### dir.clear
```javascript
["dir.clear"]
```
#### dir.info
```javascript
["dir.info"]
```
#### dir.size
```javascript
["dir.size"]
```
#### dir.permissions
```javascript
["dir.permissions"]
```
#### dir.readonly
```javascript
["dir.readonly"]
```
#### dir.hidden
```javascript
["dir.hidden"]
```
#### dir.modified
```javascript
["dir.modified"]
```
#### dir.zip
```javascript
["dir.zip"]
```
#### drive.list
```javascript
["drive.list"]
```
#### drive.name
```javascript
["drive.name"]
```
#### drive.size
```javascript
["drive.size"]
```
#### drive.used
```javascript
["drive.used"]
```
#### drive.free
```javascript
["drive.free"]
```
#### drive.mount
```javascript
["drive.mount"]
```
#### drive.unmount
```javascript
["drive.unmount"]
```
#### path.drive
```javascript
["path.drive"]
```
#### path.dir
```javascript
["path.dir"]
```
#### path.file
```javascript
["path.file"]
```
#### path.name
```javascript
["path.name"]
```
#### path.extension
```javascript
["path.extension"]
```
#### path.extension.strip
```javascript
["path.extension.strip"]
```
### cloud

#### cloud.file
```javascript
["cloud.file"]
```
#### cloud.web
```javascript
["cloud.web"]
```
#### cloud.api
```javascript
["cloud.api"]
```
#### cloud.socket
```javascript
["cloud.socket"]
```
#### cloud.websocket
```javascript
["cloud.websocket"]
```
#### cloud.mail
```javascript
["cloud.mail"]
```
#### cloud.game
```javascript
["cloud.game"]
```
#### cloud.social
```javascript
["cloud.social"]
```
#### cloud.coin
```javascript
["cloud.coin"]
```
### bot

#### bot.telegram
```javascript
["bot.telegram"]
```
#### bot.wechat
```javascript
["bot.wechat"]
```
#### bot.x
```javascript
["bot.x"]
```
#### bot.youtube
```javascript
["bot.youtube"]
```
#### bot.tiktok
```javascript
["bot.tiktok"]
```
#### bot.steam
```javascript
["bot.steam"]
```
### request

#### request
```javascript
["request"]
```
#### request.post
```javascript
["request.post"]
```
#### request.put
```javascript
["request.put"]
```
#### request.delete
```javascript
["request.delete"]
```
#### request.head
```javascript
["request.head"]
```
### cookie

#### cookie
```javascript
["cookie"]
```
#### cookie.remove
```javascript
["cookie.remove"]
```
### sql

#### sql
```javascript
["sql"]
```
#### sql.connect
```javascript
["sql.connect"]
```
#### sql.disconnet
```javascript
["sql.disconnet"]
```
#### sql.user
```javascript
["sql.user"]
```
#### sql.user.list
```javascript
["sql.user.list"]
```
#### sql.user.remove
```javascript
["sql.user.remove"]
```
#### sql.db
```javascript
["sql.db"]
```
#### sql.db.list
```javascript
["sql.db.list"]
```
#### sql.db.remove
```javascript
["sql.db.remove"]
```
#### sql.db.size
```javascript
["sql.db.size"]
```
#### sql.table
```javascript
["sql.table"]
```
#### sql.table.list
```javascript
["sql.table.list"]
```
#### sql.table.remove
```javascript
["sql.table.remove"]
```
#### sql.field
```javascript
["sql.field"]
```
#### sql.field.list
```javascript
["sql.field.list"]
```
#### sql.field.remove
```javascript
["sql.field.remove"]
```
#### sql.index
```javascript
["sql.index"]
```
#### sql.index.list
```javascript
["sql.index.list"]
```
#### sql.index.remove
```javascript
["sql.index.remove"]
```
#### sql.function
```javascript
["sql.function"]
```
#### sql.function.list
```javascript
["sql.function.list"]
```
#### sql.function.remove
```javascript
["sql.function.remove"]
```
#### sql.view
```javascript
["sql.view"]
```
#### sql.view.list
```javascript
["sql.view.list"]
```
#### sql.view.remove
```javascript
["sql.view.remove"]
```
#### sql.get
```javascript
["sql.get"]
```
#### sql.all
```javascript
["sql.all"]
```
#### sql.cursor
```javascript
["sql.cursor"]
```
#### sql.transaction
```javascript
["sql.transaction"]
```
#### sql.commit
```javascript
["sql.commit"]
```
#### sql.rollback
```javascript
["sql.rollback"]
```
### os

#### os
```javascript
["os"]
```
#### os.name
```javascript
["os.name"]
```
#### os.version
```javascript
["os.version"]
```
#### os.username
```javascript
["os.username"]
```
#### os.desktop
```javascript
["os.desktop"]
```
#### os.mobile
```javascript
["os.mobile"]
```
#### os.web
```javascript
["os.web"]
```
#### os.windows
```javascript
["os.windows"]
```
#### os.macos
```javascript
["os.macos"]
```
#### os.ios
```javascript
["os.ios"]
```
#### os.ipados
```javascript
["os.ipados"]
```
#### os.watchos
```javascript
["os.watchos"]
```
#### os.tvos
```javascript
["os.tvos"]
```
#### os.android
```javascript
["os.android"]
```
#### os.linux
```javascript
["os.linux"]
```
### device

#### cpu.name
```javascript
["cpu.name"]
```
#### cpu.cores
```javascript
["cpu.cores"]
```
#### memory.size
```javascript
["memory.size"]
```
#### memory.free
```javascript
["memory.free"]
```
#### memory.used
```javascript
["memory.used"]
```
#### memory.available
```javascript
["memory.available"]
```
### gps

#### gps
```javascript
["gps"]
```
### sensor

#### speed
```javascript
["speed"]
```
#### tilt
```javascript
["tilt"]
```
#### compass
```javascript
["compass"]
```
#### motion
```javascript
["motion"]
```
### photo

#### camera
```javascript
["camera"]
```
#### gallery
```javascript
["gallery"]
```
### contacts

#### contacts
```javascript
["contacts"]
```
### calendar

#### calendar
```javascript
["calendar"]
```
### flashlight

#### flashlight
```javascript
["flashlight"]
```
### health

#### health
```javascript
["health"]
```
### microphone

#### mic
```javascript
["mic"]
```
### notification

#### notification
```javascript
["notification"]
```
#### notification.token
```javascript
["notification.token"]
```
#### notification.send
```javascript
["notification.send"]
```
### key

#### key
```javascript
["key"]
```
#### key.remove
```javascript
["key.remove"]
```
#### key.press
```javascript
["key.press"]
```
#### key.enable
```javascript
["key.enable"]
```
#### key.disable
```javascript
["key.disable"]
```
### keyboard

#### keyboard
```javascript
["keyboard"]
```
#### keyboard.height
```javascript
["keyboard.height"]
```
### mouse

#### mouse
```javascript
["mouse"]
```
#### mouse.lock
```javascript
["mouse.lock"]
```
#### mouse.position
```javascript
["mouse.position"]
```
#### mouse.capture
```javascript
["mouse.capture"]
```
#### mouse.confine
```javascript
["mouse.confine"]
```
#### mouse.shape
```javascript
["mouse.shape"]
```
### gamepad

#### gamepad.axis
```javascript
["gamepad.axis"]
```
#### gamepad.vibrate
```javascript
["gamepad.vibrate"]
```
### clipboard

#### clipboard
```javascript
["clipboard"]
```
#### clipboard.clear
```javascript
["clipboard.clear"]
```
### say

#### say
```javascript
["say"]
```
#### say.list
```javascript
["say.list"]
```
#### say.stop
```javascript
["say.stop"]
```
#### say.pause
```javascript
["say.pause"]
```
### convert

#### convert
```javascript
["convert"]
```
### image

#### image
```javascript
["image"]
```
#### image.read
```javascript
["image.read"]
```
#### image.write
```javascript
["image.write"]
```
#### image.size
```javascript
["image.size"]
```
#### image.crop
```javascript
["image.crop"]
```
#### image.square
```javascript
["image.square"]
```
#### image.rotate
```javascript
["image.rotate"]
```
#### image.flip.h
```javascript
["image.flip.h"]
```
#### image.flip.v
```javascript
["image.flip.v"]
```
#### image.tint
```javascript
["image.tint"]
```
#### image.gray
```javascript
["image.gray"]
```
#### image.text
```javascript
["image.text"]
```
#### image.image
```javascript
["image.image"]
```
#### image.draw
```javascript
["image.draw"]
```
### video

#### video
```javascript
["video"]
```
#### video.read
```javascript
["video.read"]
```
#### video.write
```javascript
["video.write"]
```
#### video.size
```javascript
["video.size"]
```
#### video.rotate
```javascript
["video.rotate"]
```
#### video.flip.h
```javascript
["video.flip.h"]
```
#### video.flip.v
```javascript
["video.flip.v"]
```
#### video.clip
```javascript
["video.clip"]
```
#### video.speed
```javascript
["video.speed"]
```
#### video.reverse
```javascript
["video.reverse"]
```
#### video.text
```javascript
["video.text"]
```
#### video.image
```javascript
["video.image"]
```
#### video.sound
```javascript
["video.sound"]
```
#### video.video
```javascript
["video.video"]
```
### model

#### model
```javascript
["model"]
```
#### model.read
```javascript
["model.read"]
```
#### model.write
```javascript
["model.write"]
```
#### model.animate
```javascript
["model.animate"]
```
#### model.texture
```javascript
["model.texture"]
```
### sound

#### sound
```javascript
["sound"]
```
#### sound.read
```javascript
["sound.read"]
```
#### sound.write
```javascript
["sound.write"]
```
#### sound.list
```javascript
["sound.list"]
```
#### sound.remove
```javascript
["sound.remove"]
```
#### sound.volume
```javascript
["sound.volume"]
```
#### sound.speed
```javascript
["sound.speed"]
```
#### sound.clip
```javascript
["sound.clip"]
```
#### sound.sound
```javascript
["sound.sound"]
```
### music

#### music
```javascript
["music"]
```
#### music.stop
```javascript
["music.stop"]
```
#### music.pause
```javascript
["music.pause"]
```
#### music.volume
```javascript
["music.volume"]
```
### volume

#### volume
```javascript
["volume"]
```
### screen

#### screen.count
```javascript
["screen.count"]
```
#### screen.list
```javascript
["screen.list"]
```
#### screen.info
```javascript
["screen.info"]
```
#### size
```javascript
["size"]
```
#### orientation
```javascript
["orientation"]
```
#### landscape
```javascript
["landscape"]
```
#### portrait
```javascript
["portrait"]
```
#### rate
```javascript
["rate"]
```
#### pixel
```javascript
["pixel"]
```
#### symbol
```javascript
["symbol"]
```
#### dpi
```javascript
["dpi"]
```
#### dark
```javascript
["dark"]
```
#### touchscreen
```javascript
["touchscreen"]
```
### ui

#### ui
```javascript
["ui"]
```
#### bg
```javascript
["bg"]
```
#### show
```javascript
["show"]
```
#### hide
```javascript
["hide"]
```
#### visible
```javascript
["visible"]
```
#### enable
```javascript
["enable"]
```
#### disable
```javascript
["disable"]
```
#### enabled
```javascript
["enabled"]
```
#### focus
```javascript
["focus"]
```
#### scale
```javascript
["scale"]
```
#### ui.text
```javascript
["ui.text"]
```
#### ui.image
```javascript
["ui.image"]
```
#### ui.button
```javascript
["ui.button"]
```
#### ui.divider
```javascript
["ui.divider"]
```
#### ui.video
```javascript
["ui.video"]
```
#### ui.select
```javascript
["ui.select"]
```
#### ui.switch
```javascript
["ui.switch"]
```
#### ui.progress
```javascript
["ui.progress"]
```
#### ui.slider
```javascript
["ui.slider"]
```
#### ui.edit
```javascript
["ui.edit"]
```
#### ui.split.h
```javascript
["ui.split.h"]
```
#### ui.split.v
```javascript
["ui.split.v"]
```
#### ui.list
```javascript
["ui.list"]
```
#### ui.tile
```javascript
["ui.tile"]
```
#### ui.color
```javascript
["ui.color"]
```
#### ui.date
```javascript
["ui.date"]
```
#### ui.drop
```javascript
["ui.drop"]
```
#### ui.menu
```javascript
["ui.menu"]
```
#### ui.menu.context
```javascript
["ui.menu.context"]
```
#### ui.window
```javascript
["ui.window"]
```
#### ui.debug
```javascript
["ui.debug"]
```
#### ui.fps
```javascript
["ui.fps"]
```
### window

#### window.list
```javascript
["window.list"]
```
#### window.info
```javascript
["window.info"]
```
#### title
```javascript
["title"]
```
#### icon
```javascript
["icon"]
```
#### size
```javascript
["size"]
```
#### size.max
```javascript
["size.max"]
```
#### size.min
```javascript
["size.min"]
```
#### position
```javascript
["position"]
```
#### direction
```javascript
["direction"]
```
#### attention
```javascript
["attention"]
```
#### top
```javascript
["top"]
```
#### foreground
```javascript
["foreground"]
```
#### unfocusable
```javascript
["unfocusable"]
```
#### unresizable
```javascript
["unresizable"]
```
#### center
```javascript
["center"]
```
#### fullscreen
```javascript
["fullscreen"]
```
#### drop
```javascript
["drop"]
```
#### border
```javascript
["border"]
```
#### maximized
```javascript
["maximized"]
```
#### minimized
```javascript
["minimized"]
```
#### exclusive
```javascript
["exclusive"]
```
#### vsync
```javascript
["vsync"]
```
#### fps
```javascript
["fps"]
```
### dialog

#### dialog.file
```javascript
["dialog.file"]
```
#### dialog.color
```javascript
["dialog.color"]
```
#### dialog.date
```javascript
["dialog.date"]
```
#### dialog.select
```javascript
["dialog.select"]
```
### effect

#### effect
```javascript
["effect"]
```
#### effect.list
```javascript
["effect.list"]
```
#### effect.clear
```javascript
["effect.clear"]
```
#### effect.remove
```javascript
["effect.remove"]
```
### game

#### game
```javascript
["game"]
```
#### menu
```javascript
["menu"]
```
### vn

#### vn
```javascript
["vn"]
```
#### vn.clear
```javascript
["vn.clear"]
```
#### vn.say
```javascript
["vn.say"]
```
#### vn.skip
```javascript
["vn.skip"]
```
#### vn.route
```javascript
["vn.route"]
```
#### vn.route.remove
```javascript
["vn.route.remove"]
```
#### vn.route.check
```javascript
["vn.route.check"]
```
#### vn.route.select
```javascript
["vn.route.select"]
```
#### vn.route.repeat
```javascript
["vn.route.repeat"]
```
#### vn.route.skip
```javascript
["vn.route.skip"]
```
#### vn.character
```javascript
["vn.character"]
```
#### vn.come
```javascript
["vn.come"]
```
#### vn.leave
```javascript
["vn.leave"]
```
#### vn.change
```javascript
["vn.change"]
```
#### vn.env
```javascript
["vn.env"]
```
#### vn.env.change
```javascript
["vn.env.change"]
```
### 2d

#### 2d
```javascript
["2d"]
```
#### 2d.bg
```javascript
["2d.bg"]
```
#### 2d.map
```javascript
["2d.map"]
```
#### 2d.character
```javascript
["2d.character"]
```
#### 2d.object
```javascript
["2d.object"]
```
#### 2d.npc
```javascript
["2d.npc"]
```
#### 2d.enemy
```javascript
["2d.enemy"]
```
#### 2d.shoot
```javascript
["2d.shoot"]
```
#### 2d.jump
```javascript
["2d.jump"]
```
#### 2d.drop
```javascript
["2d.drop"]
```
#### 2d.look
```javascript
["2d.look"]
```
#### 2d.inventory
```javascript
["2d.inventory"]
```
#### 2d.hud
```javascript
["2d.hud"]
```
#### 2d.sound
```javascript
["2d.sound"]
```
#### 2d.light
```javascript
["2d.light"]
```
#### 2d.camera
```javascript
["2d.camera"]
```
### 3d

#### 3d
```javascript
["3d"]
```
#### 3d.bg
```javascript
["3d.bg"]
```
#### 3d.map
```javascript
["3d.map"]
```
#### 3d.character
```javascript
["3d.character"]
```
#### 3d.object
```javascript
["3d.object"]
```
#### 3d.npc
```javascript
["3d.npc"]
```
#### 3d.enemy
```javascript
["3d.enemy"]
```
#### 3d.shoot
```javascript
["3d.shoot"]
```
#### 3d.jump
```javascript
["3d.jump"]
```
#### 3d.drop
```javascript
["3d.drop"]
```
#### 3d.look
```javascript
["3d.look"]
```
#### 3d.hud
```javascript
["3d.hud"]
```
#### 3d.inventory
```javascript
["3d.inventory"]
```
#### 3d.sound
```javascript
["3d.sound"]
```
#### 3d.light
```javascript
["3d.light"]
```
#### 3d.camera
```javascript
["3d.camera"]
```
### ai

#### ai.text
```javascript
["ai.text"]
```
#### ai.image
```javascript
["ai.image"]
```
#### ai.video
```javascript
["ai.video"]
```
#### ai.music
```javascript
["ai.music"]
```
#### ai.sound
```javascript
["ai.sound"]
```
#### ai.say
```javascript
["ai.say"]
```
#### ai.2d
```javascript
["ai.2d"]
```
#### ai.3d
```javascript
["ai.3d"]
```
#### ai.character
```javascript
["ai.character"]
```
#### ai.clean
```javascript
["ai.clean"]
```
#### ai.resize
```javascript
["ai.resize"]
```
#### ai.color
```javascript
["ai.color"]
```
#### ai.style
```javascript
["ai.style"]
```
#### ai.translate
```javascript
["ai.translate"]
```
#### ai.recognize.text
```javascript
["ai.recognize.text"]
```
#### ai.recognize.image
```javascript
["ai.recognize.image"]
```
#### ai.recognize.video
```javascript
["ai.recognize.video"]
```
#### ai.recognize.motion
```javascript
["ai.recognize.motion"]
```
#### ai.capture.voice
```javascript
["ai.capture.voice"]
```
#### ai.capture.face
```javascript
["ai.capture.face"]
```
#### ai.capture.motion
```javascript
["ai.capture.motion"]
```
### social

#### social.auth
```javascript
["social.auth"]
```
#### social.auth.signin
```javascript
["social.auth.signin"]
```
#### social.auth.signup
```javascript
["social.auth.signup"]
```
#### social.auth.signout
```javascript
["social.auth.signout"]
```
#### social.auth.restore
```javascript
["social.auth.restore"]
```
#### social.auth.restore.code
```javascript
["social.auth.restore.code"]
```
#### social
```javascript
["social"]
```
#### social.send
```javascript
["social.send"]
```
#### social.profile
```javascript
["social.profile"]
```
#### social.buy
```javascript
["social.buy"]
```
### tech

#### light.on
```javascript
["light.on"]
```
#### light.off
```javascript
["light.off"]
```
#### power.on
```javascript
["power.on"]
```
#### power.off
```javascript
["power.off"]
```
#### power.timer
```javascript
["power.timer"]
```
#### door.open
```javascript
["door.open"]
```
#### door.close
```javascript
["door.close"]
```
#### door.code
```javascript
["door.code"]
```
#### dron.move
```javascript
["dron.move"]
```
#### dron.up
```javascript
["dron.up"]
```
#### dron.down
```javascript
["dron.down"]
```
#### dron.left
```javascript
["dron.left"]
```
#### dron.right
```javascript
["dron.right"]
```
#### dron.go
```javascript
["dron.go"]
```
#### dron.stop
```javascript
["dron.stop"]
```
#### dron.jump
```javascript
["dron.jump"]
```
#### dron.crouch
```javascript
["dron.crouch"]
```
#### dron.open
```javascript
["dron.open"]
```
#### dron.close
```javascript
["dron.close"]
```
#### dron.rotate
```javascript
["dron.rotate"]
```
#### dron.camera
```javascript
["dron.camera"]
```
#### dron.camera.rotate
```javascript
["dron.camera.rotate"]
```
#### dron.camera.on
```javascript
["dron.camera.on"]
```
#### dron.camera.off
```javascript
["dron.camera.off"]
```
#### dron.camera.record
```javascript
["dron.camera.record"]
```
#### dron.camera.record.stop
```javascript
["dron.camera.record.stop"]
```
#### dron.hand.open
```javascript
["dron.hand.open"]
```
#### dron.hand.close
```javascript
["dron.hand.close"]
```
#### dron.hand.move
```javascript
["dron.hand.move"]
```
#### dron.hand.gesture
```javascript
["dron.hand.gesture"]
```
#### dron.sound
```javascript
["dron.sound"]
```
#### dron.volume
```javascript
["dron.volume"]
```
#### dron.mic
```javascript
["dron.mic"]
```
#### dron.mic.on
```javascript
["dron.mic.on"]
```
#### dron.mic.off
```javascript
["dron.mic.off"]
```
#### dron.mic.record
```javascript
["dron.mic.record"]
```
#### dron.mic.record.stop
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
  123_000
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
  [
    [. "Hi World :D
    [= var 123
    [. {var}
base64
  b64:ViBPIEkgRCBmb3JtYXQ=
binary
  3:☺☺☺
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
