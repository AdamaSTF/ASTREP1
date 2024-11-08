n= int(input("enetr a non-negative number "))
if n <= 0:
  print ("invalied number, please try again!!1")
else:
    x=1
    factorial=1
while x <= n:
  factorial= factorial * x
  print (x, ":" , factorial)
