"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""
# This problem was asked by Facebook.


def is_string_pattern_match(text_string, pattern_string):
    """
    Determines if a given text string matches a given pattern string.

    Args:
        text_string (str): The text string to match against.
        pattern_string (str): The pattern string containing literal characters and wildcards.

    Returns:
        bool: True if the text string matches the pattern string, False otherwise.
    """

    # Create a 2D array to store matching status for substrings
    match_status_table = [[False] * (len(pattern_string) + 1)
                          for _ in range(len(text_string) + 1)]

    # Empty string and pattern match by default
    match_status_table[0][0] = True

    # Handle patterns starting with *
    for pattern_index in range(1, len(pattern_string) + 1):
        if pattern_string[pattern_index - 1] == '*':
            match_status_table[0][pattern_index] = match_status_table[0][pattern_index - 2]

    # Dynamic programming to fill the match status table
    for text_index in range(1, len(text_string) + 1):
        for pattern_index in range(1, len(pattern_string) + 1):
            if pattern_string[pattern_index - 1] == text_string[text_index - 1] or pattern_string[pattern_index - 1] == '.':
                match_status_table[text_index][pattern_index] = match_status_table[text_index -
                                                                                   1][pattern_index - 1]
            elif pattern_string[pattern_index - 1] == '*':
                match_status_table[text_index][pattern_index] = \
                    match_status_table[text_index][pattern_index - 2] or \
                    (match_status_table[text_index - 1][pattern_index] and
                     (text_string[text_index - 1] == pattern_string[pattern_index - 2] or pattern_string[pattern_index - 2] == '.'))

    return match_status_table[len(text_string)][len(pattern_string)]


# Examples
print(is_string_pattern_match("ray", "ra."))  # True
print(is_string_pattern_match("raymond", "ra."))  # False
print(is_string_pattern_match("chat", ".*at"))  # True
print(is_string_pattern_match("chats", ".*at"))  # False
