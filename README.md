# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **V O I D** or **JSON format**. It is used as a replacement for the standard Bash/CMD/etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one V O I D or JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

**The project is in the process of development. Code and description are subject to change and inconsistency.**

<img src="https://i.imgur.com/kx2UcUh.jpg" width="100%">

## Preinstalled Language

- **Python** ⌜CLI・Server⌟
- **PHP** ⌜CLI・Server⌟
- **JavaScript** ⌜Web・CLI (with NodeJS)・Server (with NodeJS)・Game⌟
- **Swift** ⌜macOS・iOS・iPadOS・watchOS・tvOS・Windows・Linux・Server・Game⌟
- **Java** ⌜Android・macOS・Windows・Linux・Server・Game⌟
- **C#** ⌜Windows・Server・Game⌟
- **C++** ⌜macOS・Windows・Linux・Server・Game⌟

## Game Engine

This is a pre-compiled **V O I D spawner** game for rapidly creating games, apps and animation in **V O I D lang**. It uses multiple game engines:

- **Godot Engine**
- **Unreal 5 Engine**
- **V O I D engine**

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
    ["server.http", {
      "route": [
        ["/", "home"]
      ]
    }]
  ],
  "action": {
    "home": [
      ["=", "response.text", "<h1>Hi World 😄</h1>"]
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
        ["=", "response.text", "<h1>Hi World 😄</h1>"]
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
      ["/", [
        ["title", "{text.hi}"],
        ["text", "{text.hi}", {
          "color": "white",
          "background": "green",
          "size": 20
        }]
      ]]
    ]
  },
  "text": {
    "hi": "Hi World 😄"
  }
}
```

## How To Use

1. Download **V O I D lang**
2. Create your first app in JSON file
3. Launch app with **V O I D lang**
   ```console
   python python/void.py myfirstapp.json
   php php/void.php myfirstapp.json
   ```

   ##### Or even without JSON file at all
   ```console
   python python/void.py '[[".", "Hi World :)"]]'
   ```

   ##### Tip for Linux / macOS: add alias to ~/.bashrc ・ ~/.zshrc ・ ~/.bash_profile
   ```console
   alias void="python /path/to/python/void.py"
   ```

   ##### Tip for Windows: use alias in command line
   ```console
   doskey void=python /path/to/python/void.py
   ```
   ```console
   void myfirstapp.json
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

   Or you can use the **Exporter** inside the **V O I D spawner** game to export your game to all platforms ⌜**Windows**・**macOS**・**Linux**・**Android**・**iOS**・**Web**・**Xbox**・**Switch**・**PlayStation**⌟

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
    [".", "Hi World"],
    ["//", "This line will be ignored"]
  ]
}
```

## Actions

[Value](#value)・
[Control](#control)・
[Text](#text)・
[List](#list)・
[Math](#math)・
[Time](#time)・
[Crypto](#crypto)・
[Format](#format)・
[File](#file)・
[Server](#server)・
[Request](#request)・
[Cache](#cache)・
[Data](#data)・
[OS](#os)・
[Device](#device)・
[Clipboard](#clipboard)・
[Say](#say)・
[Image](#image)・
[Video](#video)・
[Sound](#sound)・
[Music](#music)・
[Screen](#screen)・
[UI](#ui)・
[Visual Novel](#visual-novel)・
[2D](#ui)・
[3D](#ui)・
[AI](#ai)・
[Voids](#voids)・
[Social](#social)

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

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create applications and games.
