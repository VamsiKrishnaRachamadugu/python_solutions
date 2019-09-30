def count_vowels(str):
    vowel_string = 'aeiou'
    lower_count = 0
    upper_count = 0
    for i in str:
        if i.lower() in vowel_string:
            if i.islower():
                lower_count += 1
            elif i.isupper():
                upper_count += 1
    print 'Lower vowel count', lower_count
    print 'Lower vowel count', upper_count


count_vowels('How is it possible?')
