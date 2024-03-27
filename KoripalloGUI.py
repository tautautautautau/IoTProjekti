import tkinter as tk
from tkinter import simpledialog
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
inputPin = 0
inputPinStr = str(inputPin)
inputPinString = inputPinStr.encode()
ser.flushInput()

root = tk.Tk()
root.title("Basketball Arcade")
root.geometry("800x600")
current_score = 0

def add_score():
        global current_score
        current_score += 1
        score_label.config(text=f"Current Score: {current_score}")

def reset_score():
        global current_score
        hs_name = simpledialog.askstring("Input", "What is your name?", parent=root)
        score_entry = f"{hs_name}: {current_score}"
        previous_scores_list.configure(state='normal')
        previous_scores_list.insert(tk.END, score_entry)
        previous_scores_list.configure(state='disabled')
        current_score = 0
        ser.write(str(current_score).encode())
        score_label.config(text=f"Current Score: {current_score}")

# Configure grid to expand with window
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=7)  # Added third row

# Left column
score_label = tk.Label(root, text=f"Current Score: {current_score}")
score_label.grid(row=0, column=0, sticky='nsew')

add_button = tk.Button(root, text="Add Score", command=add_score, bg='green')
add_button.grid(row=1, column=0, sticky='nsew')

reset_button = tk.Button(root, text="Reset Score", command=reset_score, bg='red')
reset_button.grid(row=2, column=0, sticky='nsew')  # Moved to third row

# Right column
previous_scores_label = tk.Label(root, text="Previous Scores:")
previous_scores_label.grid(row=0, column=1, sticky='nsew')

previous_scores_list = tk.Listbox(root, font=("Helvetica", 16))
previous_scores_list.grid(row=1, column=1, sticky='nsew', rowspan=2)  # Spanning 2 rows
previous_scores_list.configure(state='disabled')

while True:
        try:
                lineBytes = ser.readline()
                line = lineBytes.decode('utf-8')
                print(line)
                if current_score != int(line):
                        current_score = int(line)
                        score_label.config(text=f"Current Score: {current_score}")
                elif current_score > int(line):
                        reset_score()
        except KeyboardInterrupt:
                ser.close()
                break
        root.update()