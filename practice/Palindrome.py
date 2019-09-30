def isPalindrome(num):
    temp = num
    result = 0
    while temp > 0:
        result = (result * 10) + temp % 10
        temp /= 10
    if result == num:
        return 'true'
    else:
        return 'false'


num = input("Enter the number")
print  isPalindrome(num)
