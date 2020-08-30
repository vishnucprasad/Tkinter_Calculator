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
    memory_store.append("M+ (" + number + ")  =>  Memory = " + memory)
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
    memory_store.append("M- (" + number + ")  =>  Memory = " + memory)
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
    global memory, memory_store, is_memory_used
    memory = "0"
    is_memory_used = False
    memory_store = []


def number_click(value):
    global number, is_operator_clicked, is_calculation_complete, on_start, is_memory_clicked
    if is_operator_clicked or is_memory_clicked:
        number = str(value)
        display_value.set(number)
        is_operator_clicked = False
        is_memory_clicked = False
    elif is_calculation_complete:
        operation_value.set("")
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
        operation_value.set(operation_value.get()[0:-1] + operation)
        operator = operation
    elif is_calculate_init:
        operation_value.set(operation_value.get() + number + operation)
        perform_operation(old_number, number, operator)
        is_operator_clicked = True
        operator = operation
        old_number = number
    else:
        operation_value.set(operation_value.get() + number + operation)
        operator = operation
        old_number = number
        is_operator_clicked = True
        is_calculate_init = True
    on_start = False
    is_dot_clicked = False
    is_calculation_complete = False


def one_by_x_click():
    global number, is_calculation_complete
    operation_value.set(operation_value.get() + "1/" + number)
    if number == "0":
        display_value.set("Cannot divide by zero")
        history.append("¹/" + number + " = " + "Cannot divide by zero")
        is_calculation_complete = True
    else:
        value = float(number)
        value = 1 / value
        history.append("¹/" + number + " = " + str(value))
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
    operation_value.set(operation_value.get() + number + "^2")
    value = float(number)
    value *= value
    history.append(number + "² = " + str(value))
    integer = value.is_integer()
    if integer:
        number = str(int(value))
    else:
        number = str(value)
    display_value.set(number)
    is_calculation_complete = True


def root_click():
    global number, is_calculation_complete
    operation_value.set(operation_value.get() + "√" + number)
    result = math.sqrt(float(number))
    history.append("√" + number + " = " + str(result))
    integer = result.is_integer()
    if integer:
        number = str(int(result))
    else:
        number = str(result)
    display_value.set(number)
    is_calculation_complete = True


def cube_root():
    global number, is_calculation_complete
    operation_value.set(operation_value.get() + "∛" + number)
    value = float(number)
    if value >= 0:
        result = value ** (1. / 3.)
    else:
        result = -(-value) ** (1. / 3.)
    history.append("∛" + number + " = " + str(result))
    integer = result.is_integer()
    if integer:
        number = str(int(result))
    else:
        number = str(result)
    display_value.set(number)
    is_calculation_complete = True


def ten_raise_to():
    global number, is_calculation_complete
    operation_value.set(operation_value.get() + "10^" + number)
    result = 10 ** float(number)
    history.append(number + "^10" + " = " + str(result))
    integer = result.is_integer()
    if integer:
        number = str(int(result))
    else:
        number = str(result)
    display_value.set(number)
    is_calculation_complete = True


def percentage():
    global number, is_calculation_complete, is_calculate_init
    operation_value.set(operation_value.get() + number + "%")
    if is_calculate_init:
        if operator == "+":
            result = float(old_number) + float(number)
        elif operator == "-":
            result = float(old_number) - float(number)
        elif operator == "*":
            result = float(old_number) * float(number)
        elif operator == "/":
            result = float(old_number) / float(number)
        result = result / 100
        if operator == "+":
            history.append("(" + old_number + "+" + number + ") % = " + str(result))
        elif operator == "-":
            history.append("(" + old_number + "-" + number + ") % = " + str(result))
        elif operator == "*":
            history.append("(" + old_number + "x" + number + ") % = " + str(result))
        elif operator == "/":
            history.append("(" + old_number + "/" + number + ") % = " + str(result))
        integer = result.is_integer()
        if integer:
            number = str(int(result))
        else:
            number = str(result)
        display_value.set(number)
        is_calculation_complete = True
        is_calculate_init = False


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
    operation_value.set(operation_value.get() + number + "=")
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
    global number, operator, old_number, is_calculate_init, is_operator_clicked, is_memory_clicked, is_dot_clicked, is_calculation_complete, on_start
    is_calculate_init = False
    is_calculation_complete = False
    is_dot_clicked = False
    is_operator_clicked = False
    is_memory_clicked = False
    on_start = True
    operator = "+"
    old_number = "0"
    number = "0"
    operation_value.set("")
    display_value.set(number)


