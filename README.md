# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **[V O I D](#v-o-i-d-format)** or **[JSON](https://en.wikipedia.org/wiki/JSON)** format. It is used as a replacement for the standard **``Bash``**・**``CMD``**・etc. languages and for creating **``games``**, **``apps``** and **``content``**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. The whole application fits in **one ``V O I D`` or ``JSON`` file**. Since the **code is presented as data**, applications can be easily generated with **``AI``**, updated, installed and launched remotely.

> [!IMPORTANT]
> **The project is in the process of development.**

  <img src="https://github.com/voidspawner/void.storage/blob/main/image/logo_muryashka.jpg" width="100%">

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

| Language                                                 | Engine                              | Web                     | CLI                     | Server                  | Mobile                  | Windows                 | macOS                   | Linux                   | iOS                     | Android                 | Xbox                    | Switch                  | PlayStation             | Steam Deck              | Steam Machine           |
| -------------------------------------------------------- | ----------------------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- |
| [**Python**](https://www.python.org/downloads)           | <p align="center">Python</p>        | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> |
| [**JavaScript**](https://nodejs.org/en/download)         | <p align="center">NodeJS</p>        | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> |
| [**Swift**](https://www.swift.org/download)              | <p align="center">LLVM</p>          | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> |
| [**Kotlin**](https://developer.android.com/studio)       | <p align="center">JVM</p>           | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> |
| [**GDScript**](https://godotengine.org/download/windows) | <p align="center">Godot</p>         | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> |
| [**C++**](https://www.unrealengine.com/download)         | <p align="center">Unreal Engine</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> |

## Example
##### Simple
<table><tr><th align="center"><img width="441" height="1"><p>V O I D format</p></th><th align="center"><img width="441" height="1"><p>JSON</p></th></tr><tr><td>

```
. Hi World :D
```
</td><td>
  
```json
". Hi World :D"
```
</td></tr></table>

##### Show current version
<table><tr><td>
<img width="441" height="1">

```
. {about.version}
```
</td><td>
<img width="441" height="1">
  
```json
". {about.version}"
```
</td></tr></table>

##### Multilanguage text
<table><tr><td>
<img width="441" height="1">

```
run
  [. {text.hi} :D
  [. language · {language}
text
  hi
    en
      Hi World
    zh
      你好世界
    fr
      Bonjour le monde
    es
      Hola Mundo
    pt
      Olá Mundo
    it
      Ciao mondo
    de
      Hallo Welt
    jp
      こんにちは世界
    ru
      Привет, мир
    ar
      مرحبا بالعالم
    hi
      हैलो वर्ल्ड
```
</td><td>
<img width="441" height="1">
  
```json
{
  "run": [
    [".", "{text.hi}", ":D"],
    [".", "language", "·", "{language}"]
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
</td></tr></table>

##### Web server
<table><tr><td>
<img width="441" height="1">

```
[. web server on port 80
[cloud '<h1>Hi World 😄</h1>
```
</td><td>
<img width="441" height="1">
  
```json
[
  [".", "web", "server", "on", "port", 80],
  ["cloud", "<h1>Hi World 😄</h1>"]
]
```
</td></tr></table>

##### File sharing
<table><tr><td>
<img width="441" height="1">

```
[. shared folder on port 80
[cloud /path/to/share
```
</td><td>
<img width="441" height="1">
  
```json
[
  [".", "shared", "folder", "on", "port", 80],
  ["cloud", "/path/to/share"]
]
```
</td></tr></table>

##### Loop and conditions
<table><tr><td>
<img width="441" height="1">

```
[= word 'Hi World :D
[o {word}
  [? {letter} = i
      [.. i!
      ]
      [.. {letter}
```
</td><td>
<img width="441" height="1">
  
```json
[
  ["=", "word", "Hi World :D"],
  ["o", "{word}", [
    ["?", "{letter}", "=", "i", [
      ["..", "i!"]
    ], [
      ["..", "{letter}"]
    ]]
  ]]
]
```
</td></tr></table>

##### Get the last result without using variables
<table><tr><td>
<img width="441" height="1">

```
[replace 'Hi World :D' i i!
[. {}
upper
.
```
</td><td>
<img width="441" height="1">
  
```json
[
  ["replace", "Hi World :D", "i", "i!"],
  [".", "{}"],
  "upper",
  "."
]
```
</td></tr></table>

##### Run native code
<table><tr><td>
<img width="441" height="1">

```
[. native python code
[code 'for i in range(10):print(i)
```
</td><td>
<img width="441" height="1">
  
```json
[
  [".", "native", "python", "code"],
  ["code", "for i in range(10):print(i)"]
]
```
</td></tr></table>

##### Import into your project
```python
from path.to.void import VOIDlang as void
encrypted = void.encrypt('Hi World :D')
print(void.decrypt(encrypted['text'], encrypted['key']))
```

## How to Use

1. Download **V O I D lang**
2. Create your first app in **``app.void``**・**``app.json``**・**``app.zip``**
3. Launch app with **V O I D lang**
 
```console
python void.py app.void
python void.py app.json
python void.py app.zip
```

> [!TIP]
> Create an app in **``run.void``**・**``run.json``** ・**``run.zip``** for autorun
> ```
> python void.py
> ```

> [!TIP]
> Type alias in the **``Windows``** command line
> ```console
> doskey void=python /path/to/void.py
> ```
>
> Add alias in **``~/.bashrc``** (Linux)・**``~/.bash_profile``** (macOS)・**``~/.zshrc``** (macOS)
> ```console
> alias void="python /path/to/void.py"
> ```
> ```console
> void app.void
> ```

> [!TIP]
> Compile **``Python``**・**``JavaScript``**・**``Swift``**・**``Kotlin``**・**``C++``** file containing your code into the exacutable
> ```console
> pip install pyinstaller
> pyinstaller --onefile void.py
> ```
> ```console
> npm install -g pkg
> pkg void.js
> ```
> ```console
> swiftc void.swift
> ```
> ```console
> kotlinc void.kt
> ```
> ```console
> clang++ void.cpp -o void.exe
> ```

> [!TIP]
> Convert your **app**・**game** to various platforms
> ```console
> void.exe convert app.void app.exe
> void.exe convert game.void game.exe
> ```

> [!TIP]
> Import **``void.py``**・**``void.js``**・**``void.swift``**・**``void.kt``** into the project to create an app
>
> Import **``void.gd``**・**``void.cpp``** into the **Godot**・**Unreal Engine** project to create a game

## Actions

> [!NOTE]
> Use **Help** to display a description of the action
> 
> ```console
> python void.py help
> python void.py h upper
> ```

> Number of actions **``240``**

| <img width="1000" height="1"><br>**value**<br>&nbsp; | <img width="1000" height="1"><br>**crypto**<br>&nbsp; |
| :--------------------------------------------------- | :---------------------------------------------------- |
| **``get``**<br>Retrieve a value based on provided parameter name | **``encrypt``**<br>Encrypts data using the AES256 algorithm and the specified key |
| **``set``**<br>Assign a value to a specified parameter | **``decrypt``**<br>Decrypts previously encrypted data using the AES256 algorithm and the specified key |
| **``remove``** · **``del``**<br>Remove a specified parameter | **``password``**<br>Hashes a password using the Argon2 algorithm for secure storage |
| **``type``**<br>Determine the data type | **``password.check``**<br>Verifies a password against a Argon2 hashed password |
| **``text``**<br>Specify a data as a text type | **``hash``**<br>Generates a hash for the data or generates a random text |
| **``number``**<br>Specify a data as a number type | **``uuid``**<br>Generates a universally unique identifier |
| **``bool``**<br>Specify a data as a boolean type | **``sha1``**<br>Generates an SHA-1 hash of a text |
| **``binary``**<br>Specify a data as a binary type | **``sha256``**<br>Generates an SHA-256 hash of a text |
| **``length``** · **``n``** · **``len``**<br>Gets the length of the data | **``sha512``**<br>Generates an SHA-512 hash of a text |
| &nbsp;<br>**expression**<br>&nbsp; | **``crc32``**<br>Calculates the CRC32 checksum of a text |
| **``+``** · **``and``**<br>Perform addition or AND operation | **``base64``**<br>Encodes the data into Base64 format |
| **``-``** · **``not``**<br>Perform subtraction or NOT operation | **``base64.decode``**<br>Decodes Base64 encoded data back to its original form |
| **``*``** · **``xor``**<br>Perform multiplication or XOR operation | **``gzip``**<br>Compresses data using the GZip compression algorithm (popular compression) |
| **``/``** · **``or``**<br>Perform division or OR operation | **``gzip.decode``**<br>Decompresses GZip compressed data |
| **``%``**<br>Perform modulo operation | **``lzma``**<br>Compresses data using the LZMA2 compression algorithm (best compression) |
| **``^``**<br>Perform power operator | **``lzma.decode``**<br>Decompresses LZMA2 compressed data |
| **``>>``** · **``shr``**<br>Perform right shift operation | **``lzss``**<br>Compresses data using the LZSS compression algorithm (fastest compression) |
| **``<<``** · **``shl``**<br>Perform left shift operation | **``lzss.decode``**<br>Decompresses LZSS compressed data |
| **``!=``**<br>Checks if values are not equal | **``lz4``**<br>Compresses data using the LZ4 compression algorithm (fastest decompression) |
| **``>``**<br>Checks if left value is greater than right | **``lz4.decode``**<br>Decompresses LZ4 compressed data |
| **``<``**<br>Checks if left value is less than right | **``rsa``**<br>Encrypts data using RSA encryption with a public key |
| **``>=``**<br>Checks if left value is greater than or equal to right | **``rsa.decode``**<br>Decrypts data encrypted with RSA encryption |
| **``<=``**<br>Checks if left value is less than or equal to right | **``ecdhe``**<br>Encrypts data using ECDHE encryption with a disposable key |
| **``#``** · **``in``**<br>Checks if value is in a list, subtext in a text or name in a dictionary | **``ecdhe.decode``**<br>Decrypts data encrypted with ECDHE encryption |
| **``!#``** · **``notin``**<br>Checks if value is not in a list, subtext in a text or name not in a dictionary | **``barcode``** · **``qr``**<br>Encodes text into a barcode image |
| **``@``** · **``is``**<br>Checks if value matches a type or one of types | **``barcode.decode``** · **``qr.decode``**<br>Decodes the barcode image into text |
| **``!@``** · **``isnot``**<br>Checks if value does not match a type or types | &nbsp;<br>**file**<br>&nbsp; |
| **``=``** · **``==``**<br>Assign value or expression to a parameter or checks if values are equal | **``file``** · **``<<<``** · **``>>>``**<br>Read or write data to a file at a specified path |
| **``+=``**<br>Add and assign value to a parameter | **``file.exists``**<br>Checks if a specified file exists at the given path |
| **``=+``**<br>Add to the beginning and assign value to a parameter | **``file.remove``** · **``file.trash``**<br>Removes a specified file |
| **``-=``**<br>Subtract and assign value to a parameter | **``file.copy``**<br>Copies a specified file to a new location |
| **``=-``**<br>Subtract from the beginning and assign value to a parameter | **``file.move``** · **``rename``**<br>Moves a specified file to a new location or renames it |
| **``*=``**<br>Multiply and assign value to a parameter | **``file.link``**<br>Creates a hard link to a specified file or checks if a hard link exists at the given path |
| **``/=``**<br>Divide and assign value to a parameter | **``file.info``**<br>Retrieves information about a specified file |
| **``%=``**<br>Modulo and assign value to a parameter | **``file.sha256``**<br>Computes the SHA256 checksum of a specified file |
| **``^=``**<br>Power and assign value to a parameter | **``file.sha512``**<br>Computes the SHA512 checksum of a specified file |
| **``>>=``**<br>Right shift and assign value to a parameter | **``file.crc32``**<br>Computes the CRC32 checksum of a specified file |
| **``<<=``**<br>Left shift and assign value to a parameter | **``file.base64``**<br>Encodes a specified file to base64 format |
| &nbsp;<br>**control**<br>&nbsp; | **``file.zip``**<br>Compresses a specified file into a ZIP archive |
| **``.``** · **``..``** · **``print``**<br>Output data to the console | **``file.gzip``**<br>Compresses a specified file using GZip compression |
| **``...``** · **``input``**<br>Input text from the user | **``file.void``**<br>Compresses the specified file using LZMA2 compression and places it in a container |
| **``?``** · **``if``**<br>Evaluate a conditional expression | **``file.extract``**<br>Decompresses a compressed files and directories from an archive |
| **``o``** · **``loop``**<br>Perform a loop operation | **``dir``**<br>Lists the contents of a specified directory |
| **``x``** · **``break``**<br>Exit the current loop or action | **``dir.create``**<br>Creates a new directory at a specified path |
| **``->``** · **``continue``**<br>Skip to the next iteration of the loop | **``dir.exists``**<br>Checks if a specified directory exists |
| **``<-``** · **``repeat``**<br>Repeat the current iteration of the loop | **``dir.remove``** · **``dir.trash``**<br>Removes a specified directory and its contents |
| **``_``** · **``__``** · **``return``** · **``response``**<br>Return a result from an action | **``dir.copy``**<br>Copies a specified directory and its contents to a new location |
| **``action``**<br>Call or initiate an action | **``dir.move``** · **``dir.rename``**<br>Moves a specified directory to a new location |
| **``open``**<br>Open a link in standard way or execute shell command or get a list of open applications | **``dir.clear``**<br>Clears all contents of a specified directory without removing the directory itself |
| **``close``**<br>Close an application by name or PID | **``dir.info``**<br>Retrieves information about a specified directory |
| **``code``**<br>Execute a block of native code | **``dir.zip``**<br>Compresses a specified directory into a ZIP archive |
| **``l``** · **``d``** · **``w``** · **``e``** · **``debug``** · **``warning``** · **``error``**<br>Log debug information | **``dir.void``**<br>Compresses a specified directory into a void container |
| **``test``**<br>Test one, group or all actions | **``drive``**<br>Lists all available drives on the system or retrives information about a volume or partition |
| **``update``**<br>Update all code or only the specified action | **``drive.mount``**<br>Mounts a volume to make it accessible |
| **``exit``** · **``xx``**<br>Exit the current application with an exit code | **``drive.unmount``**<br>Unmounts a volume |
| **``os``**<br>Running the operating system shell | **``drive.create``**<br>Creates a new volume or partition |
| **``info``** · **``i``** · **``help``** · **``h``**<br>Get info about V O I D lang, os, device, file, directory, drive, url, text, image, video, sound, model, thesaurus or other data | **``drive.resize``**<br>Resizes an existing volume or partition |
| **``convert``** · **``c``** · **``<>``**<br>Convert data from one format to another | **``drive.clear``**<br>Clears a specified volume or partition |
| **``clipboard``**<br>Storing or retrieving clipboard temporary data | **``drive.remove``**<br>Removes a specified volume or partition |
| **``sql``**<br>Execute an SQL query | **``path``**<br>Returns components of a specified path |
| **``chat``** · **``:``**<br>AI conversation and interaction through text | &nbsp;<br>**format**<br>&nbsp; |
| **``say``**<br>Text voicing with different voices | **``void``**<br>Encodes data into the V O I D format |
| **``recognize``**<br>Convert voice, image or video to text | **``void.decode``**<br>Decodes data from the V O I D format |
| **``ui``** · **``app``** · **``game``** · **``web``** · **``cli``**<br>Create a user interface | **``json``**<br>Encodes data into the JSON format |
| &nbsp;<br>**text**<br>&nbsp; | **``json.decode``**<br>Decodes data from the JSON format |
| **``lower``**<br>Convert text to lowercase | **``csv``**<br>Encodes data into the CSV format |
| **``upper``**<br>Convert text to uppercase | **``csv.decode``**<br>Decodes data from the CSV format |
| **``starts``**<br>Check if text starts with a specific substring | **``yaml``**<br>Encodes data into the YAML format |
| **``ends``**<br>Check if text ends with a specific substring | **``yaml.decode``**<br>Decodes data from the YAML format |
| **``strip``**<br>Remove leading and trailing characters from text | **``ini``**<br>Encodes data into the INI format |
| **``strip.start``**<br>Remove leading characters from text | **``ini.decode``**<br>Decodes data from the INI format |
| **``strip.end``**<br>Remove trailing characters from text | **``xml``**<br>Encodes data into the XML format |
| **``replace``**<br>Replace occurrences of a substring within text | **``xml.decode``**<br>Decodes data from the XML format |
| **``find``**<br>Locate a substring within text | &nbsp;<br>**cloud**<br>&nbsp; |
| **``parse``**<br>Parse text into structured data | **``cloud``**<br>Runs cloud services for data management |
| **``part``**<br>Extract a part of the text or list | **``request``** · **``r``**<br>Sends an HTTP request to a specified URL |
| **``split``**<br>Split text into parts based on a delimiter or list based on a length | **``download``** · **``d``**<br>Downloads content from a specified URL |
| **``join``**<br>Join a list of text into a single text with a delimiter | **``cookie``**<br>Receives or sets a specified cookie |
| **``escape``** · **``s``**<br>Escape special characters in a text | **``social``**<br>Interacting with social API |
| **``unescape``** · **``u``**<br>Unescape special characters in a text | **``notify``**<br>Send notification |
| **``translate``**<br>Translate text from one language to another | &nbsp;<br>**device**<br>&nbsp; |
| **``check``**<br>Spell check in different languages | **``device``**<br>Retrieves or sets hardware device parameters |
| &nbsp;<br>**list**<br>&nbsp; | **``cpu``**<br>Current CPU usage |
| **``push``**<br>Add an element to the list | **``gpu``**<br>Current GPU usage |
| **``pop``**<br>Remove and return an element from the list | **``memory``**<br>Current memory usage |
| **``reverse``**<br>Reverse the order of elements in a list | **``battery``**<br>Remaining battery charge |
| **``unique``**<br>Leave only unique values in a list | **``fps``**<br>Retrieves or sets frames per second for video or graphical rendering |
| **``map``**<br>Apply an action to each element in a list | **``vsync``**<br>Vertical sync settings to prevent screen tearing |
| **``reduce``**<br>Apply an action cumulatively to the elements in a list | **``resolution``**<br>Retrieves or stes the screen resolution |
| **``filter``**<br>Apply a filter action to each element in a list | **``orientation``**<br>Retrieves or stes the orientation of a device's display |
| **``names``** · **``indexes``** · **``keys``**<br>Retrieve all indexes from a list or attribute names from a dictionary | **``dark``**<br>Retrieves or stes the dark mode setting for user interfaces |
| **``values``**<br>Retrieve all values from a dictionary | **``pixel``**<br>Retrieves or sets the color of the pixel displayed on the screen |
| &nbsp;<br>**math**<br>&nbsp; | **``symbol``**<br>Retrieves or sets the symbol on the screen in text mode |
| **``sin``**<br>Sine of the value | **``cursor``**<br>Retrieves or sets the cursor position on the screen and its visibility in text mode |
| **``cos``**<br>Cosine of the value | **``clear``**<br>Clears the screen in text mode |
| **``tan``**<br>Tangent of the value | **``flashlight``**<br>Turns on or off the device's flashlight |
| **``sinh``**<br>Hyperbolic sine of the value | **``location``**<br>Retrieves the current geographic location using GPS or network triangulation |
| **``cosh``**<br>Hyperbolic cosine of the value | **``gyroscope``**<br>Provides access to the gyroscope sensor for motion detection |
| **``tanh``**<br>Hyperbolic tangent of the value | **``accelerometer``**<br>Provides access to the accelerometer sensor to detect acceleration forces |
| **``asin``**<br>Arc sine of the value | **``compass``**<br>Accesses the magnetic compass sensor to determine orientation relative to the Earth's magnetic field |
| **``acos``**<br>Arc cosine of the value | **``proximity``**<br>Detects the proximity of objects in relation to the device's proximity sensor |
| **``atan``**<br>Arc tangent of the value | **``brightness``**<br>Manages the screen brightness level of the device |
| **``asinh``**<br>Arc hyperbolic sine of the value | **``volume``**<br>Manages the sound level of the device |
| **``acosh``**<br>Arc hyperbolic cosine of the value | **``calendar``**<br>Calendar events on a device |
| **``atanh``**<br>Arc hyperbolic tangent of the value | **``gallery``**<br>Photo and video library on a device |
| **``round``**<br>Rounds a number to the nearest integer or to the specified number of decimal places | **``contacts``**<br>Contact list on a device |
| **``floor``**<br>Largest integer less than or equal to a number | **``call``**<br>Initiate a voice or video call to a specified recipient |
| **``ceil``**<br>Smallest integer greater than or equal to a number | **``sms``**<br>Send a text message (SMS) to a specified recipient |
| **``log``**<br>Logarithm of a number (natural by default) | **``net``**<br>Retrieves information about Network or connect |
| **``fact``**<br>Factorial of a given non-negative number | **``wifi``**<br>Retrieves information about Wi-Fi or connect |
| **``fib``**<br>Fibonacci numbers up to a specified index | **``bluetooth``**<br>Retrieves information about Bluetooth or connect |
| **``gold``** · **``g``**<br>Golden ratio of a number | **``cellular``**<br>Retrieves information about Cellular or connect |
| **``abs``**<br>Absolute value of a number | **``stream``**<br>Retrieves information about screen streaming or start streaming |
| **``min``**<br>Smallest of a list of numbers | **``keyboard``**<br>Keyboard information |
| **``max``**<br>Largest of a list of numbers | **``mouse``**<br>Mouse information |
| **``sum``**<br>Sum of a list of numbers | **``gamepad``**<br>Gamepad information |
| **``avg``**<br>Average value of a list of numbers | **``tap``**<br>Simulates a tap gesture |
| **``random``**<br>Generates a pseudo-random number | **``key``**<br>Key binding |
| **``random.seed``**<br>Receives, sets or refreshes the seed for the random number generator to produce reproducible results | &nbsp;<br>**content**<br>&nbsp; |
| &nbsp;<br>**time**<br>&nbsp; | **``image``**<br>Create an image |
| **``time``**<br>Provides current time since the epoch or calculates time passed since a given start time | **``video``** · **``movie``** · **``clip``** · **``anime``**<br>Create a video |
| **``timer``**<br>Creates a timer that can be used to trigger events at specific intervals | **``sound``** · **``music``**<br>Create an audio track |
| **``timer.remove``**<br>Removes previously created timer | **``model``**<br>Create a 3D model |
| **``wait``**<br>Pauses execution for a specified number of seconds | **``book``** · **``document``** · **``spreadsheet``** · **``presentation``** · **``comics``** · **``manga``**<br>Create a book, comic or manga |
| **``stopwatch``** · **``t``**<br>Stopwatch for calculating the time spent on operations | **``game``** · **``2d``** · **``3d``** · **``vn``**<br>Create a 2D, 3D or visual novel game |
| **``date``**<br>Format or parse date-related information | &nbsp; |

## V O I D format
This is a data format that inherits the best features of [**JSON**](https://en.wikipedia.org/wiki/JSON), [**YAML**](https://en.wikipedia.org/wiki/YAML), [**CSV**](https://en.wikipedia.org/wiki/Comma-separated_values) and [**plain text**](https://en.wikipedia.org/wiki/Plain_text) formats. Makes it easier to write and read data, both by human and by program. The format simplifies data creation by removing the use of unnecessary quotation marks, brackets, colons, commas and other symbols. It is possible to combine **text** and **binary** data.

<table>
<tr>
<th align="center"><img width="441" height="1"><p>V O I D format</p></th>
<th align="center"><img width="441" height="1"><p>JSON</p></th>
</tr>

<tr>
<td>

```
V O I D format
  extension
    regular
      .void
    retro file system
      .v
  mime type
    application/void
  influenced by
    json
    yaml
    csv
    ini
    python
    assembly
    text
  purpose
    data
    code
    settings
    text
    image
    video
    sound
    3d
    subtitles
    font
    other
  released
    2026
  symbol
    indent
      tab
        '\t
    newline
      line feed
        '\n
    quotation
      single
        '
    separator
      space
        ' '
    bracket
      square
        '[]
  value type
    text
      text with space
      'text with space
      'text with space'
      '
      ''
      '''
      '
        text
        in a
        line
      "
        text
        multi
        line
      'tab \t
      'line feed \n
      'quotation end ''
      'quotation ' middle
      'backslash \\t \\n \\
      backslash \t \n \
    number
      1
      100
      -100
      100 000
      100_000
      100 000.000 000 001
    bool
      true
      false
    none
      none
    list
      column
        value 1
        value 2
        value 3
      table
        name 1    value 1    1
        name 10   value 10   10
        name 100  value 100  100
      line
        full
          [1 2 3]
        short
          [1 2 3
      snake
        [1 2 3
          text 1
          text 2
          ]
          text 1
          text 2
          ] 4 5
      empty
        full
          []
        short
          [
    dictionary
      column
        name 1
          value 1
        name 2
          value 2
        name 3
          value 3
      table
        name 1    value 1
        name 10   value 10
        name 100  value 100
      line
        full
          ['name1' 'value1'  'name 2' 'value 2']
        short
          [name1 value1  'name 2' value 2
        one
          [name  value
      snake
        [1 2 3
          name 1
            value 1
          name 2
            value 2
          ]
          name 1
            value 1
          name 2
            value 2
          ] 4 5
      empty
        [ ]
    binary
      raw
        *4*data
      hex
        line
          *5620 4F20 4920 4420 666F 726D 6174
        multiline
          *
            5620 4F20
            4920 4420
            666F 726D
            6174 AABB
      bin
        line
          **00000111 11100111
        multiline
          **
            0000 0111
            1110 0111
      base64
        regular
          line
            ***ViBPIEkgRCBmb3JtYXQ=
          multiline
            ***
              ViBPIEk
              gRCBmb3
              JtYXQ=
          short
            *ViBPIEkgRCBmb3JtYXQ=
        safe
          line
            ***eNoLU_BX8FRwUUjLL8pNLAEAG0QEPA
          multiline
            ***
              eNoLU_BX8FR
              wUUjLL8pNLA
              EAG0QEPA
          short
            *eNoLU_BX8FRwUUjLL8pNLAEAG0QEPA
        gzip
          line
            ***eNoLU/BX8FRwUUjLL8pNLAEAG0QEPA==
          multiline
            ***
              eNoLU/BX8FR
              wUUjLL8pNLA
              EAG0QEPA==
          short
            *eNoLU/BX8FRwUUjLL8pNLAEAG0QEPA==
        lzma
          line
            ***/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM…
          multiline
            ***
              /Td6WFoAAATm1rRGAgAhARwAAAAQz1jM
              AQANViBPIEkgRCBmb3JtYXQAAADXR9DD
              lMsFngABJg4IG+AEH7bzfQEAAAAABFla
          short
            */Td6WFoAAATm1rRGAgAhARwAAAAQz1jM…
  comment
   .: C O M M E N T :.
    begins with a single space
```

</td>
<td>

```json
{
  "V O I D format": {
    "extension": {
      "regular": ".void",
      "retro file system": ".v"
    },
    "mime type": "application/void",
    "influenced by": [
      "json",
      "yaml",
      "csv",
      "ini",
      "python",
      "assembly",
      "text"
    ],
    "purpose": [
      "data",
      "code",
      "settings",
      "text",
      "image",
      "video",
      "sound",
      "3d",
      "subtitles",
      "font",
      "other"
    ],
    "released": 2026,
    "symbol": {
      "indent": {
        "tab": "\t"
      },
      "newline": {
        "line feed": "\n"
      },
      "quotation": {
        "single": "'"
      },
      "separator": {
        "space": " "
      },
      "bracket": {
        "square": "[]"
      }
    },
    "value type": {
      "text": [
        "text with space",
        "text with space",
        "text with space",
        "'",
        "",
        "'",
        "textin aline",
        "text\nmulti\nline",
        "tab \t",
        "line feed \n",
        "quotation end '",
        "quotation ' middle",
        "backslash \\t \\n \\",
        "backslash \\t \\n \\"
      ],
      "number": [
        1,
        100,
        -100,
        100000,
        100000,
        100000.000000001
      ],
      "bool": [
        true,
        false
      ],
      "none": null,
      "list": {
        "column": [
          "value 1",
          "value 2",
          "value 3"
        ],
        "table": [
          ["name 1", "value 1", 1],
          ["name 10", "value 10", 10],
          ["name 100", "value 100", 100]
        ],
        "line": {
          "full": [1, 2, 3],
          "short": [1,2,3]
        },
        "snake": [1, 2, 3, [
          "text 1",
          "text 2"
        ], [
          "text 1",
          "text 2"
        ], 4, 5],
        "empty": {
          "full": [],
          "short": []
        }
      },
      "dictionary": {
        "column": {
          "name 1": "value 1",
          "name 2": "value 2",
          "name 3": "value 3"
        },
        "table": {
          "name 1": "value 1",
          "name 10": "value 10",
          "name 100": "value 100"
        },
        "line": {
          "full": {"name1": "value1", "name 2": "value 2"},
          "short": {"name1": "value1", "name 2": "value 2"},
          "one": {"name": "value"}
        },
        "snake": [1, 2, 3, {
          "name 1": "value 1",
          "name 2": "value 2"
        }, {
          "name 1": "value 1",
          "name 2": "value 2"
        }, 4, 5],
        "empty": {}
      },
      "binary": "impossible"
    },
    "comment": "impossible or JSONC"
  }
}







































































```

</td>
</tr>

</table>

> [!TIP]
> Use **V O I D format [highlighting](https://github.com/voidspawner/void.storage/blob/main/settings/void.sublime-syntax)** 🔆 for **[Sublime Text](https://sublimetext.com)**.
>
> **``Tools``** → **``Developer``** → **``New Syntax…``** → **``Copy``** · **``Paste``** → Save as **``void.sublime-syntax``**
>
> You can change the **[color scheme](https://github.com/voidspawner/void.storage/blob/main/settings/void.sublime-color-scheme)** 🎨 to alternate sections.
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
This is a database that uses **``V O I D``** · **``JSON``** · **``YAML``** ·  **``CSV``** files for storage directly. Data is **cached**, **indexed** and **saved** automatically. **Easy access** to data without the need to create complex constructs.

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
> [. {data.json/name.subname}
> [. {data.json/list.1.value}
> [= data.json/list.1.value 3
> [= data.json/list.index.2.value 3
> ```
> 
> ```
> [. {https://voidsp.com/name/file.json/path/to/data.value}
> [= {https://voidsp.com/name/file.json/path/to/data.value} text
>```

> **``data.csv``**
> ```csv
> index,text,value
> 1,text 1,value 1
> 5,text 5,value 5
> ```
>
> ```
> [. {data.csv/1.2}
> [. {data.csv/1.value}
> [. {data.csv/index.5.value}
> [= data.csv/index.5.value 3
>```

## V O I D ai
This is an AI that makes working with data easier and improves communication.

> **``Characters``**
> ```
> chat.muryashka
> chat.murya
> [chat.character.kitty a cat who loves to play games often says "meow"
> chat.kitty
> [chat.kitty Hello Kitty
> ```
>
> **``ChatGPT``**
> ```
> chat.gpt
> chat.gpt.pro
> chat.pro
> [chat radius of the Earth
> [chat.gpt radius of the Earth
> [chat.pro radius of the Earth
> [: tell me a story
> [: translate to portuguese: Hi World :D
> [: svg ginger cat in a box
> [: python calculator application
> [: image dancing cats
> ```
>
> **``DeepSeek``**
> ```
> chat.deepseek
> chat.reasoner
> chat.v3
> chat.r1
> [chat radius of the Earth
> [chat.deepseek radius of the Earth
> ```
> 
> **``Ollama``**
> ```
> chat.ollama
> [chat radius of the Earth
> [chat.ollama radius of the Earth
> ```
>
> **``Gemini``**
> ```
> chat.gemini
> [chat radius of the Earth
> [chat.gemini radius of the Earth
> ```
>
> **``Claude``**
> ```
> chat.claude
> chat.claude.opus
> chat.claude.sonnet
> chat.claude.haiku
> chat.opus
> chat.sonnet
> chat.haiku
> [chat radius of the Earth
> [chat.claude radius of the Earth
> ```
>
> **``Media``**
> ```
> image.stablediffusion
> image.sd
> image.openai
> image.google
> image.nanobanana
> image.flux
> video.kling
> video.seedance
> music.minimax
> [image playing cats on the lawn
> [image.sd playing cats on the lawn
> [image.openai playing cats on the lawn
> [image.google playing cats on the lawn
> [image 'playing cats on the lawn' cats.jpg
> [image 'remove the cat in the center' cats.jpg cats-edited.jpg
> [image 'remove background' cats.jpg cats-without-background.png
> [image.bg cats.jpg cats-without-background.png
> [image 'grayscale image' cats.jpg cats-grayscaled.jpg
> [image.grayscale cats.jpg cats-grayscaled.jpg
> [image 'colorize image' cats-grayscaled.jpg cats-colorized.jpg
> [image.colorize cats-grayscaled.jpg cats-colorized.jpg
> [image 'make cyberpunk restyle' cats.jpg cats-cyberpunk.jpg
> [image.style.cyberpunk cats.jpg cats-cyberpunk.jpg
> [image.style.anime cats.jpg cats-cyberpunk.jpg
> [image.2x cats.jpg cats-resize-2x.jpg
> [image.4x cats.jpg cats-resize-4x.jpg
> [image swapface adult.jpg child.jpg adult-to-child.jpg
> [image.face adult.jpg child.jpg adult-to-child.jpg
> [video 'playing cats on the lawn' cats.mp4
> ```
> 
> **``Text to Speech``**
> ```
> voice.google
> voice.google.en-US-Wavenet-B
> voice.en-US-Wavenet-B
> [say Hi World :D
> ```
> 
> **``Voice Cloning``**
> ```
> [voice thomas.mp3
> [voice thomas.mp4
> [say Hi World :D
> ```
> 
> **``Speech Recognition``**
> ```
> [recognize
> [recognize talk.mp3
> [recognize.speech video.mp4
> [recognize.voice video.mp4
> [recognize.sound video.mp4
> ```
> 
> **``Image and Video Recognition``**
> ```
> [recognize image.jpg
> [recognize video.mp4
> ```
> 
> **``Translate``**
> ```
> translate.google
> translate.chatgpt
> translate.deepseek
> [translate 你好，世界 :D
> [translate.pt 你好，世界 :D
> [translate.zh.pt 你好，世界 :D
> [<> 你好，世界 :D
> ```

## V O I D game
This is a game that creates an **infinite** number of games, apps and content.

## V O I D social
This is a social network that lets you communicate safely through an **AI character** and create games, apps, and content.

## V O I D os
This is an Operating System that uses **V O I D lang** to run and create games, apps and content.

## V O I D tech
These are modular devices controlled by **[V O I D os](#v-o-i-d-os)** · **[V O I D ai](#v-o-i-d-ai)** for creating **individual** stand-alone productions, as well as creating individual products with **unique designs** and in the required quantities.

## V O I D ideology
This is an ideology of creating compact production systems to meet individual everyday needs.

## V O I D license
This is a license to distribute digital content and goods, expressed in a single sentence:

> **DO WHAT YOU WANT**

You can use it in both **private** and **open source**. Embed it in **free** or **paid** products. **Modify**. Create your **own solutions** based on it. **No need to specify the author**.

## V O I D task
This is a paid assignment for implementing **V O I D** technologies.
> [!IMPORTANT]
> By adding your code to the repository, you are publishing it under the **V O I D licence**.
