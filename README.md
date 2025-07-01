Smart To-Do List
A simple, intuitive desktop To-Do List application built with Python and Tkinter. Organize your tasks by title, priority, due date, and due time. All tasks are securely stored in a local CSV file for easy access and management.

Features
Add Tasks: Enter task title, set priority (High/Medium/Low), and optionally add due date and time.
Demo :![task manager work](https://github.com/user-attachments/assets/e563e99f-26ef-4814-8dd1-ff97897b9c3d) ![to do task work](https://github.com/user-attachments/assets/489a305a-ecb2-4f4b-b2ac-9ce5eaa32cbe)

View Tasks: Instantly view all your tasks in a sortable, tabular format.

Data Persistence: Tasks are saved locally in a CSV file (tasks.csv), so your data is safe even after closing the app.

Input Validation: Ensures correct date and time formats for reliable scheduling.

Simple & Lightweight: No external databases or complex setup required.

Requirements
Python 3.x

Standard Python libraries (tkinter, csv, datetime, os)

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/smart-todo-list.git
cd smart-todo-list
Run the application:

bash
python main.py
(Replace main.py with your script filename if different.)

Usage
Add a Task:

Enter the task title (required).

Select a priority (High, Medium, Low).

Optionally, enter a due date (YYYY-MM-DD) and due time (HH:MM 24-hour format).

Click Add Task.

View Tasks:

Click View Tasks to see all your tasks in a table.

Troubleshooting
Date/Time Errors: Make sure to use the correct formats (YYYY-MM-DD for date, HH:MM for time).

File Issues: The app creates tasks.csv automatically in the same folder as the script.
