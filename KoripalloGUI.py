import tkinter as tk

class ScoreApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Score App")
        self.current_score = 0
        self.previous_scores = []

        # Configure grid to expand with window
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=1)

        # Left column
        self.score_label = tk.Label(self.window, text=f"Current Score: {self.current_score}")
        self.score_label.grid(row=0, column=0, sticky='nsew')

        self.reset_button = tk.Button(self.window, text="Reset Score", command=self.reset_score, bg='red')
        self.reset_button.grid(row=1, column=0, sticky='nsew')

        # Right column
        self.previous_scores_label = tk.Label(self.window, text="Previous Scores:")
        self.previous_scores_label.grid(row=0, column=1, sticky='nsew')

        self.previous_scores_list = tk.Listbox(self.window)
        self.previous_scores_list.grid(row=1, column=1, sticky='nsew')

    def reset_score(self):
        self.previous_scores.append(self.current_score)
        self.previous_scores_list.insert(tk.END, self.current_score)
        self.current_score = 0
        self.score_label.config(text=f"Current Score: {self.current_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ScoreApp()
    app.run()