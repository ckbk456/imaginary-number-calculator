from tkinter import *
from tkinter import messagebox
import regex as re

# ============= Classes ============= #
class Number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

# ============= Functions ============= #
def calculate(num1,num2):
    x = num1
    y = num2
    # (a + bi)(c + di)
    a = int(x.real)
    b = int(x.imaginary)
    c = int(y.real)
    d = int(y.imaginary)

    try:
        if operator == "add":
            answer = Number(real = a+c, imaginary = b+d)
        elif operator == "subtract":
            answer = Number(real= a-c, imaginary= b-d)
        elif operator == "multiply":
            answer = Number(real= a*c - b*d, imaginary= a*d + b*c)
        else:
            pass
    except NameError:
        messagebox.showerror(title="No operator", message="Please select an operator")

    result.delete(0, END)
    if answer.imaginary == 0:
        result.insert(END, answer.real)
    elif answer.imaginary > 0:
        result.insert(END, f"{answer.real}+{answer.imaginary}i")
    else:
        result.insert(END, f"{answer.real}{answer.imaginary}i")

def get_entry():
    entry_list = []
    for key in entries:
        raw_entry = entries[key].get()
        no_space_entry = "".join(raw_entry.split())
        if no_space_entry.isdigit():
            entry = Number(real=int(no_space_entry), imaginary=0)
            entry_list.append(entry)
        else:
            match = re.match(r"(?P<real>[0-9]{1,})(?P<imaginary>[+-]{1}[0-9]{1,})[i]$", no_space_entry)
            if match:
                entry = Number(real=match.group("real"),imaginary=match.group("imaginary"))
                entry_list.append(entry)
            else:
                entries[key].focus()
                messagebox.showerror(title="Formatting Error", message="Please check number formatting. Allowed formatting:\n"
                                                  "- 'a' where a is a Real number\n"
                                                  "- 'a +- bi' where a and b are Real numbers")
                break
    calculate(entry_list[0], entry_list[1])

# imaginary regex format (simple): "[0-9]{1,}[+-]{1}[0-9]{1,}[i]$"
# imaginary regex format (better): r"(?P<real>[0-9]{1,}) (?P<imaginary>[+-]{1}[0-9]{1,})[i]$"

# ============= GUI ============= #
app = Tk()
app.title("Imaginary Number Calculator")
app.config(padx=50, pady=50)

title = Label(text="Imaginary Number Calculator", font=("courier", 24, "bold"))
title.grid(column=0, row=0, columnspan=5)

entry_1_label = Label(text="Num 1:", font=("courier", 14))
entry_1_label.grid(column=0, row=1)

entry_1 = Entry(width=10)

# Select operator and save it to operator var
def update_operator(selection):
    global operator
    operator = selection
    print(operator)

operator_list = ['add','subtract','multiply','divide']
selection = StringVar()
operator_button = OptionMenu(app, selection, *operator_list, command=update_operator)
operator_button.grid(column=2, row=1)

entry_2_label = Label(text="Num 2:", font=("courier", 14))
entry_2_label.grid(column=3, row=1)

entry_2 = Entry(width=10)

# putting entries in dict and displaying them, this is reserved for when you want to add in more entries
entries = {"1": entry_1,
           "2": entry_2}
entries["1"].grid(column=1, row=1)
entries["2"].grid(column=3, row=1)

result_label = Label(text="Result:", font=("courier", 14))
result_label.grid(column=3, row=2)

result = Entry(width=10)
result.grid(column=4, row=2)

calculate_button = Button(text="Calculate", width=10, command=get_entry)
calculate_button.grid(column=2, row=3)

error_label = Label(text="", font=("courier", 14))
error_label.grid(column=2, row=4)

app.mainloop()

# ============= Testing ============= #

