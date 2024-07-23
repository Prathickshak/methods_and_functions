import streamlit as st
def display_menu():
    st.write("\nTask Manager")
    st.write("============")
    st.write("1. View Tasks")
    st.write("2. Add Task")
    st.write("3. Mark Task as Done")
    st.write("4. Remove Task")
    st.write("5. Exit")

def view_tasks(tasks):
    if not tasks:
        st.write("No tasks available.")
    else:
        st.write("\nTasks:")
        for task_id, task_details in tasks.items():
            status = "Done" if task_details['done'] else "Not Done"
            st.write(f"{task_id}. {task_details['description']} ({status})")

def add_task(tasks, task_id_counter):
    description = input("Enter the new task: ")
    tasks[task_id_counter] = {'description': description, 'done': False}
    st.write("Task added.")
    return task_id_counter + 1

def mark_task_done(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the task ID to mark as done: "))
    if task_id in tasks:
        tasks[task_id]['done'] = True
        st.write("Task marked as done.")
    else:
        st.write("Invalid task ID.")

def remove_task(tasks):
    view_tasks(tasks)
    task_id = int(input("Enter the task ID to remove: "))
    if task_id in tasks:
        removed_task = tasks.pop(task_id)
        st.write(f"Task '{removed_task['description']}' removed.")
    else:
        st.write("Invalid task ID.")

def main():
    tasks = {}
    task_id_counter = 1
    
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        
        elif choice == '2':
            task_id_counter = add_task(tasks, task_id_counter)
        
        elif choice == '3':
            mark_task_done(tasks)
        
        elif choice == '4':
            remove_task(tasks)
        
        elif choice == '5':
            st.write("Exiting the task manager.")
            break
        
        else:
            st.write("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


"""
Explanation:

    Tasks Dictionary: The tasks are stored in a dictionary where each key is a unique task ID (integer), and the value is another dictionary with task details (description and done status).

    view_tasks(tasks): Displays tasks with their IDs and statuses.

    add_task(tasks, task_id_counter): Adds a new task to the dictionary with a unique task ID. The task_id_counter is incremented after each addition to ensure unique IDs.

    mark_task_done(tasks): Marks a specified task as done by changing its done status to True.

    remove_task(tasks): Removes a task from the dictionary using its ID.

    main(): The main loop that manages user interactions and task operations.


"""
