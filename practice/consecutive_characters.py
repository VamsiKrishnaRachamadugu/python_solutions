def consecutive(s):
    i = 0
    while i < len(s) - 1:

        # Counting occurrences of s[i]
        count = 1

        while s[i] == s[i + 1]:

            i += 1
            count += 1

            if i + 1 == len(s):
                break
            print str(s[i]) + str(count), ''

        i += 1


s1 = 'aasdadsssaSaaa'
consecutive(s1)
