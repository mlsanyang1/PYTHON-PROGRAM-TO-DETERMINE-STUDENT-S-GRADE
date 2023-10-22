
# ///////////////////////////////////////////////////////////////////////////////////////

# collecting inputs from user's Name and ST Number

user_name = input("Enter Name: \n")
print("Hi!", user_name, "WELCOME TO GOMINDZ ACADEMY GRADING SYSTEM \n")
print("bellow is the grading scheme")
grading_scheme = {"80-100": "A", "70-79": "B", "60-69": "C", "40-59": "PASS", "< 40": "FAIL"}
print(grading_scheme)

# ///////////////////////////////////////////////////////////////////////////////////////

# collecting inputs from user's Assessment score

Student_number = int(input("Enter your student number please: \n"))
assessment_score = int(input("Enter your assignment score: \n"))
if assessment_score >= 80:
    print("dear", user_name, "you have", "A", "in your assignment \n")
elif assessment_score >= 70:
    print("great you have B in your assignment score \n")
elif assessment_score >= 60:
    print("dear", user_name, "you obtained C, in your assignment \n")
elif assessment_score >= 40:
    print("dear", user_name, "you obtained a pass in your assignment \n")
else:
    print("sorry", user_name, "you obtained a fail, a makeup assessment might help \n")

# ///////////////////////////////////////////////////////////////////////////////////////

# collecting inputs from user's Test score
Test_score = int(input("Enter your Test score: \n"))

if Test_score >= 80:
    print("dear", user_name, "you have", "A", "in your Test \n")
elif Test_score >= 75:
    print("great you have B in your Test \n")
elif Test_score >= 60:
    print("hi", user_name, "your have C in your Test \n")
elif Test_score >= 40:
    print("dear", user_name, "you obtained a pass in your Test \n")
else:
    print("sorry", user_name, "you obtained a fail, a make up Test might help \n")

# ///////////////////////////////////////////////////////////////////////////////////////
# collecting inputs from user's Exam score

Exam_score = (int(input("please enter your exam score: \n")))
if Exam_score >= 80:
    print("dear you have A in your Exam \n")
elif Exam_score >= 75:
    print("great you have B in your Exam \n")
elif Exam_score >= 60:
    print("hi", user_name, "your have C in your Exam \n")
elif Exam_score >= 40:
    print("dear", user_name, "you obtained a pass in your Exam\n")
else:
    print("sorry", user_name, "you obtained a fail, a make up Exam might help \n")








