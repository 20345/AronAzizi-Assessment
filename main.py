
while True:
  try:
    name = input("What is your name? ")
    if name.isalpha():
      break
  except ValueError:
    print("Invalid Name ")


print("""Hello {}, welcome to this general knowledge quiz,
you will go through a variety of 
10-20 questions ranged from easy to difficult as you progress. \n
You will receive 1 point for every question you get right! 
These points will be added up and will display your final score
at the end of the quiz.
This will determine your level of intelligent
in your knowledge of General Knowledge""".format(name))
print("   ")

e = print #experiment code
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

questions = { 'Question 1: Machu Picchu is located in which country? \n a: Brazil \n b: Peru \n c: Costa Rica \n d: Philippines \n \n' : 'b' , 'Question 2: What is the biggest bone in the body? \n a: Femur \n b: Tibula \n c: Pectoralis Major  \n d: Ulna \n' :  'a' , 'Question 3: What is the largest muscle in the body? \n a: Gastrocnemius \n b: Latissimus Dorsi \n c: Brachioradialis \n d: Gluteus Maximus \n' : 'd' }

score = 0 
for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        print(" \n Correct!")
        score +=1
    else:
        print(" \n You're Wrong!")

print("Congrats! you got " + str(score) + " out of 20 right!")
      
