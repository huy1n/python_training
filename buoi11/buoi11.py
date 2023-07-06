import tkinter as tk
from tkinter import messagebox, ttk

USER = 'ghuy1'
PASS = '12345'


def click():
    user_name = txt_user_name.get()
    password = txt_pass.get()

    if user_name == USER and password == PASS:
        messagebox.showinfo("info", "login success")
    else:
        messagebox.showwarning('error', 'login failed')


# tao ra 1 cua so main window
root = tk.Tk()

# thay doi title
root.title('day11')

# thay doi chieu rong chieu cao
root.geometry("400x200+150+50")  # 150 va 50 la cach le trai va le tren

# khong thay doi kich thuoc
root.resizable(False, False)

# thay doi mau nen
# root.config(bg='#c7f9cc')

# thay doi icon
root.iconbitmap("huu.ico")

# thay doi label
lbl_text = tk.Label(root, text='Username', bg='white', fg='#000814')
# lbl_text.pack()
lbl_text.grid(row=0, column=0,  padx=(30, 0))

# tao entry
txt_user_name = tk.Entry(root, width='30')
# txt_user_name.pack()
txt_user_name.grid(row=0, column=1, padx=(20, 0), pady=20)

# tao label pass
lbl_pass = tk.Label(root, text='Password', bg='white', fg='#000814')
# lbl_pass.pack(pady=(20, 0))
lbl_pass.grid(row=1, column=0, padx=(30, 0))

# tao entry pass
txt_pass = tk.Entry(root, width='30', show='*')
# txt_pass.pack()
txt_pass.grid(row=1, column=1, padx=(20, 0), pady=20)

# tao button, command
btn_submit = ttk.Button(root, text='Submit', command=click, )
# btn_submit.pack(pady=(20, 0))
btn_submit.grid(row=2, column=1, ipadx=5, ipady=5)

# hien thi cua so
root.mainloop()
