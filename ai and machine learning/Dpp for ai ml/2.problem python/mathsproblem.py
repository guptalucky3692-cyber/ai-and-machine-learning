# # # problems of python

# # if problem1 multipy*, subtract-, additon+ ,devisible/,floordivison//,modulus%,exponention**,
# num1 = int(input(" enter the value num1 =")) 
# num2 = int(input("enter the value num2 ="))
# sum = num1 + num2
# print("the sum of provided two numbers is ",sum)

#  #problem2 square root  
# import math
# x = int(input(" enter the value x= "))
# sr = math.sqrt(x)
# print("the square root of the number is =", sr)

# #problem3 area of trangle
# height =int(input("enter the height of the trangle = "))
# base = int(input("enter the base of the trangle =" ))
# area = (0.5)*base*height 
# print("the area of the trangle" ,area)

# #problem4 even odd numbers
# num = int(input("enter the value"))
# if num % 2 == 0:
#  print("it has be even number")
# else :
#       print(" it is a odd number")

#   # problem 5random numbers
# import random
# num =random.randint(1,10)
# print(num)

# problem 6 cleander
# import calendar
# year =  int(input("enter the year"))
# month = int(input("enter the month"))
# calander = calendar.month(year,month)
# print(calendar.month(year,month))

#  #problem 7 largest numbers 
# num1 = float(input("enter the num1 number ="))
# num2 = float(input("enter the num2 number ="))
# num3 = float(input("enter the num3 number ="))
# if (num1>num2) and (num1>num3):
#     print(num1 , " is a  num1 largest numbers =")
# elif(num2 > num1 ) and (num2 > num3):
#  print(num2 , "is  a  num2 largest number = ")
# else :
#    print(num3 ," is a num3 largest number")

# #problem 8  armstrong numbers 
# num = int(input(" enter the number ="))
# order = len(str(num))
# sum = 0
# temp = num
# while temp>0:
#     digit = temp%10
#     cube = digit **order
#     sum +=  cube 
#     temp //=10
# if sum == num :
#   print("it is a armstrong number ")
# else:
#   print(" it s not a armstrong number ")

# #problem 9  shuffle cards
# import random,itertools
# deck = list(itertools.product(range(1,14),["Spade * ","Club * ","Heart * ","Dimand *"]))
# random.shuffle(deck)
# for i in range (5):
#     print(deck[i][0],"of", deck[i][1])

#  #problem 10 matrix
# x = float(input("enter the number x = "))
# y = float(input("enter the number y = "))
# z = float(input("enter the number z = "))
# w = float(input("enter the number  z ="))
# t = float(input("enter the number t = "))
# r = float(input("enter the number r ="))
# a = [[x,y,z],
#      [w,t,r]]
# T = list(map(list,zip(*a)))
# print(T)

# #problem  11 postive negative number
# num = int(input("enter the number ="))
# if num>0:
#     print("it is a positive number")
# elif num== 0:
#     print("it is a natural number")
# else :
#     num<0
#     print("it is a negativenumber ")

# #problem 12 factorial method 
# def fact(a): #define(def())
#     if a == 0:
#         return 1
#     else :
#         return ((a)*fact(a-1) )
# num  = int(input("enter the number ="))
# result = fact(num)
# print("the factorial of this number",result)

#  # problem13 mini calculater
# num1=  float(input("enter the number num1 ="))
# num2 = float(input("enter the number nu2  ="))
# print("press 1 for addition \npress2 for multiplication \npress3 for divison \npress4 for subtraction")
# choice = int(input("enter the choice from 1-4 ="))
# if choice ==1 :
#     print(num1 + num2)
# if choice ==  2:
#     print(num1 * num2)
# if choice ==3 :
#     print(num1 / num2)
# if choice ==4 :
#     print(num1 - num2)

#  #problem 14 multipication table
# num = int(input("enter the number of num ="))
# for i in range (1,11):
#   print(num,"x",i, "=" ,num*i)

#  #problem15 HCF OR GCD
# def findHCF(x,y):
#     if x>y:
#       smaller = y
#     else :
#        smaller = x
#        for i in range (1,smaller +1):
#         if (x%1 == 0) and (y%1 == 0):
#              hcf = i
#     return hcf
# print("the  hcf of given to numbers is  " ,findHCF(2,2))

