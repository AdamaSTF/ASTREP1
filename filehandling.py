
import this
file = open("student_inputfile.txt", "r")
[("Ismaila, introduction to cyber Security, 75, 40"),
    ("Mamadou, Introduction to operating system, 60, 25"),
     ("Adama, introduction to networking system, 80, 35")
    ]
for row in reader:
    name= row ["Name"]
    unit= row["Unit"]
    mark= float{row["Mark"]}
    weight= float{row["weight"]}


file = open("student_inputfile.txt")
lines = student_inputfile.readlines()
for line in lines:
    print(line)
file.close()
