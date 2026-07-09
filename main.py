import tkinter as tk
from tkinter import ttk
import string

def check_password_strength(*args):
    password = password_var.get()
    length = len(password)
    
    if length == 0:
        strength_label.config(text="Enter a password", fg="#8892b0")
        canvas.itemconfig(progress_bar, fill="#232936")
        canvas.coords(progress_bar, 0, 0, 0, 8)
        update_indicators(False, False, False, False)
        return

    # Security rule parsing
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    has_length = length >= 8

    # Calculate modern entropy score
    score = sum([has_upper, has_digit, has_symbol, has_length])
    if length >= 12 and score > 0: 
        score += 1 

    # Synchronize checkboxes dynamically
    update_indicators(has_length, has_upper, has_digit, has_symbol)

    # Dynamic UI Updates based on score evaluation
    if length < 6 or score <= 2:
        strength_label.config(text="❌ Weak Password", fg="#ff4a5a")
        canvas.itemconfig(progress_bar, fill="#ff4a5a")
        animate_bar(100)
    elif score == 3 or score == 4:
        strength_label.config(text="⚠️ Medium Strength", fg="#ffb703")
        canvas.itemconfig(progress_bar, fill="#ffb703")
        animate_bar(220)
    else:
        strength_label.config(text="🔒 Strong Password", fg="#00b4d8")
        canvas.itemconfig(progress_bar, fill="#00b4d8")
        animate_bar(340)

def animate_bar(target_width):
    canvas.coords(progress_bar, 0, 0, target_width, 8)

def update_indicators(l, u, d, s):
    lbl_len.config(text=f"{'●' if l else '○'} At least 8 characters", fg=f"{'#00b4d8' if l else '#8892b0'}")
    lbl_up.config(text=f"{'●' if u else '○'} Contains Uppercase", fg=f"{'#00b4d8' if u else '#8892b0'}")
    lbl_num.config(text=f"{'●' if d else '○'} Contains Number", fg=f"{'#00b4d8' if d else '#8892b0'}")
    lbl_sym.config(text=f"{'●' if s else '○'} Contains Symbol", fg=f"{'#00b4d8' if s else '#8892b0'}")

def toggle_password():
    if entry['show'] == '*':
        entry.config(show='')
        btn_toggle.config(text='Hide')
    else:
        entry.config(show='*')
        btn_toggle.config(text='Show')

# Base GUI window generation
root = tk.Tk()
root.title("Password Shield")
root.geometry("460x520") # Height thodi kam ki hai kyunki top header remove kiya hai
root.configure(bg="#020f22") # Deep tech midnight-blue background

# Style Configuration
style = ttk.Style()
style.theme_use('clam')

# Glassmorphism container element simulating a card overlay
card = tk.Frame(root, bg="#112240", bd=0, highlightbackground="#233554", highlightthickness=1)
card.pack(pady=25, padx=30, fill="both", expand=True)

lbl_title = tk.Label(card, text="Password Analyst", font=("Segoe UI", 18, "bold"), bg="#112240", fg="#e2e8f0")
lbl_title.pack(pady=(25, 5))

lbl_sub = tk.Label(card, text="Verify authentication safety strength indicators", font=("Segoe UI", 9), bg="#112240", fg="#8892b0")
lbl_sub.pack(pady=(0, 20))

# Password Entry Field Frame wrapper
entry_frame = tk.Frame(card, bg="#1d2d44", bd=0)
entry_frame.pack(fill="x", padx=30, pady=10)

password_var = tk.StringVar()
password_var.trace_add("write", check_password_strength)

entry = tk.Entry(entry_frame, textvariable=password_var, show='*', font=("Segoe UI", 12), bg="#1d2d44", fg="#f8fafc", bd=0, insertbackground='white', highlightthickness=8, highlightcolor="#1d2d44", highlightbackground="#1d2d44")
entry.pack(side="left", fill="x", expand=True, padx=(5, 0))

btn_toggle = tk.Button(entry_frame, text="Show", command=toggle_password, font=("Segoe UI", 9, "bold"), bg="#1d2d44", fg="#64ffda", activebackground="#1d2d44", activeforeground="#64ffda", bd=0, cursor="hand2")
btn_toggle.pack(side="right", padx=10)

# Beautiful Custom Analytical Strength Meter Line Bar
canvas = tk.Canvas(card, width=340, height=8, bg="#232936", highlightthickness=0, bd=0)
canvas.pack(pady=(15, 5), padx=30)
progress_bar = canvas.create_rectangle(0, 0, 0, 8, fill="#232936", width=0)

# Output text reading indicator
strength_label = tk.Label(card, text="Enter a password", font=("Segoe UI", 11, "bold"), bg="#112240", fg="#8892b0")
strength_label.pack(pady=5)

# Rule validation dynamic checklist stack
checklist_frame = tk.Frame(card, bg="#112240")
checklist_frame.pack(anchor="w", padx=35, pady=20)

lbl_len = tk.Label(checklist_frame, text="○ At least 8 characters", font=("Segoe UI", 10), bg="#112240", fg="#8892b0")
lbl_len.pack(anchor="w", pady=3)

lbl_up = tk.Label(checklist_frame, text="○ Contains Uppercase", font=("Segoe UI", 10), bg="#112240", fg="#8892b0")
lbl_up.pack(anchor="w", pady=3)

lbl_num = tk.Label(checklist_frame, text="○ Contains Number", font=("Segoe UI", 10), bg="#112240", fg="#8892b0")
lbl_num.pack(anchor="w", pady=3)

lbl_sym = tk.Label(checklist_frame, text="○ Contains Symbol", font=("Segoe UI", 10), bg="#112240", fg="#8892b0")
lbl_sym.pack(anchor="w", pady=3)

# App Footer
lbl_foot = tk.Label(root, text="", font=("Segoe UI", 8), bg="#0a192f", fg="#495670")
lbl_foot.pack(pady=(5, 20))

root.mainloop()