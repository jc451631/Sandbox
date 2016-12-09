__author__ = 'jc451631'
"""
"""
valid = False
while not valid:
    name = input("Enter your name:")
    if name != "" and not name.inspace() :
      valid = True
      print(valid)

l = len(name)
for i in range(0,1,2):
    print(name[i])