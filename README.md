# V O I D lang

## About
**⌜ V O I D lang ⌟** is the language for rapidly creating applications and games in the **JSON format**. It is used as a replacement for the standard Bash/CMD/etc. languages and for writing **applications**, **servers** and **games**. The language uses one of the languages already preinstalled in the system. So you don't need to install anything else. Code and data are not separated. So the whole application fits in **one JSON file**. Since the **code is presented as data**, applications can be easily generated with **AI**, updated, installed and launched remotely.

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


### Value

#### =
Setting the vlue with an expression
```javascript
["=", "i", 10]
```
```javascript
["=", "i", 1, "+", 1, "*", 2]
```
```javascript
["=", "i", 1, "+", [1, "*", 2]]
```
```javascript
["=", "i", ["sin", 0.5]]
```
```javascript
["=", "i", [[1, 2, "{value}"]]]
```
```javascript
["=", "i", [{"index": "{value}"}]]
```

#### =!
Setting the value without an expression
```javascript
["=!", "i", ["A", "B", "{value without parsing}"]]
```

#### Get
Get the value
```javascript
[".", "{i}"]
```

#### Remove
Remove the value
```javascript
["-", "i"]
```

#### type
Get the value type

#### text
Convert the value to the text type

#### number
Convert the value to the number type

#### list
Convert the value to the list type

#### bool
Convert the value to the bool type

#### Translate
Translate the text
```javascript
{"run": [[".", "{text.title}"], [".", "{text.title.zh}"]], "text": {"title": {"en": "Title", "zh": "\u6a19\u984c"}}}
```

#### Binary
Binary data in Base64 with or without Gzip
```javascript
{"data": {"image": "R0lGODlhPwA/AKEAAAAAAP..."}, "run": [["file.write", "image.gif", "{data.image}"]]}
```

#### alias
Action alias
```javascript
["alias", "vn.say", "say"]
```
```javascript
["alias", {"vn.say": "say", "vn.remove": "x"}]
```
```javascript
["=", "alias.'vn.say'", "say"]
```

#### +
Summarize the values

#### -
Subtract the values

#### \*
Multiply the values

#### /
Divide the values

#### %
Remainder of a divided

#### ~
Incrementing a value to a power

#### !
Not operation for one or two values

#### &
And operation for two values

#### |
Or operation for two values

#### ^
Xor operation for two values

#### >>
Bit shift to the right

#### <<
Bit shift to the left

#### +=
Setting the value with a sum

#### -=
Setting the value with a substract

#### \*=
Setting the value with a multiply

#### /=
Setting the value with a divide

#### %=
Setting the value with a reminder

#### ~=
Setting the value with a power

#### !=
Setting the value with a not

#### &=
Setting the value with a add

#### |=
Setting the value with a or

#### ^=
Setting the value with a xor

#### >>=
Setting the value with a right shift

#### <<=
Setting the value with a left shift

### Control

#### .
Print text or data
```javascript
[[".", "Text"]]
```
```javascript
[[".", "Count", ": ", 12]]
```
```javascript
[[".", [1, 2, 3]]]
```
```javascript
["."]
```

#### .!
Print text or data without newline at the end
```javascript
[[".!", "Print "]]
```
```javascript
[[".!", "without new line"]]
```

#### ?
If statement
```javascript
["?", ["{value}", ">", 2], [[".", ">2"]], [[".", "<=2"]]]
```

#### ??
Case / Match statement
```javascript
["??", "{value}", [[1, [[".", 1]]], [100, [[".", 100]]], [[["{value}", ">", 10], "and", ["{value}", "<", 20]], [[".", "10-20"]]], [null, [[".", "other"]]]]]
```

#### ..
For / Each / Repeat / While statement

#### x
Break loop

#### >>>
Continue loop

#### <<<
Repeat loop iteration

#### _
Return value

#### action
Run action

#### action.load
Load external action

#### X
Exit application or game

#### open
Open in the standard way

#### shell
Run shell command

#### shell.open
Run shell command in new window

