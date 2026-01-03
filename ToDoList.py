# To Do List 
# 5. To-Do List (Console Version)
# Add tasks
# Remove tasks
# Show tasks
# Save tasks to a text file (intro to file handling) -> after finshing BroCode(File Handling)

tasks = []

def add_task(task):
    tasks.append(task)

def finish_task(task):
    pass

def show_tasks():
    if not tasks:
        print("No tasks.")
    else: 
        for i, task in enumerate(tasks, 1):
            print(f"{i} - {task}")

def main():
    is_running = True
    while is_running:
        choice = input("Please Choose : Add - Finish - Show a task (A, R, S) (Q to quit): ").upper()
        match choice:
            case "A":
                add_task(input("Write a task to add it: ").strip().capitalize())
            case "R":
                finish_task()
            case "S":
                show_tasks()
            case "Q":
                is_running = False
            case _ :
                print("Invalid input")

if __name__ == '__main__':
    main()
