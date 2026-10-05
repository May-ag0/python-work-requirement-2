#task2. task list manager

import tasks

task_list = []

while True:
    user_input = input("Enter 'add', 'remove', or 'done': ").lower()

    if user_input == "done":
        print("Exiting task manager.")
        break

    elif user_input == "add":
        task = input("Enter task to add: ")
        tasks.add_task(task_list, task)
        print("Updated task list:", task_list)

    elif user_input == "remove":
        task = input("Enter task to remove: ")
        tasks.remove_task(task_list, task)


print("Updated task list:", task_list)

