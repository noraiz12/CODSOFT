# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:31:45 2024

@author: PMLS
"""

to_do_list = []

def display_list():
    print("To-Do List:")
    for index, task in enumerate(to_do_list, 1):
        print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def remove_task():
    display_list()
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(to_do_list):
            removed_task = to_do_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid task number.")

while True:
    print("\nOptions:")
    print("1. Display To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_list()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