#### code
Run native code

#### ok
Log ok messge with data

#### warning
Log warning message with data

#### error
Log error message with data

#### export
Export game or app

#### debug
Show / Hide debug info

#### fps
Show / Hide FPS

### Text

#### number
Convert number to text or text to the number

#### date
Convert date to text or text to the timestamp / date

#### path_dir
Extract directory from the path

#### path_name
Extract filename from the path

#### path_extension
Extract extension from path

#### path_basename
Extract basename from the path

#### path_drive
Extract drive from the path

#### lower
Text to lower

#### upper
Text to upper

#### strip
Strip the text

#### strip.begin
Strip begin of the text

#### strip.end
Strip end of the text

#### replace
Replace subtext with another

#### find
Find subtext in the text

#### part
Get part of the text or the list

#### split
Split the text or the list

#### join
Join the list with subtext or multiple lists

#### regex
Find text with regular expression

#### regex.replace
Replace text with regular expression

#### escape
Escape text with pattern

#### escape.html
Escape HTML text

#### escape.sql
Escape SQL query text

#### escape.url
Escape URL text

#### escape.json
Escape JSON text

#### unescape
Unescape text with pattern

#### unescape.html
Unscape HTML text

#### unescape.sql
Unscape SQL query text

#### unescape.url
Unscape URL text

#### unescape.json
Unscape JSON text

### List

#### push
Push value to the list

#### pop
Pop value from the list

#### reverse
Reverse the list

#### shuffle
Shuffle the list

### Math

#### sin
Sine value

#### cos
Cosine value

#### tan
Hyperbolic value

#### sinh
Hyperbolic sine value

#### cosh
Hyperbolic cosine value

#### tanh
Hyperbolic tangent value

#### asin
Arcsine value

#### acos
Arcosine value

#### atan
Arctangent value

#### asinh
Hyperbolic arcsine value

#### acosh
Hyperbolic arccosine value

#### atanh
Hyperbolic arctangent value

#### round
Round value

#### floor
Floor value

#### ceil
Ceil value

#### log
Logarithm value

#### pow
Power value

#### factorial
Factorial value

#### abs
Absolute value

#### min
Minimum value

#### max
Maximum value

#### avg
Average value

#### hex
Convert value to hexadecimal

#### bin
Convert value to binary

#### dec
Convert value to decimal

#### rad
Convert value to radian

#### deg
Convert value to degree

#### random
Random value

#### random.new
Create random seed

#### random.seed
Get / Set seed

### Time

#### time
Get timestamp with microseconds

#### time.milli
Get timestamp with milliseconds

#### time.seconds
Get timestamp with seconds

#### time.float
Get timestamp with seconds as float value

#### wait
Wait actions with seconds

#### timepast
Start / Check timepast

#### timer
Create timer with seconds

#### timer.remove
Remove timer by name

### Crypto

#### hash
Generate hash

#### uuid
UUID unique value

#### md5
MD5 hash

#### sha1
SHA1 hash

#### sha256
SHA256 hash

#### sha512
SHA512 hash

#### crc32
CRC32 hash

#### base64.encode
Encode data with Base64

#### base64.decode
Decode Base64 data

#### gzip
Encode data with Gzip

#### gzip.decode
Decode Gzip data

#### rsa
Encode data with RSA

#### rsa.decode
Decode RSA data

#### rsa.key.public
Get RSA public key

#### rsa.key.private
Get RSA private key

#### ssl
Encode SSL data

#### ssl.decode
Decode SSL data

#### ssl.check
Check SSL data

#### bcrypt
Encode data with Bcrypt

#### bcrypt.check
Check Bcrypt data

### Format

#### json
Encode JSON format

#### json.decode
Decode JSON format

#### yaml
Encode YAML format

#### yaml.decode
Decode YAML format

#### csv
Encode CSV format

#### csv.decode
Decode CSV format

#### ini
Encode INI format

#### ini.decode
Decode INI format

#### html
Encode HTML format

#### html.decode
Decode HTML format

