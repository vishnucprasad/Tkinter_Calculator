import math
from tkinter import *


def plus_memory():
    global memory, number, is_memory_used, is_memory_clicked
    result = float(memory) + float(number)
    integer = result.is_integer()
    if integer:
        memory = str(int(result))
    else:
        memory = str(result)
    is_memory_used = True
    is_memory_clicked = True


def minus_memory():
    global memory, number, is_memory_used, is_memory_clicked
    result = float(memory) - float(number)
    integer = result.is_integer()
    if integer:
        memory = str(int(result))
    else:
        memory = str(result)
    is_memory_used = True
    is_memory_clicked = True


def recall_memory():
    global memory, number, is_memory_clicked, on_start
    if is_memory_used:
        number = memory
        display_value.set(number)
        is_memory_clicked = True
        on_start = False


def clear_memory():
    global memory, is_memory_used
    memory = "0"
    is_memory_used = False


def number_click(value):
    global number, is_operator_clicked, is_calculation_complete, on_start, is_memory_clicked
    if is_operator_clicked or is_memory_clicked:
        number = str(value)
        display_value.set(number)
        is_operator_clicked = False
        is_memory_clicked = False
    elif is_calculation_complete:
        number = str(value)
        display_value.set(number)
        is_calculation_complete = False
    elif on_start:
        number = str(value)
        display_value.set(number)
        on_start = False
    else:
        number += str(value)
        display_value.set(number)


def operator_click(operation):
    global operator, is_operator_clicked, old_number, number, is_calculate_init, is_dot_clicked, is_calculation_complete, on_start
    if is_operator_clicked:
        operator = operation
    elif is_calculate_init:
        perform_operation(old_number, number, operator)
        is_operator_clicked = True
        operator = operation
        old_number = number
    else:
        operator = operation
        old_number = number
        is_operator_clicked = True
        is_calculate_init = True
    on_start = False
    is_dot_clicked = False
    is_calculation_complete = False


def one_by_x_click():
    global number, is_calculation_complete
    if number == "0":
        display_value.set("Cannot divide by zero")
        is_calculation_complete = True
    else:
        value = float(number)
        value = 1 / value
        integer = value.is_integer()
        if integer:
            number = str(int(value))
        else:
            number = str(value)
        display_value.set(number)
        is_calculation_complete = True


def negative_click():
    global number, is_positive
    if is_positive:
        number = "-" + number
        display_value.set(number)
        is_positive = False
    elif not is_positive:
        positive_value = float(number) * -1
        integer = positive_value.is_integer()
        if integer:
            number = str(int(positive_value))
        else:
            number = str(positive_value)
        display_value.set(number)
        is_positive = True


def square_click():
    global number, is_calculation_complete
    value = float(number)
    value *= value
    integer = value.is_integer()
    if integer:
        number = str(int(value))
    else:
        number = str(value)
    display_value.set(number)
    is_calculation_complete = True


def root_click():
    global number, is_calculation_complete
    result = math.sqrt(float(number))
    integer = result.is_integer()
    if integer:
        number = str(int(result))
    else:
        number = str(result)
    display_value.set(number)
    is_calculation_complete = True


def cube_root():
    global number, is_calculation_complete
    value = float(number)
    if value >= 0:
        result = value ** (1. / 3.)
    else:
        result = -(-value) ** (1. / 3.)
    integer = result.is_integer()
    if integer:
        number = str(int(result))
    else:
        number = str(result)
    display_value.set(number)
    is_calculation_complete = True


def pi_click():
    global number
    number = "3.141592653589793"
    display_value.set(number)


def dot_click():
    global number, is_dot_clicked, is_operator_clicked, is_calculation_complete, on_start
    if not is_dot_clicked:
        if is_operator_clicked:
            number = "0."
            display_value.set(number)
            is_operator_clicked = False
        elif is_calculation_complete:
            number = "0."
            display_value.set(number)
            is_calculation_complete = False
        elif on_start:
            number = "0."
            display_value.set(number)
            on_start = False
        else:
            number += "."
            display_value.set(number)
        is_dot_clicked = True


def equal_click():
    global is_calculate_init, is_dot_clicked, is_calculation_complete
    if is_calculate_init:
        is_calculate_init = False
        perform_operation(old_number, number, operator)
    else:
        perform_operation(old_number, number, operator)
    is_dot_clicked = False
    is_calculation_complete = True


def delete():
    global number, on_start, is_operator_clicked, is_memory_clicked
    length = len(number)
    if length >= 2:
        number = number[0:-1]
    elif display_value.get() == "Cannot divide by zero":
        number = "0"
        display_value.set(number)
        on_start = False
    else:
        number = "0"
        on_start = True
    display_value.set(number)
    is_operator_clicked = False
    is_memory_clicked = False


def clear():
    global number, operator, old_number, is_calculate_init, is_operator_clicked, is_dot_clicked, is_calculation_complete, on_start
    is_calculate_init = False
    is_calculation_complete = False
    is_dot_clicked = False
    is_operator_clicked = False
    on_start = True
    operator = "+"
    old_number = "0"
    number = "0"
    display_value.set(number)


