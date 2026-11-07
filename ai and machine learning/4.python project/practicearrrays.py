x = float(input("enter tthe number"))
even_number= []
odd_nummber = []
for i in range (1,x):
    if i%2 ==0:
      even_number.append(i)
    else:
        odd_nummber.append(i)
print("Odd",odd_nummber)

