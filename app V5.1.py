import tkinter as tk
import tkinter.font as font

correction = None

#color and writting police variable
color1 = '#2A2A2A'  #main background
color2 = '#FFFFFF' #writting
color3 = '#3A3A3A' #help background window

police = "impact"
police_size = 8
police_size2 = 6
size_result = police_size + 3


#main function : 1RM calcul
def brzycki_formula(event=None):
    global correction
    try:
        # entry value for weight and rep
        # 1RM and percentage calcul
        w = float(entry_value1.get())
        r = float(entry_value2.get())
        global result
        result = w / (1.0278 - 0.0278 * r)
        percentage = [0.9, 0.8, 0.7, 0.6, 0.5]
        results = [result * p for p in percentage]

        # update the display on the screen
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


#help screen function
def open_help_screen():
    help_window = tk.Toplevel(window)
    help_window.title("Help Screen")
    help_window.geometry("600x450")
    help_window.config(bg=color3)
#help text
    help_text = "This app is made to help you to find your 1RM (1 rep max) with a weight that you use at a precise number of repetition. For example if you push 50kg for 10 rep, your 1RM will be approximately 67kg (the result is not exact it can change a bit between 2 people). There is also a setting to calcultate your body weight ratio with your 1rm and a simple calculator."
    
    #creation of help text screen and display of the help on the screen
    text_widget = tk.Text(help_window, wrap="word")
    text_widget.config(bg=color3, fg=color2)
    text_widget.insert(tk.END, help_text)
    text_widget.pack(expand=True, fill="both")
    
    #set as diseable the state of the help widget
    text_widget.config(state="disabled")

    #ajout de la barre vertical de scroll du texte d'aide du widget
    #
    scrollbar = tk.Scrollbar(help_window, orient=tk.VERTICAL, command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.config(yscrollcommand=scrollbar.set)

#conversion entre kilo et livres et inversement
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
    try:
        bw = float(entry_bw.get())
        ratio = result / bw
        label_ratio_calcul.config(text="ratio: " + str(ratio))
    except ValueError:
        label_ratio_calcul.config(text="please enter a correct number")


def theme_switch():
    switch = tk.button

        

def button_click(item):
    if item == 'C':
        entry.delete(0, tk.END)
    elif item == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, item)


# main window
window = tk.Tk()
window.title("calculator 1RM")
window.config(bg=color1)


# creation de la frame
frame = tk.Frame(window, bg=color1, bd=16, width=400, height=300)
frame.grid(row=0, column=0, sticky="nsew")

frame2 = tk.Frame(frame, bg=color1, bd=16, width=400, height=1080)
frame2.grid(row=15, column=0, sticky="nsew")

frame3 = tk.Frame(window, bg=color1, bd=16, width=400, height=300)
frame3.grid(row=20, column=0, sticky="nsew")


#calculator

entry = tk.Entry(frame3, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_num = 1
col_num = 0
for button in buttons:
    if col_num == 4:
        col_num = 0
        row_num += 1
    tk.Button(frame3, text=button, padx=20, pady=20, font=(police, police_size), bg=color1, fg=color2, border=0, command=lambda item=button: button_click(item)).grid(row=row_num, column=col_num, sticky="nsew")
    col_num += 1

# Configure grid weights
for i in range(4):
    frame3.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    frame3.grid_rowconfigure(i, weight=1)



# conversion unit display
label_kg = tk.Label(frame2, text="Kilogrammes:", font=(police, police_size2))
label_kg.grid(row=11, column=0)

entry_kg = tk.Entry(frame2)
entry_kg.config(font=(police, police_size2))
entry_kg.grid(row=11, column=1)
entry_kg.bind("<KeyRelease>", lambda event: kg_to_lbs())

label_lbs = tk.Label(frame2, text="pounds:", font=(police, police_size2))
label_lbs.grid(row=12, column=0)

entry_lbs = tk.Entry(frame2)
entry_lbs.config(font=(police, police_size2))
entry_lbs.grid(row=12, column=1)
entry_lbs.bind("<KeyRelease>", lambda event: lbs_to_kg())


# entry for values to input
label_value1 = tk.Label(frame, text="weight in kg :")
label_value1.config(font=(police, size_result), bg=color1, fg=color2)
label_value1.grid(row=0, column=0, pady=10)
entry_value1 = tk.Entry(frame)
entry_value1.grid(row=1, column=0, pady=10)
entry_value1.bind("<KeyRelease>", brzycki_formula)

label_value2 = tk.Label(frame, text="number of reps :")
label_value2.config(font=(police, size_result), bg=color1, fg=color2)
label_value2.grid(row=2, column=0, pady=10)
entry_value2 = tk.Entry(frame)
entry_value2.grid(row=3, column=0, pady=10)
entry_value2.bind("<KeyRelease>", brzycki_formula)

# button help
button_help = tk.Button(frame, text="help", command=open_help_screen)
button_help.config(font=(police, 10), borderwidth=5, highlightthickness=5)
button_help.grid(row=0, column=1)


# affichage des resultats
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

label_result_50 = tk.Label(
frame, text="50% of 1RM : "
)
label_result_50.config(background=color1, font=(police, police_size), fg=color2)
label_result_50.grid(row=10, column=0)

# affichage de pourcentage de 1rm

label_ratio = tk.Label(frame, text="enter your body weight",  font=(police, police_size2))
label_ratio.grid(row=13, column=0)

entry_bw = tk.Entry(frame)
entry_bw.grid(row=13, column=1)

label_ratio_calcul = tk.Button(frame, text="calcul ratio",  font=(police, police_size2), command=body_weight)
label_ratio_calcul.config(font=(police, police_size2), borderwidth=5, highlightthickness=5)
label_ratio_calcul.grid(row=14, column=0)


window.mainloop()