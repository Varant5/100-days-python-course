from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global TIMER, REPS
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0
    title_label.config(text="TIMER", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    work_sec = 60 * WORK_MIN
    short_break_sec = 60 * SHORT_BREAK_MIN
    long_break_sec = 60 * LONG_BREAK_MIN

    work_reps = [0,2,4,6]
    short_break_reps = [1,3,5]

    if REPS in work_reps:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)
    elif REPS in short_break_reps:
        count_down(short_break_sec)
        title_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(long_break_sec)
        title_label.config(text="LONG BREAK", fg=RED)

    REPS += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minutes = floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        global REPS
        start_timer()
        marks = ""
        session = floor(REPS/2)
        for _ in range(session):
            marks += CHECKMARK
            checkmark_text.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(window, text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(window, text="START", font=(FONT_NAME, 10, "italic"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(window, text="RESET", font=(FONT_NAME, 10, "italic"), command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_text = checkmarks = Label(window, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(column=1, row=3)

window.mainloop()