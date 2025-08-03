class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for char in word:
            if char not in current_level:
                current_level[char] = {}
            current_level = current_level[char]
        current_level[self.end_symbol] = True

    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return self.end_symbol in current
 
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)
        current_sorted = sorted(current_level)
        for char in current_sorted:
            if char != self.end_symbol:
                new_prefix = current_prefix + char
                self.search_level(current_level[char], new_prefix, words)
        return words

    def words_with_prefix(self, prefix):
        matching_words = []
        current_level = self.root
        for char in prefix:
            if char not in current_level:
                return matching_words
            current_level = current_level[char]
        self.search_level(current_level, prefix, matching_words)
        return matching_words
  
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                char = document[j]
                if char not in current_level:
                    break
                current_level = current_level[char]
                if self.end_symbol in current_level:
                    matches.add(document[i:j+1])
        return matches

    def longest_common_prefix(self):
        current_level = self.root
        prefix = ''
        while True:
            child = list(current_level.keys())
            if self.end_symbol in child:
                break
            if len(child) == 1:
                prefix += child[0]
                current_level = current_level[child[0]]
            else:
                break
        return prefix

    def advanced_find_matches(self, document, variations):
        matches = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                char = document[j]
                if char in variations:
                    char_to_check = variations[char]
                else:
                    char_to_check = char
                if char_to_check not in current_level:
                    break
                current_level = current_level[char_to_check]
                if self.end_symbol in current_level:
                    matches.add(document[i:j+1])
        return matches
