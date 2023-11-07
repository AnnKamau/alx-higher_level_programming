#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends a string to the end of the UTF8 text file.

    Args:
        filename (str): The name of the file to append.
        text (str): The string to append to file.
    Returns:
        The number characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
