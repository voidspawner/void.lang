# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **V O I D** or **JSON format**. It is used as a replacement for the standard Bash・CMD・etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one V O I D or JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

**The project is in the process of development.**

<img src="https://i.imgur.com/kx2UcUh.jpg" width="100%">

## Preinstalled Language

| <p align="center">**Language**</p> | <p align="center">**Engine**</p> | <p align="center">**Web**</p> | <p align="center">**CLI**</p> | <p align="center">**Server**</p> | <p align="center">**Mobile**</p> | <p align="center">**Windows**</p> | <p align="center">**macOS**</p> | <p align="center">**iOS**</p> | <p align="center">**Android**</p> | <p align="center">**Linux**</p> | <p align="center">**Xbox**</p> | <p align="center">**Switch**</p> | <p align="center">**Steam Deck**</p> | <p align="center">**PlayStation**</p> |
| ---------- | ----------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ----------------------- | ----------------------- |
| Python     | <p align="center">Python</p>        | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| JavaScript | <p align="center">NodeJS</p>        | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| Swift      | <p align="center">-</p>             | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| Kotlin     | <p align="center">-</p>             | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p>  | <p align="center">-</p> |
| GDScript   | <p align="center">Godot</p>         | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p>  | <p align="center">+</p> |
| C++        | <p align="center">Unreal Engine</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p>  | <p align="center">+</p> |

## Example
##### Simple
```javascript
{
  "run": [
    [".", "Hi World :D"]
  ]
}
```
##### Even Simpler
```javascript
[
  [".", "Hi World :D"]
]
```
##### Multilanguage Text
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
##### Web Server
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
##### Web Server Simpler
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
##### Web App with UI
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
##### Web Share Files
```javascript
[
  ["cloud.file": "/path/to/share"]
]
```

## How To Use

1. Download **V O I D lang**
2. Create your first vapp in **run.json** or other JSON file
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

## How To Use Game Engine

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

## How To Add Comments
All code is data. So just add the property "description", "//" and so on.
```javascript
{
  "description": "App Description. But you can write more in version",
  "version": {
    "description": "Comment",
    "number": 1,
    "name": "First App"
  },
  "run": [
    [".", "Hi World"]
  ]
}
```

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
[".", "Hi World"]
```
```
Action name: "."
Action parameters: ["Hi World"]
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
| run            |      |   ✔    | work   | work  |  work  |     ✔    | task  |
| value          |      |   ✔    | work   | work  |  work  |   work   | task  |
| expression     |      |  work  | work   | work  |  work  |   work   | task  |
| control        |      |  work  | work   | work  |  work  |   work   | task  |
| text           |      |  work  | work   | work  |  work  |   work   | task  |
| list           |      |  work  | work   | work  |  work  |   work   | task  |
| math           |      |  work  | work   | work  |  work  |   work   | task  |
| time           |      |  work  | work   | work  |  work  |   work   | task  |
| crypto         |      |  work  | work   | work  |  work  |   work   | task  |
| format         |      |        |        |       |        |          |       |
| ・ json         |      |   ✔    | work   | work  |  work  |   work   | task  |
| ・ yaml         |      |  work  | task   | task  |  task  |   work   | task  |
| ・ csv          |      |  work  | task   | task  |  task  |   work   | task  |
| ・ other        | task |  vapp  | vapp   | vapp  |  vapp  |   vapp   | vapp  |
| file           |      |  work  | task   | task  |  task  |   work   | task  |
| cloud          |      |  work  | task   | task  |  task  |   work   | task  |
| bot            |      |  task  | task   | task  |  task  |   task   | task  |
| request        |      |  work  | task   | task  |  task  |   work   | task  |
| cookie         |      |  work  | work   | task  |  task  |   work   | task  |
| sql            |      |  work  | task   | task  |  task  |   work   | task  |
| os             |      |  work  | task   | task  |  task  |   work   | task  |
| device         |      |  -     | -      | task  |  task  |   work   | task  |
| gps            |      |  -     | -      | task  |  task  |   work   | task  |
| sensor         |      |  -     | -      | task  |  task  |   work   | task  |
| photo          |      |  -     | -      | task  |  task  |   work   | task  |
| contacts       |      |  -     | -      | task  |  task  |   work   | task  |
| calendar       |      |  -     | -      | task  |  task  |   work   | task  |
| flashlight     |      |  -     | -      | task  |  task  |   work   | task  |
| health         |      |  -     | -      | task  |  task  |   work   | task  |
| microphone     |      |  -     | -      | task  |  task  |   work   | task  |
| notification   |      |  work  | task   | task  |  task  |   work   | task  |
| key            |      |  -     | -      | task  |  task  |   work   | task  |
| keyboard       |      |  -     | -      | task  |  task  |   work   | task  |
| mouse          |      |  -     | -      | task  |  task  |   work   | task  |
| gamepad        |      |  -     | -      | task  |  task  |   work   | task  |
| clipboard      |      |  -     | -      | task  |  task  |   work   | task  |
| say            |      |  -     | -      | task  |  task  |   work   | task  |
| convert        | work |  vapp  | vapp   | vapp  |  vapp  |   vapp   | vapp  |
| video          |      |  task  | task   | task  |  task  |   work   | task  |
| model          |      |  task  | task   | task  |  task  |   work   | task  |
| sound          |      |  task  | task   | task  |  task  |   work   | task  |
| music          |      |  -     | -      | task  |  task  |   work   | task  |
| volume         |      |  -     | -      | task  |  task  |   work   | task  |
| screen         |      |  -     | -      | task  |  task  |   work   | task  |
| ui             |      |        |        |       |        |          |       |
| ・ graphic      |      |  -     | -      | task  |  task  |   work   | task  |
| ・ cli          |      |  work  | task   | task  |  task  |   work   | task  |
| window         |      |  -     | -      | task  |  task  |   work   | task  |
| dialog         |      |  -     | -      | task  |  task  |   work   | task  |
| effect         |      |  -     | -      | task  |  task  |   work   | task  |
| game           | work |  -     | -      | vapp  |  vapp  |   vapp   | vapp  |
| vn             | work |  -     | -      | vapp  |  vapp  |   vapp   | vapp  |
| 2d             |      |  -     | -      | task  |  task  |   work   | task  |
| 3d             |      |  -     | -      | task  |  task  |   work   | task  |
| ai             |      |  work  | python | task  |  task  |  python  | task  |
| social         | work |  vapp  | vapp   | vapp  |  vapp  |  vapp    | vapp  |
| tech           | wait |  vapp  | vapp   | vapp  |  vapp  |  vapp    | vapp  |

## Detail・Examples

### value
### expression
### control
### text
### list
### math
### time
### crypto
### format
### file
### cloud
### bot
### request
### cookie
### sql
### os
### device
### gps
### sensor
### photo
### contacts
### calendar
### flashlight
### health
### microphone
### notification
### key
### keyboard
### mouse
### gamepad
### clipboard
### say
### convert
### image
### video
### model
### sound
### music
### volume
### screen
### ui
### window
### dialog
### effect
### game
### vn
### 2d
### 3d
### ai
### social
### tech

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create applications and games.
