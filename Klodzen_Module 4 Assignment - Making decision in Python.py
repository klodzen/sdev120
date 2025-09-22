name=input("Please enter your name: ")
grade_str=input("Please enter your final grade: ")
grade=int(grade_str)
if grade >= 60:
    print("Hello "+name+", you passed this class.")
else:
    print("Hello "+name+", you failed this class.")
