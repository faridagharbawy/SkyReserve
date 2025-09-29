import tkinter as tk
from tkinter import ttk, messagebox
from database import get_reservations, delete_reservation

# Colors (navy theme)
BG_COLOR = "#0A1D37"
CARD_BG = "#13294B"
BTN_COLOR = "#1E90FF"
BTN_DELETE = "#D9534F"   # red for delete
BTN_BACK = "#3A3A3A"
TEXT_COLOR = "white"

class ReservationsPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg=BG_COLOR)
        self.app = app

        # Card container
        card = tk.Frame(self, bg=CARD_BG, bd=1, relief="flat")
        card.place(relx=0.5, rely=0.5, anchor="center", width=750, height=500)


        # Title
        tk.Label(card, text="Reservations List", font=("Helvetica", 16, "bold"),
                 bg=CARD_BG, fg=TEXT_COLOR).pack(pady=15)

        # Table style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="white",
                        bordercolor=CARD_BG,
                        borderwidth=0)
        style.configure("Treeview.Heading",
                        background=BTN_COLOR,
                        foreground="white",
                        font=("Helvetica", 11, "bold"))
        style.map("Treeview", background=[("selected", BTN_COLOR)])

        # Treeview table
        cols = ("id","name","flight","departure","destination","date","seat")
        self.tree = ttk.Treeview(card, columns=cols, show="headings", height=10)

        # Column headings
        headers = ["ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"]
        for c, h in zip(cols, headers):
            self.tree.heading(c, text=h)
            self.tree.column(c, anchor="center", width=90)

        self.tree.pack(fill="both", expand=True, padx=20, pady=10)

        # Buttons
        btn_frame = tk.Frame(card, bg=CARD_BG)
        btn_frame.pack(pady=10)

        edit_btn = tk.Button(btn_frame, text="Edit", bg=BTN_COLOR, fg="white",
                             width=12, relief="flat", command=self.edit)
        edit_btn.grid(row=0, column=0, padx=10)

        delete_btn = tk.Button(btn_frame, text="Delete", bg=BTN_DELETE, fg="white",
                               width=12, relief="flat", command=self.delete)
        delete_btn.grid(row=0, column=1, padx=10)

        back_btn = tk.Button(btn_frame, text="Back", bg=BTN_BACK, fg="white",
                             width=12, relief="flat", command=lambda: app.show_frame("HomePage"))
        back_btn.grid(row=0, column=2, padx=10)

    def refresh(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        for row in get_reservations():
            self.tree.insert("", "end", values=row)

    def selected_id(self):
        sel = self.tree.selection()
        if not sel:
            return None
        return self.tree.item(sel[0])["values"][0]

    def edit(self):
        res_id = self.selected_id()
        if res_id:
            self.app.frames["EditPage"].load(res_id)
            self.app.show_frame("EditPage")

    def delete(self):
        res_id = self.selected_id()
        if res_id and messagebox.askyesno("Confirm", "Delete this reservation?"):
            delete_reservation(res_id)
            self.refresh()
