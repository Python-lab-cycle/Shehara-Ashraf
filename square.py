#square of n numbers using list  comprehension
print ("enter the limit")
n=int (input())
square= [i * i for i in range(n)]
print("square of n numbers \n",square)