def clear_entry():
    global number, on_start
    on_start = True
    number = "0"
    display_value.set(number)


def perform_operation(first_number, second_number, operate_with):
    global number, is_zero_division_error
    if operate_with == "+":
        result = float(first_number) + float(second_number)
    elif operate_with == "-":
        result = float(first_number) - float(second_number)
    elif operate_with == '*':
        result = float(first_number) * float(second_number)
    elif operate_with == "/":
        if int(second_number) == 0:
            display_value.set("Cannot divide by zero")
            is_zero_division_error = True
        else:
            result = float(first_number) / float(second_number)
    elif operate_with == "^":
        result = float(first_number) ** float(second_number)
    if is_zero_division_error:
        is_zero_division_error = False
    else:
        integer = result.is_integer()
        if integer:
            to_display = int(result)
        else:
            to_display = result
        display_value.set(str(to_display))
        number = str(to_display)


# Setting Up Calculator Window
window = Tk()
window.title("Calculator")
window.configure(bg="#000")
# Setting Up Window Icon
photo = PhotoImage(file="icons/icon.png")
window.iconphoto(False, photo)

# Variable Declaration
is_operator_clicked = False
is_calculate_init = False
is_dot_clicked = False
is_calculation_complete = False
is_positive = True
is_memory_used = False
is_memory_clicked = False
is_zero_division_error = False
operator = "+"
number = "0"
old_number = "0"
memory = "0"
display_value = StringVar()
display_value.set("0")
on_start = True
theme_var = IntVar()
view_var = IntVar()

# Creating Menu
menu_bar = Menu(window)

# Adding File Menu and commands
file = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file)
show_menu = Menu(file, tearoff=0)
file.add_cascade(label='Show ', menu=show_menu)
show_menu.add_command(label='Show History', command=None)
show_menu.add_command(label='Show Memory', command=None)
theme_menu = Menu(file, tearoff=0)
file.add_cascade(label='Theme ', menu=theme_menu)
theme_menu.add_radiobutton(label='Light', value=0, variable=theme_var,  command=None)
theme_menu.add_radiobutton(label='Dark', value=1, variable=theme_var, command=None)
file.add_separator()
file.add_command(label='Exit', command=window.destroy)

# Adding View Menu and commands
view = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view)
view.add_radiobutton(label='Standard', value=0, variable=view_var, command=None)
view.add_radiobutton(label='Scientific', value=1, variable=view_var, command=None)

# Setting Up Calculator Display
display = Entry(window, font=('arial', 30, 'bold'), textvariable=display_value, width=25, bd=10, insertwidth=4,
                justify="right", state=DISABLED, disabledbackground="#aaa", disabledforeground="#0052cc").grid(
    columnspan=5)

# Setting up Calculator Buttons
# First Row
memory_clear_button = Button(window, width=5, height=1, bg="#018729", fg="#fff", activebackground="#01942d",
                             activeforeground="#fff", font=('arial', 20, 'bold'), text="MC",
                             command=lambda: clear_memory()).grid(row=1, column=0, padx=(15, 0), pady=(15, 0),
                                                                  sticky="nsew")
memory_recall_button = Button(window, width=5, height=1, bg="#018729", fg="#fff", activebackground="#01942d",
                              activeforeground="#fff", font=('arial', 20, 'bold'), text="MR",
                              command=lambda: recall_memory()).grid(row=1, column=1, padx=(0, 0), pady=(15, 0),
                                                                    sticky="nsew")
memory_plus_button = Button(window, width=5, height=1, bg="#018729", fg="#fff", activebackground="#01942d",
                            activeforeground="#fff", font=('arial', 20, 'bold'), text="M+",
                            command=lambda: plus_memory()).grid(row=1, column=2, padx=(0, 0), pady=(15, 0),
                                                                sticky="nsew")
memory_minus_button = Button(window, width=5, height=1, bg="#018729", fg="#fff", activebackground="#01942d",
                             activeforeground="#fff", font=('arial', 20, 'bold'), text="M-",
                             command=lambda: minus_memory()).grid(row=1, column=3, padx=(0, 15), pady=(15, 0),
                                                                  sticky="nsew")
delete_button = Button(window, width=5, height=1, bg="#ff6f00", fg="#fff", activebackground="#fa8100",
                       font=('arial', 20, 'bold'), text="⌫", command=lambda: delete()).grid(row=1, column=4,
                                                                                            padx=(0, 15), pady=(15, 0),
                                                                                            sticky="nsew")

# Second Row
one_by_x_button = Button(window, width=5, height=1, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                         font=('arial', 20, 'bold'), text="¹/x", command=lambda: one_by_x_click()).grid(row=2, column=0,
                                                                                                        padx=(15, 0),
                                                                                                        pady=(15, 0),
                                                                                                        sticky="nsew")
