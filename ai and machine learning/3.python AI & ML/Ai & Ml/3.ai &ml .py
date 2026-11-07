# def decorate(func):
#     def wrapper(*a,**k):
#         print("additon")
#         func(*a,**k)
#         print(" your addition is")
#     return wrapper

# @decorate
# def add(a,b):
#     print(f"your answer is{a+b}")

# add(12,34)


# def information(**K): # argument for multiple element
#     print("your information is\n\t")
#     for i in K:
#         print(f"{i}:{K[i]}")

# information(name = "peter" ,age = 23,course = "ai/ml")

## list / dictonary and set comprisons]
# l =[i for i in range(0,12) if i%2==0] #listcomprisons
# print(l)
# l ={i : i**2 for i in range(0,12)} #dictonary comprisions
# print(l)

# #lambda function
addition = lambda a: "even" if a%2 ==0 else "odd"
print(addition(90))
a = [1,2,3,4,5,6,7]
# def multiply(x):
#     return x*2
# result =map(multiply,a)
# print(list(result))


# ##filter function
# a = [12,23,44,55,49]
# result = filter(lambda x: True if x%2==0 else False,a)
# print(list(result))

check = lambda x:'positive' if x>0 else "negative" if x<0 else "zero"
print(check(9))
 
print(check(-6))
a =[1,2,3]
res = map(int)