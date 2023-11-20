"""Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries."""

# class AutocompleteSystem:
#     def __init__(self, strings):
#         self.dictionary = {}
#         for string in strings:
#             self._add_string_to_dict(string)
    
#     def _add_string_to_dict(self, string):
#         for i in range(1, len(string) + 1):
#             prefix = string[:i]
#             if prefix not in self.dictionary:
#                 self.dictionary[prefix] = []
#             self.dictionary[prefix].append(string)
    
#     def autocomplete(self, query):
#         if query in self.dictionary:
#             return self.dictionary[query]
#         else:
#             return []

# autocomplete_system = AutocompleteSystem(["dog", "deer", "deal"])

# suggestions = autocomplete_system.autocomplete("d")
# print(suggestions)  # Output: ['deer', 'deal']

# suggestions = autocomplete_system.autocomplete("cat")
# print(suggestions)  # Output: []


#Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class AutocompleteSystem:
    def __init__(self, dictionary):
        self.root = TrieNode()
        self.build_trie(dictionary)

    def build_trie(self, dictionary):
        for word in dictionary:
            self.insert_word(word)

    def insert_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def find_words(self, node, prefix):
        result = []
        if node.is_word:
            result.append(prefix)
        for char, child in node.children.items():
            result.extend(self.find_words(child, prefix + char))
        return result

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self.find_words(node, prefix)


# Example usage:
dictionary = ["dog", "deer", "deal"]
autocomplete_system = AutocompleteSystem(dictionary)

prefix = "de"
suggestions = autocomplete_system.autocomplete(prefix)
print(suggestions)  # Output: ['deer', 'deal']
