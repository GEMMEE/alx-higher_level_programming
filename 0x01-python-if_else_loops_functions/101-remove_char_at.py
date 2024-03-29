#!/usr/bin/python3


def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character at index n,

    str: the string
    n: the position
    """
    if n >= 0:
        return str[:n] + str[n+1:]
    else:
        return str
