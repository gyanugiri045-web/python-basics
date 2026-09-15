## using for loop 
l=["rohaan","roshan","shyam","reyan"]

for name in l:
    if(name.startswith("r")):
        print(f"hello {name}")


        # function they work on DRY principle -> dont repeat yourself


## using while loop        
l = ["rohaan", "roshan", "shyam", "reyan"]

i = 0

while i < len(l):
    if l[i].startswith("r"):
        print(f"hello {l[i]}")
    i += 1