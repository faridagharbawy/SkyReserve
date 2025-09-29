from tkinter import ttk

# Global color palette
BG_COLOR = "#0A1D37"     # dark navy background
CARD_BG = "#13294B"      # lighter navy card
TEXT_COLOR = "white"

# Buttons
BTN_COLOR = "#1E90FF"    # bright blue
BTN_ACTIVE = "#104E8B"   # darker blue when clicked
BTN_CANCEL = "#3A3A3A"   # dark gray (used for Back/Cancel)

# Entry field background
ENTRY_BG = "#F8F8FF"

# Default button style dict (can be reused if needed)
btn_style = {
    "bg": BTN_COLOR,
    "fg": "white",
    "activebackground": BTN_ACTIVE,
    "activeforeground": "white",
    "width": 20,
    "height": 2,
    "bd": 0,
    "font": ("Helvetica", 10, "bold")
}

# Treeview styling
def style_treeview():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="white")
    style.configure("Treeview.Heading",
                    background=BTN_COLOR,
                    foreground="white",
                    font=("Helvetica", 11, "bold"))
    style.map("Treeview", background=[("selected", BTN_COLOR)])
