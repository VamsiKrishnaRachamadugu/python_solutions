def remove_space_join(str):
    li = str.split(' ')
    recover = ''.join(li)
    print recover


def remove_space_replace(str):
    print str.replace(' ', '')


quote = 'How is it possible?'
remove_space_join(quote)
remove_space_replace(quote)
