import tkinter as tk
from tkinter import simpledialog

class ScoreApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Score App")
        self.window.geometry("1024x768")
        self.current_score = 0

        # Configure grid to expand with window
        self.window.grid_columnconfigure(0, weight=3)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=7)
        self.window.grid_rowconfigure(2, weight=7)  # Added third row

        # Left column
        self.score_label = tk.Label(self.window, text=f"Current Score: {self.current_score}")
        self.score_label.grid(row=0, column=0, sticky='nsew')

        self.add_button = tk.Button(self.window, text="Add Score", command=self.add_score, bg='green')
        self.add_button.grid(row=1, column=0, sticky='nsew')

        self.reset_button = tk.Button(self.window, text="Reset Score", command=self.reset_score, bg='red')
        self.reset_button.grid(row=2, column=0, sticky='nsew')  # Moved to third row

        # Right column
        self.previous_scores_label = tk.Label(self.window, text="Previous Scores:")
        self.previous_scores_label.grid(row=0, column=1, sticky='nsew')

        self.previous_scores_list = tk.Listbox(self.window, font=("Helvetica", 16))
        self.previous_scores_list.grid(row=1, column=1, sticky='nsew', rowspan=2)  # Spanning 2 rows
        self.previous_scores_list.configure(state='disabled')

    def add_score(self):
        self.current_score += 1
        self.score_label.config(text=f"Current Score: {self.current_score}")

    def reset_score(self):
        hs_name = simpledialog.askstring("Input", "What is your name?", parent=self.window)
        score_entry = f"{hs_name}: {self.current_score}"
        self.previous_scores_list.configure(state='normal')
        self.previous_scores_list.insert(tk.END, score_entry)
        self.previous_scores_list.configure(state='disabled')
        self.current_score = 0
        self.score_label.config(text=f"Current Score: {self.current_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ScoreApp()
    app.run()