import os  # Module for interacting with the operating system
import pickle  # Module for serializing and deserializing Python objects
from datetime import datetime  # Module for handling dates and times

todos = []  # Initialize an empty list to store todo items
TODO_FILE = "todos.pkl"  # Define the filename for storing todos

# Define a class to represent a todo item
class Todo:
    def __init__(self, title, created_at, is_completed=False):
        self.title = title
        self.created_at = created_at
        self.is_completed = is_completed

# Function to save todos to a file using pickle
def save_to_file():
    with open(TODO_FILE, "wb") as file:
        pickle.dump(todos, file)

# Function to read todos from a file using pickle
def read_from_file():
    global todos
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "rb") as file:
            todos = pickle.load(file)

# Function to add a new todo item
def add_todo():
    title = input("Type your todo: ")  # Prompt user for todo title
    created_at = datetime.now().strftime("%d/%m %H:%M")  # Get current date and time
    todo = Todo(title, created_at)  # Create a new Todo object
    todos.append(todo)  # Add the new todo to the list
    save_to_file()  # Save todos to file

# Function to print all todos
def print_all_todos():
    print("+----+-------------------------------------+--------------+-------------+")
    print("| ID |            Todo Title               |  Created at  |  Completed  |")
    print("+----+-------------------------------------+--------------+-------------+")

    # Iterate through todos and print each one
    for i, todo in enumerate(todos):
        print(f"| {i + 1:2} | {todo.title:35} | {todo.created_at:12} | {'✅' if todo.is_completed else '❌':^11} |")

    print("+----+-------------------------------------+--------------+-------------+")

# Function to mark a todo as complete
def mark_as_complete():
    print_all_todos()  # Print all todos
    try:
        todo_id = int(input("Enter the ID of the todo: ")) - 1  # Prompt user for todo ID
        todos[todo_id].is_completed = True  # Mark todo as completed
        save_to_file()  # Save todos to file
    except IndexError:
        print("Invalid todo ID.")  # Handle invalid todo ID
    except ValueError:
        print("Invalid input.")  # Handle invalid input

# Function to delete a todo
def delete_todo():
    print_all_todos()  # Print all todos
    try:
        todo_id = int(input("Enter the ID of the todo: ")) - 1  # Prompt user for todo ID
        del todos[todo_id]  # Delete todo from list
        save_to_file()  # Save todos to file
    except IndexError:
        print("Invalid todo ID.")  # Handle invalid todo ID
    except ValueError:
        print("Invalid input.")  # Handle invalid input

# Function to show options to the user
def show_options():
    while True:
        user_choice = input("Type 'A' to add, 'D' to delete, 'C' to mark complete, or 'Q' to quit: ").upper()
        if user_choice == 'A':
            add_todo()
        elif user_choice == 'D':
            delete_todo()
        elif user_choice == 'C':
            mark_as_complete()
        elif user_choice == 'Q':
            break
        else:
            print("Command not found.")  # Handle invalid command

        print_all_todos()  # Print all todos after each action

# Function to check if this is the first time running the app
def is_this_first_time():
    if os.path.exists(TODO_FILE):  # Check if todo file exists
        read_from_file()  # Read todos from file
        print_all_todos()  # Print all todos
    else:
        print("Welcome to the Great Todo App")  # Display welcome message
        add_todo()  # Add a new todo
        print_all_todos()  # Print all todos

# Entry point of the program
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print("\033[32;1m")  # Set text color to green
    is_this_first_time()  # Check if it's the first time running the app
    show_options()  # Show options to the user
