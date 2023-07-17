#!/usr/bin/python3
# returns-tuple_with_length_of_string_and_first_character

def multiple_returns(sentence):
    """Return tuple with the length of a string and first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
