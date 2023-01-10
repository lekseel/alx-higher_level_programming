#!/usr/bin/python3
""" Module that adds all arguments to a Python list, and then
save them to a file
"""
import sys
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
with open(filename, 'a+') as f:
    pass

try:
    my_list = load_from_json_file(filename)
except ValueError:
    my_list = []
list1 = sys.argv[1:]
my_list += list1
save_to_json_file(my_list, filename)
