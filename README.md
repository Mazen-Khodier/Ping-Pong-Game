# Project Details:
- **Project Name**: Python Pong Game
- **Group Members**: 
   * Mazen Muhammad Saad Ali Khodier (120180019)
   * Martin Ihab Ibrahim Agban Farahat (120180004)
   * Mohamed Hatem Mohamed Mohamed Shahin (120170012)

---

# Running Instructions:
- Our program consists of two main parts:
    * **Menus File**: for launching different modes and choosing games settings.
    * **Games File**: containing the game itself with its various modes. <br><br>
- As we mentioned in our presentations, unforetunately we couldn't get the menus code to interact properly with the game code. As such, we prepared seperate files for running and a basic launcher that takes input form the user to run the suitable file with the appropriate game mode settings. <br>
- This file can be found in the folder named **`For Running`** under the name **`Basic_launcher.py`** .
- **Please note** that the files in this folder are merely for the purpose of showing the final product in an accesible manner rather than making the user try and tweak the code theirselves for trying to see different modes. These are not meant to be taken as the actual finalised code in any way.<br><br>
- The game modes have a brief description in the Files & Folders section below. <br><br> 
- As for the menus, this can be seen by openning **`Menu`** folder and running **`main.py`**<br><br>
- The libraires used were: **`pygame`, `numpy`, `sys`, `os`**

---

# Files & Folders:
- **`8-BIT WONDER.TTF`**: Font used in the game
- **`Advanced Programming Pong Game.pptx`**: Group presentation for the project
- **`ping-pong.png`**: Game icon image
- **`Pong_Game`**: The main file of the project. Contains the code implementing the various game modes using object oriented programming
- **`Read Me`** Files with different extensions for documenting the project<br><br>

- **For Running**: As previously mentioned, it contains files for showing the demo in a somewhat presentable manner
    * **`Basic_Launcher.py`**: For running the remaining files
    * **`Practice_Mode.py`**: Singleplayer mode vs wall
    * **`Multiplayer_Mode.py`**: Two human players vs each other
    * **`VS_Computer_Mode.py`**: Singleplayer vs AI
    * **`Watch_Computer_Mode.py`**: Watch AI practice vs a wall with advanced physics<br><br>
- **Menu**: Contains Menus file with the old implementation of the game (more details can be found in the Notes Section below)
    * **`game.py`**: old implementation of the game
    * **`main.py`**: file for running both game and menus
    * **`menu.py`**: file of the menus implementation<br><br>
- **Other**: Contains screenshots of the final product and a csv data file
    * **Demo**: Folder containing screenshots showing various aspects and features of the project. Used in the presentation
    * **`data.csv`**: Some data that were collected for implementing an AI using machine learning (K nearest neighbor algorithm). This approach was later discarded but the file is left for possible future upgrades. The data consists of the ball position and speed (x, y, vx, vy) vs the paddle position (paddle.y). Collected by playing the old implementation of the game<br><br>
    
- **Under Development**: This folder is for files that are still not yet complete
    * **`New_Menu.py`**: A new approach to the menus file implementation using abstract factory design pattern but still under early development<br><br>

---

# Notes:
- The testing for this project was mainly dependent on running the code and not on having well-defined test cases<br><br>
- We started the project with developing both the game and menus seperately as we decided to later join them
- The old implementation of the game was meant to be a temporary one for testing the menus file and how they interacted with each other
- Unfortunately, at the end the files were written in a dependent way that was not expected and it would have been better (and easier!) to start a new implementation of the menus file from scratch
- As mentioned above, the **`New_Menu.py`** is an incomplete attempt at exactly that<br><br>
- The settings of the game modes are found in the Game class variables. Namely:
    * **`COM`**: AI Settings
    * **`SEC`**: Multiplayer Settings
    * **`KEYBOARD`**: Mouse/Keyboard Settings
    * **`PHSYX`**: Advanced/Simpled Physics Settings
    * And many others!

---

# Update Notes:
Since the presentation there were some further updates were made to the code. These include:
- Added pause feauture in the game by pressing Esc
- Improved the complex physics feature to be more playable
- Started development of of a new menus code

---

# Some Features to be Added in the Future:
- Fullscreen
- Sound Effects
- How to Play Section
- Backgrounds
- AI Difficulties

---
