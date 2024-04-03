import tkinter as tk
from tkinter import simpledialog
import serial

# Connect to Arduino
ser = serial.Serial('/dev/ttyUSB0', 9600)
inputPin = 0
inputPinStr = str(inputPin)
inputPinString = inputPinStr.encode()
ser.flushInput()

# Create GUI
root = tk.Tk()
root.title("Basketball Arcade")
root.geometry("800x600")

# Variables
current_score = 0
highest_score = ("", 0)

# Read highest score from file and write it to the GUI
def read_highest_score():
        global highest_score
        try:
                with open("hiscore", "r") as file:
                        data = file.readline().split(":")
                        highest_score = (data[0].strip(), int(data[1].strip()))
                highest_score_label.config(text=f"Highest Score\n {highest_score[0]}: {highest_score[1]}")
        except FileNotFoundError:
                print(f"File not found!")
        except Exception as e:
                print(f"Error occurred: {e}")

# Write highest score to file
def write_highest_score():
        global highest_score
        print(f"Writing highest score: {highest_score}")
        with open("hiscore", "w") as file:
                file.write(f"{highest_score[0]}: {highest_score[1]}")
        read_highest_score()

# Add +1 to current score
def add_score():
        global current_score
        current_score += 1
        score_label.config(text=f"Current Score: {current_score}")

# Reset current score and update highest score if needed
def reset_score():
        global current_score
        global highest_score
        hs_name = simpledialog.askstring("Input", "What is your name?", parent=root)
        if current_score > highest_score[1]:
                highest_score = (hs_name, current_score)
                write_highest_score()
        score_entry = f"{hs_name}: {current_score}"
        previous_scores_list.configure(state='normal')
        previous_scores_list.insert(tk.END, score_entry)
        previous_scores_list.configure(state='disabled')
        current_score = 0
        ser.write(str(current_score).encode())
        score_label.config(text=f"Current Score: {current_score}")

# Configure grid
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_rowconfigure(2, weight=7)

# Left column
score_label = tk.Label(root, text=f"Current Score: {current_score}")
score_label.grid(row=0, column=0, sticky='nsew')

add_button = tk.Button(root, text="Add Score", command=add_score, bg='green')
add_button.grid(row=1, column=0, sticky='nsew')

reset_button = tk.Button(root, text="Reset Score", command=reset_score, bg='red')
reset_button.grid(row=2, column=0, sticky='nsew')

# Right column
highest_score_label = tk.Label(root,font=("Helvetica", 16) , text=f"Highest Score\n {highest_score[0]}: {highest_score[1]}")
highest_score_label.grid(row=0, column=1, sticky='nsew')

previous_scores_label = tk.Label(root, text="Previous Scores:")
previous_scores_label.grid(row=1, column=1, sticky='nsew')

previous_scores_list = tk.Listbox(root, font=("Helvetica", 16))
previous_scores_list.grid(row=2, column=1, sticky='nsew')
previous_scores_list.configure(state='disabled')

# Read highest score from file on startup
read_highest_score()

#Main loop
while True:
        try:
                lineBytes = ser.readline()
                line = lineBytes.decode('utf-8')
                print(line)
                if current_score > int(line):
                        reset_score()
                if current_score != int(line):
                        current_score = int(line)
                        score_label.config(text=f"Current Score: {current_score}")
        except KeyboardInterrupt:
                ser.close()
                break
        root.update()