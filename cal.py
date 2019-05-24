
import sys
import ui
#  printing data, asking user for input
import storage
# saving and loading files


def schedule_new_meeting(table):
    labels_title = ["Enter meeting title", "Enter duration in hours (1 or 2)", "Enter start time"]
    inputs = ui.get_input(labels_title, 'Your choise: s')



def cancel_existing_meeting(table):
    pass


def handle_menu():
    options = ["schedule a new meeting", "cancel an existing meeting"]
    ui.print_menu("Menu", options, "quit")


def main_menu():
    while True:
        table = storage.get_table_from_file(".txt")
        inputs = ui.get_input(["Please chose an option"], "")
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
        handle_menu()
        try:
            main_menu()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == "__main__":
    main()