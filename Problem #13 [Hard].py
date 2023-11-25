"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

# This problem was asked by Amazon.


def longest_substring_with_k_distinct(s, k):
    if k == 0:
        return 0

    max_length = 0
    char_count = {}
    start = 0

    for end in range(len(s)):
        char = s[end]
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# Example usage
s = "abcbaba"
k = 2

print(longest_substring_with_k_distinct(s, k))