#  #problem16 natural number
# num = float(input("enter the number of num = "))
# if num<0 :
#     print(" please enter the  positive number")
# else:
#     sum = 0
#     while num>0:
#      sum += num
#      num -=1 
#     print(sum)

# #problem 17 prime number
# num = int(input('enter the number = '))
# for i in range (2, num) :
#     if num % i == 0:
#      print("it is not a prime number")
#      break
#     else :
#        print(" it is a prime number ")
#        break

#  #problem 18 alphetical order 
# x = input(" enter the wards = ")

# y= x.split()

# for i in range(len(y)):
#     y[i] = y[i].lower()
# y.sort()
# print(y)
 
# # problem 19 image height width
# import PIL
# from PIL import Image
# img = PIL.Image.open("c:/Users/asus/OneDrive/Pictures/Screenshots 1/Screenshot 2026-05-30 005505.png")
# width,height = img.size 
# print(width, "x ", height)
 
#problem 20  copy file 
# from shutil import copyfile 
# copyfile("C:/ Users/asus/OneDrive/Desktop/cscorner/quiz.py","C:/ Users/asus/OneDrive/Desktop/cscorner/quiz.py")

# #problem 21 curency converter
# from currency_converter import CurrencyConverter
# a = CurrencyConverter()
# print(a.convert(1000,"USD","INR"))

# #problem 22 create window 
# import tkinter as tk
# window = tk.Tk()

#problem 23 window me text show 
# window.geometry("500x360")
# window.mainloop()
# from currency_converter import CurrencyConverter
# import tkinter as tk
# a = CurrencyConverter() 
# window = tk.Tk()
# window.geometry("600x460")

# #problem 24 sequence and seires 
# while True:
#     print("========[Sequence And Seires] ========")
#     print("1.AP Sequence")
#     print("2.Sum of AP ")
#     print("3.GP Sequence")
#     print("4.Sum of GP ")
#     print("5.Exit")
#     choice = int(input("enter the choice"))
#     if choice == 1:
#         a = int(input("Enter the first term = "))
#         d = int(input("Enter the comon differnce = "))
#         n = int(input("Enter thre number of terms = "))
#         print("AP sequence =  ")
#         for i in  range(n):
#          print(a+ i*d,end =" ")

#     elif choice == 2:
#         a = int(input("Enter the first term = "))
#         d = int(input("Enter the comon differnce = "))
#         n = int(input("Enter thre number of terms = "))
#         s = n*(2*a + (n-1)*d)/2
#         print("AP sires of sum =",s)
#     elif choice ==3:
#         a = int(input("Enter the first term = "))
#         r = int(input("Enter the comon ratio = "))
#         n = int(input("Enter thre number of terms = "))
#         print("GP sequence =  ")
#         for i in range(n):
#             print(a*(r**i),end ="")
#     elif choice ==4:
#         a = int(input("Enter the first term = "))
#         r = int(input("Enter the comon ratio = "))
#         n = int(input("Enter thre number of terms = "))
#         if r==1:
#             s = a*n
#         else :
#             s = a*(r*n-1)/(r -1)
#         print("GP seires of sum =",s)
#     else:
#         print("invalid choice")

#   #problem 25 diffrention(calculus)
# from sympy import symbols ,diff,simplify
# x = symbols('x')                 #symbols use for sympy   
# expr = input("enter the diirention function = ")
# value = int(input("enter the value of differention ="))
# f = simplify(expr)         #simplify for mathmatmatics expression
# d = diff(f,x)                #diff for diffrenttion
# print("Derivative",d)
# print("Derivative at x =" ,value, ":" ,d.subs(x,value))

# #problem 26 integeration(calculus)
# from sympy import symbols ,integrate,simplify
# x = symbols('x')                 #symbols use for sympy   
# expr = input("enter  function  of integeration = ")
# f = simplify(expr)         #simplify for mathmatmatics expression
# i = integrate(f,x)                #integerate  for integeration
# print("functiom",f)
# print("Integeration" ,i)

 #problem 25 integeration lower and upper limit
# from sympy import symbols ,integrate,simplify
# x = symbols('x') 
# expr = input("enter the  function  of integeration = ")
# a = int(input("enter the lower limit = "))
# b = int(input("enter the upper limit = "))
# f = simplify(expr)
# i = integrate(f,(x,a,b))
# print("the valie of i = ",i)

