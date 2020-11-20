from cryptography.fernet import Fernet
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import easygui

height = 600
width = 600
path = None
background_color = "#40C840"

def encrypt(path):
    key = Fernet.generate_key()
    token = Fernet(key)
    with open(path, 'r+') as plain_file:
        plain_text = bytes(plain_file.read(), "utf-8")  # File data
        cipher_text = str(token.encrypt(plain_text), "utf-8")
        plain_file.seek(0)  # Return to the beginning of the file
        plain_file.truncate()  # Empty the file
        plain_file.write(cipher_text)
        plain_file.write(f'\n\n{str(key, "utf-8")}')
        messagebox.showinfo("Encryption Successful", "The Encryption Is Completed")
        label2["text"] = "You Have Not Chosen\nAny File Yet."

def decrypt(path):
    with open(path, 'r+') as cipher_file:
        cipher_text = cipher_file.read()
        cipher_text, key = str(cipher_text).split("\n\n")
        token = Fernet(key)
        plain_text = token.decrypt(bytes(cipher_text, "utf-8"))
        cipher_file.seek(0)
        cipher_file.truncate()
        cipher_file.write(str(plain_text, "utf-8"))
        messagebox.showinfo("Decryption Successful", "The Decryption Is Completed")
        label2["text"] = "You Have Not Chosen\nAny File Yet."

def choose_file():
    global path
    path = easygui.fileopenbox()
    breakpoint = len(path)//2
    label_path = f"{path[0:breakpoint]}\n{path[breakpoint:-1]+path[-1]}"
    label2["text"] = label_path
    print(label_path)
    print(path)

def crypt():
    global path
    global option
    print(path)
    if path == None:
        messagebox.showerror("File Path Empty", "You Have Not Selected A File Path. Please Select A File Path.")
    if option.get() == 0:
        encrypt(path)        
    else:
        decrypt(path)

root = tk.Tk()
root.geometry(f"{width}x{height}")
logo_image = tk.PhotoImage(file="Logo.png")
root.iconphoto(False, logo_image)
root.iconbitmap("Icon.ico")
background_image = tk.PhotoImage(file='Background.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

root.title("Encrypter And Decrypter")

option = IntVar()
option.set(0)

topframe = tk.Frame(root, bd=5, bg=background_color)
topframe.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

labelframe = tk.Frame(topframe, bd=5, bg=background_color, relief=GROOVE)
labelframe.place(relx=0.1, rely=0.07, relwidth=0.8, relheight=0.3)

label = tk.Label(labelframe, text="Select What Do You Want To Do?", bg=background_color, fg="black", font=("Times New Roman", 18))
label.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.3)

option1 = tk.Radiobutton(labelframe, text="Encryption", variable=option, value="0", font=("Times New Roman", 18))
option1.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.3)

option2 = tk.Radiobutton(labelframe, text="Decryption", variable=option, value="1", font=("Times New Roman", 18))
option2.place(relx=0.1, rely=0.61, relwidth=0.8, relheight=0.3)

fileframe = tk.Frame(topframe, bd=5, bg=background_color, relief=GROOVE)
fileframe.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

button1 = tk.Button(fileframe, text="Choose A File",font=("Times New Roman", 18), command=choose_file)
button1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.4)

label2 = tk.Label(fileframe, text="You Have Not Chosen\nAny File Yet.", bg=background_color, fg="black", font=("Times New Roman", 18))
label2.place(relx=0.05, rely=0.6, relwidth=0.9, relheight=0.4)

button2 = tk.Button(topframe, text="Submit",font=("Times New Roman", 18), command=crypt)
button2.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.1)

root.mainloop()
