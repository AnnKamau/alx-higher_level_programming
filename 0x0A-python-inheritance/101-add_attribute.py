#!/usr/bin/python3
"""Define a function that adds attributes to objjects."""

def add_attribute(obj, att, value):
    """Adds a new atrribute to an object is possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: if the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
