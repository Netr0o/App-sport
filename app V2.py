import tkinter as tk

correction = None

def calcul():   
    global correction
    
    try:
        # Récupérer les valeurs des Entry et effectuer le calcul
        w = float(entry_valeur1.get())
        r = float(entry_valeur2.get())
        
        if weight_unit.get() == "lbs":
            # Convertir le poids de livres à kilogrammes
            w = w * 0.453592
        
        resultat = w / (1.0278 - 0.0278 * r)
        pourcentages = [0.9, 0.8, 0.7, 0.6, 0.5]
        resultats = [resultat * p for p in pourcentages]

        # Mettre à jour l'affichage du résultat
        label_resultat.config(text="1RM estimé : " + str(round(resultat, 0)))
        label_resultat_90.config(text="90% de 1RM : " + str(round(resultats[0], 0)) + " --> 4 reps")
        label_resultat_80.config(text="80% de 1RM : " + str(round(resultats[1], 0)) + " --> 8 reps")
        label_resultat_70.config(text="70% de 1RM : " + str(round(resultats[2], 0)) + " --> 11 reps")
        label_resultat_60.config(text="60% de 1RM : " + str(round(resultats[3], 0)) + " --> 15 reps")
        label_resultat_50.config(text="50% de 1RM : " + str(round(resultats[4], 0)) + " --> 19 reps")
    except ValueError:       
        if not correction:
            correction = tk.Label(label_resultat, wraplength=600)
        correction.config(text="please enter correct number ! (1; 2; 3; 4; 5; 6; 7; 8; 9)", bg='#0404B4', fg='red', font=("impact", 9))
        correction.pack()
    else:
        if correction:
            correction.pack_forget()

        
#fenetre aide
def open_help_screen():
    help_window = tk.Toplevel(window)
    help_window.title("Help Screen")
    help_window.geometry("720x700")
    help_window.config(bg='blue')
    # Content of the help screen
    help_label = tk.Label(help_window, wraplength=600, text="This app is made to help you to find your 1RM (1 rep max) with a weight that you use at a precise number of repetition. For exemple if you push 50kg for 10 rep, your 1RM will be aproximatively 67. There is also an setting to change the weight between kg and lbs, but the result if you enter in lbs will be in kg.")
    help_label.config(bg='blue', fg='white')
    help_label.pack(pady=20)
    
            
#weight unit

def choose_unit_screen():
    choose_unit = tk.Toplevel(frame2)
    choose_unit.geometry("200x160")
    choose_unit.config(bg='blue')
    choose_label = tk.Label(choose_unit, wraplength=600)
    choose_label.config(bg='blue', fg='white')
    choose_label.grid(row=0, column=0, pady=10)
    label_weight_unit = tk.Label(choose_unit)
    label_weight_unit.config(font=("impact", 9), bg='blue', fg='white')
    label_weight_unit.grid(row=4, column=0, pady=5)

    radio_kg = tk.Radiobutton(choose_unit, text="kg", variable=weight_unit, value="kg")
    radio_kg.config(bg='#0404B4', fg='white', font=("impact", 9))
    radio_kg.grid(row=0, column=1, pady=5)
    radio_kg.select()

    radio_lbs = tk.Radiobutton(choose_unit, text="lbs", variable=weight_unit, value="lbs")
    radio_lbs.config(bg='#0404B4', fg='white', font=("impact", 9))
    radio_lbs.grid(row=1, column=1, pady=5)
    
    def update_radio_buttons():
        current_unit = weight_unit.get()
        if current_unit == "kg":
            radio_kg.config(bg='grey')
            radio_lbs.config(bg='#0404B4')
        elif current_unit == "lbs":
            radio_lbs.config(bg='grey')
            radio_kg.config(bg='#0404B4')
    def kg_selected():
        weight_unit.set("kg")
        update_radio_buttons()

    def lbs_selected():
        weight_unit.set("lbs")
        update_radio_buttons()
    radio_kg.config(command=kg_selected)
    radio_lbs.config(command=lbs_selected)
    update_radio_buttons()
    
    
    return radio_kg, radio_lbs  # Renvoie les boutons radios pour pouvoir les utiliser


#conversion
def kg_to_lbs():
    try:
        kg = float(entry_kg.get())
        lbs = kg * 2.20462
        entry_lbs.delete(0, tk.END)
        entry_lbs.insert(0, str(round(lbs, 0)))
    except ValueError:
        pass

