import os

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"

    os.makedirs("chapter_9/tables", exist_ok=True)
    with open(f"chapter_9/tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2, 21):
    generateTable(i)