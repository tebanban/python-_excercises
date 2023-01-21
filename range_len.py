string1 = 'World'
string2 = 'Goodbye'
length1 = len(string1)
length2 = len(string2)
length = 0

if len(string1) < len(string2):
    length = length2
else:
    length = length1
    
for i in range(length):
    if i < length1:
        char1 = string1[i]
    else:
        char1 = ' '
    if i < length2:
        char2 = string2[i]
    else:
        char2 = ' '
        
    print(char1 + "   " + char2)

# Expect

# W   G
# o   o
# r   o
# l   d
# d   b
#     y
#     e

