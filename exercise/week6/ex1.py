def find_anagrams(f):
    words = [word.rstrip() for word in f]

    # Initialize variables
    anagrams = []
    selected_words = []
    base_words = {}
    most_count = 0

    for word in words:
        base_chars = str(sorted(list(word)))
        if base_chars not in base_words:
            base_words[base_chars] = 1
        else:
            base_words[base_chars] += 1

    for word in base_words:
        if base_words[word] > most_count:
            most_count = base_words[word]

    for word in words:
        for base_word in base_words:
            if base_words[base_word] == most_count:
                if str(sorted(list(word))) == base_word:
                    selected_words.append(word)
                    base_words[base_word] = 0

    for i in range(len(selected_words)):
        anagram = []
        for word in words:
            if str(sorted(list(word))) == str(sorted(list(selected_words[i]))):
                anagram.append(word)
                if anagram not in anagrams:
                    anagrams.append(anagram)

    return anagrams