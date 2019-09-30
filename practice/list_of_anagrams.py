def is_anagram(list_anagrams, word):
    result_list = []
    word_list = list(word)
    word_string = ''.join(sorted(word_list))
    for i in list_anagrams:
        string_list = list(i)
        string = ''.join(sorted(string_list))
        if string == word_string:
            result_list.append(i)
    return result_list


ana_list = ['nagaram', 'add', 'aaangrm']
word = 'anagram'
print(is_anagram(ana_list, word))
