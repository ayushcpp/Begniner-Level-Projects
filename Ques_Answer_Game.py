# This is absolutely made by me HAHAHA 
# I am BEST HAHAHHAAHA

import random

def ques(user_question,i):
    print(f"Ques{i}:{user_question}")

def ANS(user_ans,num,answer):
    if user_ans==answer[num]:
        return 1
    return 0

def main():
    DICT = {
        "int": "Which data type is used to store whole numbers in Python?",
        "float": "Which data type is used to store decimal numbers in Python?",
        "str": "Which data type is used to store text in Python?",
        "list": "Which data type stores ordered and changeable collection of items?",
        "tuple": "Which data type stores ordered but immutable items?",
        "dict": "Which data type stores data in key-value pairs?",
        "set": "Which data type stores unique unordered elements?",
        "len()": "Which function is used to find the length of an object?",
        "type()": "Which function is used to check the data type of a variable?",
        "import random": "How do you import the random module in Python?",
        "random.randint()": "Which function generates a random integer within a given range?",
        "append()": "Which list method is used to add an element at the end?",
        "upper()": "Which string method converts text to uppercase?",
        "pop()": "Which method removes and returns an element from a list?",
        "keys()": "Which dictionary method returns all keys?"
    }

    answer = list(DICT.keys())
    check =-1
    Total_Ques=15
    correct_ans=0

    question = list(DICT.values())
    for i in range(1,len(DICT)+1):
        num=random.randint(0,14)
        while(num==check):
            num=random.randint(0,14)
        user_question=question[num]
        ques(user_question,i)
        ans=input("Enter Ans:")
        user_ans=ans.lower().strip().replace("()","")
        if ANS(user_ans,num,answer):
            print("Your answer is correct")
            correct_ans+=1
        else:
            print("Your Answer is incorrect")
            print(f'correct Ans:{answer[num]}')
        
        print("\n")
    
    print(f"You Scored :{correct_ans}/{Total_Ques}")

    

if __name__=="__main__":
    main()
        