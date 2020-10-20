import sys
import pyperclip
import pickle

if len(sys.argv) < 2:
    print('\nUsage: py mclip.py [command] - key/add/edit/delete/keys/all/exit')
    sys.argv.append(input("What do you want to do?").lower())
    if sys.argv[1] == 'exit':
        sys.exit()

command = sys.argv[1].lower()  # second command line arg is the command


def yn_input(prompt):
    raw = input(prompt+"(yes/no): ")
    if(len(raw) == 0 or (raw[0].lower() != 'y' and raw[0].lower() != 'n')):
        print('I am not sure what you typed in, please try again.')
        return yn_input(prompt)
    return raw[0].lower() == 'y'


def print_entry(key, val):
    print(key + " : " + val.replace("\n", " ")[0:10], end="")
    if len(val) >= 10:
        print("...")
    print()


def get(key):
    key = key.replace("\n", "")
    if key in clipboard:
        # remove the newline at the end and replace (n) with new line
        result = clipboard[key][0:len(clipboard[key]) - 1]
        print_entry(key, result)
        pyperclip.copy(result)
        print('Value of \"' + key + '\" copied to clipboard.')
    else:
        print('There is no value for \"' + key+'\"')


def edit():
    print_keys()
    newKey = input("What is the key that you want to edit?")
    if(newKey in clipboard):
        print("What is the value? (press control-z and enter to end)")
        clipboard[newKey] = "".join(sys.stdin.readlines())
    else:
        print("Key \"" + newKey + "\" cannot be found.")


def add():
    newKey = input("What is the key that you want to add?")
    if newKey in clipboard.keys():
        if(not yn_input("There is already an entry, want to edit it?")):
            return
    print("What is the value? (press control-z and enter to end)")
    clipboard[newKey] = "".join(sys.stdin.readlines())



def delete():
    print_keys()
    key = input("What is the key that you want to delete?")
    if key in clipboard.keys():
        print("Key \""+key+"\" deleted")
        clipboard.pop(key)
    else:
        print("Key \""+key+"\"not found")


def print_keys():
    print("The keys that you saved are: ")
    for keyword in clipboard.keys():
        print(keyword, end=', ')
    print()


def print_all():
    print("\nYour Clipboard:")
    for keyword in clipboard.keys():
        print_entry(keyword, clipboard.get(keyword))
    print()


def read():
    try:
        file = open('mclip.dat', 'rb')
        data = pickle.load(file)
        file.close()
        return data
    except FileNotFoundError:
        print("File \"mclip.bat\" is not found and will be created")
        return {}  # create a new dictionary clipboard if the file does not exist


def write():
    file = open("mclip.dat", "wb")
    pickle.dump(clipboard, file)
    file.close()


clipboard = read()


def main(command):
    if command == 'edit':
        edit()
    elif command == 'add':
        add()
    elif command == 'delete':
        delete()
    elif command == 'all':
        print_all()
    elif command == 'keys':
        print_keys()
    else:
        get(command)
    write()
    if(yn_input("Anything else")):
        print()
        print_keys()
        command = input('What else do you want to do: ')
        main(command)


main(command)
