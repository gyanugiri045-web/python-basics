def rem(l, word):
    n=[]
    for item in l:
        if  (item != word):
            n.append(item.strip(word))

    return n 
    
l=["an","shubham","roshan","harry"]
print(rem(l, "an"))