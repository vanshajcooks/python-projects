
# defining a list of questions
questions = [{"question": "What is 2+2?", "options": ["2", "3", "4", "5"], "answer": "4"},{"question": "What is 2+3?", "options": ["2", "3", "4", "5"], "answer": "5"},{"question": "What is 2+4?", "options": ["2", "3", "4", "6"], "answer": "6"},{"question": "What is 2+5?", "options": ["2", "3", "5", "7"], "answer": "7"}]


def ask_ques():
    a = input("Do you wanna start? (y/n): ")
    if a.lower() == "y":
        count = 0 
        for question in questions:
            a = str(input(question["question"]))
            if a == question["answer"]:
                count+=1 
        print(f"Damn! you got {count} answers correct")
    if a.lower() == "n":
        ask_ques()

ask_ques()

        
    
    


