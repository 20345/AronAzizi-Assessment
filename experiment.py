questions = { 'Question one \n a: answer a\n b: answer b\n c: answer c\n' : 'a' , 'Question 2\n a: answer a\n b: answer b\n c: answer c \n' :  'b' , 
             'Question 3 \n a: answer a\n b: answer b\n c: answer c \n' : 'c' }

for key in questions.keys():
    user_answer=input(key)
    if questions.get(key)==user_answer:
        print("Correct!") 
    else:
        print("You're Wrong!")


Change user answer to lower case and take spaces out
    user_answer = input(key).lower().strip()