def perform_operation(first_number, second_number, operate_with):
    global number, is_zero_division_error
    if operate_with == "+":
        result = float(first_number) + float(second_number)
        history.append(first_number + "+" + second_number + " = " + str(result))
    elif operate_with == "-":
        result = float(first_number) - float(second_number)
        history.append(first_number + "-" + second_number + " = " + str(result))
    elif operate_with == '*':
        result = float(first_number) * float(second_number)
        history.append(first_number + "x" + second_number + " = " + str(result))
    elif operate_with == "/":
        if int(second_number) == 0:
            display_value.set("Cannot divide by zero")
            history.append(first_number + "/" + second_number + " = " + "Cannot divide by zero")
            is_zero_division_error = True
        else:
            result = float(first_number) / float(second_number)
            history.append(first_number + "/" + second_number + " = " + str(result))
    elif operate_with == "^":
        result = float(first_number) ** float(second_number)
        history.append(first_number + "^" + second_number + " = " + str(result))
    elif operate_with == "hyp":
        result = math.hypot(float(first_number), float(second_number))
        history.append("hyp (" + first_number + "," + second_number + ") = " + str(result))
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


def trignometric_operations(second_number, operate_with):
    global number, is_calculation_complete, is_dot_clicked
    operation_value.set(operation_value.get() + operate_with + "(" + second_number + ")")
    value = float(second_number)
    if operate_with == "sin":
        result = math.sin(math.radians(value))
        history.append("Sin (" + second_number + ") = " + str(result))
    elif operate_with == "cos":
        result = math.cos(math.radians(value))
        history.append("Cos (" + second_number + ") = " + str(result))
    elif operate_with == "tan":
        result = math.tan(math.radians(value))
        history.append("Tan (" + second_number + ") = " + str(result))
    elif operate_with == "sec":
        result = 1 / (math.cos(math.radians(value)))
        history.append("Sec (" + second_number + ") = " + str(result))
    elif operate_with == "csc":
        result = 1 / (math.sin(math.radians(value)))
        history.append("Csc (" + second_number + ") = " + str(result))
    elif operate_with == "cot":
        result = 1 / (math.tan(math.radians(value)))
        history.append("Cot (" + second_number + ") = " + str(result))
    elif operate_with == "rad":
        result = math.radians(value)
        history.append("rad (" + second_number + ") = " + str(result))
    integer = result.is_integer()
    if integer:
        number = str(int(result))
    else:
        number = str(result)
    display_value.set(str(number))
    is_calculation_complete = True
    is_dot_clicked = False


def dark_theme():
    global is_dark_theme
    displays = [display, operation_display]
    number_buttons = [one_button, two_button, three_button, four_button, five_button, six_button, seven_button,
                      eight_button, nine_button, zero_button]
    memory_control_buttons = [memory_plus_button, memory_minus_button, memory_recall_button, memory_clear_button,
                              memory_show_button, raise_to_button, square_button, one_by_x_button, sin_button,
                              cos_button, tan_button, sec_button, csc_button, cot_button, hyp_button, rad_button,
                              percent_button, ten_raise_to_x_button]
    for i in displays:
        i.config(disabledbackground="#000000", disabledforeground="#ffffff")
    for i in number_buttons:
        i.config(bg="#000", fg="#fff", activebackground="#333", activeforeground="#fff")
    for i in memory_control_buttons:
        i.config(bg="#333", fg="#fff", activebackground="#000", activeforeground="#fff")
    window.config(bg="#000")
    is_dark_theme = True


def light_theme():
    global is_dark_theme
    number_buttons = [one_button, two_button, three_button, four_button, five_button, six_button, seven_button,
                      eight_button, nine_button, zero_button]
    memory_control_buttons = [memory_plus_button, memory_minus_button, memory_recall_button, memory_clear_button,
                              memory_show_button, raise_to_button, square_button, one_by_x_button, sin_button,
                              cos_button, tan_button, sec_button, csc_button, cot_button, hyp_button, rad_button,
                              percent_button, ten_raise_to_x_button]
    for i in number_buttons:
        i.config(bg="#fff", fg="#000", activebackground="#eee", activeforeground="#000")
    for i in memory_control_buttons:
        i.config(bg="#eee", fg="#000", activebackground="#fff", activeforeground="#000")
    display.config(disabledbackground="#ffffff", disabledforeground="#000000")
    operation_display.config(disabledbackground="#ffffff", disabledforeground="#aaaaaa")
    window.config(bg="#fff")
    is_dark_theme = False


