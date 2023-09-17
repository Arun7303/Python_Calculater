import tkinter as tk
win = tk.Tk()
win.geometry("321x324")
win.resizable(0, 0)
win.title("calculator")


input_value = ""

display_txt = tk.StringVar()


def click_button(item):
    global input_value
    input_value = input_value+str(item)
    display_txt.set(input_value)


def clear_button():
    global input_value
    input_value = ""
    display_txt.set("")


def equal_button():
    global input_value
    result = str(eval(input_value))
    display_txt.set(result)
    input_value = result  # ""


input_frame = tk.Frame(win, width=312, height=50, bd=0,
                       highlightbackground="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)


input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'),
                       textvariable=display_txt, width=50, bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


bt_frme = tk.Frame(win, width=321, height=272.5, bg="grey")
bt_frme.pack()

clear_btn = tk.Button(bt_frme, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
                      cursor="hand2", command=lambda: clear_button()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide_btn = tk.Button(bt_frme, text="/", fg="black", width=10, height=3, bd=0, bg="#eee",
                       cursor="hand2", command=lambda: click_button("/")).grid(row=0, column=3, padx=1, pady=1)


btn_7 = tk.Button(bt_frme, text="7", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("7")).grid(row=1, column=0, padx=1, pady=1)
btn_8 = tk.Button(bt_frme, text="8", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("8")).grid(row=1, column=1, padx=1, pady=1)
btn_9 = tk.Button(bt_frme, text="9", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("9")).grid(row=1, column=2, padx=1, pady=1)
btn_multi = tk.Button(bt_frme, text="*", fg="black", width=10, height=3, bd=0, bg="#fff",
                      cursor="hand2", command=lambda: click_button("*")).grid(row=1, column=3, padx=1, pady=1)


btn_4 = tk.Button(bt_frme, text="4", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("4")).grid(row=2, column=0, padx=1, pady=1)
btn_5 = tk.Button(bt_frme, text="5", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("5")).grid(row=2, column=1, padx=1, pady=1)
btn_7 = tk.Button(bt_frme, text="6", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("6")).grid(row=2, column=2, padx=1, pady=1)
btn_sub = tk.Button(bt_frme, text="-", fg="black", width=10, height=3, bd=0, bg="#fff",
                    cursor="hand2", command=lambda: click_button("-")).grid(row=2, column=3, padx=1, pady=1)


btn_1 = tk.Button(bt_frme, text="1", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("1")).grid(row=3, column=0, padx=1, pady=1)
btn_2 = tk.Button(bt_frme, text="2", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("2")).grid(row=3, column=1, padx=1, pady=1)
btn_3 = tk.Button(bt_frme, text="3", fg="black", width=10, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("3")).grid(row=3, column=2, padx=1, pady=1)
btn_add = tk.Button(bt_frme, text="+", fg="black", width=10, height=3, bd=0, bg="#fff",
                    cursor="hand2", command=lambda: click_button("+")).grid(row=3, column=3, padx=1, pady=1)


btn_0 = tk.Button(bt_frme, text="0", fg="black", width=21, height=3, bd=0, bg="#fff",
                  cursor="hand2", command=lambda: click_button("0")).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
btn_point = tk.Button(bt_frme, text=".", fg="black", width=10, height=3, bd=0, bg="#eee",
                      cursor="hand2", command=lambda: click_button(".")).grid(row=4, column=2, padx=1, pady=1)
btn_equal = tk.Button(bt_frme, text="=", fg="black", width=10, height=3, bd=0, bg="#eee",
                      cursor="hand2", command=lambda: equal_button()).grid(row=4, column=3, padx=1, pady=1)

win.mainloop()
