
while True:
  try:
    name = input("What is your name? ")
    if name.isalpha():
      break
  except ValueError:
    print("Invalid Name ")


print("""Hello {}, welcome to this general knowledge quiz,
you will go through a variety of 
10-20 questions ranged from easy to difficult as you progress.""".format(name))
print("   ")

e = print #experiement code
while True:
  try:
    age = input("Before you begin, please enter your age ")
    if age.isnumeric():
      break
  except ValueError as e:
    print(e) #experiment
    print("Invalid age")
  except Exception as e: #experiment
    print(e) #experiment
    print("invalid age") #experiment
else: #experiment
  print(e) #experiment

print("Good luck and I hope you enjoy {}!".format(name))

print (" ")

questions = { 'Question 1: Machu Picchu is located in which country? \n a: Brazil \n b: Peru \n c: Costa Rica \n d: Philippines \n \n' : 'b' , 'Question 2: What is the biggest bone in the body? \n a: Femur \n b: Tibula \n c: Pectoralis Major  \n d: Ulna \n' :  'a' , 'Question 3: What is the largest muscle in the body? \n a: Gastrocnemius \n b: Latissimus Dorsi \n c: Brachioradialis \n d: Gluteus Maximus' : 'd' }


for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
      
      print("\n Correct!")
    else:
        print(" \n You're Wrong!")


    user_answer = input(key).lower().strip()