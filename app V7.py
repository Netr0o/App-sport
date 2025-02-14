import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3


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

        self.container = tk.Frame(root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, SecondPage):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")
        self.apply_theme(self.light_mode)

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def apply_theme(self, theme):
        self.root.config(bg=theme['bg'])
        self.recursive_theme_apply(self.container, theme)

    def recursive_theme_apply(self, parent, theme):
        for widget in parent.winfo_children():
            widget_type = widget.winfo_class()

            if widget_type == 'Label':
                widget.config(bg=theme['bg'], fg=theme['fg'], font=theme['font'])
            elif widget_type == 'Entry':
                widget.config(bg=theme['entry_bg'], fg=theme['entry_fg'], insertbackground=theme['fg'],
                              font=theme['font'])
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


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="Weight")
        self.label.grid(row=0, column=0, padx=0, pady=0, ipadx=5, ipady=5, sticky=tk.W)

        self.Entry_weight = tk.Entry(self, width=5)
        self.Entry_weight.grid(row=0, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.Entry_weight.bind("<KeyRelease>", lambda event: self.calcul())

        self.label = tk.Label(self, text="Reps")
        self.label.grid(row=1, column=0, padx=0, pady=0, ipadx=5, ipady=5, sticky=tk.W)

        self.Entry_reps = tk.Entry(self, width=5)
        self.Entry_reps.grid(row=1, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.Entry_reps.bind("<KeyRelease>", lambda event: self.calcul())

        self.label_result = tk.Label(self, text=(
                "Estimate 1RM :\n" +
                "3 rep : -> 95% of 1rm\n" +
                "5 rep : -> 90% of 1rm\n" +
                "8 rep : -> 80% of 1rm\n" +
                "10 rep : -> 75% of 1rm\n" +
                "12 rep : -> 70% of 1rm\n" +
                "15 rep : -> 65% of 1rm\n"
        ))
        self.label_result.grid(row=2, column=0, columnspan=3, padx=0, pady=0, ipadx=0, ipady=0)

        self.Entry_ratio = tk.Entry(self)
        self.Entry_ratio.grid(row=3, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.label_ratio = tk.Label(self, text=str(""))
        self.label_ratio.grid(row=3, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.button_ratio = tk.Button(self, text="Calcul du ratio", command=self.ratio)
        self.button_ratio.grid(row=4, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.kg_label = tk.Label(self, text="Weight in kg :")
        self.kg_label.grid(row=5, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.kg_entry = tk.Entry(self)
        self.kg_entry.grid(row=5, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.kg_entry.bind("<KeyRelease>", lambda event: self.kg_to_lbs())

        self.lbs_label = tk.Label(self, text="Weight in pounds :")
        self.lbs_label.grid(row=6, column=0, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)

        self.lbs_entry = tk.Entry(self)
        self.lbs_entry.grid(row=6, column=1, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.W)
        self.lbs_entry.bind("<KeyRelease>", lambda event: self.lbs_to_kg())

        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=3, padx=0, pady=0, ipadx=0, ipady=0, sticky=tk.NE)

        self.button_switch = tk.Button(self.frame, text="Switch", command=controller.switch)
        self.button_switch.grid(row=0, column=0, padx=0, pady=0, ipadx=0, ipady=0)

        # def __init__(self, parent, title, message, theme):
        self.help_window = tk.Button(self.frame, text="help", command=lambda: HelpWindow(
            self,
            'help_window',
            'This app is made to help you to find your 1RM\n'
            '(1 rep max) with a weight that you use at a precise\n'
            'number of repetition. For example if you push 50kg\n'
            'for 10 rep, your 1RM will be approximately 67kg\n'
            '(the result is not exact it can change a bit between\n'
            '2 people). There is also a setting to calculate your\n'
            'body weight ratio with your 1rm and a simple calculator.',
            self.controller.dark_mode if self.controller.is_dark_mode else self.controller.light_mode
        ))
        self.help_window.grid(row=1, column=0, padx=0, pady=0, ipadx=0, ipady=0)

        self.page_button = tk.Button(self.frame, text="SBD performances",
                                     command=lambda: controller.show_frame("SecondPage"))
        self.page_button.grid(row=2, column=0, padx=0, pady=0)

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
            ratio = round(self.result / bw, 2)
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


class DBHandler:

    def __init__(self, db_name='performances.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS squat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL NOT NULL,
            date INTEGER
            );
        ''')

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS bench (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL NOT NULL,
            date INTEGER
            );
        ''')

        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS deadlift (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            weight REAL NOT NULL,
            date INTEGER
            );
        ''')

        self.conn.commit()

    def save_performances(self, table_name, date, weight):
        query = f'''INSERT INTO {table_name} (date, weight)
            VALUES (?, ?)'''
        self.cursor.execute(query, (date, weight))
        self.conn.commit()

    def get_performances(self, table_name):
        query = f'''SELECT weight, date FROM {table_name}'''
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


class SecondPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.db = DBHandler()
        self.controller = controller

        self.back_button = tk.Button(self, text="return to the 1rm calculator",
                                     command=lambda: controller.show_frame("MainPage"))
        self.back_button.grid(row=0, column=2, padx=10, pady=10, ipadx=0, ipady=0, sticky=tk.NE)

        self.sbd = tk.Label(self, text="choose the movement")
        self.sbd.grid(row=0, column=0, padx=10, pady=10, ipadx=0, ipady=0, sticky=tk.W)

        self.selected_movement = tk.StringVar()
        self.movement_choice = ttk.Combobox(self, textvariable=self.selected_movement)
        self.movement_choice['value'] = ['squat', 'bench', 'deadlift']
        self.movement_choice['state'] = 'readonly'
        self.movement_choice.grid(row=0, column=1, padx=10, pady=10, ipadx=0, ipady=0, sticky=tk.W)

        self.WeightOfTheDay = tk.Label(self, text="Enter the weight lifted:")
        self.WeightOfTheDay.grid(row=1, column=0, padx=10, pady=10, ipadx=0, ipady=0, sticky=tk.W)

        self.weight_entry = tk.Entry(self)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        self.save_button = tk.Button(self, text="Save performance", command=self.save_perf)
        self.save_button.grid(row=2, column=1, padx=10, pady=10)

        self.show_graph = tk.Button(self, text="show the progression", command=self.show_graph)
        self.show_graph.grid(row=2, column=0, padx=10, pady=10)

    def save_perf(self):
        move = self.selected_movement.get()
        weight = self.weight_entry.get()

        if move and weight:
            try:
                weight = float(weight)
                date = datetime.now().strftime("%Y-%m-%d")
                table_name = move.lower()
                self.db.save_performances(table_name, date, weight)
                self.weight_entry.delete(0, tk.END)
                tk.messagebox.showinfo("Success", "Performance saved successfully!")

            except ValueError:
                tk.messagebox.showerror("Error", "Please enter a valid number for weight.")
        else:
            tk.messagebox.showerror("Error", "Please fill in all fields.")



    def show_graph(self):
        move = self.selected_movement.get()
        if move:
            ShowGraph(self, move)
        else:
            tk.messagebox.showerror("Error", "Please choose the movement")


class ShowGraph(tk.Toplevel):

    def __init__(self, parent, move):
        super().__init__(parent)
        self.db = DBHandler()
        self.title(f"{move.capitalize()} Progression Graph")
        self.geometry("800x600")
        self.move = move
        self.plot_graph()


    def plot_graph(self):
        dates = []
        weights = []
        try:
            if self.move:
                table_name = self.move.lower()
                performances = self.db.get_performances(table_name)
                print(performances)
                for performance in performances:
                    weight = performance[0]
                    date_str = performance[1]
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    dates.append(date)
                    weights.append(weight)
                print(dates, weights)
            else:
                tk.messagebox.showerror("Error", "Please choose the movement")


            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(dates, weights, marker='o', linestyle='-', label=f'{self.move.capitalize()} Performance')
            ax.set_xlabel('Date')
            ax.set_ylabel('Weight (kg)')
            ax.set_title(f'{self.move.capitalize()} Performance Over Time')
            ax.legend()
            ax.grid(True)


            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except FileNotFoundError:
            tk.messagebox.showerror("Error", f"No data found for {self.move}. Please save some performance data first.")
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Data format error in the CSV file: {e}")


class HelpWindow(tk.Toplevel):

    def __init__(self, parent, title, message, theme):
        super().__init__(parent)
        self.theme = theme

        self.title(title)
        self.geometry("350x200")
        self.config(bg=self.theme['bg'])

        self.label = tk.Label(self, text=message, bg=self.theme['bg'], fg=self.theme['fg'])
        self.label.pack(pady=20, padx=20)

        self.ok_button = tk.Button(self, text="ok", bg=self.theme['btn_bg'], fg=self.theme['btn_fg'],
                                   command=self.destroy)
        self.ok_button.pack(pady=10)


root = tk.Tk()
root.title("App")
app = MyApp(root)
root.mainloop()
