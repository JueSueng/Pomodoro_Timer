import tkinter as tk

second = 11
after_id = None

def timer():
    global second
    global after_id

    start_button.config(
        state="disabled"
    )

    if second > 0: 

        second-=1

        timer_label.config(
            text=f"{second//60:02}:{second%60:02}"
        )

        after_id = window.after(1000, timer)

        pause_button.config(
            state="normal"
        )

        resume_button.config(
            state="disabled"
        )

    else:
        timer_label.config(
            text="시간 종료!"
        )

        pause_button.config(
            state="disabled"
        )

        resume_button.config(
            state="disabled"
        )

def pause():
    pause_button.config(
        state="disabled"
    )

    global after_id
    
    if after_id is not None:
        window.after_cancel(after_id)

    resume_button.config(
        state="normal" 
    )

window = tk.Tk()

window.title("Pomodoro Timer")

window.geometry("400x300")

timer_label = tk.Label(
    window,
    text=f"{second//60:02}:{second%60:02}"
)

timer_label.pack()

start_button = tk.Button(
    window,
    text="시작",
    command=timer
)

start_button.pack()

pause_button = tk.Button(
    window,
    text="일시정지",
    command=pause,
    state="disabled"
)

pause_button.pack()

resume_button = tk.Button(
    window,
    text="재개",
    command=timer,
    state="disabled"
)

resume_button.pack()

window.mainloop()