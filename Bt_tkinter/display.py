from tkinter import *


# root window
root = Tk()
root.geometry("550x450")
root.resizable(False, False)
root.title('Sign In')

id = StringVar()
password = StringVar()


# id
id = Label(root, text="ID :", font='Verdana 10 bold')
id.place(x=80, y=120)

id_entry = Entry(root, width=40, textvariable=id)
id_entry.focus()
id_entry.place(x=200, y=123)

# password
password_label = Label(root, text="Password :", font='Verdana 10 bold')
password_label.place(x=80, y=160)

password_entry = Entry(root, width=40, show="*", textvariable=password)
password_entry.place(x=200, y=160)

# button B1
btn_b1 = Button(root, text="B1", font='Verdana 10 bold')
btn_b1.place(x=200, y=193)

# button B2
btn_b2 = Button(root, text="B2", font='Verdana 10 bold')
btn_b2.place(x=260, y=193)

# button B3 -sent
btn_b3 = Button(root, text="B3 - sent", font='Verdana 10 bold')
btn_b3.place(x=320, y=193)


root.mainloop()
