import tkinter as tk
from tkinter import ttk, messagebox
from database import get_reservation, update_reservation

# Colors (navy theme)
BG_COLOR = "#0A1D37"    # dark navy background
CARD_BG = "#13294B"     # lighter navy card
BTN_COLOR = "#1E90FF"   # blue button
BTN_CANCEL = "#3A3A3A"  # dark gray cancel/back button
TEXT_COLOR = "white"

class EditPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_COLOR)
        self.app = app

        # Centered card
        card = tk.Frame(self, bg=CARD_BG, bd=1, relief="flat")
        card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)

        # Title
        tk.Label(card, text="Edit Reservation", font=("Helvetica", 16, "bold"),
                 bg=CARD_BG, fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=15)

        # Fields
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        for i, lab in enumerate(fields):
            tk.Label(card, text=lab, font=("Helvetica", 11),
                     bg=CARD_BG, fg=TEXT_COLOR).grid(row=i+1, column=0, sticky="w", padx=20, pady=5)
            e = ttk.Entry(card, width=30)
            e.grid(row=i+1, column=1, padx=20, pady=5)
            self.entries[lab] = e

        # Buttons
        btn_frame = tk.Frame(card, bg=CARD_BG)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=20)

        cancel = tk.Button(btn_frame, text="Back", bg=BTN_CANCEL, fg="white",
                           width=12, relief="flat",
                           command=lambda: app.show_frame("ReservationsPage"))
        cancel.grid(row=0, column=0, padx=10)

        update_btn = tk.Button(btn_frame, text="Update", bg=BTN_COLOR, fg="white",
                               width=12, relief="flat", command=self.update)
        update_btn.grid(row=0, column=1, padx=10)

        self.current_id = None

    def load(self, res_id):
        """Load reservation details into the form"""
        row = get_reservation(res_id)
        if not row:
            return
        self.current_id = row[0]
        values = list(row[1:])
        for (lab, e), v in zip(self.entries.items(), values):
            e.delete(0, "end")
            e.insert(0, v if v else "")

    def update(self):
        """Save updated reservation details"""
        if not self.current_id:
            return
        data = {
            'name': self.entries["Name"].get(),
            'flight_number': self.entries["Flight Number"].get(),
            'departure': self.entries["Departure"].get(),
            'destination': self.entries["Destination"].get(),
            'date': self.entries["Date"].get(),
            'seat_number': self.entries["Seat Number"].get()
        }
        update_reservation(self.current_id, data)
        messagebox.showinfo("Success", "Reservation updated")
        self.app.show_frame("ReservationsPage")
