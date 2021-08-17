

x=1      #int
y=2.5   #float
z="Hello" #string 
xy=True   #booleam

#print(f"{x} is int and {y} is float")

#replication
#print(z*5);

#INPUT 
#name=input("whay is your name ")
#print("hello"+name)

#len()
'''
x=[6,8,8,7,8,9]
y="Hello friends I love friends"
#print(f"length is {len(x)}")
print(f"LENGTH IS {len(y)}")
yArr=y.split()
print(yArr);
'''
"""
x=2
y=3.5
print(int(y),float(x))

#break statement
while True:
   nam=input("Your Name : ")
   if nam=="Yarzar":
     break
print("Thank you")
"""
'''
while True:
  nam=input("Please Type ")
  if nam=="lee":
    break
print("Thank You")
'''
'''
import sys
while True:
  nam=input("what is your name : ")
  print(f"Hello {nam} , type exit to exit")
  checkRes=input(" : ")
  if checkRes=="exit":
    sys.exit()
    
print("Bye Bye...")
'''
'''
#loop with for in 
arr=[6,8,6,9,7,8,5,7]
for i in arr:
  if i==5:
    break
  else:
    print(i)

'''
'''
import random
#for in range(start,stop,step value)
for i in range(0,20,4):
  print(f"my name is {i}")

for i in range(20,0,-3):
  print(f" from 20 now is {i}")


for i in range(10):
  print(random.randint(2,6))
'''
'''
#while loop
x=10
while x>0:
  print(f"{x} is still in loop")
  x-=1 
  
'''