square_button = Button(window, width=5, height=1, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                       font=('arial', 20, 'bold'), text="x²", command=lambda: square_click()).grid(row=2, column=1,
                                                                                                   padx=(0, 0),
                                                                                                   pady=(15, 0),
                                                                                                   sticky="nsew")
raise_to_button = Button(window, width=5, height=1, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                         font=('arial', 20, 'bold'), text="xʸ", command=lambda: operator_click("^")).grid(row=2,
                                                                                                          column=2,
                                                                                                          padx=(0, 0),
                                                                                                          pady=(15, 0),
                                                                                                          sticky="nsew")
clear_entry_button = Button(window, width=5, height=1, bg="#ff6f00", fg="#fff", activebackground="#fa8100",
                            font=('arial', 20, 'bold'), text="CE", command=lambda: clear_entry()).grid(row=2, column=3,
                                                                                                       padx=(15, 0),
                                                                                                       pady=(15, 0),
                                                                                                       sticky="nsew")
clear_button = Button(window, width=5, height=1, bg="#ff6f00", fg="#fff", activebackground="#fa8100",
                      font=('arial', 20, 'bold'), text="C", command=lambda: clear()).grid(row=2, column=4, padx=(0, 15),
                                                                                          pady=(15, 0), sticky="nsew")

# Third Row
seven_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="7",
                      command=lambda: number_click(7)).grid(row=3, column=0, padx=(15, 0), pady=(15, 0), sticky="nsew")
eight_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="8",
                      command=lambda: number_click(8)).grid(row=3, column=1, padx=(0, 0), pady=(15, 0), sticky="nsew")
nine_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="9",
                     command=lambda: number_click(9)).grid(row=3, column=2, padx=(0, 0), pady=(15, 0), sticky="nsew")
pi_button = Button(window, width=5, height=1, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                   font=('arial', 20, 'bold'), text="π", command=lambda: pi_click()).grid(row=3, column=3, padx=(15, 0),
                                                                                          pady=(15, 0),
                                                                                          sticky="nsew")
cube_root_button = Button(window, width=5, height=1, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                          font=('arial', 20, 'bold'), text="∛", command=lambda: cube_root()).grid(row=3, column=4,
                                                                                                  padx=(0, 15),
                                                                                                  pady=(15, 0),
                                                                                                  sticky="nsew")

# Fourth Row
four_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="4",
                     command=lambda: number_click(4)).grid(row=4, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
five_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="5",
                     command=lambda: number_click(5)).grid(row=4, column=1, sticky="nsew")
six_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="6",
                    command=lambda: number_click(6)).grid(row=4, column=2, sticky="nsew")
negative_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                         font=('arial', 20, 'bold'), text="+/-", command=lambda: negative_click()).grid(
    row=4, column=3, padx=(15, 0), sticky="nsew")
root_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                     font=('arial', 20, 'bold'), text="√ ", command=lambda: root_click()).grid(
    row=4, column=4, padx=(0, 15), sticky="nsew")

# Fifth Row
one_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="1",
                    command=lambda: number_click(1)).grid(row=5, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
two_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="2",
                    command=lambda: number_click(2)).grid(row=5, column=1, sticky="nsew")
three_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="3",
                      command=lambda: number_click(3)).grid(row=5, column=2, sticky="nsew")
multiplication_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                               font=('arial', 20, 'bold'), text="x", command=lambda: operator_click("*")).grid(
    row=5, column=3, padx=(15, 0), sticky="nsew")
division_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                         font=('arial', 20, 'bold'), text="÷", command=lambda: operator_click("/")).grid(
    row=5, column=4, padx=(0, 15), sticky="nsew")

# Sixth Row
dot_button = Button(window, width=4, height=1, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                    font=('arial', 20, 'bold'), text=".", command=lambda: dot_click()).grid(
    row=6, column=0, padx=(15, 15), pady=(15, 15), sticky="nsew")
zero_button = Button(window, width=5, height=2, bg="#fff", fg="#00f", font=('arial', 20, 'bold'), text="0",
                     command=lambda: number_click(0)).grid(
    row=6, column=1, pady=(0, 15), sticky="nsew")
equal_button = Button(window, width=4, height=1, bg="#fa0000", fg="#fff", activebackground="#ff3b3b",
                      font=('arial', 20, 'bold'), text="=",
                      command=lambda: equal_click()).grid(
    row=6, column=2, padx=(15, 0), pady=(15, 15), sticky="nsew")
plus_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                     font=('arial', 20, 'bold'), text="+", command=lambda: operator_click("+")).grid(
    row=6, column=3, padx=(15, 0), pady=(0, 15), sticky="nsew")
minus_button = Button(window, width=5, height=2, bg="#0052cc", fg="#fff", activebackground="#006cfa",
                      font=('arial', 20, 'bold'), text="-", command=lambda: operator_click("-")).grid(
    row=6, column=4, padx=(0, 15), pady=(0, 15), sticky="nsew")

# Preventing Window From resizing
window.resizable(0, 0)

# displaying menu

window.config(menu=menu_bar)

# Calculator mainloop
window.mainloop()
