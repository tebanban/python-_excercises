name= "World"
line = ""
spaces= ""

print( "+" + name + "+")

for character in name:
    spaces += " "
    
for character in name:
    line= (character + spaces + character)
    print(line)
    

print( "+" + name + "+")

# expect:
# +World+
# W     W
# o     o
# r     r
# l     l
# d     d
# +World+