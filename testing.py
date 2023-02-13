def surround(string, sides):
     return sides + string + sides
     
def alert(string, level):
    string = surround(string, " ")
    for i in range(level):
        string = surround(string, "!")
    return  string 
    

assert_equal(alert("Warning", 2), "!! Warning !!")
assert_equal(alert("DANGER", 4), "!!!! DANGER !!!!")