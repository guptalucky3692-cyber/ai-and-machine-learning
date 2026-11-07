# #exception handling
a = int(input("enter the number:"))
try:
    print(10/a)
except Exception as err:
    print(f"sorry there is an err as {err}")
except (ValueError,TypeError) as err:
   print("enter a valid numbers")
else:
    print("there is no exception")
finally:
    print("i will run no matter what")
print("devison by zero")

# age =  float(input("enter the age"))
# try:
#    if age <10 or age>18:
#       raise ValueError("your age`s is not requaired club")
#    else: 
#        print("Welcome to the club")
# except Exception as err:
#    print(f" an error is occuired as{err}")
# print("the club will start soon")
# # File handling
# p = open("3.python AI & ML/1.ai & ml .py")
# print(p.read())

 