def standard():
    global is_standard
    scientific_buttons = [sin_button, cos_button, tan_button, sec_button, csc_button, cot_button, hyp_button,
                          rad_button, percent_button, ten_raise_to_x_button]
    for i in scientific_buttons:
        i.grid_forget()
    is_standard = True


def scientific():
    global is_standard
    sin_button.grid(row=3, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
    cos_button.grid(row=3, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
    tan_button.grid(row=3, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
    hyp_button.grid(row=3, column=3, padx=(0, 0), pady=(0, 0), sticky="nsew")
    rad_button.grid(row=3, column=4, padx=(0, 15), pady=(0, 0), sticky="nsew")
    sec_button.grid(row=4, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
    csc_button.grid(row=4, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
    cot_button.grid(row=4, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
    percent_button.grid(row=4, column=3, padx=(0, 0), pady=(0, 0), sticky="nsew")
    ten_raise_to_x_button.grid(row=4, column=4, padx=(0, 15), pady=(0, 0), sticky="nsew")
    bottom_buttons = [zero_button, plus_button, minus_button]
    dot_button.grid(pady=(0, 15))
    equal_button.grid(pady=(0, 15))
    for i in bottom_buttons:
        i.grid(pady=(0, 15))
    is_standard = False


def show_history():
    history_window = Toplevel(window)
    history_window.title("History")
    history_window.iconphoto(False, photo)
    scrollbar = Scrollbar(history_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    if is_standard:
        history_window.geometry("756x240+5+490")
    else:
        history_window.geometry("756x240+5+560")

    history_list = Listbox(history_window, bg="#000", fg="#fff", width=50, height=8, font=('arial', 20, 'bold'))
    history_list.pack(padx=(15, 15), pady=(15, 15))

    if is_dark_theme:
        history_window.configure(bg="#000")
        history_list.config(bg="#000", fg="#fff")
    else:
        history_window.configure(bg="#fff")
        history_list.config(bg="#fff", fg="#000")

    if history == []:
        history_list.insert(END, "Nothing to show")
    for i in history:
        history_list.insert(END, " " + i)

    history_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=history_list.yview)

    history_window.resizable(0, 0)
    history_window.mainloop()


def show_memory():
    memory_window = Toplevel(window)
    memory_window.title("Memory")
    memory_window.iconphoto(False, photo)
    scrollbar = Scrollbar(memory_window)
    scrollbar.pack(side=RIGHT, fill=Y)

    if is_standard:
        memory_window.geometry("756x240+5+490")
    else:
        memory_window.geometry("756x240+5+560")

    memory_list = Listbox(memory_window, bg="#000", fg="#fff", width=50, height=8, font=('arial', 20, 'bold'))
    memory_list.pack(padx=(15, 15), pady=(15, 15))

    if is_dark_theme:
        memory_window.configure(bg="#000")
        memory_list.config(bg="#000", fg="#fff")
    else:
        memory_window.configure(bg="#fff")
        memory_list.config(bg="#fff", fg="#000")

    if memory_store == []:
        memory_list.insert(END, "Nothing to show")
    for i in memory_store:
        memory_list.insert(END, " " + i)

    memory_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=memory_list.yview)

    memory_window.resizable(0, 0)
    memory_window.mainloop()


# Setting Up Calculator Window
window = Tk()
window.title("Calculator")
window.configure(bg="#ffffff")
window.geometry("+5+10")
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
is_dark_theme = False
is_standard = True
operator = "+"
number = "0"
old_number = "0"
memory = "0"
operation_value = StringVar()
display_value = StringVar()
display_value.set("0")
on_start = True
theme_var = IntVar()
view_var = IntVar()
history = []
memory_store = []

# Creating Menu
menu_bar = Menu(window)

# Adding File Menu and commands
file = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file)
show_menu = Menu(file, tearoff=0)
file.add_cascade(label='Show ', menu=show_menu)
show_menu.add_command(label='Show History', command=lambda: show_history())
show_menu.add_command(label='Show Memory', command=lambda: show_memory())
file.add_separator()
file.add_command(label='Exit', command=window.destroy)

# Adding Theme Menu and commands
Theme = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Theme', menu=Theme)
Theme.add_radiobutton(label='Light', value=0, variable=theme_var, command=lambda: light_theme())
Theme.add_radiobutton(label='Dark', value=1, variable=theme_var, command=lambda: dark_theme())

# Adding View Menu and commands
view = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='View', menu=view)
view.add_radiobutton(label='Standard', value=0, variable=view_var, command=lambda: standard())
view.add_radiobutton(label='Scientific', value=1, variable=view_var, command=lambda: scientific())

# Setting Up Calculator Display
operation_display = Entry(window, font=('arial', 20), textvariable=operation_value, bd=0, width=48, insertwidth=4,
                          justify="right", state=DISABLED, disabledbackground="#ffffff",
                          disabledforeground="#aaaaaa")
operation_display.grid(columnspan=5, padx=(15, 15), pady=(0, 15))

display = Entry(window, font=('arial', 40), textvariable=display_value, bd=0, width=25, insertwidth=4,
                justify="right", state=DISABLED, disabledbackground="#ffffff", disabledforeground="#000000")
display.grid(columnspan=5, padx=(15, 15))

# Setting up Calculator Buttons
# First Row
memory_clear_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                             font=('arial', 15), text="MC",
                             command=lambda: clear_memory())
memory_clear_button.grid(row=2, column=0, padx=(15, 0), pady=(15, 0), sticky="nsew")
memory_recall_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                              font=('arial', 15), text="MR",
                              command=lambda: recall_memory())
memory_recall_button.grid(row=2, column=1, padx=(0, 0), pady=(15, 0), sticky="nsew")
memory_plus_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                            font=('arial', 15), text="M+",
                            command=lambda: plus_memory())
