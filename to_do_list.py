#Mini Project 1: To-Do List Application

#Part 1: Defining the tasks

def add_task(to_do_list, title): 
    to_do_list.append({'title': title, 'status': 'Incomplete'})
    print('Task added successfully!')

def view_tasks(to_do_list):
    if not to_do_list:
        print('No tasks available.')
    else:
        print('Tasks:')
        idx = 1
        for task in to_do_list:
            print(f"{idx}. {task['title']} - {task['status']}")
            idx += 1

def mark_task_complete(to_do_list, task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(to_do_list):
            to_do_list[task_index - 1]['status'] = 'Complete'
            print('Task marked as complete!')
        else: #make sure user (aka Dylan) can't break code
            print('Invalid task index.')
    except ValueError:
        print('Invalid input. Please enter a valid task index.')

def delete_task(to_do_list, task_index):
    try:
        task_index = int(task_index)
        if 1 <= task_index <= len(to_do_list): 
            del to_do_list[task_index - 1]
            print('Task deleted successfully!')
        else: # make sure user (aka Dylan) can't break code
            print('Invalid task index.')
    except ValueError: 
        print('Invalid input. Please enter a valid task index.')

# Part 2: Setting up UI

# Where tasks will append to
todo_list = []

while True: # Menu in while loop to pop up after every entry for easier user experience
    print('''
         Welcome to the To-Do List App!
Menu:
1. Add a task
2. View tasks
3. Mark a task as complete
4. Delete a task
5. Quit
''')

    choice = input('Enter your choice: ')

    if choice == '1':
        title = input('Add a new task: ')
        add_task(to_do_list, title)
    elif choice == '2':
        view_tasks(to_do_list)
    elif choice == '3':
        task_index = input('Enter the index of the task to mark as complete: ')
        mark_task_complete(to_do_list, task_index)
    elif choice == '4':
        task_index = input('Enter the index of the task to delete: ')
        delete_task(to_do_list, task_index)
    elif choice == '5':
        print('Goodbye!')
        break
    else: #Just in case user (aka Dylan) tries to break code
        print('Invalid choice. Please choose a valid option.')