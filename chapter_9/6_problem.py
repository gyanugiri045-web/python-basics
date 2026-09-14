with open("chapter_9/tables/log.txt") as f:
    content=f.read()

if("python" in content):
    print("yes python is present")
else:
    print("No python is not present")