memory_plus_button.grid(row=2, column=2, padx=(0, 0), pady=(15, 0), sticky="nsew")
memory_minus_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                             font=('arial', 15), text="M-",
                             command=lambda: minus_memory())
memory_minus_button.grid(row=2, column=3, padx=(0, 0), pady=(15, 0), sticky="nsew")
memory_show_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                            font=('arial', 15), text="MS", command=lambda: show_memory())
memory_show_button.grid(row=2, column=4, padx=(0, 15), pady=(15, 0), sticky="nsew")

# Second Row
sin_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    activeforeground="#fff", font=('arial', 15), text="Sin",
                    command=lambda: trignometric_operations(number, "sin"))
cos_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    activeforeground="#fff", font=('arial', 15), text="Cos",
                    command=lambda: trignometric_operations(number, "cos"))
tan_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    activeforeground="#fff", font=('arial', 15), text="Tan",
                    command=lambda: trignometric_operations(number, "tan"))
hyp_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    activeforeground="#fff", font=('arial', 15), text="hyp",
                    command=lambda: operator_click("hyp"))
rad_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    font=('arial', 15), text="rad",
                    command=lambda: trignometric_operations(number, "rad"))

# Third Row
sec_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    activeforeground="#fff", font=('arial', 15), text="Sec",
                    command=lambda: trignometric_operations(number, "sec"))
csc_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    activeforeground="#fff", font=('arial', 15), text="Cse",
                    command=lambda: trignometric_operations(number, "csc"))
cot_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                    activeforeground="#fff", font=('arial', 15), text="Cot",
                    command=lambda: trignometric_operations(number, "cot"))
percent_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                        activeforeground="#fff", font=('arial', 15), text="%",
                        command=lambda: percentage())
ten_raise_to_x_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                               font=('arial', 15), text="10ˣ", command=lambda: ten_raise_to())

