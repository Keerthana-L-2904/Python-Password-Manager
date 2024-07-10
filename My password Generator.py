import tkinter 
from tkinter import messagebox
import string
import random

def add():
    username = entryName.get()
    password = entryPassword.get()
    if username and password:
        with open("passwords.txt", 'a') as f:
            f.write(f"{username} {password}\n")
        messagebox.showinfo("Success", "Password added !!")
    else:
        messagebox.showerror("Error", "Please enter both the fields")
def generatePass():
    try:
        s1 = list(string.ascii_lowercase)
        s2 = list(string.ascii_uppercase)
        s3 = list(string.digits)
        
        # Ask user about the number of characters
        user_input = entryGenerate.get()
        
        # check this input is it number? is it more than 8?
        while True:
            try:
                characters_number = int(user_input)
                if characters_number < 8:
                    messagebox.showerror("Error", "Your length of the password should be at least 8.")
                    return
                else:
                    break
            except ValueError:
                messagebox.showerror("Error", "Please enter numbers only.")
                return
        
        # shuffle all lists
        random.shuffle(s1)
        random.shuffle(s2)
        random.shuffle(s3)
        
        # calculate 30% & 20% of number of characters
        part1 = round(characters_number * (30 / 100))
        part2 = round(characters_number * (20 / 100))
        
        # generation of the password (60% letters and 40% digits & punctuations)
        result = []
        for x in range(part1):
            result.append(s1[x])
            result.append(s2[x])
        for x in range(part2):
            result.append(s3[x])
        
        # shuffle result
        random.shuffle(result)
        
        # join result
        password = "".join(result)
        messagebox.showinfo("Passwords", password)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
def get():
    username = entryName.get()
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                # creating the key-value pair of username and password.
                passwords[i[0]] = i[1]
    except:
        # displaying the error message
        print("ERROR !!")

    if passwords:
        mess = "Your passwords:\n"
        for i in passwords:
            if i == username:
                mess += f"Password for {username} is {passwords[i]}\n"
                break
        else:
            mess += "No Such Username Exists !!"
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "EMPTY LIST!!")


def getlist():
    # creating a dictionary
    passwords = {}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                passwords[i[0]] = i[1]
    except:
        print("No passwords found!!")

    if passwords:
        mess = "List of passwords:\n"
        for name, password in passwords.items():
            # generating a proper message
            mess += f"Password for {name} is {password}\n"
        # Showing the message
        messagebox.showinfo("Passwords", mess)
    else:
        messagebox.showinfo("Passwords", "Empty List !!")


def delete():
    # accepting input from the user
    username = entryName.get()

    # creating a temporary list to store the data
    temp_passwords = []

    # reading data from the file and excluding the specified username
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                if i[0] != username:
                    temp_passwords.append(f"{i[0]} {i[1]}")

        # writing the modified data back to the file
        with open("passwords.txt", 'w') as f:
            for line in temp_passwords:
                f.write(line)

        messagebox.showinfo(
            "Success", f"User {username} deleted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting user {username}: {e}")


if __name__ == "__main__":
    app = tkinter.Tk()
    app.geometry("560x270")
    app.title("My Password Manager cum Strong Password Generator")

    # Username block
    labelName = tkinter.Label(app, text="USERNAME:")
    labelName.grid(row=0, column=0, padx=15, pady=15)
    entryName = tkinter.Entry(app)
    entryName.grid(row=0, column=1, padx=15, pady=15)

    # Password block
    labelPassword = tkinter.Label(app, text="PASSWORD:")
    labelPassword.grid(row=1, column=0, padx=10, pady=5)
    entryPassword = tkinter.Entry(app)
    entryPassword.grid(row=1, column=1, padx=10, pady=5)

    # Add button
    buttonAdd = tkinter.Button(app, text="Add", command=add)
    buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

    # Get button
    buttonGet = tkinter.Button(app, text="Get", command=get)
    buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

    # List Button
    buttonList = tkinter.Button(app, text="List", command=getlist)
    buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

    # Delete button
    buttonDelete = tkinter.Button(app, text="Delete", command=delete)
    buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")
    # Generate Password Button
    labelGenerate = tkinter.Label(app, text="Enter Size to Randomly Generate Password:")
    labelGenerate.grid(row=4, column=0, padx=10, pady=8)
    entryGenerate = tkinter.Entry(app)
    entryGenerate.grid(row=4, column=1, padx=15, pady=8)
    buttonGenerate = tkinter.Button(app, text="Generate", command=generatePass)
    buttonGenerate.grid(row=5, column=0,columnspan=2,padx=15, pady=8, sticky="we")

    app.mainloop()
