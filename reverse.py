text = "this is not a reversed text"

def reverse(m):
    #complete this function so that it takes string x as an input
    #and returns its reverse
    s=m[-1];
    for i in range (-2,-len(m)-1,-1):
        s=s+m[i]
    return s
print("the reversed text is: "+reverse(text))