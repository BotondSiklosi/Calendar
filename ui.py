def print_menu(title, list_options, exit_message):
    print(title + ": ")
    for i in range(len(list_options)):
        print("(" + list_options[i][0] + ") " + list_options[i])
    print("(q) " + exit_message)


def get_input(list_labels, title):
    print(title)
    input_list = []
    for i in range(len(list_labels)):
        input_list.append(input(list_labels[i] + ": "))
    return input_list

def print_error_message(message):
    print(message)