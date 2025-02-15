def numeric_value (a):
    n = []
    for i in a :
        if type(i) == int or type(i) == float:
            n.append(i)
        return n
        
print(numeric_value([1,2,3,'a','b','c',"vishal"]))