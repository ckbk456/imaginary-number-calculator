from tkinter import *
import regex as re

# ============= Classes ============= #
class Number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

# ============= Function ============= #
# def calculate():
    # num1 = int(entry_1.get())
    # num2 = int(entry_2.get())
    # sum = num1 + num2
    # result.delete(0, END)
    # result.insert(END, sum)
def data_type_error():
    error_label.config(text="Please check number formatting")
def get_entry():
    for key in entries:
        raw_entry = entries[key].get()
        no_space_entry = "".join(raw_entry.split())
        if no_space_entry.isdigit():
            print(f"{no_space_entry} is real")
            error_label.config(text="")
        else:
            match = re.match(r"(?P<real>[0-9]{1,})(?P<imaginary>[+-]{1}[0-9]{1,})[i]$", no_space_entry)
            if match:
                entry = Number(real=match.group("real"),imaginary=match.group("imaginary"))
                print(f"{int(entry.real)}, {int(entry.imaginary)}")
                error_label.config(text="")
            else:
                entries[key].focus()
                data_type_error()

a = "+45"
print(int(a))
# match = re.match(r"(?P<real>[0-9]{1,})(?P<imaginary>[+-]{1}[0-9]{1,})[i]$", a)
# if match:
#     print(match.group("imaginary"))
# else:
#     print("nope")
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
# entry_1.grid(column=1, row=1)

operator_list = ['add','minus','multiply','divide']
operator = StringVar(app)
operator_button = OptionMenu(app, operator, *operator_list)
operator_button.grid(column=2, row=1)

entry_2_label = Label(text="Num 2:", font=("courier", 14))
entry_2_label.grid(column=3, row=1)

entry_2 = Entry(width=10)
# entry_2.grid(column=4, row=1)
entries = {"1":entry_1,
           "2":entry_2}
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
# a+bi

