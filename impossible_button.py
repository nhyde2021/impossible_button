import tkinter as tk
from random import randint

root = tk.Tk()
root.title("Impossible Button")

def add_point():
    global points
    global value
    global chance
    global highScore

    points += 1
    press.config(text=str(points))

    chance = randint(1, 100)

    value -= 1
    if chance > value:
        press.config(text="Game Over "+ str(points), bg="red", disabledforeground="black", state="disabled")
    print(value)
    print(chance)

def high_score():
    global highScore

    if points >= highScore:
        highScore = points
        label.config(text="High Score: " + str(highScore))

def start_over():
    global points
    global value

    points = 0
    value = 100
    press.config(text="Press", bg="light gray", state="normal")

def attempts_count():
    global attempts

    attempts += 1
    label2.config(text="Attempt: " + str(attempts))




points = 0
value = 100
chance = randint(1, 100)
highScore = 0
attempts = 1


press = tk.Button(root, text="Press", width=20, bg="light gray", command=lambda:[add_point(), high_score()])
press.pack()
press.place(x=120, y=100)

reset = tk.Button(root, text="Reset", width=10, bg="light gray", command=lambda:[start_over(), attempts_count()])
reset.pack()
reset.place(x=300, y=20)

label = tk.Label(root, text="High Score: " + str(points))
label.pack()
label.place(x=10, y=20)

label2 = tk.Label(root, text="Attempt: 1")
label2.pack()
label2.place(x=10, y=40)

root.geometry("400x200")
root.mainloop()