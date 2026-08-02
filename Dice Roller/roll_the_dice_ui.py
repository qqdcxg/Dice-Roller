import tkinter as tk
from tkinter import messagebox

from roll_the_dice import get_die_face_positions, roll_dice, roll_single_die

entry_times = None
button_roll = None
result_text = None
die_canvas = None


def draw_die_face(value: int) -> None:
    if die_canvas is None:
        return
    die_canvas.delete("all")
    die_canvas.create_rectangle(10, 10, 150, 150, width=3, outline="#0f172a", fill="#f8fafc")
    for x, y in get_die_face_positions(value):
        die_canvas.create_oval(x - 6, y - 6, x + 6, y + 6, fill="#0f172a", outline="#0f172a")


def on_roll() -> None:
    global entry_times, result_text
    entry_value = entry_times.get().strip()
    if not entry_value:
        messagebox.showwarning("Input Error", "Please enter the number of dice rolls.")
        return

    try:
        times = int(entry_value)
        if times <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter an integer greater than 0.")
        return

    average = roll_dice(times)
    latest_face = roll_single_die()
    draw_die_face(latest_face)
    result_text.set(f"Rolled the dice {times} times. Average value: {average:.4f}")


def build_ui(root: tk.Tk) -> None:
    global entry_times, button_roll, result_text, die_canvas

    frame = tk.Frame(root, bg="#111827", padx=24, pady=24)
    frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    title_label = tk.Label(frame, text="Dice Roller", font=("Segoe UI", 18, "bold"), bg="#111827", fg="#f8fafc")
    title_label.grid(row=0, column=0, columnspan=2, sticky="w")

    subtitle_label = tk.Label(
        frame,
        text="Simulate dice rolls and view the average result instantly.",
        font=("Segoe UI", 10),
        bg="#111827",
        fg="#cbd5e1",
        wraplength=500,
        justify="left",
    )
    subtitle_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(6, 18))

    die_panel = tk.LabelFrame(frame, text="Die Preview", font=("Segoe UI", 11, "bold"), bg="#111827", fg="#a5b4fc", bd=2, relief=tk.GROOVE)
    die_panel.grid(row=2, column=1, rowspan=4, sticky="nsew", padx=(16, 0), pady=(0, 0))

    die_canvas = tk.Canvas(die_panel, width=160, height=160, bg="#f8fafc", highlightthickness=0)
    die_canvas.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

    label_prompt = tk.Label(frame, text="Number of rolls:", font=("Segoe UI", 12), bg="#111827", fg="#e2e8f0")
    label_prompt.grid(row=2, column=0, sticky="w")

    entry_times = tk.Entry(frame, font=("Segoe UI", 12, "bold"), bg="#e2e8f0", fg="#0f172a", insertbackground="#0f172a", width=18)
    entry_times.grid(row=3, column=0, sticky="ew", pady=(8, 10), ipady=6)
    entry_times.focus()

    button_roll = tk.Button(
        frame,
        text="Roll Dice",
        font=("Segoe UI", 12, "bold"),
        bg="#6366f1",
        fg="#ffffff",
        activebackground="#4f46e5",
        activeforeground="#ffffff",
        relief=tk.FLAT,
        command=on_roll,
        padx=10,
        pady=8,
    )
    button_roll.grid(row=4, column=0, sticky="ew", pady=(4, 10))

    result_box = tk.LabelFrame(frame, text="Result", font=("Segoe UI", 11, "bold"), bg="#111827", fg="#a5b4fc", bd=2, relief=tk.GROOVE, labelanchor="n")
    result_box.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=(6, 0))

    result_text = tk.StringVar(value="Waiting for input...")
    label_result = tk.Label(
        result_box,
        textvariable=result_text,
        font=("Segoe UI", 13, "bold"),
        bg="#0f172a",
        fg="#34d399",
        wraplength=500,
        justify="left",
        anchor="w",
        padx=14,
        pady=14,
    )
    label_result.pack(fill=tk.BOTH)

    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(5, weight=1)

    draw_die_face(1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dice Roller")
    root.geometry("680x420")
    root.resizable(False, False)
    root.configure(bg="#0b1120")
    build_ui(root)
    root.mainloop()
