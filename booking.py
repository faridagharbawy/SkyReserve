import tkinter as tk
from tkinter import ttk, messagebox
from database import create_reservation

# Colors (navy theme)
BG_COLOR = "#0A1D37"    # dark navy background
CARD_BG = "#13294B"     # lighter navy card
BTN_COLOR = "#1E90FF"   # blue button
BTN_CANCEL = "#3A3A3A"  # dark gray cancel button
TEXT_COLOR = "white"

class BookingPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_COLOR)
        self.app = app

        # Centered card
        card = tk.Frame(self, bg=CARD_BG, bd=1, relief="flat")
        card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)

        # Title
        tk.Label(card, text="Book a Flight", font=("Helvetica", 16, "bold"),
                 bg=CARD_BG, fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=15)

        # Fields and placeholders
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        placeholders = ["Enter your full name", "e.g. FS123", "e.g. New York",
                        "e.g. London", "Pick a date (YYYY-MM-DD)", "e.g. 12A"]

        self.entries = {}
        for i, (label, ph) in enumerate(zip(fields, placeholders)):
            tk.Label(card, text=label, font=("Helvetica", 11),
                     bg=CARD_BG, fg=TEXT_COLOR).grid(row=i+1, column=0, sticky="w", padx=20, pady=5)
            e = ttk.Entry(card, width=30)
            e.insert(0, ph)   # show placeholder
            e.grid(row=i+1, column=1, padx=20, pady=5)
            self.entries[label] = e

        # Buttons
        btn_frame = tk.Frame(card, bg=CARD_BG)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=20)

        cancel = tk.Button(btn_frame, text="Cancel", bg=BTN_CANCEL, fg="white",
                           width=12, relief="flat",
                           command=lambda: app.show_frame("HomePage"))
        cancel.grid(row=0, column=0, padx=10)

        submit = tk.Button(btn_frame, text="Book Flight", bg=BTN_COLOR, fg="white",
                           width=12, relief="flat", command=self.submit)
        submit.grid(row=0, column=1, padx=10)

    def submit(self):
        # collect values
        data = {
            'name': self.entries["Name"].get(),
            'flight_number': self.entries["Flight Number"].get(),
            'departure': self.entries["Departure"].get(),
            'destination': self.entries["Destination"].get(),
            'date': self.entries["Date"].get(),
            'seat_number': self.entries["Seat Number"].get()
        }

        # validation: must enter real values, not placeholders
        if not data['name'] or data['name'].startswith("Enter"):
            messagebox.showwarning("Validation", "Please enter a valid Name")
            return

        create_reservation(data)
        messagebox.showinfo("Success", "Reservation added!")
        
        # clear form
        for e in self.entries.values():
            e.delete(0, "end")

        self.app.show_frame("ReservationsPage")
