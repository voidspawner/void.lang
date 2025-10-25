# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **[V O I D](#v-o-i-d-format)** or **[JSON](https://en.wikipedia.org/wiki/JSON)** format. It is used as a replacement for the standard **``Bash``**・**``CMD``**・etc. languages and for writing **``applications``**, **``servers``** and **``games``**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one ``V O I D`` or ``JSON`` file**. Since the **code is presented as data**, applications can be easily generated with **``AI``**, updated, installed and launched remotely.

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
| [**Swift**](https://www.swift.org/download)              | <p align="center">LLVM</p>             | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> |
| [**Kotlin**](https://developer.android.com/studio)       | <p align="center">JVM</p>             | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">-</p> | <p align="center">+</p> |
| [**GDScript**](https://godotengine.org/download/windows) | <p align="center">Godot</p>         | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> |
| [**C++**](https://www.unrealengine.com/download)         | <p align="center">Unreal Engine</p> | <p align="center">-</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> | <p align="center">+</p> |

## Example
##### Even simpler
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
    . {text.hi} :D
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
  "run": ". {text.hi} :D",
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
cloud <h1>Hi World 😄</h1>
```
</td><td>
<img width="441" height="1">
  
```json
"cloud <h1>Hi World 😄</h1>"
```
</td></tr></table>

##### File sharing
<table><tr><td>
<img width="441" height="1">

```
cloud /path/to/share
```
</td><td>
<img width="441" height="1">
  
```json
"cloud /path/to/share"
```
</td></tr></table>

##### Add comments
<table><tr><td>
<img width="441" height="1">

```
comment
  Comment as a property
run
  [
 Comment begins with space
    [. Hi World :D
        Comment with double indent
```
</td><td>
<img width="441" height="1">
  
```json
{
  "comment": "Comment as a property",
  "run": [
    [".", "Hi", "World", ":D"]
  ]
}
```
</td></tr></table>

##### Loop and conditions
<table><tr><td>
<img width="441" height="1">

```
[
  [= word 'Hi World :D
  [o letter {word}
    [? [{letter} = i
      [.. i!

      [.. {letter}
```
</td><td>
<img width="441" height="1">
  
```json
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
</td></tr></table>

##### Get the last result without using variables
<table><tr><td>
<img width="441" height="1">

```
[
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
[[code 'for i in range(10):print(i)
```
</td><td>
<img width="441" height="1">
  
```json
[
  ["code", "for i in range(10):print(i)"]
]
```
</td></tr></table>

##### Import into your project
```python
exec(open('void.py').read())
encrypted = void.encrypt('Hi World :D')
print(void.decrypt(encrypted['text'], encrypted['key']))
```

## How to Use

1. Download **V O I D lang**
2. Create your first app in **``run.void``** · **``run.json``** or other JSON file
3. Launch app with **V O I D lang**
 
```console
python void.py app.void
python void.py app.json
```

**Alternative**

```console
python void.py app.py
```
```console
python void.py . Hi World :D
```
```console
python void.py cloud.file /path/to/share
```

> [!TIP]
> **``Linux``・``macOS``**: Add alias to **``~/.bashrc``** ・ **``~/.zshrc``** ・ **``~/.bash_profile``** (macOS)
> ```console
> alias void="python /path/to/void.py"
> ```
> 
> **``Windows``**: Use alias in command line
> ```console
> doskey void=python /path/to/void.py
> ```
> ```console
> void app.json
> ```
> 
> **``Swift``・``Kotlin``・``C++``**: Embed the **V O I D app (vapp)** in the source code and compile it into an executable
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

1. Download **V O I D spawner** game
2. Create your first game in **``run.void``** · **``run.json``** file
3. Copy the **``void.exe``** file to the same directory as **``run.void``** · **``run.json``** file
4. Sell your game or share with friends

> [!NOTE]
> Run with game engine
> ```console
> void.exe game.void
> void.exe game.json
> ```
>
> The archive contains **``run.void``** · **``run.json``** and all game files
> ```console
> void.exe game.zip
> ```
>
> The execution directory contains **``run.void``** · **``run.json``** · **``run.zip``** file
> ```console
> void.exe
> ```
>
> You can **export** your game to various platforms
> ```console
> void.exe convert game.void game.exe
> ```

**Alternative**

1. Download **V O I D lang**
2. Import **``void.gd``**・**``void.cpp``** into the **Godot**・**Unreal Engine**
3. Create your first game in **``run.void``** · **``run.json``** file
4. Export the game in the engine itself to the available platforms
5. Sell your game or share with friends

## Actions

> [!NOTE]
> Use **Help** to display a description of the action
> 
> ```console
> python void.py help
> python void.py h upper
> ```

> Number of actions **``269``**

| <img width="1000" height="1"><br>**value**<br>&nbsp; | <img width="1000" height="1"><br>**crypto**<br>&nbsp; |
| :--- | :--- |
| **``get``**<br>Retrieve a value based on provided parameter name | **``encrypt``**<br>Encrypts data using a specified key |
| **``set``**<br>Assign a value to a specified parameter | **``decrypt``**<br>Decrypts previously encrypted data using the specified key |
| **``remove``**<br>Remove a specified parameter or value | **``hash``**<br>Generates a hash for the data or generates a random text |
| **``type``**<br>Determine the data type of a specified parameter | **``uuid``**<br>Generates a universally unique identifier |
| **``text``**<br>Specify a parameter as a text type | **``md5``**<br>Generates an MD5 hash of a text |
| **``number``**<br>Specify a parameter as a number type | **``sha1``**<br>Generates an SHA-1 hash of a text |
| **``bool``**<br>Specify a parameter as a boolean type | **``sha256``**<br>Generates an SHA-256 hash of a text |
| **``list``**<br>Specify a parameter as a list type | **``sha512``**<br>Generates an SHA-512 hash of a text |
| **``binary``**<br>Specify a parameter as a binary type | **``crc32``**<br>Calculates the CRC32 checksum of a text |
| **``l``** · **``length``**<br>Gets the length of the text, the number of items in a list or dictionary, the count of bytes in a number | **``base64``**<br>Encodes the data into Base64 format |
| &nbsp;<br>**expression**<br>&nbsp; | **``base64.decode``**<br>Decodes Base64 encoded data back to its original form |
| **``+``**<br>Perform addition operation | **``base85``**<br>Encodes the data into Base85 format |
| **``-``**<br>Perform subtraction operation | **``base85.decode``**<br>Decodes Base85 encoded data back to its original form |
| **``*``**<br>Perform multiplication operation | **``gzip``**<br>Compresses data using the GZip compression algorithm |
| **``/``**<br>Perform division operation | **``gzip.decode``**<br>Decompresses GZip compressed data |
| **``%``**<br>Perform modulo operation | **``rsa``**<br>Encrypts data using RSA encryption with a public key |
| **``^``**<br>Elevation operator | **``rsa.decode``**<br>Decrypts data encrypted with RSA using the corresponding private key |
| **``not``**<br>Perform negation | **``ssl``**<br>Performs SSL encryption on data to secure communication |
| **``and``**<br>Perform AND operation | **``ssl.decode``**<br>Decrypts data encrypted with SSL for secure data transfer |
| **``or``**<br>Perform OR operation | **``bcrypt``**<br>Hashes a password using the bcrypt algorithm for secure storage |
| **``xor``**<br>Perform XOR operation | **``bcrypt.check``**<br>Verifies a password against a bcrypt hashed password |
| **``shr``**<br>Perform right shift operation | &nbsp;<br>**file**<br>&nbsp; |
| **``shl``**<br>Perform left shift operation | **``file``**<br>Read or write data to a file at a specified path |
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
| **``shr=``**<br>Right shift and assign value to a variable | **``file.sha256``**<br>Computes the SHA256 checksum of a specified file |
| **``shl=``**<br>Left shift and assign value to a variable | **``file.sha512``**<br>Computes the SHA512 checksum of a specified file |
| **``==``**<br>Checks if left value is equal to right | **``file.crc32``**<br>Computes the CRC32 checksum for a specified file |
| **``!=``**<br>Check if values are not equal | **``file.base64``**<br>Encodes a specified file to base64 format |
| **``>``**<br>Checks if left value is greater than right | **``file.zip``**<br>Compresses a specified file into a ZIP archive |
| **``<``**<br>Checks if left value is less than right | **``file.zip.list``**<br>Lists the files contained within a ZIP archive |
| **``>=``**<br>Checks if left value is greater than or equal to right | **``file.zip.exists``**<br>Checks if a specific file exists within a ZIP archive |
| **``<=``**<br>Checks if left value is less than or equal to right | **``file.zip.read``**<br>Reads a specific file from within a ZIP archive |
| **``in``**<br>Checks if value is in a list or subtext in a text or name in a dictionary | **``file.zip.remove``**<br>Removes a specific file from a ZIP archive |
| **``notin``**<br>Checks if value is not in a list or subtext in a text or or name not in a dictionary | **``file.unzip``**<br>Extracts files from a ZIP archive into a specified directory |
| **``is``**<br>Checks if value is in a list or name in a dictionary | **``file.gzip``**<br>Compresses a specified file using GZip compression |
| **``isnot``**<br>Checks if value is not in a list or name not in a dictionary | **``file.ungzip``**<br>Decompresses a GZip-compressed file |
| &nbsp;<br>**control**<br>&nbsp; | **``file.void``**<br>Compresses the specified file using GZip compression and places it in a Void container |
| **``.``** · **``print``**<br>Output data to the console | **``file.unvoid``**<br>Decompresses a GZip-compressed files and directories from a Void container |
| **``..``** · **``printn``**<br>Output data to the console without newline | **``dir``**<br>Lists the contents of a specified directory |
| **``...``** · **``input``**<br>Input text from the user | **``dir.create``**<br>Creates a new directory at a specified path |
| **``?``** · **``if``**<br>Evaluate a conditional expression | **``dir.exists``**<br>Checks if a specified directory exists |
| **``o``** · **``loop``**<br>Perform a loop operation | **``dir.remove``**<br>Removes a specified directory and its contents |
| **``x``** · **``break``**<br>Exit the current loop | **``dir.move``**<br>Moves a specified directory to a new location |
| **``>>``** · **``continue``**<br>Skip to the next iteration of the loop | **``dir.copy``**<br>Copies a specified directory and its contents to a new location |
| **``<<``** · **``repeat``**<br>Repeat the current iteration of the loop | **``dir.rename``**<br>Renames a specified directory |
| **``X``** · **``return``** · **``response``**<br>Return a result from an action | **``dir.clear``**<br>Clears all contents of a specified directory without deleting the directory itself |
| **``action``**<br>Initiate or call an action | **``dir.info``**<br>Retrieves information about a specified directory |
| **``open``**<br>Open a link in standard way | **``dir.size``**<br>Calculates the total size of a specified directory and its contents |
| **``code``**<br>Execute a block of native code | **``dir.permission``**<br>Gets or sets the permissions of a specified directory |
| **``i``** · **``info``**<br>Log data | **``dir.time``**<br>Gets or sets the timestamps of a specified directory |
| **``c``** · **``convert``**<br>Convert data from one format to another | **``dir.zip``**<br>Compresses a specified directory into a ZIP archive |
| **``clipboard``**<br>Storing or retrieving clipboard temporary data | **``dir.void``**<br>Compresses a specified directory into a Void container |
| **``sql``**<br>Execute SQL query | **``drive``**<br>Lists all available drives on the system |
| **``test``**<br>Test one or all actions | **``drive.name``**<br>Gets or sets the name of a specified drive |
| **``h``** · **``help``**<br>Show description and use of the action | **``drive.size``**<br>Total size of a specified drive |
| **``xx``** · **``exit``**<br>Exit the current application | **``drive.used``**<br>Amount of used space on a specified drive |
| **``chat``**<br>AI conversation and interaction through text | **``drive.free``**<br>Amount of free space on a specified drive |
| **``say``**<br>Text voicing with different voices | **``drive.info``**<br>Retrieves information about a specified drive |
| **``voice``**<br>List of available voices | **``drive.mount``**<br>Mounts a drive to make it accessible |
| **``recognize``**<br>Convert voice to text | **``drive.unmount``**<br>Unmounts a drive |
| **``capture``**<br>Records or analyzes motion data in real-time | **``drive.create``**<br>Creates a new virtual drive or volume |
| **``ui``** · **``app``** · **``game``** · **``web``** · **``cli``**<br>Create a user interface | **``drive.resize``**<br>Resizes an existing drive partition or volume |
| &nbsp;<br>**text**<br>&nbsp; | **``drive.format``**<br>Formats a drive with a specified file system |
| **``lower``**<br>Convert text to lowercase | **``drive.remove``**<br>Removes or deletes a specified drive or partition |
| **``upper``**<br>Convert text to uppercase | **``path``**<br>Returns components of a specified file path |
| **``starts``**<br>Check if text starts with a specific substring | **``path.drive``**<br>Drive component of a specified file path |
| **``ends``**<br>Check if text ends with a specific substring | **``path.dir``**<br>Directory portion of a specified file path |
| **``strip``**<br>Remove leading and trailing spaces from text | **``path.file``**<br>File portion of a specified file path |
| **``strip.start``**<br>Remove leading spaces from text | **``path.name``**<br>Name of the file without extension from a specified path |
| **``strip.end``**<br>Remove trailing spaces from text | **``path.extension``**<br>File extension from a specified file path |
| **``replace``**<br>Replace occurrences of a substring within text | **``path.strip``**<br>Removes the extension from a specified path |
| **``find``**<br>Locate a substring within text | &nbsp;<br>**format**<br>&nbsp; |
| **``parse``**<br>Parse text into structured data | **``void``**<br>Encodes data into the Void format |
| **``part``**<br>Extract a part of the text or list | **``void.decode``**<br>Decodes data from the Void format |
| **``split``**<br>Split text into parts based on a delimiter | **``json``**<br>Encodes data into the JSON format |
| **``join``**<br>Join a list of strings into a single string with a delimiter | **``json.decode``**<br>Decodes data from the JSON format |
| **``date``**<br>Format or parse date-related information | **``csv``**<br>Encodes data into the CSV format |
| **``e``** · **``escape``**<br>Escape special characters in a text | **``csv.decode``**<br>Decodes data from the CSV format |
| **``unescape``**<br>Unescape special characters in a text | **``yaml``**<br>Encodes data into the YAML format |
| **``words``**<br>Count the number of words | **``yaml.decode``**<br>Decodes data from the YAML format |
| **``sentences``**<br>Count the number of sentences | **``ini``**<br>Encodes data into the INI format |
| **``lines``**<br>Count the number of lines | **``ini.decode``**<br>Decodes data from the INI format |
| **``translate``**<br>Converts text from one language to another | **``xml``**<br>Encodes data into the XML format |
| **``spellcheck``**<br>Spell check in different languages | **``xml.decode``**<br>Decodes data from the XML format |
| &nbsp;<br>**list**<br>&nbsp; | &nbsp;<br>**communication**<br>&nbsp; |
| **``push``**<br>Add an element to the end of a list | **``cloud``**<br>Runs cloud storage or services for data management |
| **``pop``**<br>Remove and return an element from the end of a list | **``r``** · **``request``**<br>Sends an HTTP (GET by default) request to a specified URL |
| **``merge``**<br>Combine multiple lists into one | **``d``** · **``download``**<br>Downloads content from a specified URL |
| **``reverse``**<br>Reverse the order of elements in a list | **``cookie``**<br>Gets or sets a specified cookie |
| **``shuffle``**<br>Randomly reorder elements in a list | **``cookie.remove``**<br>Removes a specified cookie from the client's storage |
| **``unique``**<br>Leave only unique values in a list | **``social``**<br>Interacting with social API |
| **``map``**<br>Apply a function to each element in a list | **``notification``**<br>Send notification |
| **``reduce``**<br>Apply a function cumulatively to the elements in a list | **``mail``**<br>Send mail |
| **``filter``**<br>Apply a filter function to each element in a list | **``call``**<br>Initiate a voice or video call to a specified recipient |
| **``indexes``**<br>Retrieve all keys or attribute names from a structure | **``sms``**<br>Send a text message (SMS) to a specified recipient |
| **``values``**<br>Retrieve all values from a structure | &nbsp;<br>**device**<br>&nbsp; |
| &nbsp;<br>**math**<br>&nbsp; | **``device``**<br>Information related to the hardware device |
| **``sin``**<br>Sine of the value (in radians) | **``cpu``**<br>Information about the CPU, including its usage and specifications |
| **``cos``**<br>Cosine of the value (in radians) | **``fps``**<br>Frames per second for video or graphical rendering |
| **``tan``**<br>Tangent of the value (in radians) | **``vsync``**<br>Vertical sync settings to reduce screen tearing during rendering |
| **``sinh``**<br>Hyperbolic sine of the value | **``resolution``**<br>Screen resolution |
| **``cosh``**<br>Hyperbolic cosine of the value | **``orientation``**<br>Orientation of a device's display (landscape or portrait) |
| **``tanh``**<br>Hyperbolic tangent of the valu | **``dark``**<br>Dark mode setting for user interfaces |
| **``asin``**<br>Arc sine of the value | **``pixel``**<br>Color of the pixel displayed on the screen |
| **``acos``**<br>Arc cosine of the value | **``char``**<br>Symbol on the screen in text mode |
| **``atan``**<br>Arc tangent of the value | **``cursor``**<br>Cursor position on the screen in text mode |
| **``asinh``**<br>Arc hyperbolic sine of the value | **``clear``**<br>Clears the screen in text mode |
| **``acosh``**<br>Arc hyperbolic cosine of the value | **``light``**<br>Turns on or off the device's flashlight |
| **``atanh``**<br>Arc hyperbolic tangent of the value | **``location``**<br>Retrieves the current geographic location using GPS or network triangulation |
| **``round``**<br>Rounds a number to the nearest integer or to the specified number of decimal places | **``gyroscope``**<br>Provides access to the gyroscope sensor for motion detection |
| **``floor``**<br>Largest integer less than or equal to a number | **``accelerometer``**<br>Provides access to the accelerometer sensor to detect acceleration forces |
| **``ceil``**<br>Smallest integer greater than or equal to a number | **``compass``**<br>Accesses the magnetic compass sensor to determine orientation relative to the Earth's magnetic field |
| **``log``**<br>Logarithm (natural by default) of a number | **``proximity``**<br>Detects the proximity of objects in relation to the device's proximity sensor |
| **``fact``**<br>Factorial of a given non-negative number | **``brightness``**<br>Manages the screen brightness level of the device |
| **``fib``**<br>Fibonacci numbers up to a specified index | **``calendar``**<br>Calendar events on a device |
| **``gr``**<br>Golden ratio of a number | **``gallery``**<br>Photo and video library on a device |
| **``abs``**<br>Absolute value of a number | **``contacts``**<br>Contact list on a device |
| **``min``**<br>Smallest of a list of numbers | **``keyboard``**<br>Keyboard information |
| **``max``**<br>Largest of a list of numbers | **``mouse``**<br>Mouse information |
| **``avg``**<br>Average value of a list of numbers | **``gamepad``**<br>Gamepad information |
| **``sum``**<br>Sum of a list of numbers | **``tap``**<br>Simulates a tap gesture |
| **``random``**<br>Generates a pseudo-random number | **``key``**<br>Key binding |
| **``random.seed``**<br>Sets or gets the seed for the random number generator to produce reproducible results | &nbsp;<br>**content**<br>&nbsp; |
| &nbsp;<br>**time**<br>&nbsp; | **``image``**<br>Create an image |
| **``time``**<br>Provides current time since the epoch (1970-01-01 00:00:00 UTC) or calculates time passed since a given start time | **``video``** · **``movie``** · **``anime``**<br>Create a video |
| **``timer``**<br>Creates a timer that can be used to trigger events at specific intervals | **``sound``**<br>Create audio track |
| **``timer.remove``**<br>Removes previously created timer | **``music``**<br>Generates music |
| **``t``** · **``timecheck``**<br>Stopwatch for calculating the time spent on operations | **``model``**<br>Create 3D model |
| **``wait``**<br>Pauses execution for a specified number of seconds | **``book``** · **``novel``** · **``manga``**<br>Create a book, graphic novel, manga |

## V O I D format
**⌜ V O I D format ⌟** is the data format that inherits the best features of [**JSON**](https://en.wikipedia.org/wiki/JSON), [**YAML**](https://en.wikipedia.org/wiki/YAML), [**CSV**](https://en.wikipedia.org/wiki/Comma-separated_values) and [**plain text**](https://en.wikipedia.org/wiki/Plain_text) formats. Makes it easier to write and read data, both by human and by program. The format simplifies data creation by removing the use of unnecessary quotation marks, brackets, colons, commas and other symbols. It is possible to combine **text** and **binary** data.

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
    void
    txt
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
    subtitles
    sound
    3d
    font
    other
  indent
    tab
      '\t
  newline
    line feed
      '\n
  separator
    list
      double space
        '  '
    dictionary
      name
        double space
          '  '
      value
        triple space
          '   '
  value type
    text
      text with space
      'text with space
      'text with space'
      '
        text
        in a
        line
      "
        text
        multi
        line
    number
      1
      100
      -100
      100 000
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
        name1  value1  100
        name2  value2  200
        name3  value3  300
        name4  value4  400
      nested
          value 1
          value 2

          value 3
          value 4
      line
        value 1  value 2  value 3
      one
          value
      empty
        none
    dictionary
      column
        name 1
          value 1
        name 2
          value 2
        name 3
          value 3
      row
        name1      value 1
        name100    value 100
        name10000  value 10000
      table
        name      value

        name 1    value 1
        name 10   value 10
        name 100  value 100
      nested
          name 1
            value 1
          name 2
            value 2


          name 3
            value 3
          name 4
            value 4
      line
        name 1  value 1   name 2  value 2
      empty
        none
    binary
      data
        *4*data
      base64
        simple
          line
            *ViBPIEkgRCBmb3JtYXQ=
          multiline
            *
              ViBPIEk
              gRCBmb3
              JtYXQ=
        gzip
          line
            *eNoLU/BX8FRwUUjLL8pNLAEAG0QEPA==
          multiline
            *
              eNoLU/BX8FR
              wUUjLL8pNLA
              EAG0QEPA==
        safe
          line
            *eNoLU_BX8FRwUUjLL8pNLAEAG0QEPA
          multiline
            *
              eNoLU_BX8FR
              wUUjLL8pNLA
              EAG0QEPA
      hex
        short
          line
            *5620 4F20 4920 4420 666F 726D 6174
          multiline
            *
              5620 4F20
              4920 4420
              666F 726D
              6174 AABB
        full
          line
            *h*5620 4F20 4920 4420 666F 726D 6174
          multiline
            *h
              5620 4F20
              4920 4420
              666F 726D
              6174 AABB
      bin
        short
          line
            *00001000 11110001
          multiline
            *
              0000 1000
              1111 0001
        full
          line
            *b*00001000 11110001
          multiline
            *b
              0000 1000
              1111 0001
  comment
    begins with a space
       C O M M E N T
```

</td>
<td>

```json
{
  "V O I D format": {
    "extension": [
      "void",
      "txt"
    ],
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
      "subtitles",
      "sound",
      "3d",
      "font",
      "other"
    ],
    "indent": {
      "tab": "\t"
    },
    "newline": {
      "line feed": "\n"
    },
    "separator": {
      "list": {
        "double space": "  "
      },
      "dictionary": {
        "name": {
          "double space": "  "
        },
        "value": {
          "triple space": "   "
        }
      }
    },
    "value type": {
      "text": [
        "text with space",
        "text with space",
        "text with space",
        "textin aline",
        "text\nmulti\nline"
      ],
      "number": [
        1,
        100,
        -100,
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
          ["name1", "value1", 100],
          ["name2", "value2", 200],
          ["name3", "value3", 300],
          ["name4", "value4", 400]
        ],
        "nested": [
          [
            "value 1",
            "value 2"
          ],
          [
            "value 3",
            "value 4"
          ]
        ],
        "line": ["value 1", "value 2", "value 3"],
        "one": ["value"],
        "empty": null
      },
      "dictionary": {
        "column": {
          "name 1": "value 1",
          "name 2": "value 2",
          "name 3": "value 3"
        },
        "row": {
          "name1": "value 1",
          "name100": "value 100",
          "name10000": "value 10000"
        },
        "table": [
          [
            "name": "name 1",
            "value": "value 1"
          ],
          [
            "name": "name 10",
            "value": "value 10"
          ],
          [
            "name": "name 100",
            "value": "value 100"
          ]
        ],
        "nested": [
          {
            "name 1": "value 1",
            "name 2": "value 2"
          },
          {
            "name 3": "value 3",
            "name 4": "value 4"
          }
        ],
        "line": {"name 1": "value 1", "name 2": "value 2"},
        "empty": null
      },
      "binary": {
        "data": "impossible",
        "base64": {
          "simple": {
            "line": "need to convert",
            "multiline": "need to convert"
          },
          "gzip": {
            "line": "need to convert",
            "multiline": "need to convert"
          },
          "safe": {
            "line": "need to convert",
            "multiline": "need to convert"
          }
        },
        "hex": {
          "short": {
            "line": "need to convert",
            "multiline": "need to convert"
          },
          "full": {
            "line": "need to convert",
            "multiline": "need to convert"
          }
        },
        "bin": {
          "short": {
            "line": "need to convert",
            "multiline": "need to convert"
          },
          "full": {
            "line": "need to convert",
            "multiline": "need to convert"
          }
        }
      }
    },
    "comment": "property or JSONC"
  }
}
```

</td>
</tr>

</table>

> [!TIP]
> Use **V O I D format [highlighting](https://github.com/voidspawner/void.data/blob/main/asset/settings/void.sublime-syntax)** 🔆 for **[Sublime Text](https://sublimetext.com)**.
>
> **``Tools``** → **``Developer``** → **``New Syntax…``** → **``Copy · Paste``** → **``Save as void.sublime-syntax``**
>
> You can change the **[color scheme](https://github.com/voidspawner/void.data/blob/main/asset/settings/void.sublime-color-scheme)** 🎨 to alternate sections.
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
> chat radius of the Earth
> chat tell me a story
> chat translate to portuguese: Hi World :D
> chat svg ginger cat in a box
> chat python calculator application
> chat image dancing cats
> ```
>
> **``DeepSeek``**
> ```
> chat deepseek radius of the Earth
> ```
> 
> **``Stable Diffusion``**
> ```
> video 'playing cats on the lawn' cats.mp4
> image 'playing cats on the lawn' cats.jpg
> image draw 'remove the cat in the center' cats.jpg cats-edited.jpg
> image grayscale cats.jpg cats-grayscaled.jpg
> image colorize cats-grayscaled.jpg cats-colorized.jpg
> image style cyberpunk cats.jpg cats-cyberpunk.jpg
> image background cats.jpg cats-without-background.png
> image 2x cats.jpg cats-resize-2x.jpg
> image 4x cats.jpg cats-resize-4x.jpg
> image swapface adult.jpg child.jpg adult-to-child.jpg
> ```
> 
> **``Voice Cloning``**
> ```
> voice mike.mp3
> say mike 'Hi World :D
> ```
> 
> **``Speech Recognition``**
> ```
> recognize
> recognize talk.mp3
> recognize video.mp4
> ```
> 
> **``Text-to-Speech``**
> ```
> say Hi World :D
> ```
> 
> **``Google Text-to-Speech``**
> ```
> say en-US-Wavenet-B Hi World :D
> ```
> 
> **``Google Translate``**
> ```
> translate 你好，世界 :D
> translate pt 你好，世界 :D
> ```
> 
> **``DeepL``**
> ```
> translate deepl 你好，世界 :D
> translate deepl pt 你好，世界 :D
> ```

Work is underway to develop a custom AI that will run on a **V O I D chip**.

## V O I D game
**⌜ V O I D game ⌟** is a game that creates an **infinite** number of games, apps and content.

## V O I D social
**⌜ V O I D social ⌟** is a social network where you can **quickly** and **easily** communicate with people all over the world.

## V O I D os
**⌜ V O I D os ⌟** is an Operating System that uses **V O I D lang** to run and create applications and games.

## V O I D tech
**⌜ V O I D tech ⌟** are combinable devices controlled by **[V O I D ai](#v-o-i-d-ai)** for creating **individual** stand-alone productions, as well as creating individual products with **unique designs** and in the required quantities.

## V O I D ideology
**⌜ V O I D ⌟**  is not only about compact technologies, but also an **ideology** that shows where these technologies are taking us.

## V O I D license
**⌜ V O I D license ⌟** is a license to distribute digital content and goods. Expressed in a single sentence:

> **DO WHAT YOU WANT**

You can use it in both **private** and **open source**. Embed it in **free** or **paid** products. **Modify**. Create your **own solutions** based on it. **No need to specify the author**.

## V O I D task
> [!IMPORTANT]
> By adding your code to the repository, you are publishing it under the **V O I D licence**.






























