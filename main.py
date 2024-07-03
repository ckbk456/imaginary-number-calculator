from tkinter import *

# ============= Classes ============= #

# ============= Function ============= #
def calculate():
    num1 = int(input1.get())
    num2 = int(input2.get())
    sum = num1 + num2
    result.delete(0, END)
    result.insert(END, sum)

# ============= GUI ============= #
app = Tk()
app.title("Imaginary Number Calculator")
app.config(padx=50, pady=50)

input1 = Entry(width=10)
input1.grid(column=0, row=0)

input2 = Entry(width=10)
input2.grid(column=1, row=0)

result = Entry(width=10)
result.grid(column=2, row=0)

button = Button(text="Calculate", width=20, command=calculate)
button.grid(column=1, row=1)

app.mainloop()