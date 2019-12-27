# ----- Imports -----
from cryptography.fernet import Fernet
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import easygui

# ----- Global Variables ----
height = 600
width = 600
background_color = "#40C840"
path = None

# ----- Functions -----
def encrypt(path):
    """Returns The Encrypted File"""
    key = Fernet.generate_key()
    token = Fernet(key)
    with open(path, 'rb+') as plain_file:
        plain_text = bytes(plain_file.read(), "utf-8")  # File data
        cipher_text = str(token.encrypt(plain_text), "utf-8")
        plain_file.seek(0)  # Return to the beginning of the file
        plain_file.truncate()  # Empty the file
        plain_file.write(cipher_text)
        plain_file.write(f'\n\n{str(key, "utf-8")}')
        messagebox.showinfo("Encryption Successful", "The Encryption Is Completed")
        label2["text"] = "You Have Not Chosen\nAny File Yet."

def decrypt(path):
    """Returns The Decrypted File"""
    with open(path, 'rb+') as cipher_file:
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
    """Opens The File Choosing Dialog Box"""
    global path
    path = easygui.fileopenbox()
    label2["text"] = f"{path[0:len(path)//2]}\n{path[len(path)//2:-1]+path[-1]}"
                         
def crypt():
    """Redirects To The Appropriate Functions"""
    if path =  = None:
        messagebox.showerror("File Path Empty", "You Have Not Selected A File Path. Please Select A File Path.")
    if option.get() == 0:
        encrypt(path)        
    else:
        decrypt(path)
    
# ----- Main Code -----

# Initializing The Main Tkinter Window
root = tk.Tk()
root.title("Encrypter And Decrypter")
root.geometry(f"{width}x{height}")

# Initializing And Setting The Images                         
logo_image = tk.PhotoImage(file = "Logo.png")
root.iconphoto(False, logo_image)
root.iconbitmap("Icon.ico")
background_image = tk.PhotoImage(file = 'Background.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

# Creating The Main Window
option = IntVar()
option.set(0)

# Initializing All The Window
frame1 = tk.Frame(root, bd = 5, bg = background_color)
frame1.place(relx = 0.05, rely = 0.05, relwidth = 0.9, relheight = 0.9)

frame2 = tk.Frame(frame1, bd = 5, bg = background_color, relief = GROOVE)
frame2.place(relx = 0.1, rely = 0.07, relwidth = 0.8, relheight = 0.3)

label1 = tk.Label(frame2, text = "Select What Do You Want To Do?", bg = background_color, fg = "black", font = ("Times New Roman", 18))
label1.place(relx = 0.01, rely = 0.01, relwidth = 0.98, relheight = 0.3)

option1 = tk.Radiobutton(frame2, text = "Encryption", variable = option, value = "0", font = ("Times New Roman", 18), cursor = "hand2")
option1.place(relx = 0.1, rely = 0.31, relwidth = 0.8, relheight = 0.3)

option2 = tk.Radiobutton(frame2, text = "Decryption", variable = option, value = "1", font = ("Times New Roman", 18), cursor = "hand2")
option2.place(relx = 0.1, rely = 0.61, relwidth = 0.8, relheight = 0.3)

frame3 = tk.Frame(frame1, bd = 5, bg = background_color, relief = GROOVE)
frame3.place(relx = 0.1, rely = 0.4, relwidth = 0.8, relheight = 0.4)

button1 = tk.Button(frame3 text = "Choose A File", font = ("Times New Roman", 18), command = choose_file, cursor = "hand2")
button1.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.4)

label2 = tk.Label(frame3 text = "You Have Not Chosen\nAny File Yet.", bg = background_color, fg = "black", font = ("Times New Roman", 18))
label2.place(relx = 0.05, rely = 0.6, relwidth = 0.9, relheight = 0.4)

button2 = tk.Button(frame1 text = "Submit", font = ("Times New Roman", 18), command = crypt, cursor = "hand2")
button2.place(relx = 0.4, rely = 0.85, relwidth = 0.2, relheight = 0.1)

# ----- Driver Code -----
if __name__ == "__main__":
    root.mainloop()
