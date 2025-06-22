import os

tasks = [] # empty task list



#load file
def load_tasks():
    if not os.path.exists("tasks.txt"):
        return []
    with open("tasks.txt","r") as file:
        lines = file.readlines()
        return [line.strip() for line in lines]

#save file
def save_tasks():
    with open("tasks.txt","w") as file:
        file.writelines(task +"\n" for task in tasks)




#adding a task
def add_task():
    a = input("Task to be added: ")
    tasks.append(a)
    save_tasks()
    print("task kardiya ADD!!!")

#delete a task
def delete_task():
    user_input = input("Task to be deleted (number from the list): ")

    # check if input is digit or not
    if not user_input.isdigit():
        print("Please enter a valid number.")
        return

    index = int(user_input) - 1

    # check if index is within range
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
    else:
        removed = tasks.pop(index)
        save_tasks()
        print(f"Task '{removed}' deleted.")

#view tasks
def view_tasks():
    if not tasks:
        print("No tasks lol.")
    else:
        print("Tasks: ")
        for i,task in enumerate(tasks, start =1):
            print(f"Task{i}. {task}")


#Main todo Function
def todo():
    global tasks
    tasks = load_tasks()
    while True:
        action = input("Todo List\nWhat action would you like to perform Enter\n(v) for view tasks\n" \
                "(d) for delete tasks\n" \
                "(a) for add tasks\n")
        
        action = action.lower()

        if action == "v":
            view_tasks()
            
        elif action == "d":
            delete_task()
       
        elif action == "a":
            add_task()
  
        elif action == "x":
            print("leaving APP BYEEEEE!!")
            break


todo()