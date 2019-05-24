import sys

import ui
#  printing data, asking user for input
import storage
# saving and loading files

MEETING_TITLE = 0
HOW_LONG = 1
STARTING_TIME = 2


def schedule_new_meeting(table):
    labels_title = ["Enter meeting title", "Enter duration in hours (1 or 2)", "Enter start time"]
    items_to_add = ui.get_input(labels_title, "Schedule a new meeting.")
    table.append(items_to_add)
    storage.write_file_from_table("meetings.txt", table)
    return table


def cancel_existing_meeting(table):
    labels_title = ["Enter the start time"]
    inputs = ui.get_input(labels_title, "Cancel an existing meeting.")
    item_to_delete = inputs[0]
    for i in table:
        if i[STARTING_TIME] == item_to_delete:
            table.remove(i)
    storage.write_file_from_table("meetings.txt", table)
    return table


def handle_menu():
    options = ["schedule a new meeting", "cancel an existing meeting"]
    ui.print_menu("Menu", options, "quit")


def main_menu():
    table = storage.get_table_from_file("meetings.txt")
    ui.print_table("Your schedule for the day", table)
    handle_menu()
    inputs = ui.get_input(["Your choise"], "")
    options = inputs[0]
    if options == "s":
        schedule_new_meeting(table)

    if options == "c":
        cancel_existing_meeting(table)

    if options == "q":
        sys.exit(0)

    else:
        raise KeyError("There is no such option.")


def main():
    while True:
        try:
            main_menu()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
