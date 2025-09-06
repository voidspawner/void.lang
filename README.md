# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **[V O I D](#v-o-i-d-format)** or **[JSON](https://en.wikipedia.org/wiki/JSON)** format. It is used as a replacement for the standard **``Bash``**・**``CMD``**・etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one ``V O I D`` or ``JSON`` file**. Since the **code is presented as data**, applications can be easily generated with **``AI``**, updated, installed and launched remotely.

> [!IMPORTANT]
> **The project is in the process of development.**

  <img src="https://github.com/voidspawner/void.data/blob/main/asset/image/logo.jpg" width="100%">

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
<table><tr><th align="center"><img width="441" height="1"><p>V O I D format</p></th><th align="center"><img width="441" height="1"><p>JSON</p></th></tr><tr><td>

```
run
  [[. 'Hi World :D
```

</td><td>

```json
{
  "run": [
    [".", "Hi World :D"]
  ]
}
```

</td></tr></table>

##### Even simpler
<table><tr><td>
<img width="441" height="1">

```
. Hi World :D
```
</td><td>
<img width="441" height="1">
  
```json
[
  [".", "Hi World :D"]
]
```
</td></tr></table>

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

> Count of actions **``274``**

| <img width="1000" height="1"> | <img width="1000" height="1"> |
| --- | --- |
| **⌜ value ⌟** | **⌜ crypto ⌟** |
| **``set``**<br>Assign a value to a specified parameter | **``decrypt``**<br>Decrypts previously encrypted data using the specified key |
| **``remove``**<br>Remove a specified parameter or value | **``hash``**<br>Generates a hash for the data or generates a random text |
| **``type``**<br>Determine the data type of a specified parameter | **``uuid``**<br>Generates a universally unique identifier |
| **``text``**<br>Specify a parameter as a text type | **``md5``**<br>Generates an MD5 hash of a text |
| **``number``**<br>Specify a parameter as a number type | **``sha1``**<br>Generates an SHA-1 hash of a text |
| **``bool``**<br>Specify a parameter as a boolean type | **``sha256``**<br>Generates an SHA-256 hash of a text |
| **``list``**<br>Specify a parameter as a list type | **``sha512``**<br>Generates an SHA-512 hash of a text |
| **``binary``**<br>Specify a parameter as a binary type | **``crc32``**<br>Calculates the CRC32 checksum of a text |
| **``l``**<br>Gets the length of the text, the number of items in a list or dictionary, the count of bytes in a number | **``base64``**<br>Encodes the data into Base64 format |
| **⌜ expression ⌟** | **``base64.decode``**<br>Decodes Base64 encoded data back to its original form |
| **``-``**<br>Perform subtraction operation | **``base85``**<br>Encodes the data into Base85 format |
| **``*``**<br>Perform multiplication operation | **``base85.decode``**<br>Decodes Base85 encoded data back to its original form |
| **``/``**<br>Perform division operation | **``gzip``**<br>Compresses data using the GZip compression algorithm |
| **``%``**<br>Perform modulo operation | **``gzip.decode``**<br>Decompresses GZip compressed data |
| **``^``**<br>Elevation operator | **``rsa``**<br>Encrypts data using RSA encryption with a public key |
| **``not``**<br>Perform negation | **``rsa.decode``**<br>Decrypts data encrypted with RSA using the corresponding private key |
| **``and``**<br>Perform AND operation | **``ssl``**<br>Performs SSL encryption on data to secure communication |
| **``or``**<br>Perform OR operation | **``ssl.decode``**<br>Decrypts data encrypted with SSL for secure data transfer |
| **``xor``**<br>Perform XOR operation | **``bcrypt``**<br>Hashes a password using the bcrypt algorithm for secure storage |
| **``>>``**<br>Perform right shift operation | **``bcrypt.check``**<br>Verifies a password against a bcrypt hashed password |
| **``<<``**<br>Perform left shift operation | **⌜ file ⌟** |
| **``=``**<br>Assign value to a variable | **``file.exists``**<br>Checks if a specified file exists at the given path |
| **``+=``**<br>Add and assign value to a variable | **``file.lines``**<br>Reads a specified file line by line into a list |
| **``=+``**<br>Assign and add value to a variable | **``file.remove``**<br>Removes a specified file from the file system |
| **``-=``**<br>Subtract and assign value to a variable | **``file.move``**<br>Moves a specified file to a new location |
| **``*=``**<br>Multiply and assign value to a variable | **``file.copy``**<br>Copies a specified file to a new location |
| **``/=``**<br>Divide and assign value to a variable | **``file.rename``**<br>Renames a specified file |
| **``%=``**<br>Modulo and assign value to a variable | **``file.link``**<br>Creates a hard link to a specified file |
| **``^=``**<br>Elevation and assign value to a variable | **``file.link.exists``**<br>Checks if a hard link exists at the given path |
| **``not=``**<br>NOT and assign value to a variable | **``file.info``**<br>Retrieves information about a specified file |
| **``and=``**<br>AND and assign value to a variable | **``file.size``**<br>Returns the size of a specified file in bytes |
| **``or=``**<br>OR and assign value to a variable | **``file.permission``**<br>Retrieves or sets permissions for a specified file |
| **``xor=``**<br>XOR and assign value to a variable | **``file.time``**<br>Gets or sets the modified timestamp for a specified file |
| **``>>=``**<br>Right shift and assign value to a variable | **``file.sha256``**<br>Computes the SHA256 checksum of a specified file |
| **``<<=``**<br>Left shift and assign value to a variable | **``file.crc32``**<br>Computes the CRC32 checksum for a specified file |
| **``==``**<br>Checks if left value is equal to right | **``file.base64``**<br>Encodes a specified file to base64 format |
| **``!=``**<br>Check if values are not equal | **``file.zip``**<br>Compresses a specified file into a ZIP archive |
| **``>``**<br>Checks if left value is greater than right | **``file.zip.list``**<br>Lists the files contained within a ZIP archive |
| **``<``**<br>Checks if left value is less than right | **``file.zip.exists``**<br>Checks if a specific file exists within a ZIP archive |
| **``>=``**<br>Checks if left value is greater than or equal to right | **``file.zip.read``**<br>Reads a specific file from within a ZIP archive |
| **``<=``**<br>Checks if left value is less than or equal to right | **``file.zip.remove``**<br>Removes a specific file from a ZIP archive |
| **``in``**<br>Checks if value is in a list or subtext in a text or name in a dictionary | **``file.unzip``**<br>Extracts files from a ZIP archive into a specified directory |
| **``notin``**<br>Checks if value is not in a list or subtext in a text or or name not in a dictionary | **``file.gzip``**<br>Compresses a specified file using GZip compression |
| **``is``**<br>Checks if value is in a list or name in a dictionary | **``file.ungzip``**<br>Decompresses a GZip-compressed file |
| **``isnot``**<br>Checks if value is not in a list or name not in a dictionary | **``file.void``**<br>Compresses the specified file using GZip compression and places it in a Void container |
| **⌜ control ⌟** | **``file.unvoid``**<br>Decompresses a GZip-compressed files and directories from a Void container |
| **``printn``**<br>Output data to the console without newline | **``dir``**<br>Lists the contents of a specified directory |
| **``input``**<br>Input text from the user | **``dir.create``**<br>Creates a new directory at a specified path |
| **``if``**<br>Evaluate a conditional expression | **``dir.exists``**<br>Checks if a specified directory exists |
| **``loop``**<br>Perform a loop operation | **``dir.remove``**<br>Removes a specified directory and its contents |
| **``break``**<br>Exit the current loop | **``dir.move``**<br>Moves a specified directory to a new location |
| **``continue``**<br>Skip to the next iteration of the loop | **``dir.copy``**<br>Copies a specified directory and its contents to a new location |
| **``repeat``**<br>Repeat the current iteration of the loop | **``dir.rename``**<br>Renames a specified directory |
| **``result``**<br>Return a result from an action | **``dir.clear``**<br>Clears all contents of a specified directory without deleting the directory itself |
| **``action``**<br>Initiate or call an action | **``dir.info``**<br>Retrieves information about a specified directory |
| **``open``**<br>Open a link | **``dir.size``**<br>Calculates the total size of a specified directory and its contents |
| **``code``**<br>Execute a block of native code | **``dir.permission``**<br>Gets or sets the permissions of a specified directory |
| **``info``**<br>Log data | **``dir.time``**<br>Gets or sets the timestamps of a specified directory |
| **``convert``**<br>Convert data from one format to another | **``dir.zip``**<br>Compresses a specified directory into a ZIP archive |
| **``sql``**<br>Execute SQL query | **``dir.void``**<br>Compresses a specified directory into a Void container |
| **``clipboard``**<br>Storing or retrieving clipboard temporary data | **``drive``**<br>Lists all available drives on the system |
| **``test``**<br>Test one or all actions | **``drive.name``**<br>Gets or sets the name of a specified drive |
| **``help``**<br>Show description and use of the action | **``drive.size``**<br>Total size of a specified drive |
| **``exit``**<br>Exit the current application | **``drive.used``**<br>Amount of used space on a specified drive |
| **⌜ content ⌟** | **``drive.free``**<br>Amount of free space on a specified drive |
| **``say``**<br>Text voicing with different voices | **``drive.info``**<br>Retrieves information about a specified drive |
| **``voice``**<br>List of available voices | **``drive.mount``**<br>Mounts a drive to make it accessible |
| **``recognize``**<br>Convert voice to text | **``drive.unmount``**<br>Unmounts a drive |
| **``capture``**<br>Records or analyzes motion data in real-time | **``drive.create``**<br>Creates a new virtual drive or volume |
| **``ui``**<br>Creating a basic element of user interface | **``drive.resize``**<br>Resizes an existing drive partition or volume |
| **⌜ text ⌟** | **``drive.format``**<br>Formats a drive with a specified file system |
| **``upper``**<br>Convert text to uppercase | **``drive.remove``**<br>Removes or deletes a specified drive or partition |
| **``starts``**<br>Check if text starts with a specific substring | **``path``**<br>Returns components of a specified file path |
| **``ends``**<br>Check if text ends with a specific substring | **``path.drive``**<br>Drive component of a specified file path |
| **``strip``**<br>Remove leading and trailing spaces from text | **``path.dir``**<br>Directory portion of a specified file path |
| **``strip.start``**<br>Remove leading spaces from text | **``path.file``**<br>File portion of a specified file path |
| **``strip.end``**<br>Remove trailing spaces from text | **``path.name``**<br>Name of the file without extension from a specified path |
| **``replace``**<br>Replace occurrences of a substring within text | **``path.extension``**<br>File extension from a specified file path |
| **``find``**<br>Locate a substring within text | **``path.strip``**<br>Removes the extension from a specified path |
| **``parse``**<br>Parse text into structured data | **⌜ format ⌟** |
| **``part``**<br>Extract a part of the text or list | **``void.decode``**<br>Decodes data from the Void format |
| **``split``**<br>Split text into parts based on a delimiter | **``json``**<br>Encodes data into the JSON format |
| **``join``**<br>Join a list of strings into a single string with a delimiter | **``json.decode``**<br>Decodes data from the JSON format |
| **``date``**<br>Format or parse date-related information | **``csv``**<br>Encodes data into the CSV format |
| **``escape``**<br>Escape HTML tags and attributes in a string | **``csv.decode``**<br>Decodes data from the CSV format |
| **``unescape``**<br>Unescape HTML tags and attributes in a string | **``yaml``**<br>Encodes data into the YAML format |
| **``words``**<br>Count the number of words | **``yaml.decode``**<br>Decodes data from the YAML format |
| **``sentences``**<br>Count the number of sentences | **``ini``**<br>Encodes data into the INI format |
| **``lines``**<br>Count the number of lines | **``ini.decode``**<br>Decodes data from the INI format |
| **``translate``**<br>Converts text from one language to another | **``html``**<br>Encodes data into the HTML format |
| **``spellcheck``**<br>Spell check in different languages | **``html.decode``**<br>Decodes data from the HTML format |
| **⌜ list ⌟** | **``markdown``**<br>Encodes Markdown-formatted text into the HTML format |
| **``pop``**<br>Remove and return an element from the end of a list | **``markdown.decode``**<br>Decodes data from the Markdown-formatted text |
| **``merge``**<br>Combine multiple lists into one | **``xml``**<br>Encodes data into the XML format |
| **``reverse``**<br>Reverse the order of elements in a list | **``xml.decode``**<br>Decodes data from the XML format |
| **``shuffle``**<br>Randomly reorder elements in a list | **``css``**<br>Encodes data into the CSS format |
| **``unique``**<br>Leave only unique values in a list | **``css.decode``**<br>Decodes data from the CSS format |
| **``map``**<br>Apply a function to each element in a list | **⌜ communication ⌟** |
| **``reduce``**<br>Apply a function cumulatively to the elements in a list | **``request``**<br>Sends an HTTP (GET by default) request to a specified URL |
| **``filter``**<br>Apply a filter function to each element in a list | **``download``**<br>Downloads content from a specified URL |
| **``indexes``**<br>Retrieve all keys or attribute names from a structure | **``cookie``**<br>Gets or sets a specified cookie |
| **``values``**<br>Retrieve all values from a structure | **``cookie.remove``**<br>Removes a specified cookie from the client's storage |
| **⌜ math ⌟** | **``social``**<br>Interacting with social API |
| **``cos``**<br>Cosine of the value (in radians) | **``notification``**<br>Send notification |
| **``tan``**<br>Tangent of the value (in radians) | **``mail``**<br>Send mail |
| **``sinh``**<br>Hyperbolic sine of the value | **``call``**<br>Initiate a voice or video call to a specified recipient |
| **``cosh``**<br>Hyperbolic cosine of the value | **``sms``**<br>Send a text message (SMS) to a specified recipient |
| **``tanh``**<br>Hyperbolic tangent of the valu | **⌜ device ⌟** |
| **``asin``**<br>Arc sine of the value | **``cpu``**<br>Information about the CPU, including its usage and specifications |
| **``acos``**<br>Arc cosine of the value | **``fps``**<br>Frames per second for video or graphical rendering |
| **``atan``**<br>Arc tangent of the value | **``vsync``**<br>Vertical sync settings to reduce screen tearing during rendering |
| **``asinh``**<br>Arc hyperbolic sine of the value | **``resolution``**<br>Screen resolution |
| **``acosh``**<br>Arc hyperbolic cosine of the value | **``orientation``**<br>Orientation of a device's display (landscape or portrait) |
| **``atanh``**<br>Arc hyperbolic tangent of the value | **``dark``**<br>Dark mode setting for user interfaces |
| **``round``**<br>Rounds a number to the nearest integer or to the specified number of decimal places | **``pixel``**<br>Color of the pixel displayed on the screen |
| **``floor``**<br>Largest integer less than or equal to a number | **``char``**<br>Symbol on the screen in text mode |
| **``ceil``**<br>Smallest integer greater than or equal to a number | **``cursor``**<br>Cursor position on the screen in text mode |
| **``log``**<br>Logarithm (natural by default) of a number | **``clear``**<br>Clears the screen in text mode |
| **``fact``**<br>Factorial of a given non-negative number | **``light``**<br>Turns on or off the device's flashlight |
| **``fib``**<br>Fibonacci numbers up to a specified index | **``location``**<br>Retrieves the current geographic location using GPS or network triangulation |
| **``gr``**<br>Golden ratio of a number | **``gyroscope``**<br>Provides access to the gyroscope sensor for motion detection |
| **``abs``**<br>Absolute value of a number | **``accelerometer``**<br>Provides access to the accelerometer sensor to detect acceleration forces |
| **``min``**<br>Smallest of a list of numbers | **``compass``**<br>Accesses the magnetic compass sensor to determine orientation relative to the Earth's magnetic field |
| **``max``**<br>Largest of a list of numbers | **``proximity``**<br>Detects the proximity of objects in relation to the device's proximity sensor |
| **``avg``**<br>Average value of a list of numbers | **``brightness``**<br>Manages the screen brightness level of the device |
| **``sum``**<br>Sum of a list of numbers | **``calendar``**<br>Calendar events on a device |
| **``random``**<br>Generates a pseudo-random number | **``gallery``**<br>Photo and video library on a device |
| **``random.seed``**<br>Sets or gets the seed for the random number generator to produce reproducible results | **``contacts``**<br>Contact list on a device |
| **⌜ time ⌟** | **``keyboard``**<br>Keyboard information |
| **``timer``**<br>Creates a timer that can be used to trigger events at specific intervals | **``mouse``**<br>Mouse information |
| **``timer.remove``**<br>Removes previously created timer | **``gamepad``**<br>Gamepad information |
| **``timecheck``**<br>Stopwatch for calculating the time spent on operations | **``tap``**<br>Simulates a tap gesture |
| **``wait``**<br>Pauses execution for a specified number of seconds | **``key``**<br>Key binding |
| &nbsp; | **⌜ content ⌟** |
| &nbsp; | **``video``**<br>Create a video |
| &nbsp; | **``sound``**<br>Create audio track |
| &nbsp; | **``music``**<br>Generates music |
| &nbsp; | **``model``**<br>Create 3D model |
| &nbsp; | **``book``**<br>Create a book, comic, manga |

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





