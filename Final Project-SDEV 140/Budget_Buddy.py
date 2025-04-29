import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Registration")
window.geometry("280x260")
window.resizable(False, False)

def showlogin():
    loginform()
    window.withdraw()

def loginform():
    loginwindow = tk.Toplevel()
    loginwindow.title("Login")
    loginwindow.geometry("250x150")
    loginwindow.resizable(False, False)

    username_label = tk.Label(loginwindow, text="Username", justify="left")
    username_label.grid(row=0, column=0, padx=10, pady=10)
    password_label = tk.Label(loginwindow, text="Password", justify="left")
    password_label.grid(row=1, column=0, padx=10, pady=10)

    username_entry = tk.Entry(loginwindow)
    username_entry.grid(row=0, column=1, pady=10)
    password_entry = tk.Entry(loginwindow, show="*")
    password_entry.grid(row=1, column=1, pady=10)

    def login():
        messagebox.showinfo("Login", "Login Successful")
        loginwindow.destroy()
        budget_dashboard()

    submit_button = tk.Button(loginwindow, text="Log In", command=login)
    submit_button.grid(row=2, column=0, columnspan=2)

def register():
    firstname = firstname_entry.get().strip()
    lastname = lastname_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get()
    confirm_pass = confirmpass_entry.get()

    if not firstname or not lastname or not username or not password or not confirm_pass:
        messagebox.showerror("Check Entries", "All fields are required")
    elif password != confirm_pass:
        messagebox.showerror("Check Password", "Passwords do not match")
    elif len(password) < 8:
        messagebox.showerror("Check Password", "Passwords is too short")
    else:
        regdata = open("users.txt", "a")
        regdata.write(firstname + ",")
        regdata.write(lastname + ",")
        regdata.write(username + ",")
        regdata.write(password + "\n")
        regdata.close()

        messagebox.showinfo("Information", "Registration Successful")

        firstname_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirmpass_entry.delete(0, tk.END)

def budget_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Budget Buddy Dashboard")
    dashboard.geometry("400x400")

    def submit_data():
        try:
            income = float(income_entry.get())
            fixed = float(fixed_entry.get())
            variable = float(variable_entry.get())
            debt = float(debt_entry.get())
            spending = fixed + variable + debt
            balance = income - spending
            summary_label.config(text=f"Monthly Summary:\nIncome: ${income:.2f}\nSpending: ${spending:.2f}\nBalance: ${balance:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers")

    tk.Label(dashboard, text="Enter Monthly Budget Info").pack(pady=10)

    tk.Label(dashboard, text="Income:").pack()
    income_entry = tk.Entry(dashboard)
    income_entry.pack()

    tk.Label(dashboard, text="Fixed Expenses:").pack()
    fixed_entry = tk.Entry(dashboard)
    fixed_entry.pack()

    tk.Label(dashboard, text="Variable Expenses:").pack()
    variable_entry = tk.Entry(dashboard)
    variable_entry.pack()

    tk.Label(dashboard, text="Debts:").pack()
    debt_entry = tk.Entry(dashboard)
    debt_entry.pack()

    tk.Button(dashboard, text="Submit", command=submit_data).pack(pady=10)

    summary_label = tk.Label(dashboard, text="")
    summary_label.pack(pady=10)

firstname_label = tk.Label(window, text="First name", justify="left")
firstname_label.grid(row=0, column=0, padx=10, pady=10)
lastname_label = tk.Label(window, text="Last name", justify="left")
lastname_label.grid(row=1, column=0, padx=10, pady=10)
username_label = tk.Label(window, text="Username", justify="left")
username_label.grid(row=2, column=0, padx=10, pady=10)
password_label = tk.Label(window, text="Password", justify="left")
password_label.grid(row=3, column=0, padx=10, pady=10)
confirmpass_label = tk.Label(window, text="Confirm Password", justify="left")
confirmpass_label.grid(row=4, column=0, padx=10, pady=10)

firstname_entry = tk.Entry(window)
firstname_entry.grid(row=0, column=1, pady=10)
lastname_entry = tk.Entry(window)
lastname_entry.grid(row=1, column=1, pady=10)
username_entry = tk.Entry(window)
username_entry.grid(row=2, column=1, pady=10)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=3, column=1, pady=10)
confirmpass_entry = tk.Entry(window, show="*")
confirmpass_entry.grid(row=4, column=1, pady=10)

submit_button = tk.Button(window, text="Submit", command=register)
submit_button.grid(row=5, column=0, columnspan=2)

gotologin_button = tk.Button(window, text="Log In", justify="right", command=showlogin)
gotologin_button.grid(row=6, column=1)

window.mainloop()
