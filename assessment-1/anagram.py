def is_anagaram(str1, str2):
    if len(str1) == len(str2):
        s1_list = list(str1.lower())
        s2_list = list(str2.lower())
        # for i in range(len(str1)):
        #     s1_list.append(str1[i])
        #     s2_list.append(str2[i])
        s1_list.sort()
        s2_list.sort()
        count = 0
        for i in range(len(s1_list)):
            if s1_list[i] == s2_list[i]:
                count = count + 1
            else:
                break
        if len(s1_list) == count:
            return True
        else:
            return False
    else:
        return False


is_anagaram('Dad', 'Add')