#### xml
Encode XML format

#### xml.decode
Decode XML format

#### css
Encode CSS format

#### css.decode
Decode CSS format

#### robots
Encode Robots format

#### robots.decode
Decode Robots format

#### sitemap
Encode Sitemap format

#### sitemap.decode
Decode Sitemap format

### File

#### file.exists
Checking file existence

#### file.write
Write data to file

#### file.read
Read data from file

#### file.remove
Remove file

#### file.move
Move file

#### file.copy
Copy file

#### file.rename
Rename file

#### file.info
Get file info

#### file.size
Get file size

#### file.permissions
Get / Set file permissions

#### file.modified
Get / Set file modified time

#### file.sha256
Get SHA256 file hash

#### file.zip
Zip file / Add file to zip archive

#### file.zip.list
Get list of the zip archive

#### file.zip.exists
Checking path existence in the zip archive

#### file.zip.read
Read file from the zip archive

#### file.zip.remove
Remove path from the zip archive

#### file.unzip
Unzip archive

#### file.gzip
Gzip file

#### file.ungzip
Ungzip archive

#### file.link
Create symlink

#### file.link.exists
Checking link existence

#### dir.exists
Checking directory existence

#### dir.create
Create directory

#### dir.copy
Copy directory

#### dir.move
Move directory

#### dir.rename
Rename directory

#### dir.remove
Remove directory

#### dir.list
Get directory content

#### dir.clear
Clear directory

#### dir.info
Get directory info

#### dir.size
Get directory size

#### dir.permissions
Get directory permissions

#### dir.modified
Get / Set directory modified time

#### dir.zip
Zip directory

#### drive.list
Get list of the drives

#### drive.name
Get / Set drive name

#### drive.size
Get drive size

#### drive.free
Get drive free space

#### drive.mount
Mount the drive

#### drive.unmount
Unmount the drive

### Server

#### server
Start / Get server

#### server.stop
Stop server

#### socket
Start Socket server

#### http
Start HTTP server

#### https
Start HTTP server

#### server.mail
Start Mail server

#### cloud
Start Cloud server

### Request

#### request
Make network request

#### request.post
Make POST request

#### request.put
Make PUT request

#### request.delete
Make DELETE request

### Cache

#### cache
Get / Set cache by name

#### cache.list
Get list of the cache

#### cache.info
Get info of the cache by name

#### cache.remove
Remove cache by name

#### cache.clear
Clear all cache

### Data

#### sql
Raw SQL querry

#### sql.connect
Connect to the SQL server

#### sql.disconnet
Disconnect from the SQL server

#### sql.user
Get / Set user

#### sql.user.list
Get list of users

#### sql.user.remove
Remove user

#### sql.db
Get / Set database

#### sql.db.list
Get list of databases

#### sql.db.remove
Remove the database

#### sql.db.size
Get size of the database

#### sql.table
Get / Set table

#### sql.table.list
Get list of tables

#### sql.table.remove
Remove table

#### sql.field
Get / Set field

#### sql.field.list
Get list of fields

#### sql.field.remove
Rmove the field

#### sql.index
Get / Set index

#### sql.index.list
Get list of indexes

#### sql.index.remove
Remove index

#### sql.function
Get / Set function

#### sql.function.list
Get list of functions

#### sql.function.remove
Remove function

#### sql.view
Get / Set view

#### sql.view.list
Get list of views

#### sql.view.remove
Remove view

#### sql.one
Fetch one result

#### sql.all
Fetch all results

#### sql.cursor
Get / Set cursor position

#### sql.transaction
Start transaction

#### sql.commit
Commit transaction

#### sql.rollback
Rollback transaction

### OS

#### os.name
Get OS name

#### os.version
Get OS version

#### os.username
Get username

#### os.desktop
Check whether the OS is desktop

#### os.mobile
Check whether the OS is mobile

#### os.web
Check whether the OS is web

#### os.windows
Check whether the OS is Windows

#### os.macos
Check whether the OS is macOS

