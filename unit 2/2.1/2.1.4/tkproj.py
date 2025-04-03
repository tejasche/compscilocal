#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("225x100")
root.title("Authorization")

# Add this code before the code that creates your "Login" button
bt_image = tk.PhotoImage(file="button2.gif")
bt_image = bt_image.subsample(10,10)

# create empty frame
frame_auth = tk.Frame(root, width = 225, height = 100)
frame_auth.grid(row = 0, column = 0, sticky = "nsew")

frame_login = tk.Frame(root)
frame_login.grid(row = 0, column = 0)
frame_login.tkraise()

def test_my_button():
    frame_auth.tkraise()
    authtext = ent_password.get()
    auth_label.config(text = f"Password: {authtext}")
    
lbl_username = tk.Label(frame_login, text = 'Username:', font = "Courier")
lbl_username.grid(row = 0, column = 0)

lbl_password = tk.Label(frame_login, text = "Password:", font = "Courier")
lbl_password.grid(row = 1, column = 0)

ent_username = tk.Entry(frame_login, bd = 3)
ent_username.grid(row = 0, column = 1)

ent_password = tk.Entry(frame_login, bd = 3)
ent_password.grid(row = 1, column = 1)

btn_login = tk.Button(frame_login, text = "Login", command = test_my_button, image = bt_image)
btn_login.grid(row = 2, column = 0, columnspan = 2)


auth_label = tk.Label(frame_auth)
auth_label.pack()

root.mainloop()