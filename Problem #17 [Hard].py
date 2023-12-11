"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period."""

# This problem was asked by Google.


# def length_longest_path(input_string):
#     stack = []  # Stack to track path lengths at different levels
#     max_length = 0
#     segments = input_string.split('\n')  # Split the input by '\n'

#     for segment in segments:
#         level = segment.count('\t')  # Calculate the depth level
#         while len(stack) > level:
#             stack.pop()  # Remove paths deeper than the current level

#         if '.' in segment:  # Check if it's a file
#             path_length = (stack[-1] if stack else 0) + \
#                 len(segment) - level  # Calculate the path length
#             max_length = max(max_length, path_length)
#         else:
#             path_length = (stack[-1] if stack else 0) + \
#                 len(segment)-level+1  # Add 1 for the '/'
#             # Add the path length at this level to the stack
#             stack.append(path_length)

#     return max_length
def length_longest_path(input_string):
    max_length = 0
    level_lengths = {0: 0}  # Dictionary to store the length at each level

    for segment in input_string.split('\n'):
        level = segment.count('\t')  # Calculate the depth level
        name_length = len(segment) - level  # Length of the name without '\t'

        if '.' in segment:  # Check if it's a file
            # Get length at previous level or default to 0
            path_length = level_lengths.get(level - 1, 0) + name_length
            max_length = max(max_length, path_length)
        else:
            # Get length at previous level or default to 0 and add 1 for '/'
            level_lengths[level] = level_lengths.get(level-1, 0)+name_length+1

    return max_length


input_string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
result = length_longest_path(input_string)
print(result)  # Output: 32
