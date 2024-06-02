studentName = str(input("Enter your name :   "))
Javascript = int(input("Enter your Javascript Marks:   "))
Typescript = int(input("Enter your Typescript Marks:   "))
Python = int(input("Enter your Python Marks:   "))
CSharp = int(input("Enter your C# ( C Sharp )  Marks:   "))
CloudComputing = int(input("Enter your Cloud Computing Marks:   ")) 


Subtotal = Javascript + Typescript + Python + CloudComputing + CSharp
TotalMarks = 100

Average = Subtotal / 500
Percentage = (Average) * 100

print(f"\n\tHello {studentName}!\n")
print(f"\tYou obtained {Javascript} marks in Javascript")
print(f"\tYou obtained {Typescript} marks in Typescript")
print(f"\tYou obtained {Python} marks in Python")
print(f"\tYou obtained {CSharp} marks in C#")
print(f"\tYou obtained {CloudComputing} marks in CloudComputing")
print(f"\n\tYour Percentage is {Percentage:.2f}\n\n")




if Percentage >= 80:
    print (f"\n\tYou get A-1 Grade")
elif Percentage >=70 or Percentage <= 79:
    print (f"\n\tYou get A Grade")
elif Percentage >=60 or Percentage <= 69:
    print (f"\n\tYou get B Grade")
elif Percentage >=50 or Percentage <= 59:
    print (f"\n\tYou get C Grade")
elif Percentage >=33 or Percentage <= 49:
    print (f"\n\tYou get D Grade")
else:
    print(f"\n\tYou are failed")