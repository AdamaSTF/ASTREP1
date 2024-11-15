#asking user input in celsius 
c = float(input("Enter temperature in celsius "))
def f_to_c (c) :
    return (c *9/5) +32
f = f_to_c(c)
print (f"{c} celsius is equal to {f} fahrenheit.")
