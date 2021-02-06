# GCD of two numbers
a=int(input("Enter first number:"))
b=int(input("Enter the second number:"))
for i in range (1, min(a,b) +1):
  if (a%i==0 and b%i==0): gcd=i
print("GCD of",a,  "and",b,    "is",gcd)