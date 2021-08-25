import sys
import pyperclip
import pickle


def yn_input(prompt):
    """get yes/no type input from user

    Args:
        prompt (str): the question to ask user

    Returns:
        bool: True if input starts with y, False if input starts with n
    """    
    raw = input(prompt+"(yes/no): ")
    acceptable_input = ['y','ye','yes','yeah','n','no','nah','naw', '']
    if raw not in acceptable_input:
        print('I am not sure what you typed in, please try again.')
        return yn_input(prompt)
    if len(raw) > 0 and raw[0].lower() == 'y':
        return True
    return False


def str_input():
    """get string input from user (multi lines or single line)

    Returns:
        str: user input
    """    
    if yn_input("Will you be inputting multiple lines?"):
        print("What is the value? (press control-z and enter to end)")
        return "".join(sys.stdin.readlines())
    else:
        return input("What is the value? (press enter to end):")



def print_entry(key, val):
    """print one entry in the database, hide part of the value if it's too long

    Args:
        key (str): the key to print
        val (str): the value to print
    """    
    print(key + " : " + val.replace("\n", " ")[0:10], end="")
    if len(val) >= 10:
        print("...")
    print()


def get(key):
    """get the value of given key from database and copy to clipboard

    Args:
        key (str): the key to get the value from
    """    
    key = key.replace("\n", "")
    if key in clipboard:
        ps_result = clipboard[key]
        # remove the newline at the end and replace (n) with new line
        result = ps_result[0:len(ps_result) - 1]
        print_entry(key, result)
        pyperclip.copy(result)
        print('Value of \"' + key + '\" copied to clipboard.')
    else:
        print('There is no value for \"' + key+'\"')


def edit():
    """edit specific entry in database
    """    
    print_keys()
    key = input("What is the key that you want to edit?")
    if(key in clipboard):
        clipboard[key] = str_input()
    else:
        if yn_input("Key \"" + key + "\" cannot be found, wanna add it?"):
            clipboard[key] = str_input()


def add():
    """ask the user for input and add an entry to the database
    """    
    newKey = input("What is the key that you want to add?")
    if newKey in clipboard.keys():
        if(not yn_input("There is already an entry, want to edit it?")):
            return
    clipboard[newKey] = str_input()


def delete():
    """delete an entry from the database
    """    
    print_keys()
    key = input("What is the key that you want to delete?")
    if key in clipboard.keys():
        print("Key \""+key+"\" deleted")
        clipboard.pop(key)
    else:
        print("Key \"" + key + "\" cannot be found.")


def print_keys():
    """print all existing keys in the database
    """    
    print("The keys that you saved are: ")
    for keyword in clipboard.keys():
        print(keyword, end=', ')
    print()


def print_all():
    """print all entries in the database (key:value)
    """    
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
        print("File \"mclip.dat\" is not found and will be created")
        return {}  # create a new dictionary clipboard if the file does not exist


def write():
    file = open("mclip.dat", "wb")
    pickle.dump(clipboard, file)
    file.close()


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


if __name__ == '__main__':
    clipboard = read()
    # when the user types "mclip" and no argument
    if len(sys.argv) < 2:
        print('\nUsage: py mclip.py [command] - key/add/edit/delete/keys/all/exit')
        sys.argv.append(input("What do you want to do?").lower())
        if sys.argv[1] == 'exit':
            sys.exit()
    main(sys.argv[1].lower())