#### os.ios
Check whether the OS is iOS

#### os.ipados
Check whether the OS is ipadOS

#### os.watchos
Check whether the OS is watchOS

#### os.tvos
Check whether the OS is tvOS

#### os.android
Check whether the OS is Android

#### os.linux
Check whether the OS is Linux

### Device

#### cpu.name
Get CPU name

#### cpu.cores
Get the number of CPU cores

#### gps
Get GPS position

#### speed
Get speed

#### tilt
Get the device tilt

#### compass
Get a compass direction

#### motion
Get the device motion

#### photo
Get photos from the gallery

#### contacts
Get the device contacts

#### calendar
Accessing the calendar

#### light
Turn the flashlight On / Off

#### health
Access to health data

#### camera
Access to the camera

#### mic
Access to the microphone

#### notification
Send a notification

#### notification.token
Get a notification token

#### key
Bind the action to the key

#### key.remove
Unbind the action from the key

#### key.press
Key press imitation

#### key.enable
Enable the key

#### key.disable
Disable the key

#### keyboard
Show / Hide the virtual keyboard

#### keyboard.height
Get the height of the virtual keyboard

#### mouse
Show / Hide the mouse

#### mouse.lock
Lock the mouse position

#### mouse.position
Get / Set the mouse position

#### mouse.capture
Capture the mouse

#### mouse.confine
Confine the mouse

#### mouse.shape
Get / Set the mouse shape

#### gamepad.axis
Get axis of the gamepad

#### gamepad.vibrate
Gamepad vibration

### Clipboard

#### clipboard
Get / Set the clipboard

#### clipboard.clear
Clear the clipboard

### Say

#### say
Say the text

#### say.list
Get the list of the voices

#### say.name
Get / Set the voice

#### say.stop
Stop the speech

#### say.pause
Pause / Continue the speech

### Image

#### image
Create the image

#### image.size
Resize the image

#### image.crop
Crop the image

#### image.square
Crop the image to the square shape

#### image.rotate
Rotate the image

#### image.flip.h
Flip the horizontally

#### image.flip.v
Flip the image vertically

#### image.tint
Tint the image

#### image.gray
Grayscale the image

### Video

#### video
Create the video

#### video.size
Resize the video

#### video.rotate
Rotate the video

#### video.flip.h
Flip the video horizontally

#### video.flip.v
Flip the video vertically

#### video.clip
Clip the video

#### video.speed
Change the speed of the video

#### video.reverse
Reverse the video

### Sound

#### volume
Change master volume

#### sound
Play the sound

#### sound.list
Get the list of the sounds

#### sound.remove
Remove the sound

#### sound.volume
Change the sound volume

#### sound.speed
Change the sound speed

#### sound.clip
Clip the sound

### Music

#### music
Play the music

#### music.stop
Stop the music

#### music.pause
Pause / Resume the music

#### music.volume
Change the music volume

### Screen

#### screen.count
Get screens count

#### screen.list
Get the list of screens

#### size
Get the screen size

#### screen.name
Get the screen name

#### orientation
Get / Set / Flip the orientation

#### landscape
Landscape orientation

#### portrait
Portrait orientation

#### rate
Get the refresh rate of the screen

#### pixel
Get the pixel on the screen

#### screen.info
Get the screen info

#### dpi
Get the screen DPI

#### dark
Get / Set the dark mode

#### touchscreen
Check if the screen is touchscreen

### UI

#### ui
Create / Edit the UI container

#### title
Get / Set the window title

#### icon
Get / Set the window icon

#### bg
Get / Set the window background

#### size
Get / Set the window size

#### max
Get / Set the window maximum size

#### size.min
Get / Set the window minimum size

#### position
Get / Set the window position

#### direction
Get / Set the window writing direction

#### attention
Pay attention to the window

#### on
Make the window on top

#### foreground
Make the window foreground

#### unfocusable
Make the window unfocusable

#### unresizble
Make the window unresizable

#### center
Center the window to the screen

#### fullscreen
Toggle fullscreen mode

