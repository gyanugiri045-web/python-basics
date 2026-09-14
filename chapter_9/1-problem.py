f= open("chapter_9/poem.txt","r")
content=f.read()
if ("hello " in content):
    print("The word hello is contained in the content")

else:
    print("The word hello is not contained in the content.")

f.close()