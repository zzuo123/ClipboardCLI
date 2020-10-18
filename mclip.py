import sys
import pyperclip

TEXT = {}  # store data from the phrases file

if len(sys.argv) < 2:
    print(
        '\nUsage: py mclip.py [keyphrase] - keys/add/edit/delete/keys/all/exit')
    sys.argv.append(input("what do you want to do?").lower())
    if sys.argv[1] == 'exit':
        sys.exit()

keyphrase = sys.argv[1].lower()  # first command line arg is the keyphrase


def get(keyphrase):
    if keyphrase in TEXT:
        result = TEXT[keyphrase][0:len(
            TEXT[keyphrase]) - 1].replace("(n)", "\n")
        print(keyphrase+" : "+result)
        pyperclip.copy(result)
        print('Text for ' + keyphrase + ' copied to clipboard.')
    else:
        print('There is no text for ' + keyphrase)


def edit():
    print_content()
    newKey = input("what is the keyword that you want to edit? ")
    if(newKey in TEXT):
        TEXT[newKey] = input(
            "what is the new phrase that you want to change to?")
    else:
        print("Sorry, your key does not exist.")


def add():
    print_content()
    newKey = input("what is the keyword that you want to add? ")
    TEXT[newKey] = input("what is the new phrase that you want to add?")


def delete():
    print_content()
    del TEXT[input("what is the keyword that you want to delete?")]


def print_content():
    print("The keywords that you saved are: ")
    for keyword in TEXT.keys():
        print(keyword, end=', ')
    print()


def print_all():
    print("\nYour Clipboard:")
    for keyword in TEXT.keys():
        print(keyword, end="\t")
        print(TEXT.get(keyword), end="")
    print()


def read():
    file = open("phrases.txt", "r")
    count = 1
    key = ""
    for lines in file:
        if count == 1:
            key = lines.split()[0]
        elif count == 2:
            TEXT[key] = lines
        elif count == 3:
            count = 0
        count += 1


def write():
    file = open("phrases.txt", "w")
    for key in TEXT.keys():
        file.write(key)
        file.write("\n")
        file.write(TEXT[key])
        file.write("\n")


def main(keyphrase):
    read()
    if keyphrase == 'edit':
        edit()
    elif keyphrase == 'add':
        print("attention: type(n) for new line.")
        add()
    elif keyphrase == 'delete':
        delete()
    elif keyphrase == 'all':
        print_all()
    elif keyphrase == 'keys':
        print_content()
    else:
        get(keyphrase)
    write()
    if(input("Anything else (y/n): ") == 'y'):
        print_content()
        keyphrase = input('WHat else do you want to do: ')
        main(keyphrase)


main(keyphrase)
