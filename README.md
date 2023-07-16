# V O I D spawner lang

### About
**V O I D spawner lang** is a language for rapidly creating applications in the JSON format. It is used as a replacement for both the standard Bash/CMD/etc. languages and for writing **UI Applications**, **Servers** and **Games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one json file**.

### Preinstalled Language

- **Python** ⌜CLI App | Web Server | API Server | Game (with Godot)⌟
- **PHP** ⌜CLI App | Web Server | API Server⌟
- **JS** ⌜Web App | Web Server (with NodeJS) | API Server (with NodeJS) | CLI App (with NodeJS)⌟
- **Swift** ⌜macOS App | iOS App | iPadOS App | watchOS App | tvOS App | Linux App | Windows App | Web Server | API Server | Game (with Godot) | Game (with UE5) | Game Native⌟
- **Java** ⌜Android App | Linux App | Windows App | Web Server | API Server | Game (with Godot) | Game (with UE5) | Game Native⌟
- **C#** ⌜Windows App | Web Server | API Server | Game (with Godot) | Game (with UE5) | Game Native⌟

### Example
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
##### Multilanguage
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
      "jp": "こんにちは世界"
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
      ["/", "home.start"],
      ["/hello", "home.hello"]
    ]
  },
  "action": {
    "home": {
      "start": [
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
