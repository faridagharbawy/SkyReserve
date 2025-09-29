import tkinter as tk
from styles import BG_COLOR, BTN_COLOR, BTN_CANCEL, TEXT_COLOR

class HomePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_COLOR)
        self.app = app

        # Centered card
        card = tk.Frame(self, bg="#13294B", bd=1, relief="flat")
        card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=300)

        # Title
        tk.Label(card, text="✈ SkyReserve",
                 font=("Helvetica", 18, "bold"),
                 bg="#13294B", fg=TEXT_COLOR).pack(pady=(30, 10))

        # Subtitle
        tk.Label(card, text="Book, view, and manage your flights",
                 font=("Helvetica", 12),
                 bg="#13294B", fg="lightgray").pack(pady=(0, 30))

        # Buttons
        book_btn = tk.Button(card, text="Book Flight",
                             bg=BTN_COLOR, fg="white",
                             width=20, height=2, relief="flat",
                             command=lambda: app.show_frame("BookingPage"))
        book_btn.pack(pady=10)

        view_btn = tk.Button(card, text="View Reservations",
                             bg=BTN_CANCEL, fg="white",
                             width=20, height=2, relief="flat",
                             command=lambda: app.show_frame("ReservationsPage"))
        view_btn.pack(pady=10)
