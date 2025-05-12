
import tkinter as tk  #Import tkinter for GUI
from tkinter import messagebox  #Import messagebox for alerts and messages

#Create the main registration window
window = tk.Tk()
window.title("Registration")  #Title of the window
window.geometry("280x260")  #Set the size of the window
window.resizable(False, False)  #Prevent window resizing

#Login Form
def loginform():
    loginwindow = tk.Toplevel()  #Create a new top-level window
    loginwindow.title("Login")  #Set the title
    loginwindow.geometry("250x200")  #Size of login window
    loginwindow.resizable(False, False)

    #Labels and entry fields for login credentials
    tk.Label(loginwindow, text="Username").grid(row=0, column=0, padx=10, pady=10)
    tk.Label(loginwindow, text="Password").grid(row=1, column=0, padx=10, pady=10)

    username_entry = tk.Entry(loginwindow)
    username_entry.grid(row=0, column=1)
    password_entry = tk.Entry(loginwindow, show="*")
    password_entry.grid(row=1, column=1)

    #When user clicks login button
    def login():
        messagebox.showinfo("Login", "Login Successful")  #Show success message
        loginwindow.destroy()  #Close login window
        budget_dashboard()  #Open the main budget dashboard

    #Button to perform login
    login_button = tk.Button(loginwindow, text="Log In", command=login)
    login_button.grid(row=2, column=0, columnspan=2)

#Budget Dashboard
def budget_dashboard():
    dashboard = tk.Toplevel()  #Create a new window
    dashboard.title("Budget Buddy Dashboard")
    dashboard.geometry("500x600")

    expense_entries = []  #List to store all expense entries

    #Function to handle calculation when user clicks "Submit"
    def submit_data():
        try:
            income = float(income_entry.get())  #Get income and convert to float
            total_spending = 0

            #Go through each expense and add up the cost
            for expense_name, expense_cost_entry in expense_entries:
                expense_cost = float(expense_cost_entry.get())
                total_spending += expense_cost

            balance = income - total_spending  #Calculate remaining balance

            #Display results in the summary label
            summary_label.config(
                text=f"Monthly Summary:\nIncome: ${income:.2f}\n"
                     f"Spending: ${total_spending:.2f}\n"
                     f"Balance: ${balance:.2f}")
        except ValueError:
            #Show error if something wasn't a number
            messagebox.showerror("Input Error", "Please enter valid numbers")

    #Income input field
    tk.Label(dashboard, text="Income:").pack()
    income_entry = tk.Entry(dashboard)
    income_entry.pack()

    tk.Label(dashboard, text="Enter Monthly Budget Info").pack(pady=10)

    #Frame to hold expenses
    expense_frame = tk.LabelFrame(dashboard, text="Expenses", padx=10, pady=10)
    expense_frame.pack(pady=10, fill="both", expand=True)

    #Function to dynamically add new expense input fields
    def add_expense():
        expense_row = tk.Frame(expense_frame)
        expense_row.pack(pady=5, fill="x")

        tk.Label(expense_row, text="Expense Name:").pack(side=tk.LEFT)
        expense_name_entry = tk.Entry(expense_row)
        expense_name_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(expense_row, text="Cost:").pack(side=tk.LEFT)
        expense_cost_entry = tk.Entry(expense_row)
        expense_cost_entry.pack(side=tk.LEFT, padx=5)

        #Save references to the input fields
        expense_entries.append((expense_name_entry, expense_cost_entry))

    #Button to add new expense fields
    add_expense_button = tk.Button(dashboard, text="Add Expense", command=add_expense)
    add_expense_button.pack(pady=5)

    #Button to calculate summary
    submit_data_button = tk.Button(dashboard, text="Submit", command=submit_data)
    submit_data_button.pack(pady=10)

    #Label to show the results
    summary_label = tk.Label(dashboard, text="Monthly Summary: ")
    summary_label.pack(pady=10)

#Registration Function
def register():
    #Get user inputs
    firstname = firstname_entry.get().strip()
    lastname = lastname_entry.get().strip()
    username = username_entry.get().strip()
    password = password_entry.get()
    confirm_pass = confirmpass_entry.get()

    #Validation checks
    if not firstname or not lastname or not username or not password or not confirm_pass:
        messagebox.showerror("Check Entries", "All fields are required")
    elif password != confirm_pass:
        messagebox.showerror("Check Password", "Passwords do not match")
    elif len(password) < 8:
        messagebox.showerror("Check Password", "Password is too short (min 8 characters)")
    else:
        #Save the user data
        with open("users.txt", "a") as regdata:
            regdata.write(f"{firstname},{lastname},{username},{password}\n")

        messagebox.showinfo("Information", "Registration Successful")

        #Clear input fields after registration
        firstname_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirmpass_entry.delete(0, tk.END)

#Show login Function 
def showlogin():
    loginform()  #Open the login window
    window.withdraw()  #Hide the registration window

#UI Element for registration
tk.Label(window, text="First name").grid(row=0, column=0, padx=10, pady=10)
tk.Label(window, text="Last name").grid(row=1, column=0, padx=10, pady=10)
tk.Label(window, text="Username").grid(row=2, column=0, padx=10, pady=10)
tk.Label(window, text="Password").grid(row=3, column=0, padx=10, pady=10)
tk.Label(window, text="Confirm Password").grid(row=4, column=0, padx=10, pady=10)

firstname_entry = tk.Entry(window)
firstname_entry.grid(row=0, column=1)
lastname_entry = tk.Entry(window)
lastname_entry.grid(row=1, column=1)
username_entry = tk.Entry(window)
username_entry.grid(row=2, column=1)
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=3, column=1)
confirmpass_entry = tk.Entry(window, show="*")
confirmpass_entry.grid(row=4, column=1)

#Submit and Login buttons
submit_button = tk.Button(window, text="Submit", command=register)
submit_button.grid(row=5, column=0, columnspan=2)

gotologin_button = tk.Button(window, text="Log In", command=showlogin)
gotologin_button.grid(row=6, column=1, pady=5)

#Start GUI
window.mainloop()
