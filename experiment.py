questions = { 'Question one \n a: answer a\n b: answer b\n c: answer c\n' : 'a' , 'Question 2\n a: answer a\n b: answer b\n c: answer c \n' :  'b' , 
             'Question 3 \n a: answer a\n b: answer b\n c: answer c \n' : 'c' }

for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        print("Correct!") 
    else:
        print("You're Wrong!")


    user_answer = input(key).lower().strip()



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
