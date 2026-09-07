marks={
    "ram":34,
    "shyam":44,
    "reyan":99
}

print(marks.items())      #print all the list in key value pair

print(marks.keys())       #print keys of marks 

print(marks.values())     #print values of keys

print(marks.get("ram"))   #give none wen there is no key 
print(marks["ram"])       #give error when there is no key 