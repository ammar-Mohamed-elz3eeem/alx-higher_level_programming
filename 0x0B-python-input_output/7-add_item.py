#!/usr/bin/python3
""" script that adds arguemnts to list object """


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    from sys import argv
    FILENAME = "add_item.json"

    try:
        old_list = load_from_json_file(FILENAME)
    except Exception:
        old_list = []

    new_list = old_list + argv[1:]
    save_to_json_file(new_list, FILENAME)
