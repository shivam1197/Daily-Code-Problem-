"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

"""
# This problem was asked by Microsoft.


def wordBreakUtil(s, word_dict, memo):
    if s in memo:
        return memo[s]

    if not s:
        return []

    result = []
    for word in word_dict:
        if s.startswith(word):
            remaining_str = s[len(word):]
            if remaining_str == '':
                result.append(word)
            else:
                remaining_words = wordBreakUtil(remaining_str, word_dict, memo)
                if remaining_words is not None:
                    result.append(word)
                    result.extend(remaining_words)
                    break

    memo[s] = result if result else None
    return memo[s]


def wordBreak(s, word_dict):
    memo = {}
    reconstructed = wordBreakUtil(s, word_dict, memo)
    return reconstructed if reconstructed else None


# Example usage:
dictionary1 = {'quick', 'brown', 'the', 'fox'}
sentence1 = "thequickbrownfox"
result1 = wordBreak(sentence1, dictionary1)
print(result1)

dictionary2 = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
sentence2 = "bedbathandbeyond"
result2 = wordBreak(sentence2, dictionary2)
print(result2)
