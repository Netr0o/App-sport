import tkinter as tk

correction = None

color1 = '#04146B'
color2 = 'white'
color3 = 'blue'

police = "impact"
police_size = 17
police_size2 = 14
size_result = police_size + 3

def brzycki_formula(event=None):
    global correction
    try:
        # Retrieve the input values and perform the calculation
        w = float(entry_value1.get())
        r = float(entry_value2.get())
        global result
        result = w / (1.0278 - 0.0278 * r)
        percentage = [0.9, 0.8, 0.7, 0.6, 0.5]
        results = [result * p for p in percentage]

        # update the display of the screen
        label_result.config(text="estimate 1RM : " + str(round(result, 2)))
        label_result_90.config(text="90% of 1RM : " + str(round(results[0], 2)) + " --> 4 reps")
        label_result_80.config(text="80% of 1RM : " + str(round(results[1], 2)) + " --> 8 reps")
        label_result_70.config(text="70% of 1RM : " + str(round(results[2], 2)) + " --> 11 reps")
        label_result_60.config(text="60% of 1RM : " + str(round(results[3], 2)) + " --> 15 reps")
        label_result_50.config(text="50% of 1RM : " + str(round(results[4], 2)) + " --> 19 reps")
    except ValueError:
        if not correction:
            correction = tk.Label(label_result, wraplength=600)
        correction.config(text="please enter correct number ! (1; 2; 3; 4; 5; 6; 7; 8; 9)", bg=color1, fg='red', font=(police, 9))
        correction.pack()
    else:
        if correction:
            correction.pack_forget()


# window aide
def open_help_screen():
    help_window = tk.Toplevel(window)
    help_window.title("Help Screen")
    help_window.geometry("600x300")
    help_window.config(bg=color3)

    # Content of the help screen
    help_label = tk.Label(help_window, wraplength=600, text="This app is made to help you to find your 1RM (1 rep max) with a weight that you use at a precise number of repetition. For example if you push 50kg for 10 rep, your 1RM will be approximately 67. There is also an setting to change the weight between kg and lbs, but the result if you enter in lbs will be in kg.")
    help_label.config(bg=color3, fg=color2)
    help_label.pack(pady=20)


def kg_to_lbs():
    try:
        kg = float(entry_kg.get())
        lbs = kg * 2.20462
        entry_lbs.delete(0, tk.END)
        entry_lbs.insert(0, str(round(lbs, 2)))
    except ValueError:
        pass


def lbs_to_kg():
    try:
        lbs = float(entry_lbs.get())
        kg = lbs / 2.20462
        entry_kg.delete(0, tk.END)
        entry_kg.insert(0, str(round(kg, 2)))
    except ValueError:
        pass


def body_weight():
    bw = float(entry_bw.get())
    ratio = result/bw
    label_ratio_calcul.config(text="ratio: " + str(ratio))


# main window
window = tk.Tk()
window.title("calculator 1RM")
window.config(background=color1)


# creation de la frame
frame = tk.Frame(window, bg=color1, bd=16, width=400, height=300)
frame.grid(row=0, column=0, sticky="nsew")
frame2 = tk.Frame(window, bg=color1, bd=16, width=400, height=1080)
frame2.grid(row=0, column=1, sticky="nsew")


# conversion unit display
label_kg = tk.Label(frame, text="Kilogrammes:", font=(police, police_size2))
label_kg.grid(row=11, column=0)

entry_kg = tk.Entry(frame)
entry_kg.config(font=(police, police_size2))
entry_kg.grid(row=11, column=1)
entry_kg.bind("<KeyRelease>", lambda event: kg_to_lbs())

label_lbs = tk.Label(frame, text="pounds:", font=(police, police_size2))
label_lbs.grid(row=12, column=0)

entry_lbs = tk.Entry(frame)
entry_lbs.config(font=(police, police_size2))
entry_lbs.grid(row=12, column=1)
entry_lbs.bind("<KeyRelease>", lambda event: lbs_to_kg())


# entry for values to input
label_value1 = tk.Label(frame, text="weight in kg :")
label_value1.config(font=(police, size_result), bg=color1, fg=color2)
label_value1.grid(row=0, column=0, pady=10)
entry_value1 = tk.Entry(frame)
entry_value1.config(font=police_size2)
entry_value1.grid(row=1, column=0, pady=10)
entry_value1.bind("<KeyRelease>", brzycki_formula)

label_value2 = tk.Label(frame, text="number of reps :")
label_value2.config(font=(police, size_result), bg=color1, fg=color2)
label_value2.grid(row=2, column=0, pady=10)
entry_value2 = tk.Entry(frame)
entry_value2.config(font=police_size2)
entry_value2.grid(row=3, column=0, pady=10)
entry_value2.bind("<KeyRelease>", brzycki_formula)

# button help
button_help = tk.Button(frame2, text="help", command=open_help_screen)
button_help.config(font=(police, 10), borderwidth=5, highlightthickness=5)
button_help.grid(row=0, column=0)


# result
label_result = tk.Label(frame, text="estimate 1RM : ")
label_result.config(background=color1, font=(police, size_result), fg=color2)
label_result.grid(row=5, column=0)

label_result_90 = tk.Label(frame, text="90% of 1RM : ")
label_result_90.config(background=color1, font=(police, police_size), fg=color2)
label_result_90.grid(row=6, column=0)

label_result_80 = tk.Label(frame, text="80% of 1RM : ")
label_result_80.config(background=color1, font=(police, police_size), fg=color2)
label_result_80.grid(row=7, column=0)

label_result_70 = tk.Label(frame, text="70% of 1RM : ")
label_result_70.config(background=color1, font=(police, police_size), fg=color2)
label_result_70.grid(row=8, column=0)

label_result_60 = tk.Label(frame, text="60% of 1RM : ")
label_result_60.config(background=color1, font=(police, police_size), fg=color2)
label_result_60.grid(row=9, column=0)

label_result_50 = tk.Label(frame, text="50% of 1RM : ")
label_result_50.config(background=color1, font=(police, police_size), fg=color2)
label_result_50.grid(row=10, column=0)

label_ratio = tk.Label(frame, text="enter your body weight",  font=(police, police_size2))
label_ratio.grid(row=5, column=1)
entry_bw = tk.Entry(frame)
entry_bw.config(font=police_size2)
entry_bw.grid(row=5, column=2)
label_ratio_calcul = tk.Button(frame, text="calcul ratio",  font=(police, police_size2), command=body_weight)
label_ratio_calcul.config(font=(police, police_size2), borderwidth=5, highlightthickness=5)
label_ratio_calcul.grid(row=6, column=1)


window.mainloop()