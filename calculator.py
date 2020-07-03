from tkinter import *


def number_click(value):
    global number, is_operator_clicked, is_calculation_complete
    if is_operator_clicked == "true":
        number = str(value)
        display_value.set(number)
        is_operator_clicked = "false"
    elif is_calculation_complete == "true":
        number = str(value)
        display_value.set(number)
        is_calculation_complete = "false"
    else:
        number += str(value)
        display_value.set(number)


def operator_click(operation):
    global operator, is_operator_clicked, old_number, number, is_calculate_init, is_dot_clicked, is_calculation_complete
    if is_calculate_init == "true":
        perform_operation(old_number, number, operator)
        is_operator_clicked = "true"
        operator = operation
        old_number = number
    else:
        operator = operation
        old_number = number
        is_operator_clicked = "true"
        is_calculate_init = "true"
    is_dot_clicked = "false"
    is_calculation_complete = "false"


def dot_click():
    global number, is_dot_clicked, is_operator_clicked, is_calculation_complete
    if is_dot_clicked == "false":
        if is_operator_clicked == "true":
            number = "0."
            display_value.set(number)
            is_operator_clicked = "false"
        elif is_calculation_complete == "true":
            number = "0."
            display_value.set(number)
            is_calculation_complete = "false"
        else:
            number += "."
            display_value.set(number)
        is_dot_clicked = "true"


def equal_click():
    global is_calculate_init, is_dot_clicked, is_calculation_complete
    if is_calculate_init == "true":
        is_calculate_init = "false"
        perform_operation(old_number, number, operator)
    else:
        perform_operation(old_number, number, operator)
    is_dot_clicked = "false"
    is_calculation_complete = "true"


def clear():
    global number, operator, old_number, is_calculate_init, is_operator_clicked, is_dot_clicked, is_calculation_complete
    is_calculate_init = "false"
    is_calculation_complete = "false"
    is_dot_clicked = "false"
    is_operator_clicked = "false"
    operator = ''
    old_number = ""
    number = ""
    display_value.set(number)


def clear_entry():
    global number
    number = ""
    display_value.set(number)


def perform_operation(first_number, second_number, operate_with):
    global number
    if operate_with == "+":
        result = float(first_number) + float(second_number)
    elif operate_with == "-":
        result = float(first_number) - float(second_number)
    elif operate_with == '*':
        result = float(first_number) * float(second_number)
    elif operate_with == "/":
        result = float(first_number) / float(second_number)
    display_value.set(str(result))
    number = str(result)


# Setting Up Calculator Window
window = Tk()
window.title("Calculator")
window.configure(bg="#000")
# Setting Up Window Icon
photo = PhotoImage(file="icons/icon.png")
window.iconphoto(False, photo)

# Variable Declaration
is_operator_clicked = "false"
is_calculate_init = "false"
is_dot_clicked = "false"
is_calculation_complete = "false"
operator = ""
number = ""
old_number = ""
display_value = StringVar()

# Setting Up Calculator Display
display = Entry(window, font=('arial', 30, 'bold'), textvariable=display_value, width=25, bd=10, insertwidth=4,
                bg="#aaa", fg="#0052cc", justify="right").grid(columnspan=5)

# Setting up Calculator Buttons
# First Row
seven_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="7",
                      command=lambda: number_click(7)).grid(row=1, column=0, padx=(15, 0), pady=(15, 0), sticky="nsew")
eight_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="8",
                      command=lambda: number_click(8)).grid(row=1, column=1, padx=(0, 0), pady=(15, 0), sticky="nsew")
nine_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="9",
                     command=lambda: number_click(9)).grid(row=1, column=2, padx=(0, 0), pady=(15, 0), sticky="nsew")
clear_entry_button = Button(window, width=5, height=1, bg="#ff6f00", fg="#fff", activebackground="#fa8100",
                   font=('arial', 20, 'bold'), text="CE", command=lambda: clear_entry()).grid(
    row=1, column=3, padx=(15, 0), pady=(15, 15), sticky="nsew")
clear_button = Button(window, width=5, height=1, bg="#ff6f00", fg="#fff", activebackground="#fa8100",
                      font=('arial', 20, 'bold'), text="C", command=lambda: clear()).grid(
    row=1, column=4, padx=(0, 15), pady=(15, 15), sticky="nsew")

# Second Row
four_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="4",
                     command=lambda: number_click(4)).grid(row=2, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
five_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="5",
                     command=lambda: number_click(5)).grid(row=2, column=1, sticky="nsew")
six_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="6",
                    command=lambda: number_click(6)).grid(row=2, column=2, sticky="nsew")
negative_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                         font=('arial', 20, 'bold'), text="+/-").grid(
    row=2, column=3, padx=(15, 0), sticky="nsew")
# Setting square root button icon
root_icon = PhotoImage(file="icons/root.png")
root_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                     font=('arial', 20, 'bold'), image=root_icon).grid(
    row=2, column=4, padx=(0, 15), sticky="nsew")

# Third Row
one_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="1",
                    command=lambda: number_click(1)).grid(row=3, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
two_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="2",
                    command=lambda: number_click(2)).grid(
    row=3, column=1, sticky="nsew")
three_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="3",
                      command=lambda: number_click(3)).grid(
    row=3, column=2, sticky="nsew")
multiplication_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                               font=('arial', 20, 'bold'), text="x", command=lambda: operator_click("*")).grid(
    row=3, column=3, padx=(15, 0), sticky="nsew")
division_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                         font=('arial', 20, 'bold'), text="/", command=lambda: operator_click("/")).grid(
    row=3, column=4, padx=(0, 15), sticky="nsew")

# Fourth Row
dot_button = Button(window, width=4, height=1, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                    font=('arial', 20, 'bold'), text=".", command=lambda: dot_click()).grid(
    row=4, column=0, padx=(15, 15), pady=(15, 15), sticky="nsew")
zero_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="0",
                     command=lambda: number_click(0)).grid(
    row=4, column=1, pady=(0, 15), sticky="nsew")
equal_button = Button(window, width=4, height=1, bg="#fa0000", fg="#fff", activebackground="#ff3b3b",
                      font=('arial', 20, 'bold'), text="=",
                      command=lambda: equal_click()).grid(
    row=4, column=2, padx=(15, 0), pady=(15, 15), sticky="nsew")
plus_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                     font=('arial', 20, 'bold'), text="+", command=lambda: operator_click("+")).grid(
    row=4, column=3, padx=(15, 0), pady=(0, 15), sticky="nsew")
minus_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                      font=('arial', 20, 'bold'), text="-", command=lambda: operator_click("-")).grid(
    row=4, column=4, padx=(0, 15), pady=(0, 15), sticky="nsew")

# Preventing Window From resizing
window.resizable(0, 0)

# Calculator mainloop
window.mainloop()
