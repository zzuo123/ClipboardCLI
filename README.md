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
```
mclip *** :: (*** is the key) This will copy the value of the entry that matches the key
mclip all :: This shows you all the entries in the mclip clipboard
mclip add :: This will allow you to add an entry to mclip (key and value) (type (n) as newline)
mclip delete :: This will allow you to delete an entry
mclip keys :: This will only show you the keys of all the entries in mclip
```
There are so much more !

## Example
The following segment demonstrates how to add an entry.
```
C:\Downloads\Directory>mclip 

attention: type(n) for new line.
The keywords that you saved are: 

what is the keyword that you want to add? hello
what is the new phrase that you want to add?world

Anything else (y/n): n
Press any key to continue . . .
```
The following segment demonstrates how to get the value of an entry to your device clipboard
```
C:\Downloads\Directory>mclip hello
hello : world
Text for hello copied to clipboard.
Anything else (y/n): n
Press any key to continue . . .
```

## Sidenote
Mclip is a personal project, and the data you entered will be stored locally in a text file called phrases.txt, which you will download with the rest of the program. However, the data will not be encrypted (not in this version), so use it at your own risk.

## Credit
This program is inspired by the Mclip program in Chapter6 of [Automate the Boring Stuff with Python: Practical Programming for Total Beginners](https://automatetheboringstuff.com/) written by [Al Sweigart](https://alsweigart.com/). However, I added my own twist to it to make it work differently and have much more functionality.

## Enjoy!