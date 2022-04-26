#Name input system system with error handling
def name():
  global name
  while True:
      name = input("What is your name? ")
      if name.isalpha():
        break
      else:
       print("Please enter a valid name: ")


#Input of instructions and steps for the quiz
def instructions():
  print("""Hello {}, welcome to
        this general knowledge quiz,
  you will go through 10 questions ranged from easy to difficult as you progress. \n
  You will receive 1 point for every question you get right! 
  These points will be added up and will display your
        final score at the end of the quiz.
  This will determine your level of intelligent
  in your knowledge of General Knowledge""".format(name))
  print("   ")



#Age input system with error handling
def age():
    
  while True:
        try:
            age = input("Please enter your age: \n ")
            age = int(age)
            break
        except ValueError:
            print("Please enter a valid age:")



#Relevant implications reference
def information():
  print("""Additionally, I would like to add, any offensive
  or negative comments or messages is purely
  accidental and it isnt my intention to hurt or insult anyone!""")
#Final message before starting the quiz
  print("Good luck and I hope you enjoy and learn something!")

print (" ")


       
#When adding def questions(): it breaks the program, probably a indent problem, thats why I chose to remove it

#Quetions collection
questions = { 'Question 1: Machu Picchu is located in which country? \n a: Brazil \n b: Peru \n c: Costa Rica \n d: Philippines \n \n' : 'b' , 'Question 2: What is the biggest bone in the body? \n a: Femur \n b: Tibula \n c: Pectoralis Major  \n d: Ulna \n' :  'a' , 'Question 3: What is the largest muscle in the body? \n a: Gastrocnemius \n b: Latissimus Dorsi \n c: Brachioradialis \n d: Gluteus Maximus \n' : 'd' , 'Question 4: What is the biggest mammal to ever live? \n a: Titanosaur \n b: Argentinosaurus \n c: Mammoth \n d: Blue Whale \n' : 'd' , 'Question 5: What is the smallest planet in our solar system? \n a: Venus\n b: Mars \n c: Jupiter \n d: Neptune \n e: Saturn \n f: Mercury \n g: Earth \n h: Uranus \n' : 'f' , 'Question 6: How many hearts does a octopus have? \n a: 2\n b: 1\n c: 3\n d: 4 \n e: 7\n' : 'c' , 'Question 7: How many keys are on a piano? \n a: 60 \n b: 76 \n c: 78 \n d: 80 \n e: 88 \n f: 94 \n g: 102 \n' : 'e' , 'Question 8: How many countries is there? \n a: 193 \n b: 194 \n c: 195 \n d: 196 \n e: 197 \n f: 200 \n g: 204 \n' : 'c' , 'Question 9: What is the population as of 2022? \n a: 7,657,556,952 \n b: 7,939,469,726 \n c: 7,745,359,242 \n d: 7,839,297,247 \n e: 8,031,985,239 \n f: 7,691,485,978 \n g: 7,758,298,127 \n' : 'b' , 'Question 10: Which country has the highest life expectancy? \n a: New Zealand \n b: Switzerland \n c: Japan \n d: Iceland \n e: Spain \n f: Italy \n g: Norway \n h: Hong Kong \n i: Cyprus \n j: Nepal \n' : 'h' }


#Score system
def score():
  score = 0
  for key in questions.keys():
      user_answer=input(key)
      if questions.get(key)==user_answer:
          print(" \n Correct!")
          score +=1
      else:
          print(" \n You're Wrong!")
  
  print("Congrats! you got " + str(score) + " out of (10) right! Thank you for participating in my quiz and I hope you enjoyed!")



#when program starts
name()
instructions()  
age()
information()
score()
