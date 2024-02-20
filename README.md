# Todo App
This is a simple command-line todo application written in Python. 
It allows users to add, delete, and mark todos as complete. 
Todos are stored in a pickle file named todos.pkl. 
The application uses the terminal to interact with the user.


# Features
Add a new todo with a title and automatically record the creation time.
Display all todos with their corresponding IDs, titles, creation times, and completion status.
Mark a todo as complete.
Delete a todo.
Save todos to a binary file (todos.pkl) for persistence.
Getting Started
To run the application, follow these steps:

Clone the repository:
```bash
Copy code
git clone https://github.com/BekBrace/bekbrace-python-todo.git
```

Navigate to the project directory:
```bash
Copy code
cd bekbrace-python-todo
```
Run the application:
```
bash
Copy code
python todo.py
```
# Usage
Add Todo: Type 'A' to add a new todo. Enter the title when prompted.
Delete Todo: Type 'D' to delete a todo. Enter the ID of the todo to be deleted when prompted.
Mark as Complete: Type 'C' to mark a todo as complete. Enter the ID of the todo to be marked as complete when prompted.
Quit: Type 'Q' to quit the application.

# Notes
The todos are stored in a pickle file named todos.pkl. Ensure that the application has write permissions in the directory.
Dependencies
This application uses only standard Python libraries. No additional dependencies are required.

# Contributing
Fork the repository.
Clone the forked repository.

Create a new branch for your feature:
```bash
Copy code
git checkout -b feature-name
```

Make your changes and commit them:
```bash
Copy code
git commit -m 'Add some feature'
```
Push the branch:
```bash
Copy code
git push origin feature-name
```
Create a pull request.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Inspired by the need for a simple and quick todo app in the command line. Created with the hope of improving productivity and task management.

If it's your first time running the application, a welcome message will be displayed, and an initial todo will be added.
