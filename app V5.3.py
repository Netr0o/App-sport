import tkinter as tk


class MyApp:
    def __init__(self, root):
        self.root = root
        self.is_dark_mode = False

        self.dark_mode = {
            'bg': "white",
            'fg': "black",
            'entry_bg': "#eee",
            'entry_fg': "black",
            'btn_bg': "#ddd",
            'btn_fg': "black",
            'font': ("open_sans", 15)
        }

        self.light_mode = {
            'bg': "#333",
            'fg': "white",
            'entry_bg': "#555",
            'entry_fg': "white",
            'btn_bg': "#444",
            'btn_fg': "white",
            'font': ("open_sans", 15)
        }

        self.label = tk.Label(root, text="Weight")
        self.label.grid(row=0, column=0, padx=0, pady=0, ipadx=5, ipady=5, sticky=tk.W)

        self.Entry_weight = tk.Entry(root, width=5)
        self.Entry_weight.grid(row=0, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.Entry_weight.bind("<KeyRelease>", lambda event: self.calcul())

        self.label = tk.Label(root, text="Reps")
        self.label.grid(row=1, column=0, padx=0, pady=0, ipadx=5, ipady=5, sticky=tk.W)

        self.Entry_reps = tk.Entry(root, width=5)
        self.Entry_reps.grid(row=1, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.Entry_reps.bind("<KeyRelease>", lambda event: self.calcul())

        self.label_result = tk.Label(root, text=(
            "Estimate 1RM :\n" +
            "3 rep : -> 95% of 1rm\n" +
            "5 rep : -> 90% of 1rm\n" +
            "8 rep : -> 80% of 1rm\n" +
            "10 rep : -> 75% of 1rm\n" +
            "12 rep : -> 70% of 1rm\n" +
            "15 rep : -> 65% of 1rm\n"
        ))
        self.label_result.grid(row=2, column=0, columnspan=3, padx=0, pady=0, ipadx=0, ipady=0)

        self.Entry_ratio = tk.Entry(root)
        self.Entry_ratio.grid(row=3, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.label_ratio = tk.Label(root, text=str(""))
        self.label_ratio.grid(row=3, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.button_ratio = tk.Button(root, text="Calcul du ratio", command=self.ratio)
        self.button_ratio.grid(row=4, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.kg_label = tk.Label(root, text="Weight in kg :")
        self.kg_label.grid(row=5, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.kg_entry = tk.Entry(root)
        self.kg_entry.grid(row=5, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.kg_entry.bind("<KeyRelease>", lambda event: self.kg_to_lbs())

        self.lbs_label = tk.Label(root, text="Weight in pounds :")
        self.lbs_label.grid(row=6, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.lbs_entry = tk.Entry(root)
        self.lbs_entry.grid(row=6, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.lbs_entry.bind("<KeyRelease>", lambda event: self.lbs_to_kg())

        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=2, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.NE)

        self.button_switch = tk.Button(self.frame, text="Switch", command=self.switch)
        self.button_switch.grid(row=0, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.NE)

        self.help_window = tk.Button(self.frame, text="help", command=lambda: HelpWindow(
            self.root,
            'help_window',
            'This app is made to help you to find your 1RM\n'
            '(1 rep max) with a weight that you use at a precise\n'
            'number of repetition. For example if you push 50kg\n'
            'for 10 rep, your 1RM will be approximately 67kg\n'
            '(the result is not exact it can change a bit between\n'
            '2 people). There is also a setting to calcultate your\n'
            'body weight ratio with your 1rm and a simple calculator.',
            self.dark_mode if self.is_dark_mode else self.light_mode
        )
                                     )
        self.help_window.grid(row=1, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.NE)

        self.apply_theme(self.light_mode)  # it applies the initial theme, not like before because I'm just a huge autistic monkey as fuck

    def apply_theme(self, theme):
        self.root.config(bg=theme['bg'])
        self.recursive_theme_apply(self.root, theme)

    def recursive_theme_apply(self, parent, theme):
        for widget in parent.winfo_children():
            widget_type = widget.winfo_class()

            if widget_type == 'Label':
                widget.config(bg=theme['bg'], fg=theme['fg'], font=theme['font'])
            elif widget_type == 'Entry':
                widget.config(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['fg'], font=theme['font'])
            elif widget_type == 'Button':
                widget.config(bg=theme['btn_bg'], fg=theme['btn_fg'], font=theme['font'])
            elif widget_type == 'Frame':
                widget.config(bg=theme['bg'])
                self.recursive_theme_apply(widget, theme)

    def switch(self):
        if self.is_dark_mode:
            self.apply_theme(self.light_mode)
        else:
            self.apply_theme(self.dark_mode)

        self.is_dark_mode = not self.is_dark_mode

    def calcul(self):
        try:
            weight = float(self.Entry_weight.get())
            reps = float(self.Entry_reps.get())

            self.result = weight / (1.0278 - 0.0278 * reps)
            percentage = [0.94, 0.90, 0.80, 0.75, 0.70, 0.65]
            results = [self.result * p for p in percentage]

            self.label_result.config(text=(
                    f"estimate 1RM : {self.result:.1f}\n" +
                    f"3 rep : {results[0]:.1f} -> 95% of 1rm\n" +
                    f"5 rep : {results[1]:.1f} -> 90% of 1rm\n" +
                    f"8 rep : {results[2]:.1f} -> 80% of 1rm\n" +
                    f"10 rep : {results[3]:.1f} -> 75% of 1rm\n" +
                    f"12 rep : {results[4]:.1f} -> 70% of 1rm\n" +
                    f"15 rep : {results[5]:.1f} -> 65% of 1rm\n"
            ))
            return self.result
        except ValueError:
            self.label_result.config(text="please enter correct number ! (1; 2; 3; 4; 5; 6; 7; 8; 9)")

    def ratio(self):
        try:
            bw = float(self.Entry_ratio.get())
            ratio = round(self.result/bw, 2)
            self.label_ratio.config(text=ratio)
        except ValueError:
            self.label_ratio.config(text="please enter correct number ! (1; 2; 3; 4; 5; 6; 7; 8; 9)")

    def kg_to_lbs(self):
        try:
            kg = float(self.kg_entry.get())
            lbs = kg * 2.20462
            self.lbs_entry.delete(0, tk.END)
            self.lbs_entry.insert(0, str(round(lbs, 2)))
        except ValueError:
            pass

    def lbs_to_kg(self):
        try:
            lbs = float(self.lbs_entry.get())
            kg = lbs / 2.20462
            self.kg_entry.delete(0, tk.END)
            self.kg_entry.insert(0, str(round(kg, 2)))
        except ValueError:
            pass


class HelpWindow(tk.Toplevel):

    def __init__(self, parent, title, message, theme):
        super().__init__(parent)
        self.theme = theme

        self.title(title)
        self.geometry("350x200")
        self.config(bg=self.theme['bg'])

        self.label = tk.Label(self, text=message, bg=self.theme['bg'], fg=self.theme['fg'])
        self.label.pack(pady=20, padx=20)

        self.ok_button = tk.Button(self, text="ok", bg=self.theme['btn_bg'], fg=self.theme['btn_fg'], command=self.destroy)
        self.ok_button.pack(pady=10)


root = tk.Tk()
root.title("App")
app = MyApp(root)
root.mainloop()