# Fourth Row
one_by_x_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                         font=('arial', 15), text="¹/x", command=lambda: one_by_x_click())
one_by_x_button.grid(row=5, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
square_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                       font=('arial', 15), text="x²", command=lambda: square_click())
square_button.grid(row=5, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
raise_to_button = Button(window, width=5, height=1, bd=0, bg="#eee", fg="#000", activebackground="#fff",
                         font=('arial', 15), text="xʸ", command=lambda: operator_click("^"))
raise_to_button.grid(row=5, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
clear_button = Button(window, width=5, height=1, bd=0, bg="#ff4625", fg="#fff", activebackground="#ff3815",
                      activeforeground="#fff",
                      font=('arial', 15), text="C", command=lambda: clear())
clear_button.grid(row=5, column=3, padx=(0, 0), pady=(0, 0), sticky="nsew")
delete_button = Button(window, width=5, height=1, bd=0, bg="#ff4625", fg="#fff", activebackground="#ff3815",
                       activeforeground="#fff",
                       font=('arial', 15), text="⌫", command=lambda: delete())
delete_button.grid(row=5, column=4, padx=(0, 15), pady=(0, 0), sticky="nsew")

# Fifth Row
seven_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="7",
                      command=lambda: number_click(7))
seven_button.grid(row=6, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
eight_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="8",
                      command=lambda: number_click(8))
eight_button.grid(row=6, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
nine_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="9",
                     command=lambda: number_click(9))
nine_button.grid(row=6, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
pi_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                   activeforeground="#fff",
                   font=('arial', 20, 'bold'), text="π", command=lambda: pi_click())
pi_button.grid(row=6, column=3, padx=(0, 0), pady=(0, 0), sticky="nsew")
cube_root_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                          activeforeground="#fff",
                          font=('arial', 20, 'bold'), text="∛", command=lambda: cube_root())
cube_root_button.grid(row=6, column=4, padx=(0, 15), pady=(0, 0), sticky="nsew")

# Sixth Row
four_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="4",
                     command=lambda: number_click(4))
four_button.grid(row=7, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
five_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="5",
                     command=lambda: number_click(5))
five_button.grid(row=7, column=1, sticky="nsew")
six_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="6",
                    command=lambda: number_click(6))
six_button.grid(row=7, column=2, sticky="nsew")
negative_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                         activeforeground="#fff",
                         font=('arial', 20, 'bold'), text="+/-", command=lambda: negative_click())
negative_button.grid(row=7, column=3, padx=(0, 0), sticky="nsew")
root_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                     activeforeground="#fff",
                     font=('arial', 20, 'bold'), text="√ ", command=lambda: root_click())
root_button.grid(row=7, column=4, padx=(0, 15), sticky="nsew")

# Seventh Row
one_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="1",
                    command=lambda: number_click(1))
one_button.grid(row=8, column=0, padx=(15, 0), pady=(0, 0), sticky="nsew")
two_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="2",
                    command=lambda: number_click(2))
two_button.grid(row=8, column=1, sticky="nsew")
three_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="3",
                      command=lambda: number_click(3))
three_button.grid(row=8, column=2, sticky="nsew")
multiplication_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                               activeforeground="#fff",
                               font=('arial', 20, 'bold'), text="x", command=lambda: operator_click("*"))
multiplication_button.grid(row=8, column=3, padx=(0, 0), sticky="nsew")
division_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                         activeforeground="#fff",
                         font=('arial', 20, 'bold'), text="÷", command=lambda: operator_click("/"))
division_button.grid(row=8, column=4, padx=(0, 15), sticky="nsew")

# Eighth Row
dot_button = Button(window, width=5, height=1, bd=0, bg="#ff4625", fg="#fff", activebackground="#ff3815",
                    activeforeground="#fff",
                    font=('arial', 20, 'bold'), text=".", command=lambda: dot_click())
dot_button.grid(row=9, column=0, padx=(15, 0), pady=(0, 35), sticky="nsew")
zero_button = Button(window, width=5, height=1, bd=0, bg="#fff", fg="#000000", font=('arial', 20), text="0",
                     command=lambda: number_click(0))
zero_button.grid(row=9, column=1, pady=(0, 35), sticky="nsew")
equal_button = Button(window, width=5, height=1, bd=0, bg="#ff4625", fg="#fff", activebackground="#ff3815",
                      activeforeground="#fff",
                      font=('arial', 20, 'bold'), text="=",
                      command=lambda: equal_click())
equal_button.grid(row=9, column=2, padx=(0, 0), pady=(0, 35), sticky="nsew")
plus_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                     activeforeground="#fff",
                     font=('arial', 20, 'bold'), text="+", command=lambda: operator_click("+"))
plus_button.grid(row=9, column=3, padx=(0, 0), pady=(0, 35), sticky="nsew")
minus_button = Button(window, width=5, height=1, bd=0, bg="#f07800", fg="#fff", activebackground="#f08113",
                      activeforeground="#fff",
                      font=('arial', 20, 'bold'), text="-", command=lambda: operator_click("-"))
minus_button.grid(row=9, column=4, padx=(0, 15), pady=(0, 35), sticky="nsew")

# Preventing Window From resizing
window.resizable(0, 0)

# displaying menu

window.config(menu=menu_bar)

# Calculator mainloop
window.mainloop()