#### drop
Drag & Drop event of the window

#### border
Get / Set the border of the screen

#### show
Show the UI element

#### hide
Hide the UI element

#### focus
Focus the UI element

#### enable
Enable the UI element

#### disable
Disable the UI element

#### visible
Get / Set the visibility of the UI element

#### enabled
Get / Set the activity of the UI element

#### scale
Scale the UI element

#### maximized
Get / Set maximized mode

#### minimized
Get / Set minimized mode

#### exclusive
Get / Set exclusive mode

#### vsync
Get / Set vertical synchronization

#### ui.text
Create 'text' UI element

#### ui.image
Create 'image' UI element

#### ui.button
Create 'button' UI element

#### ui.video
Create 'video' UI element

#### ui.select
Create 'select' UI element

#### ui.switch
Create 'switch' UI element

#### ui.progress
Create 'progress' UI element

#### ui.slider
Create 'slider' UI element

#### ui.edit
Create 'edit' UI element

#### ui.split.h
Create 'split horizontally' UI element

#### ui.split.v
Create 'split vertically' UI element

#### ui.list
Create 'list' UI element

#### ui.tile
Create 'tile' UI element

#### ui.color
Create 'color' UI element

#### ui.date
Create 'date' UI element

#### ui.drop
Create 'drag & drop' UI element

#### ui.menu
Create 'system menu' UI element

#### ui.menu.context
Create 'context menu' UI element

#### ui.window
Create 'window' UI element

#### window.list
Get the list of windows

#### dialog.file
Show `select file` dialog

#### dialog.color
Show `select color` dialog

#### dialoog.date
Show `select date` dialog

#### dialog.select
Show `select` dialog

#### effect
Add the effect to the UI element

#### effect.list
List all effects of the UI element

#### effect.clear
Remove all effects from the UI element

#### effect.remove
Remove the effect from the UI element

#### game
Initialize / Run the game

#### menu
Create / Show / Hide the game menu

### Visual Novel

#### vn
Show / Hide the visual novel

#### vn.clear
Reset the visual novel to the initial state

#### vn.say
Say the text of the visual novel

#### vn.skip
Skip the text of the visual novel

#### vn.route
Make the route selection of the visual novel

#### vn.route.remove
Remove the route selection of the visual novel

#### vn.route.check
Check the route selection of the visual novel

#### vn.route.select
Select the route of the visual novel

#### vn.route.repeat
Repeat the route selection of the visual novel

#### vn.route.skip
Skip the route selection of the visual novel

#### vn.character
Get / Set / Change the character of the visual novel

#### vn.come
Character comes in the visual novel

#### vn.leave
Character leaves in the visual novel

### 2D

#### 2d
Show / Hide the 2D game

#### 2d.bg
Create the 2D background with parallax effect

#### 2d.map
Create the 2D map

#### 2d.character
Create the 2D character

#### 2d.object
Create the 2D object

#### 2d.npc
Create the 2D NPC character

#### 2d.enemy
Create the 2D enemy character

#### 2d.shoot
Create the 2D shoot event

#### 2d.jump
Create the 2D jump event

#### 2d.drop
Create the 2D drop event

#### 2d.look
Create the 2D look event

#### 2d.inventory
Create the 2D inventory

#### 2d.hud
Create the 2D HUD

#### 2d.sound
Create the 2D sound

#### 2d.light
Create the 2D source of light

#### 2d.camera
Create the 2D camera

#### klicker
Create / Show / Hide 2D clicker or idle game

### 3D

#### 3d
Show / Hide the 3D game

#### 3d.bg
Create the 3D background

#### 3d.map
Create the 3D map

#### 3d.character
Create the 3D character

#### 3d.object
Create the 3D object

#### 3d.npc
Create the 3D NPC

#### 3d.enemy
Create the 3D enemy

#### 3d.shoot
Create the 3D shoot event

#### 3d.jump
Create the 3D jump event

#### 3d.drop
Create the 3D drop event

#### 3d.look
Create the 3D look event

