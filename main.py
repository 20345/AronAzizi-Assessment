#Name input system system with error handling
while True:
  try:
    name = input("What is your name? ")
    if name.isalpha():
      break
  except ValueError:
    print("Please enter a valid name ")

#Input of instructions and steps for the quiz
print("""Hello {}, welcome to this general knowledge quiz,
you will go through a variety of 
5-15 questions ranged from easy to difficult as you progress. \n
You will receive 1 point for every question you get right! 
These points will be added up and will display your final score
at the end of the quiz.
This will determine your level of intelligent
in your knowledge of General Knowledge""".format(name))
print("   ")

#Age input system with error handling
while True:
      try:
          age = input("Before you begin, please enter your age ")
          age = int(age)
          break
      except ValueError:
          print("Invalid age")


#Final message before starting the quiz
print("Good luck and I hope you enjoy {}!".format(name))

print (" ")

#Quetions collection
questions = { 'Question 1: Machu Picchu is located in which country? \n a: Brazil \n b: Peru \n c: Costa Rica \n d: Philippines \n \n' : 'b' , 'Question 2: What is the biggest bone in the body? \n a: Femur \n b: Tibula \n c: Pectoralis Major  \n d: Ulna \n' :  'a' , 'Question 3: What is the largest muscle in the body? \n a: Gastrocnemius \n b: Latissimus Dorsi \n c: Brachioradialis \n d: Gluteus Maximus \n' : 'd' , 'Question 4: What is the biggest mammal to ever live? \n a: Titanosaur \n b: Argentinosaurus \n c: Mammoth \n d: Blue Whale \n' : 'd' , 'Question 5: What is the smallest planet in our solar system? \n a: Venus \n b: Mars \n c: Jupiter \n d: Neptune \n e: Saturn \n f: Mercury \n g: Earth \n h: Uranus \n' : 'f' , 'Question 6:'}

#Score system with accurate precision
score = 0
for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        print(" \n Correct!")
        score +=1
    else:
        print(" \n You're Wrong!")

print("Congrats! you got " + str(score) + " out of (20) right!")
      
