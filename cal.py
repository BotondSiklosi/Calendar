import sys

import ui
#  printing data, asking user for input
import storage
# saving and loading files

MEETING_TITLE = 0
HOW_LONG = 1
STARTING_TIME = 2


def edit_meeting(table, items_to_edit):
    new_line = []
    new_line_option_list = ["Enter a new meeting title", "Enter a new duration in hours (1 or 2)", "Enter a new start time"]
    for i in range(len(table)):
        if items_to_edit == table[i][STARTING_TIME]:
            new_line = ui.get_input(new_line_option_list, "Edit an existing meeting")
            table[i] = new_line
            storage.write_file_from_table("meetings.txt", table)
    return table


def valid_time_error(items_to_add, table):
    work_starts = 8
    work_ends = 18
    if int(items_to_add[STARTING_TIME]) + int(items_to_add[HOW_LONG]) > work_ends:
        return True
    if int(items_to_add[STARTING_TIME]) < work_starts:
        return True
    else:
        return False


def already_used_time(items_to_add, table):
    for i in table:
        if items_to_add[STARTING_TIME] == i[STARTING_TIME]:
            return True
        if i[HOW_LONG] == "2":
            if int(items_to_add[STARTING_TIME]) == (int(i[STARTING_TIME]) + 1):
                return True
        else:
            return False


def too_long_meeting(items_to_add, table):
    for i in table:
        if items_to_add[HOW_LONG] == "1" or items_to_add[HOW_LONG] == "2":
            return False
    return True


def schedule_new_meeting(table):
    labels_title = ["Enter meeting title", "Enter duration in hours (1 or 2)", "Enter start time"]
    while True:
        items_to_add = ui.get_input(labels_title, "Schedule a new meeting.")
        if valid_time_error(items_to_add, table) == True:
            ui.print_error_message("Meeting is outside of your working hours (8 to 18)!")
            continue
        if already_used_time(items_to_add, table) == True:
            ui.print_error_message("Meeting overlaps with existing meeting!")
            continue
        if too_long_meeting(items_to_add, table) == True:
            ui.print_error_message("Duration is out of range!")
            continue
        else:
            table.append(items_to_add)
            storage.write_file_from_table("meetings.txt", table)
            return table


def cancel_existing_meeting(table):
    labels_title = ["Enter the start time"]
    while True:
        inputs = ui.get_input(labels_title, "Cancel an existing meeting.")
        item_to_delete = inputs[0]
        if any(item_to_delete in i for i in table):
            for i in table:
                if i[STARTING_TIME] == item_to_delete:
                    table.remove(i)
                    storage.write_file_from_table("meetings.txt", table)
                    return table
        else:
            ui.print_error_message("There is no meeting starting at that time!")


def handle_menu():
    options = ["schedule a new meeting", "cancel an existing meeting", "edit an existing meeting"]
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

    if options == "e":
        starting_time_input = ui.get_input(["Which meeting would you like to edit (starting time)"], "")
        items_to_edit = starting_time_input[0]
        edit_meeting(table, items_to_edit)

    if options == "q":
        sys.exit(0)

    else:
        ui.print_error_message("There is no such option.")


def main():
    while True:
        try:
            main_menu()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()