def lbs_to_kg():
    try:
        lbs = float(entry_lbs.get())
        kg = lbs / 2.20462
        entry_kg.delete(0, tk.END)
        entry_kg.insert(0, str(round(kg, 0)))
    except ValueError:
        pass
        

# 1ere fenetre
window = tk.Tk()
window.title("calculateur 1RM")
window.config(background='#0404B4')


window.rowconfigure(0, weight=1, minsize=300)  # Poids pour la première ligne
window.columnconfigure(0, weight=1, minsize=400)  # Poids pour la première colonne
window.columnconfigure(1, weight=1, minsize=400)  # Poids pour la deuxième colonne

# creation de la frame
frame = tk.Frame(window, bg='#0404B4', bd=16, width=400, height=300)
frame.grid(row=0, column=0, sticky="nsew")
#frame2
frame2 = tk.Frame(window, bg='#0404B4', bd=16, width=400, height=1080)
frame2.grid(row=0, column=1, sticky="nsew")
#frame3
frame3 = tk.Frame(window, bg='#0404B4', bd=16, width=400, height=720)
frame3.grid(row=1, column=1)

weight_unit = tk.StringVar()
weight_unit.set("kg")  # Par défaut, le poids est en kilogrammes

radio_kg, radio_lbs = choose_unit_screen()



#
label_kg = tk.Label(frame3, text="Kilogrammes:", font=("impact", 7))
label_kg.grid(row=5, column=0)

entry_kg = tk.Entry(frame3)
entry_kg.config(font=("impact", 5))
entry_kg.grid(row=5, column=1)
entry_kg.bind("<KeyRelease>", lambda event: kg_to_lbs())

label_lbs = tk.Label(frame3, text="Livres:", font=("impact", 7))
label_lbs.grid(row=6, column=0)

entry_lbs = tk.Entry(frame3)
entry_lbs.config(font=("impact", 5))
entry_lbs.grid(row=6, column=1)
entry_lbs.bind("<KeyRelease>", lambda event: lbs_to_kg())


# Entrées pour les valeurs à rentrer
label_valeur1 = tk.Label(frame, text="weight in kg :")
label_valeur1.config(font=("impact", 12), bg='#0404B4', fg='white')
label_valeur1.pack(pady=10)
entry_valeur1 = tk.Entry(frame)
entry_valeur1.pack(pady=10)
label_valeur2 = tk.Label(frame, text="number of reps :")
label_valeur2.config(font=("impact", 12), bg='#0404B4', fg='white')
label_valeur2.pack(pady=10)
entry_valeur2 = tk.Entry(frame)
entry_valeur2.pack(pady=10)


# Bouton calcul
bouton_calculer = tk.Button(frame, text="Calculate", command=calcul)
bouton_calculer.config(fg='#0404B4', bg='white', font=("impact", 15), borderwidth=5, highlightthickness=5)
bouton_calculer.pack(pady=10)


#bouton help
bouton_help = tk.Button(frame2, text= "help", command=open_help_screen)
bouton_help.config(font=("impact", 12), borderwidth=5, highlightthickness=5)
bouton_help.grid(row=0, column=0)


#bouton unités
bouton_unit = tk.Button(frame2, text="choose unit", command=choose_unit_screen)
bouton_unit.config(font=("impact", 12), borderwidth=5, highlightthickness=5)
bouton_unit.grid(row=4, column=0)

# résultat
label_resultat = tk.Label(frame, text="estimed 1RM : ")
label_resultat.config(background='#0404B4', font=("impact", 9), fg='white')
label_resultat.pack(pady=10)
label_resultat_90 = tk.Label(frame, text="90% of 1RM : ")
label_resultat_90.config(background='#0404B4', font=("impact", 7), fg='white')
label_resultat_90.pack(pady=10)
label_resultat_80 = tk.Label(frame, text="80% of 1RM : ")
label_resultat_80.config(background='#0404B4', font=("impact", 7), fg='white')
label_resultat_80.pack(pady=10)
label_resultat_70 = tk.Label(frame, text="70% of 1RM : ")
label_resultat_70.config(background='#0404B4', font=("impact", 7), fg='white')
label_resultat_70.pack(pady=10)
label_resultat_60 = tk.Label(frame, text="60% of 1RM : ")
label_resultat_60.config(background='#0404B4', font=("impact", 7), fg='white')
label_resultat_60.pack(pady=10)
label_resultat_50 = tk.Label(frame, text="50% of 1RM : ")
label_resultat_50.config(background='#0404B4', font=("impact", 7), fg='white')
label_resultat_50.pack(pady=10)

window.mainloop()