#### 3d.hud
Create the 3D HUD

#### 3d.inventory
Create the 3D inventory

#### 3d.sound
Create the 3D sound

#### 3d.light
Create the 3D source of light

#### 3d.camera
Create the 3D camera

### AI

#### ai.text
Create the AI text

#### ai.image
Create the AI image

#### ai.video
Create the AI video

#### ai.music
Create the AI music

#### ai.sound
Create the AI sound

#### ai.say
Create the AI speech

#### ai.2d
Create the AI 2D asset

#### ai.3d
Create the AI 3D asset

#### ai.character
Create the AI character

#### ai.clean
Clean the image or the video with the AI

#### ai.resize
Resize the image or the video with the AI

#### ai.color
Recolor the image or the video with the AI

#### ai.style
Restyle the image or the video with the AI

#### ai.translate
Translate the text with the AI

#### ai.capture.voice
Capture the voice with the AI

#### ai.capture.object
Capture the object with the AI

#### ai.capture.motion
Capture the motion with the AI

### Voids

#### voids
Get the Voids wallet

#### buy
Buy the currency or other asset

#### sell
Sell the currency or other asset

#### send
Send the currency or other asset

#### crypto
Get crypto currencies info

#### currency
Get currencies info

#### stocks
Get stocks info

#### futures
Get futures info

#### options
Get options info

#### bonds
Get bonds info

#### etf
Get etfs info

#### exchange
Get exchanges info

#### exchange.crypto
Get crypto exchanges info

#### token
Get the token info

#### token.list
Get the list of tokens

#### token.add
Add the tokens

#### token.remove
Remove the tokens

### Social

#### void.chat
Get / Set / Send the chat message

#### void.chat.list
Get the list of the chat messages

#### void.chat.remove
Remove the chat message

#### void.contact
Create / Get / Set the contact

#### void.contact.list
Get the list of the contacts

#### void.contact.remove
Remove the contact

#### void.image
Create / Get / Set the image

#### void.image.list
Get the list of the images

#### void.image.remove
Remove the image

#### void.video
Create / Get / Set the video

#### void.video.list
Get the list of the videos

#### void.video.remove
Remove the video

#### void.text
Create / Get / Set the text

#### void.text.list
Get the list of the texts

#### void.text.remove
Remove the text

#### void.site
Create / Get / Set the site

#### void.site.list
Get the list of the sites

#### void.site.remove
Remove the site

#### void.data
Create / Get / Set the data

#### void.data.list
Get the list of the data

#### void.data.remove
Remove the data

#### void.app
Create / Get / Set the app

#### void.app.run
Run the app

#### void.app.list
Get the list of the apps

#### void.app.remove
Remove the app

#### void.game
Create / Get / Set the game

#### void.game.run
Run the game

#### void.game.list
Get the list of the games

#### void.game.remove
Remove the game


## V O I D format
**[⌜ V O I D format ⌟](https://github.com/voidspawner/void.format)** is the data format that inherits the best features of **JSON**, **YAML**, **CSV** formats. Makes it easier to write and read data, both by human and by program.

## V O I D os
**[⌜ V O I D os ⌟](https://github.com/voidspawner/void.os)** is an Operating System that uses **V O I D lang** to run and create apps and games.

## V O I D ai
Generate **images・videos・texts・assets**. A limited number of uses are available for free. To use extra **V O I D ai** you can **pay** with **⦵ voids** digital currency.

## V O I D voids
Digital currency used in the **V O I D ecosystem**.

- Name ```voids```
- Symbol ```⦵```
- Exchange rate ```⦵ 1``` = ```$ 1``` = ```USD₮ 1```

The currency is also a **spawner**. Every month the profit is distributed among the **voids** holders. The number of voids increases proportionally and can be withdrawn to other digital currencies.

## V O I D social
**[⌜ V O I D social ⌟](https://voidsp.com)** is a **social network** for messaging, sharing apps, games, images, videos and other content. Buy and sell, find job, crypto exchange, transfer **V O I D voids** and more other.
