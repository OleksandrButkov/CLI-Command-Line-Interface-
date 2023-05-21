CONTACTS = {}  # Словник для збереження контактів


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No contact found."
        except ValueError:
            return "Invalid input. Give me name and phone please."
        except IndexError:
            return "Invalid input. Give me name please."
    return inner


@input_error
def handle_hello():
    return "How can I help you?"


@input_error
def handle_add(input_str):
    name, phone = input_str.split(' ', 1)
    CONTACTS[name] = phone
    return "Contact added successfully."


@input_error
def handle_change(input_str):
    name, phone = input_str.split(' ', 1)
    CONTACTS[name] = phone
    return "Phone number updated successfully."


@input_error
def handle_phone(input_str):
    if input_str not in CONTACTS:
        raise IndexError
    return CONTACTS[input_str]


@input_error
def handle_show_all():
    if not CONTACTS:
        return "No contacts found."
    else:
        result = ""
        for name, phone in CONTACTS.items():
            result += f"{name}: {phone}\n"
        return result


def main():
    while True:
        command = input("Enter a command: ").lower()
        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print(handle_hello())
        elif command.startswith("add"):
            print(handle_add(command[4:]))
        elif command.startswith("change"):
            print(handle_change(command[7:]))
        elif command.startswith("phone"):
            print(handle_phone(command[6:]))
        elif command == "show all":
            print(handle_show_all())
        else:
            print("Invalid command. Please try again.")


if __name__ == '__main__':
    main()
