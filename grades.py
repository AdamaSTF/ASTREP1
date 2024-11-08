student_mark= int(input("what is the student mark? "))

if 70 <= student_mark <= 100:
    print ("the student grade is A")
elif  60 <= student_mark <= 69:
    print ("the student grade is B")
elif  50 <= student_mark <= 59:
    print ("the student grade is C")
elif  40 <= student_mark <= 49:
    print ("the student grade is D")
elif  30 <= student_mark <= 39:
    print ("the student grade is E")
elif  20 <= student_mark <= 29:
    print ("the student grade is F")
else:
    print ("invalied mark, please enter again")
