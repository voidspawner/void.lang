# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **[V O I D](#v-o-i-d-format)** or **[JSON](https://en.wikipedia.org/wiki/JSON)** format. It is used as a replacement for the standard **``Bash``**・**``CMD``**・etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one ``V O I D`` or ``JSON`` file**. Since the **code is presented as data**, applications can be easily generated with **``AI``**, updated, installed and launched remotely.

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
[**V O I D game**](#v-o-i-d-game)・
[**V O I D social**](#v-o-i-d-social)・
[**V O I D os**](#v-o-i-d-os)・
[**V O I D tech**](#v-o-i-d-tech)・
[**V O I D ideology**](#v-o-i-d-ideology)・
[**V O I D license**](#v-o-i-d-license)・
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
##### Show current version
```json
[
  ["." "{description.about.version}"]
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
      [".", "i!"]
    ], [
      [".", "{letter}"]
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
  ["code", "for i in range(10):print(i)"]
]
```
##### Import into your project
```python
exec(open('void.py').read())
encrypted = void.encrypt('Hi World :D')
print(void.decrypt(encrypted.text, encrypted.key))
```

## How to Use

1. Download **V O I D lang**
2. Create your first vapp (V O I D app) in **``run.json``** or other JSON file
3. Launch vapp with **V O I D lang**
 
```console
python void.py vapp.json
```

**Alternative**

```console
python void.py vapp.void
```
```console
python void.py app.py
```
```console
python void.py "['.', 'Hi World :D']"
```

> [!TIP]
> **Linux・macOS**: Add alias to **``~/.bashrc``** ・ **``~/.zshrc``** ・ **``~/.bash_profile``** (macOS)
> ```console
> alias void="python /path/to/void.py"
> ```
> 
> **Windows**: Use alias in command line
> ```console
> doskey void=python /path/to/void.py
> ```
> ```console
> void vapp.json
> ```
> 
> **Swift・Kotlin・C++**: Embed the **vapp** in the source code and compile it into an executable
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
2. Create your first game in **``run.json``** file
3. Copy the **void.exe** file from the **V O I D spawner** game to the same directory as **``run.json``** file
4. Sell your game or share with friends

> [!NOTE]
> **Run with game engine**
> ```console
> void.exe game.json
> ```
>
> **The archive contains ``run.json`` and all game files**
> ```console
> void.exe game.zip
> ```
>
> **The execution directory contains ``run.json`` and all game files or contains ``run.zip`` file**
> ```console
> void.exe
> ```
>
> You can use the **Exporter** inside the **V O I D spawner** game to export your game to all platforms ⌜**Windows**・**macOS**・**Linux**・**Android**・**iOS**・**Web**・**Xbox**・**Switch**・**PlayStation**⌟

**Alternative**

1. Download **V O I D lang**
2. Import **``void.gd``**・**``void.cpp``** into the **Godot**・**Unreal Engine**
3. Create your first game in **``run.json``** file
4. Export the game in the engine itself to the available platforms
5. Sell your game or share with friends

## Actions

> [!NOTE]
> **Use Help to display a description of the action**
>
> ```json
> ["help"],
> ["help", "upper"]
> ```
> 
> ```console
> python void.py help
> python void.py help upper
> ```

> Count of actions **``416``**

| <img width="1000" height="1"> | <img width="1000" height="1"> |
| --- | --- |
| **value** | **format** |
| **``get``**<br>Retrieve a value based on provided parameter name | **``void.encode``**<br>Encodes data into the Void format |
| **``set``**<br>Assign a value to a specified parameter | **``void.decode``**<br>Decodes data from the Void format |
| **``remove``**<br>Remove a specified parameter or value | **``json.encode``**<br>Encodes data into the JSON format |
| **``type``**<br>Determine the data type of a specified parameter | **``json.decode``**<br>Decodes data from the JSON format |
| **``text``**<br>Specify a parameter as a text type | **``csv.encode``**<br>Encodes data into the CSV format |
| **``number``**<br>Specify a parameter as a number type | **``csv.decode``**<br>Decodes data from the CSV format |
| **``bool``**<br>Specify a parameter as a boolean type | **``yaml.encode``**<br>Encodes data into the YAML format |
| **``list``**<br>Specify a parameter as a list type | **``yaml.decode``**<br>Decodes data from the YAML format |
| **``dict``**<br>Specify a parameter as a dictionary type | **``ini.encode``**<br>Encodes data into the INI format |
| **``binary``**<br>Specify a parameter as a binary type | **``ini.decode``**<br>Decodes data from the INI format |
| **``n``**<br>Gets the length of the text, the number of items in a list or dictionary | **``html.encode``**<br>Encodes data into the HTML format |
| &nbsp; | **``html.decode``**<br>Decodes data from the HTML format |
| **expression** | **``html.markdown``**<br>Encodes Markdown-formatted text into the HTML format |
| **``+``**<br>Perform addition operation | **``xml.encode``**<br>Encodes data into the XML format |
| **``-``**<br>Perform subtraction operation | **``xml.decode``**<br>Decodes data from the XML format |
| **``*``**<br>Perform multiplication operation | **``css.encode``**<br>Encodes data into the CSS format |
| **``/``**<br>Perform division operation | **``css.decode``**<br>Decodes data from the CSS format |
| **``%``**<br>Perform modulo operation | &nbsp; |
| **``~``**<br>Elevation operator | **request** |
| **``!``**<br>Perform logical negation | **``request``**<br>Sends an HTTP (GET by default) request to a specified URL |
| **``&``**<br>Perform bitwise AND operation | **``request.post``**<br>Sends an HTTP POST request to a specified URL |
| **``\|``**<br>Perform bitwise OR operation | **``request.put``**<br>Sends an HTTP PUT request to a specified URL |
| **``^``**<br>Perform bitwise XOR operation | **``request.delete``**<br>Sends an HTTP DELETE request to a specified URL |
| **``>>``**<br>Perform right bitwise shift operation | **``request.head``**<br>Sends an HTTP HEAD request to a specified URL |
| **``<<``**<br>Perform left bitwise shift operation | **``download``**<br>Downloads content from a specified URL |
| **``=``**<br>Assign value to a variable | **``download.info``**<br>Retrieves information about a content available for download |
| **``+=``**<br>Add and assign value to a variable | **``download.audio``**<br>Downloads audio from a specified URL |
| **``=+``**<br>Assign and add value to a variable | **``download.video``**<br>Downloads video from a specified URL |
| **``-=``**<br>Subtract and assign value to a variable | **``download.text``**<br>Downloads subtitles from a specified URL |
| **``*=``**<br>Multiply and assign value to a variable | &nbsp; |
| **``/=``**<br>Divide and assign value to a variable | **cloud** |
| **``%=``**<br>Modulo and assign value to a variable | **``cloud``**<br>Runs cloud storage or services for data management |
| **``~=``**<br>Elevation and assign value to a variable | **``cloud.file``**<br>Runs cloud storage |
| **``&=``**<br>Bitwise AND and assign value to a variable | **``cloud.web``**<br>Runs WEB service |
| **``\|=``**<br>Bitwise OR and assign value to a variable | **``cloud.api``**<br>Runs API service |
| **``^=``**<br>Bitwise XOR and assign value to a variable | **``cloud.socket``**<br>Runs Socket service |
| **``>>=``**<br>Right shift and assign value to a variable | **``cloud.mail``**<br>Runs Mail service |
| **``<<=``**<br>Left shift and assign value to a variable | **``cloud.proxy``**<br>Runs Proxy service |
| **``==``**<br>Checks if left value is equal to right | **``cookie``**<br>Gets or sets a specified cookie |
| **``!=``**<br>Check if values are not equal | **``cookie.remove``**<br>Removes a specified cookie from the client's storage |
| **``>``**<br>Checks if left value is greater than right | **``social``**<br>Interacting with social API |
| **``<``**<br>Checks if left value is less than right | &nbsp; |
| **``>=``**<br>Checks if left value is greater than or equal to right | **notification** |
| **``<=``**<br>Checks if left value is less than or equal to right | **``notification``**<br>Send notification |
| **``not``**<br>Logical NOT operation | **``mail``**<br>Send mail |
| **``and``**<br>Logical AND operation | **``call``**<br>Initiate a voice or video call to a specified recipient |
| **``or``**<br>Logical OR operation | **``sms``**<br>Send a text message (SMS) to a specified recipient |
| **``in``**<br>Checks if value is in a list or name in a dictionary | &nbsp; |
| **``!in``**<br>Checks if value is not in a list or name not in a dictionary | **os** |
| &nbsp; | **``os``**<br>Gets or checks the operating system type |
| **control** | **``os.version``**<br>Current version of the operating system |
| **``.``**<br>Output data to the console | **``os.user``**<br>Information about the current user logged into the operating system |
| **``..``**<br>Input text from the user | **``language``**<br>System language |
| **``?``**<br>Evaluate a conditional expression | &nbsp; |
| **``o``**<br>Perform a loop operation | **device** |
| **``x``**<br>Exit the current loop | **``device``**<br>Information related to the hardware device |
| **``->``**<br>Skip to the next iteration of the loop | **``cpu``**<br>Information about the CPU, including its usage and specifications |
| **``<-``**<br>Repeat the current iteration of the loop | **``fps``**<br>Frames per second for video or graphical rendering |
| **``X``**<br>Return a result from an action | **``vsync``**<br>Vertical sync settings to reduce screen tearing during rendering |
| **``action``**<br>Initiate or call an action | **``resolution``**<br>Screen resolution |
| **``open``**<br>Open a link | **``orientation``**<br>Orientation of a device's display (landscape or portrait) |
| **``code``**<br>Execute a block of native code | **``darkmode``**<br>Dark mode setting for user interfaces |
| **``xx``**<br>Exit the current application | **``pixel``**<br>Color of the pixel displayed on the screen |
| **``l``**<br>Log data | **``textmode.character``**<br>Symbol on the screen in text mode |
| **``convert``**<br>Convert data from one format to another | **``textmode.cursor``**<br>Cursor position on the screen in text mode |
| **``sql``**<br>Execute SQL query | **``textmode.clear``**<br>Clears the screen in text mode |
| **``clipboard``**<br>Storing or retrieving clipboard temporary data | **``flashlight``**<br>Turns on or off the device's flashlight |
| **``spawner``**<br>Export code to an application, game or operation system | **``location``**<br>Retrieves the current geographic location using GPS or network triangulation |
| **``test``**<br>Test one or all actions | **``gyroscope``**<br>Provides access to the gyroscope sensor for motion detection |
| **``help``**<br>Show description and use of the action | **``accelerometer``**<br>Provides access to the accelerometer sensor to detect acceleration forces |
| **``void``**<br>Perform a void action on the hash | **``compass``**<br>Accesses the magnetic compass sensor to determine orientation relative to the Earth's magnetic field |
| &nbsp; | **``proximity``**<br>Detects the proximity of objects in relation to the device's proximity sensor |
| **text** | **``brightness``**<br>Manages the screen brightness level of the device |
| **``lower``**<br>Convert text to lowercase | **``calendar``**<br>Calendar events on a device |
| **``upper``**<br>Convert text to uppercase | **``gallery``**<br>Photo and video library on a device |
| **``starts``**<br>Check if text starts with a specific substring | **``contacts``**<br>Contact list on a device |
| **``ends``**<br>Check if text ends with a specific substring | &nbsp; |
| **``strip``**<br>Remove leading and trailing spaces from text | **ai** |
| **``strip.start``**<br>Remove leading spaces from text | **``translate``**<br>Converts text from one language to another |
| **``strip.end``**<br>Remove trailing spaces from text | **``spellcheck``**<br>Spell check in different languages |
| **``replace``**<br>Replace occurrences of a substring within text | **``chat``**<br>AI conversation and interaction through text |
| **``find``**<br>Locate a substring within text | **``image``**<br>Create an image |
| **``parse``**<br>Parse text into structured data | **``image.size``**<br>Adjusts the dimensions of an image |
| **``similar``**<br>Find similarity between texts | **``image.square``**<br>Crops an image to a square aspect ratio |
| **``part``**<br>Extract a part of the text | **``image.crop``**<br>Cuts a portion of the image according to specified dimensions |
| **``split``**<br>Split text into parts based on a delimiter | **``image.rotate``**<br>Rotates an image by a specified number of degrees |
| **``join``**<br>Join a list of strings into a single string with a delimiter | **``image.text``**<br>Adds text to an image at specified positions |
| **``date``**<br>Format or parse date-related information | **``image.image``**<br>Adds an image onto another |
| **``escape``**<br>Escape special characters in a string | **``image.grayscale``**<br>Converts an image to grayscale |
| **``escape.html``**<br>Escape HTML tags and attributes in a string | **``image.tint``**<br>Applies a color tint to an image |
| **``escape.url``**<br>Escape URL components | **``image.flip.h``**<br>Flips an image horizontally |
| **``escape.sql``**<br>Escape SQL query components to prevent injection | **``image.flip.v``**<br>Flips an image vertically |
| **``unescape``**<br>Unescape special characters in a string | **``image.upscale``**<br>Increases the resolution of an image |
| **``unescape.html``**<br>Unescape HTML tags and attributes in a string | **``image.draw``**<br>Allows draw, clear or replace objects on an image |
| **``unescape.url``**<br>Unescape URL components | **``image.style``**<br>Applies stylistic effects to an image |
| **``unescape.sql``**<br>Unescape SQL query components | **``image.colorize``**<br>Adds color to a grayscale image |
| **``words``**<br>Split text into individual words | **``image.recognize``**<br>Identifies objects or text within an image |
| **``sentences``**<br>Split text into sentences | **``image.face``**<br>Detects and processes faces within an image |
| **``lines``**<br>Split text into lines | **``image.effect``**<br>Applies special effects to an image |
| **``bytes``**<br>Convert a string into bytes | **``video``**<br>Create a video |
| &nbsp; | **``video.crop``**<br>Cuts a portion of the video according to specified dimensions |
| **list** | **``video.text``**<br>Adds text to a video at specified positions |
| **``merge``**<br>Combine multiple lists into one | **``video.image``**<br>Adds an image to a video |
| **``push``**<br>Add an element to the end of a list | **``video.sound``**<br>Adds audio track to a video |
| **``pop``**<br>Remove and return an element from the end of a list | **``video.video``**<br>Adds another video clip to a video |
| **``reverse``**<br>Reverse the order of elements in a list | **``video.trim``**<br>Trims the video to a specified length |
| **``shuffle``**<br>Randomly reorder elements in a list | **``video.size``**<br>Adjusts the dimensions of a video |
| **``map``**<br>Apply a function to each element in a list | **``video.upscale``**<br>Increases the resolution of a video |
| **``reduce``**<br>Apply a function cumulatively to the elements in a list | **``video.speed``**<br>Adjusts the playback speed of a video |
| **``names``**<br>Retrieve all keys or attribute names from a structure | **``video.volume``**<br>Adjusts the volume of the video's audio track |
| **``values``**<br>Retrieve all values from a structure | **``video.mute``**<br>Removes sound from a video |
| &nbsp; | **``video.face``**<br>Detects and processes faces within a video |
| **math** | **``video.effect``**<br>Applies special effects to a video |
| **``sin``**<br>Sine of the value (in radians) | **``sound``**<br>Create audio track |
| **``cos``**<br>Cosine of the value (in radians) | **``sound.trim``**<br>Trims the audio track to a specified length |
| **``tan``**<br>Tangent of the value (in radians) | **``sound.speed``**<br>Adjusts the playback speed of audio |
| **``sinh``**<br>Hyperbolic sine of the value | **``sound.volume``**<br>Adjusts the volume of an audio track |
| **``cosh``**<br>Hyperbolic cosine of the value | **``sound.effect``**<br>Applies special effects to an audio track |
| **``tanh``**<br>Hyperbolic tangent of the valu | **``music``**<br>Generates music |
| **``asin``**<br>Arc sine of the value | **``voice``**<br>Text voicing with different voices |
| **``acos``**<br>Arc cosine of the value | **``voice.list``**<br>List of available voices |
| **``atan``**<br>Arc tangent of the value | **``voice.recognize``**<br>Convert voice to text |
| **``asinh``**<br>Arc hyperbolic sine of the value | **``voice.stop``**<br>Stop dictation of the text |
| **``acosh``**<br>Arc hyperbolic cosine of the value | **``voice.capture``**<br>Create a specific voice |
| **``atanh``**<br>Arc hyperbolic tangent of the value | **``motion``**<br>Processes motion-based data |
| **``round``**<br>Rounds a number to the nearest integer or to the specified number of decimal places | **``motion.capture``**<br>Records or analyzes motion data in real-time |
| **``floor``**<br>Largest integer less than or equal to a number | &nbsp; |
| **``ceil``**<br>Smallest integer greater than or equal to a number | **ui** |
| **``log``**<br>Logarithm (natural by default) of a number | **``ui``**<br>Creating a basic element of user interface |
| **``factorial``**<br>Factorial of a given non-negative number | **``bg``**<br>Sets or updates the background properties, such as color or image |
| **``fibonacci``**<br>Fibonacci numbers up to a specified index | **``show``**<br>Displays a UI element to make it visible |
| **``golden``**<br>Golden ratio of a number | **``hide``**<br>Hides a UI element to make it invisible |
| **``abs``**<br>Absolute value of a number | **``enable``**<br>Enables a UI element, making it interactive and functional |
| **``min``**<br>Smallest of a list of numbers | **``disable``**<br>Disables a UI element, preventing interaction or use |
| **``max``**<br>Largest of a list of numbers | **``focus``**<br>Sets focus on a specific UI element, making it active or highlighted |
| **``avg``**<br>Average value of a list of numbers | **``unfocus``**<br>Removes focus from a UI element |
| **``sum``**<br>Sum of a list of numbers | **``scale``**<br>Adjusts the size of a UI element by scaling it up or down |
| **``random``**<br>Generates a pseudo-random number | **``ui.text``**<br>Displays or manages text within the user interface |
| **``random.seed``**<br>Sets or gets the seed for the random number generator to produce reproducible results | **``ui.image``**<br>Displays or manages images within the user interface |
| **``random.reseed``**<br>Sets a new random seed for the random number generator | **``ui.video``**<br>Handles video playback or displays video content in the UI |
| &nbsp; | **``ui.sound``**<br>Manages sound playback or controls audio settings in the UI |
| **time** | **``ui.camera``**<br>Handles camera input or streams video from a camera in the UI |
| **``t``**<br>Stopwatch for calculating the time spent on operations | **``ui.draw``**<br>Enables drawing within the user interface |
| **``time``**<br>Provides current time since the epoch (1970-01-01 00:00:00 UTC) | **``ui.header``**<br>Defines or manages the header section of the user interface |
| **``timer``**<br>Creates a timer that can be used to trigger events at specific intervals | **``ui.footer``**<br>Defines or manages the footer section of the user interface |
| **``timer.remove``**<br>Removes previously created timer | **``ui.wait``**<br>Displays a waiting indicator within the UI |
| **``timepast``**<br>Calculates time passed since a given start time | **``ui.gallery``**<br>Manages or displays a collection of images or media items |
| **``wait``**<br>Pauses execution for a specified number of seconds | **``ui.button``**<br>Defines or manages buttons in the UI for user interaction |
| &nbsp; | **``ui.select``**<br>Creates or manages a selection interface, such as a dropdown menu |
| **crypto** | **``ui.switch``**<br>Implements a toggle switch for binary choices in the UI |
| **``encrypt``**<br>Encrypts data using a specified key | **``ui.progress``**<br>Displays a progress bar or status indicator |
| **``decrypt``**<br>Decrypts previously encrypted data using the specified key | **``ui.slider``**<br>Implements a sliding control for adjusting values along a range |
| **``hash``**<br>Generates a hash for the data or generates a random text | **``ui.edit``**<br>Enables text editing or manages editable fields in the UI |
| **``uuid``**<br>Generates a universally unique identifier | **``ui.divider``**<br>Inserts a visual divider or separating line within the UI layout |
| **``md5``**<br>Generates an MD5 hash of a text | **``ui.split.h``**<br>Splits a UI container horizontally to create multiple sections |
| **``sha1``**<br>Generates an SHA-1 hash of a text | **``ui.split.v``**<br>Splits a UI container vertically to create multiple sections |
| **``sha256``**<br>Generates an SHA-256 hash of a text | **``ui.list``**<br>Displays a list of items for selection or viewing |
| **``sha512``**<br>Generates an SHA-512 hash of a text | **``ui.tile``**<br>Arranges content in a tiled format for visual organization |
| **``crc32``**<br>Calculates the CRC32 checksum of a text | **``ui.chart``**<br>Data visualization using charts and graphs |
| **``base64.encode``**<br>Encodes the data into base64 format | **``ui.color``**<br>Color selection or manages color properties in the UI |
| **``base64.decode``**<br>Decodes base64 encoded data back to its original form | **``ui.date``**<br>Date selection or displays date information |
| **``gzip.encode``**<br>Compresses data using the GZip compression algorithm | **``ui.menu``**<br>Creates or manages menu options for navigation or actions |
| **``gzip.decode``**<br>Decompresses GZip compressed data | **``ui.menu.context``**<br>Defines a context menu for right-click actions or additional options |
| **``rsa.encode``**<br>Encrypts data using RSA encryption with a public key | **``window``**<br>Creates or manages window |
| **``rsa.decode``**<br>Decrypts data encrypted with RSA using the corresponding private key | **``window.list``**<br>List of windows |
| **``rsa.public``**<br>Generates the RSA public key used for encryption | **``title``**<br>Sets or updates the title of a window or UI element |
| **``rsa.private``**<br>Generates the RSA private key used for decryption | **``icon``**<br>Defines or changes an icon associated with a window or UI element |
| **``ssl.encode``**<br>Performs SSL encryption on data to secure communication | **``size``**<br>Adjusts the dimensions or size of a window or UI element |
| **``ssl.decode``**<br>Decrypts data encrypted with SSL for secure data transfer | **``size.max``**<br>Sets the maximum size constraints for a window or UI element |
| **``ssl.check``**<br>Verifies the validity and authenticity of an SSL certificate | **``size.min``**<br>Sets the minimum size constraints for a window or UI element |
| **``bcrypt.encode``**<br>Hashes a password using the bcrypt algorithm for secure storage | **``position``**<br>Adjusts the position or placement of a window or UI element |
| **``bcrypt.check``**<br>Verifies a password against a bcrypt hashed password | **``direction``**<br>Text writing direction for the selected language |
| &nbsp; | **``attention``**<br>Highlights a window or UI element |
| **file** | **``top``**<br>Brings a window or UI element to the top layer or foreground |
| **``file``**<br>Read or write data to a file at a specified path | **``nofocus``**<br>Prevents a UI element from receiving focus or interaction |
| **``file.exists``**<br>Checks if a specified file exists at the given path | **``noresize``**<br>Locks the size of a window or UI element, preventing resizing |
| **``file.read``**<br>Reads the contents of a specified file | **``center``**<br>Centers a window or UI element within its parent container or screen |
| **``file.read.text``**<br>Reads the text contents of a specified file | **``fullscreen``**<br>Switches a window or UI element to fullscreen mode |
| **``file.read.lines``**<br>Reads a specified file line by line into a list | **``maximize``**<br>Minimizes a window to the taskbar or dock |
| **``file.write``**<br>Writes data to a specified file, creating or replacing it | **``minimize``**<br> |
| **``file.append``**<br>Appends data to the end of a specified file without replacing it | **``exclusive``**<br>Enables exclusive mode restricting other operations |
| **``file.remove``**<br>Removes a specified file from the file system | **``border``**<br>Border properties or visibility for a UI element |
| **``file.move``**<br>Moves a specified file to a new location | **``filedrop``**<br>File drag-and-drop capabilities within the application UI |
| **``file.copy``**<br>Copies a specified file to a new location | **``dialog``**<br>Dialog box for user prompts or options |
| **``file.rename``**<br>Renames a specified file | **``dialog.file``**<br>Opens a file selection dialog |
| **``file.link``**<br>Creates a hard link to a specified file | **``effect``**<br>Applies visual or audio effect to a UI element |
| **``file.link.exists``**<br>Checks if a hard link exists at the given path | **``effect.remove``**<br>Removes applied effect from a UI element |
| **``file.info``**<br>Retrieves information about a specified file | &nbsp; |
| **``file.size``**<br>Returns the size of a specified file in bytes | **input** |
| **``file.permission``**<br>Retrieves or sets permissions for a specified file | **``tap``**<br>Simulates a tap gesture |
| **``file.time``**<br>Gets or sets the modified timestamp for a specified file | **``key``**<br>Key binding |
| **``file.sha256``**<br>Computes the SHA256 checksum of a specified file | **``key.remove``**<br>Removes a key binding |
| **``file.crc32``**<br>Computes the CRC32 checksum for a specified file | **``key.enable``**<br>Enables key binding |
| **``file.base64``**<br>Encodes a specified file to base64 format | **``key.disable``**<br>Disable key binding |
| **``file.zip``**<br>Compresses a specified file into a ZIP archive | **``key.press``**<br>Simulates a key press event |
| **``file.zip.list``**<br>Lists the files contained within a ZIP archive | **``keyboard``**<br>Keyboard information |
| **``file.zip.exists``**<br>Checks if a specific file exists within a ZIP archive | **``mouse``**<br>Mouse information |
| **``file.zip.read``**<br>Reads a specific file from within a ZIP archive | **``mouse.lock``**<br>Locks the mouse cursor to prevent it from leaving a designated area |
| **``file.zip.remove``**<br>Removes a specific file from a ZIP archive | **``mouse.position``**<br>Retrieves or sets the current position of the mouse cursor |
| **``file.unzip``**<br>Extracts files from a ZIP archive into a specified directory | **``mouse.shape``**<br>Change the shape of the mouse cursor |
| **``file.gzip``**<br>Compresses a specified file using GZip compression | **``gamepad``**<br>Gamepad information |
| **``file.ungzip``**<br>Decompresses a GZip-compressed file | **``gamepad.vibrate``**<br>Gamepad vibration |
| **``file.void``**<br>Compresses the specified file using GZip compression and places it in a Void container | &nbsp; |
| **``file.unvoid``**<br>Decompresses a GZip-compressed files and directories from a Void container | **game** |
| **``dir.exists``**<br>Checks if a specified directory exists | **``scene``**<br>Create or show a custom game scene |
| **``dir.create``**<br>Creates a new directory at a specified path | **``character``**<br>Create or change a game character |
| **``dir.copy``**<br>Copies a specified directory and its contents to a new location | **``say``**<br>Say or show the character's speech |
| **``dir.move``**<br>Moves a specified directory to a new location | **``item``**<br>Create or change a game item |
| **``dir.rename``**<br>Renames a specified directory | **``item.put``**<br>Put a game item to the inventory |
| **``dir.remove``**<br>Removes a specified directory and its contents | **``item.remove``**<br>Remove an item from the inventory |
| **``dir.list``**<br>Lists the contents of a specified directory | **``item.on``**<br>Put item on |
| **``dir.clear``**<br>Clears all contents of a specified directory without deleting the directory itself | **``item.off``**<br>Take item off |
| **``dir.info``**<br>Retrieves information about a specified directory | **``camera``**<br>Create or change a game camera |
| **``dir.size``**<br>Calculates the total size of a specified directory and its contents | **``world``**<br>Create a game world |
| **``dir.permission``**<br>Gets or sets the permissions of a specified directory | &nbsp; |
| **``dir.time``**<br>Gets or sets the timestamps of a specified directory | &nbsp; |
| **``dir.zip``**<br>Compresses a specified directory into a ZIP archive | &nbsp; |
| **``dir.void``**<br>Compresses a specified directory into a Void container | &nbsp; |
| **``drive.list``**<br>Lists all available drives on the system | &nbsp; |
| **``drive.name``**<br>Gets or sets the name of a specified drive | &nbsp; |
| **``drive.size``**<br>Total size of a specified drive | &nbsp; |
| **``drive.used``**<br>Amount of used space on a specified drive | &nbsp; |
| **``drive.free``**<br>Amount of free space on a specified drive | &nbsp; |
| **``drive.info``**<br>Retrieves information about a specified drive | &nbsp; |
| **``drive.mount``**<br>Mounts a drive to make it accessible | &nbsp; |
| **``drive.unmount``**<br>Unmounts a drive | &nbsp; |
| **``drive.create``**<br>Creates a new virtual drive or volume | &nbsp; |
| **``drive.resize``**<br>Resizes an existing drive partition or volume | &nbsp; |
| **``drive.format``**<br>Formats a drive with a specified file system | &nbsp; |
| **``drive.remove``**<br>Removes or deletes a specified drive or partition | &nbsp; |
| **``path.drive``**<br>Drive component of a specified file path | &nbsp; |
| **``path.dir``**<br>Directory portion of a specified file path | &nbsp; |
| **``path.file``**<br>File portion of a specified file path | &nbsp; |
| **``path.name``**<br>Name of the file without extension from a specified path | &nbsp; |
| **``path.extension``**<br>File extension from a specified file path | &nbsp; |
| **``path.strip``**<br>Removes the extension from a specified path | &nbsp; |

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
        [void.encode [1 2 3]]
    decode
        [void.decode "[1 2 3]"]
    write
        [file path/to/file.void [1 2 3]]
    read
        [file path/to/file.void]
    compress
        [file.void path/to/file]
        [dir.void path/to/dir]
    decompress
        [file.unvoid path/to/file.void]
    encrypt
        [file.void path/to/file key]
        [dir.void path/to/dir key]
    decrypt
        [file.unvoid path/to/file.void key]
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
list short
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
base64 short
    *ViBPIEkgRCBmb3JtYXQ=
binary
    *
        3
        <00 01 02>
binary short
   *3 <00 01 02>
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
    "list short": ["text", 1, true, false, null],
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
    "base64 short": "need to convert",
    "binary": "impossible",
    "binary short": "impossible",
    "binary in hex": "need to convert",
    "binary in bin": "need to convert"
}
```

</td>
</tr>

</table>

> [!TIP]
> Use **V O I D format [highlighting 📃](https://github.com/voidspawner/void.ideology/blob/main/asset/settings/void.sublime-syntax)** for **[Sublime Text](https://sublimetext.com)**.
>
> **``Tools``** → **``Developer``** → **``New Syntax…``** → **``Copy · Paste``** → **``Save as void.sublime-syntax``**
>
> You can change the **color scheme** to alternate sections.
> 
> **``Preferences``** → **``Customize Color Scheme``**
>
> ```json
> {
>   "rules":
>   [
>     {
>       "scope": "variable.void.odd",
>       "foreground": "hsl(185, 100%, 50%)"
>     },
>     {
>       "scope": "variable.void.even",
>       "foreground": "hsl(185, 100%, 80%)"
>     }
>   ]
> }
> ```

## V O I D db
A database that uses **``V O I D``** · **``JSON``** · **``CSV``** files for storage directly. Data is **cached**, **indexed** and **saved** automatically. **Easy access** to data without the need to create complex constructs.

> **``data.json``**
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
> = data.json/list.index.2.value 3
>```

> **``data.csv``**
> ```csv
> index,text,value
> 1,text 1,value 1
> 5,text 5,value 5
> ```
>
> ```
> . {data.csv/index.5.value}
> . {data.csv/1.value}
> = data.csv/index.5.value 3
>```

## V O I D ai
**[Artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)** that makes it easier to work with data. Third-party AI is currently connected.

> **``ChatGPT``**
> ```
> chat "radius of the Earth"
> chat "tell me a story"
> chat "translate to portuguese: Hi world :D"
> translate "嗨，世界 :D"
> translate "Hi world :D" portuguese
> image "playing cats on the lawn" cats.jpg
> code python "mouse movement simulation"
> ```
>
> **``Stable Diffusion``**
> ```
> image "playing cats on the lawn" cats.jpg
> video "playing cats on the lawn" cats.mp4
> image.draw "remove the cat in the center and add more grass" cats.jpg cats-edited.jpg
> image.colorize dogs.jpg dogs-colorized.jpg
> image.style "cyberpunk" cats.jpg cats-cyberpunk.jpg
> image.background cats.jpg cats-without-background.png
> image.upscale cats.jpg cats-resize-2x.jpg
> image.upscale cats.jpg cats-resize-4x.jpg 4
> image.face man.jpg child.jpg man-to-child.jpg
> ```
> 
> **``Voice Cloning``**
> ```
> voice "Hi world :D"
> voice.capture my
> voice "Hi world :D" my
> ```
> 
> **``Speech Recognition``**
>
> ```
> voice.recognize
> voice.recognize talk.mp3
> voice.recognize video.mp4
> ```
> 
> **``Google TTS``**
>
> ```
> google.voice "Hi world :D"
> voice "Hi world :D"
> ```
> 
> **``DeepL``**
>
> ```
> deepl.translate "你好，世界 :D"
> translate "你好，世界 :D"
> ```

Work is underway to develop a custom AI that will run on a **[V O I D chip](https://github.com/voidspawner/void.tech#chip)**.

## V O I D game
**[⌜ V O I D game ⌟](https://voidsp.ru/void.game)** is a game that creates an **infinite** number of games, vapps and content.

## V O I D social
**[⌜ V O I D social ⌟](https://voidsp.ru/void.social)** is a social network where you can **quickly** and **easily** communicate without words with people all over the world.

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create applications and games.

## V O I D tech
**[⌜ V O I D tech ⌟](https://github.com/voidspawner/void.tech)** are combinable devices controlled by **[V O I D ai](#v-o-i-d-ai)** for creating **individual** stand-alone productions, as well as creating individual products with **unique designs** and in the required quantities.

## V O I D ideology
**[⌜ V O I D ⌟](https://github.com/voidspawner/void.ideology)**  is not only about compact technologies, but also an **ideology** that shows where these technologies are taking us.

## V O I D license
**⌜ V O I D license ⌟** is a license to distribute digital content and goods. Expressed in a single sentence:

> **DO WHAT YOU WANT**

You can use it in both **private** and **open source**, embed it in **free** or **paid** products. **Modify**. Create your **own solutions** based on it. **No need to specify the author**.

## V O I D task
> [!IMPORTANT]
> By adding your code to the repository, you are publishing it under the **V O I D licence**.

Find out current **tasks** and **payment** at [**V O I D task**](https://voidsp.ru/void.task)
