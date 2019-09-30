def count_vowels(str):
    vowel_string = 'aeiou'
    count = 0
    for i in str:
        if i.lower() in vowel_string:
            count += 1
    print 'vowel count', count


count_vowels('How is it possible?')
