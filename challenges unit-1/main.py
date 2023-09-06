print ("FACTORIAL CALCULATOR")
def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)
x=int(input("Enter The Number:"))
y=factorial(x)
print("THE FACTORIAL OF",x,"IS",y)