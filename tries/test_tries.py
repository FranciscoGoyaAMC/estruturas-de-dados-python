from tries import Trie


def test_add_and_exists():
    trie = Trie()
    trie.add("hello")
    trie.add("help")
    trie.add("hi")

    assert trie.exists("hello") is True
    assert trie.exists("help") is True
    assert trie.exists("hi") is True
    assert trie.exists("hel") is False
    assert trie.exists("hey") is False


def test_words_with_prefix():
    trie = Trie()
    words = ["dev", "developer", "development", "devops", "design", "data"]
    for w in words:
        trie.add(w)

    result = trie.words_with_prefix("dev")
    expected = ["dev", "developer", "development", "devops"]
    assert sorted(result) == sorted(expected)

    assert trie.words_with_prefix("x") == []
    assert trie.words_with_prefix("") == sorted(words)  # empty prefix returns all words


def test_find_matches():
    trie = Trie()
    words = ["dev", "developer", "data", "hi"]
    for w in words:
        trie.add(w)

    doc = "developerdataisimportant"
    matches = trie.find_matches(doc)
    expected = {"dev", "developer", "data"}
    assert matches == expected


def test_longest_common_prefix():
    trie = Trie()
    for w in ["flower", "flow", "flight"]:
        trie.add(w)
    assert trie.longest_common_prefix() == "fl"

    trie2 = Trie()
    for w in ["dog", "racecar", "car"]:
        trie2.add(w)
    assert trie2.longest_common_prefix() == ""


def test_advanced_find_matches():
    trie = Trie()
    for w in ["darnit", "bad", "hello"]:
        trie.add(w)

    doc = "This is a d@rn1t test with b@d words!"
    variations = {'@': 'a', '1': 'i', '4': 'a', '!': 'i'}

    matches = trie.advanced_find_matches(doc, variations)
    expected = {"b@d", "d@rn1t"}
    assert matches == expected


if __name__ == "__main__":
    test_add_and_exists()
    test_words_with_prefix()
    test_find_matches()
    test_longest_common_prefix()
    test_advanced_find_matches()
    print("Todos os testes passaram!")
