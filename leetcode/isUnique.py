# implement an algorith to determine if a string a has all unique characters.
# what if you cannot use additional data structure

# i.e 'string' -> unique coz no repeating char; 'hello' not unique coz its repeating 'l's

""" string1 = 'string'
string2 = 'hello'

unique = []

uniqueBool = True

for x in string2:
    # print(x)
    if x not in unique:
        unique.append(x)
    elif x in unique:
        uniqueBool = False

print('String is unique?: {bool}'.format(bool=uniqueBool)) """
str1 = 'hello'
str2 = 'mike'

unique = True
uniqueChar = []
index = 0
for x in str2:
    # print(x)
    if x not in uniqueChar:
        uniqueChar.append(x)
        unique = True
    elif x in uniqueChar:
        unique = False


print(unique)
