# class Student:
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print("your personal detail=",firstname,lastname)
    
    
    
#     @staticmethod
#     def contact_detail(mobil_no,rollno):
#         print("your contact detail=", mobil_no,rollno)
    
# Student.get_personal_detail("prashant","jha")
# Student.contact_detail(5548554,101)

#==================================================================
#Inheritance

# class College:
#     def college_name(self):
#         print("Modern College")
        
# class Student(College):
#     def student_info(self):
#         print("Name:  Prashant Jha")
#         print("Branch: Mechanical")
        
# obj = Student()
# obj.college_name()
# obj.student_info()


# class College:
#     def college_name(self):
#         print("Modern College")
        
# class Student(College):
#     def student_info(self):
#         print("Name:  Prashant Jha")
#         print("Branch: Mechanical")
        
# class Exam(Student):
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-language")
# obj = Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

# Parent Class 1
# class SubjMarks:

#     math = int(input("Enter marks of Math: "))
#     DE = int(input("Enter marks of Design Engineering: "))
#     c = int(input("Enter marks of C Language: "))
#     english = int(input("Enter marks of English: "))


# # Parent Class 2
# class PractMarks:

#     cpract = int(input("Enter practical marks of C Language: "))


# # Child Class
# class Result(SubjMarks, PractMarks):

#     def total(self):

#         if (self.math >= 40 and
#             self.DE >= 40 and
#             self.c >= 40 and
#             self.english >= 40 and
#             self.cpract >= 20):

#             print("Pass")

#         else:
#             print("Fail")


# # Object Creation
# obj = Result()

# # Method Call
# obj.total()

# Polymorphism

# class RBI:
#     def home_loan(self):
#         print("Home Loan ROI = 8%")

#     def education_loan(self):
#         print("Education loan = 9%")

# class SBI(RBI):
#     def education_loan(self):
#         print("Education loan = 10%")

# obj = SBI()
# obj.education_loan()


#constructor overriding
# class RBI:
#    def __init__(self):
#         print("Parent class constructor")
# class SBI(RBI):
#    def __init__(self):
#        print("Child class constructor")
       

# obj = SBI()


