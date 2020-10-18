# MclipPlusPlus
 A multipurpose clipboard "app" for windows command prompt

## Installation
1. Download python from : https://python.org/downloads/
2. Navigate to whatever folder you downloaded this program into
3. Type "cmd" into the directory box in file explorer to open up command prompt (or open command prompt and navigate to the folder)
4. Run the following command to create a virtual environment for Python (This might take a while)
```batch
python -m venv venv
```
5. After the virtual encironment is created, use [pip](https://pip.pypa.io/en/stable/) to install libraries for mclip (This might also take a while)
```batch
pip install sys
pip install pyperclip
```
6. You might want to add an entry of the current directory to system path so that you can access the mclip program from anywhere in command prompt. A [tutorial](https://www.computerhope.com/issues/ch000549.htm#:~:text=%20Setting%20the%20path%20and%20variables%20in%20Windows,system%20settings%20link%20in%20the%20left...%20More%20) can be found [here](https://www.computerhope.com/issues/ch000549.htm#:~:text=%20Setting%20the%20path%20and%20variables%20in%20Windows,system%20settings%20link%20in%20the%20left...%20More%20).

## Usage
1. Type in mclip in command prompt and you will see a list of commands you can do with this program
2. You may also specify command when you run mclip, such as
```batch
mclip all :: This shows you all the entries in the mclip clipboard
mclip add :: This will allow you to add an entry to mclip
mclip delete :: This will allow you to delete an entry
mclip keys :: This will only show you the keys of all the entries in mclip
```
There are so much more !

## Sidenote
Mclip is a personal project, and the data you entered will be stored locally in a text file called phrases.txt, which you will download with the rest of the program. However, the data will not be encrypted (not in this version), so use it at your own risk.

Enjoy!