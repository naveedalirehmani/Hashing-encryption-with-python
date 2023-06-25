# Create an empty list to store tasks
tasks = []
GREEN = "\033[32m"
RESET = "\033[0m"

while True:
    # Display menu options
    print("Todo List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. delete a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # Add a task
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        # View tasks
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(tasks):
                print(GREEN+f"{index + 1}. {task}"+RESET)

    elif choice == "3":
        # delete a task
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            task_index = int(input("Enter the task number to delete: "))
            if 1 <= task_index <= len(tasks):
                completed_task = tasks.pop(task_index - 1)
                print(f"Task '{completed_task}' deleted!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        # Exit the program
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
