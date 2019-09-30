nameAndAge = input('Enter your full name(firstname and lastname) and age : ')
splittedString = nameAndAge.split()
firstName = splittedString[0]
lastName = splittedString[1]
age = splittedString[2]
print ('First Name:' + firstName)
print ('Last Name:' + lastName)
print ('Age:' + age)
if age >= 18:
    print (firstName + ' is eligible to vote')
else:
    print (firstName + ' is not eligible to vote')
