This is Password manager that stores the username and password locally. 
I have used Tkinter module for the GUI development.
This application can also generate random password. The input will be the size/length of the password.
The length password should atleast be 8.
I have used Pycharm as my IDE.
MODULES used in this project:
    1.	tkinter 
        Purpose: tkinter is the standard GUI (Graphical User Interface) library for Python. It provides various widgets like labels, buttons, entry fields, and message boxes to create user interfaces.
        Key Functions:
            Tk(): Initializes the main window of the application.
            Label(): Creates a label widget to display text.
            Entry(): Creates an input field where users can enter text.
            Button(): Creates a button widget that users can click to trigger actions.
            messagebox: Provides methods to display message boxes for showing information, warnings, and errors.
    2.	string
        Purpose: The string module provides a collection of string constants which include ASCII letters, digits, punctuation, etc.
        Key Constants:
            ascii_lowercase: Contains all lowercase letters.
            ascii_uppercase: Contains all uppercase letters.
            digits: Contains all digit characters (0-9).
    3.	random
        Purpose: The random module provides functions to generate random numbers and perform random operations, such as shuffling.
        Key Functions:
            shuffle(): Randomly reorders elements in a list.
            choice(): Returns a randomly selected element from a non-empty sequence.
TECH STACK
1.	Python
       Description: Python is a high-level, interpreted programming language known for its readability and simplicity. It is widely used for various applications, including web development, data analysis, artificial intelligence, and more.
       Usage in Project: The entire project is written in Python, utilizing its standard libraries and modules for GUI development, file handling, and random operations.
2.  Tkinter
      Description: tkinter is the standard GUI toolkit in Python. It allows the creation of desktop applications with graphical user interfaces.
      Usage in Project: tkinter is used to create the user interface of the password manager. It provides the main window, input fields, buttons, and message boxes.
3.  Text File Handling
      Description: The project uses text file handling to store and retrieve passwords. Text files are a simple and efficient way to manage small amounts of data.
      Usage in Project: Passwords are saved in a text file (passwords.txt). The application reads from and writes to this file to add, retrieve, list, and delete passwords.
