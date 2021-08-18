'''
def showMe():
  print("Hello world")
  
showMe()
'''
'''
def welcome(name):
  print(f"Hello {name}")

welcome("Yarzar")
'''
'''
import random
def checkRam(nam):
  if nam==1:
    return "Hello Yarzar"
  elif nam==2:
    return "Hello Messi"
  elif nam==3:
    return "Hello Ronaldo"
  else:
    return "Hello World"

namber=random.randint(1,5)
ans=checkRam(namber)
print(ans)
'''
# global scope
def myFun():
  global nam
  nam=77769

myFun()
print(nam)
    
    
    
    




