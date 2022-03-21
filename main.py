
while True:
  try:
    name = input("What Is Your Name? ")
    if name.isalpha():
      break
  except ValueError:
    print("Invalid Name ")


print("""Hello {}, Welcome to this General Knowledge Quiz,
you will go through a variety of 
10-20 questions ranged from easy to difficult as you progress.""".format(name))
print(" ")

print("Good luck and I hope you enjoy {}!".format(name))