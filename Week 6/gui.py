import tkinter as tk
from tkinter import Frame
import math

def calculate(ent_radius, lbl_result, lbl_status):
    """Calculate the area of a circle based on the input radius."""
    radius_str = ent_radius.get()
    try:
        radius = float(radius_str)
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        area = math.pi * (radius ** 2)
        lbl_result.config(text=f"Result: {area:.2f}")
        lbl_status.config(text="Calculation successful", fg="green")
    except ValueError:
        lbl_result.config(text="Result: ")
        lbl_status.config(text="Invalid input: Please enter a valid number", fg="red")

def clear(ent_radius, lbl_result, lbl_status):
    """Clear the input field, result label, and status bar."""
    ent_radius.delete(0, tk.END)
    lbl_result.config(text="Result: ")
    lbl_status.config(text="")

def main():
    # Create the main application window.
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x300")
    root.config(bg="lightblue")
    root.resizable(False, False)

    # Create and pack the main frame.
    frm_main = Frame(root, bg="lightblue")
    frm_main.pack(padx=10, pady=10)

    # Title label.
    lbl_title = tk.Label(frm_main, text="Area of a Circle Calculator", font=("Arial", 16), bg="lightblue", fg="black")
    lbl_title.pack(pady=10)

    # Label and entry for radius input.
    lbl_radius = tk.Label(frm_main, text="Enter the radius:", font=("Arial", 12), bg="lightblue")
    lbl_radius.pack()
    ent_radius = tk.Entry(frm_main, font=("Arial", 12))
    ent_radius.pack(pady=5)

    # Label to display the result.
    lbl_result = tk.Label(frm_main, text="Result: ", font=("Arial", 12), bg="lightblue")
    lbl_result.pack(pady=10)

    # Status bar label at the bottom of the window.
    lbl_status = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="lightgrey", font=("Arial", 10))
    lbl_status.pack(side=tk.BOTTOM, fill=tk.X)

    # Calculate button.
    btn_calculate = tk.Button(
        frm_main,
        text="Calculate",
        command=lambda: calculate(ent_radius, lbl_result, lbl_status),
        font=("Arial", 12)
    )
    btn_calculate.pack(pady=5)

    # Clear button.
    btn_clear = tk.Button(
        frm_main,
        text="Clear",
        command=lambda: clear(ent_radius, lbl_result, lbl_status),
        font=("Arial", 12)
    )
    btn_clear.pack(pady=5)

    # MacOS-specific fix: bring window to the front.
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    # Start the Tkinter event loop.
    root.mainloop()

if __name__ == "__main__":
    main()
