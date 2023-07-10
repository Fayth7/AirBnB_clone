#!/usr/bin/python3
"""Defines the HBnB console."""

import sys

# Function to handle the commands
def process_command(command):
    # Implement your logic to handle different commands
    if command == 'help':
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")
    elif command == 'quit':
        sys.exit()

# Interactive mode
if sys.stdin.isatty():
    while True:
        command = input("(hbnb) ")
        process_command(command)

# Non-interactive mode
else:
    for line in sys.stdin:
        command = line.strip()
        process_command(command)
