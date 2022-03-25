
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
print("     ")


while True:
  try:
    age = input("Before you begin, please enter your age ")
    if age.isnumeric():
      break
  except ValueError:
    print("Invalid age")
print(" ")
print("Good luck and I hope you enjoy {}!".format(name))
print (" ")

questions = { 'Two plus two \n a: 3 a\n b: 4 b\n c: 2 c\n' : 'a' , 'Question 2\n a: answer a\n b: answer b\n c: answer c \n' :  'b' , 
             'Question 3 \n a: answer a\n b: answer b\n c: answer c \n' : 'c' }


for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        print("Correct!") 
    else:
        print("You're Incorrect!")


    user_answer = input(key).lower().strip()