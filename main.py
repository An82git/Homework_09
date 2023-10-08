
contacts = {}
ERROR_DIC = {"add_IndexError": "Give me name and phone please",
             "change_IndexError": "Give me name and phone please",
             "phone_IndexError": "Enter user name",
             "phone_KeyError": "There is no such name"}

COMMAND_DIC = {"hello": lambda: "How can I help you?",
               "add": lambda name, phone: contacts.update({name.title(): phone}),
               "change": lambda name, phone: contacts.update({name.title(): phone}),
               "phone": lambda name: contacts[name.title()],
               "show all": lambda: contacts,
               "good bye": lambda: "Good bye!",
               "close": lambda: "Good bye!",
               "exit": lambda: "Good bye!"}


def input_error(func):
    def inner(string: str):
        try:
            return func(string)

        except IndexError:
            command_error = pars(string)

            if not command_error:
                return "A non-existent team"
            elif command_error[0] + "_IndexError" in ERROR_DIC:
                return ERROR_DIC[command_error[0] + "_IndexError"]
            return "Unknown error"

        except KeyError:
            command_error = pars(string)

            if command_error[0] + "_KeyError" in ERROR_DIC:
                return ERROR_DIC[command_error[0] + "_KeyError"]
            return "A non-existent team"

    return inner


@input_error
def command_processing(string: str):
    string_list = pars(string)
    command = COMMAND_DIC[string_list[0]]

    if string_list[0] in ["add"]:
        return command(string_list[1], string_list[2])
    elif string_list[0] in ["change"]:

        if string_list[1].title() not in contacts:
            return "There is no such name"

        return command(string_list[1], string_list[2])
    elif string_list[0] in ["phone"]:
        return command(string_list[1])
    else:
        return command()


def pars(string: str) -> list:
    string_list = []
    string = string.strip()

    for command in COMMAND_DIC:
        if command in string:
            string_list.append(command)
            string = string.removeprefix(command).strip()

    if string:
        for item in string.split(" "):
            if item[0] in "+0123456789":
                string_list.insert(2, item)
            else:
                string_list.insert(1, item)

    return string_list


def main():
    end_of_program = True

    while end_of_program:
        string = input().lower()

        if string:
            rezult_command = command_processing(string)

            if type(rezult_command) in [str, dict]:
                print(rezult_command)

                if rezult_command == "Good bye!":
                    end_of_program = False

        else:
            end_of_program = False


if __name__ == "__main__":
    main()
