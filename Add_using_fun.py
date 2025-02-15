# Variable length arguments >> when you dont know the No of arguments 

def sum (*args):
    s = 0
    for i in args :
        s = s+1
        return s 
    else :
        print ("end")
    
print (sum (1,2,3))  #output 3