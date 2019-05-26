import os

# TABLE CONSTANS
MEETING_TITLE = 0
HOW_LONG = 1
STARTING_TIME = 2


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
    print("ERROR: " + message)


def print_table(title, table):
    l_table = len(table)
    for i in range(0, l_table):
        for j in range(0, l_table-i-1):
            if (table[j][1] > table[j + 1][1]):
                tempo = table[j]
                table[j] = table[j + 1]
                table[j + 1] = tempo
    print(title, ":")
    if os.stat("meetings.txt").st_size == 0:
        print("(empty)")
        print()
    else:
        for i in table:
            print(i[STARTING_TIME] + " - " + str(int(i[STARTING_TIME]) + int(i[HOW_LONG])) + " " + i[MEETING_TITLE])
        print()
    return table
