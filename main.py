import tkinter as tk
from database import init_db
from styles import BG_COLOR, style_treeview
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SkyReserve")
        self.geometry("800x600")
        self.configure(bg=BG_COLOR)

        # Apply custom Treeview style
        style_treeview()

        # Main container (fills the window)
        container = tk.Frame(self, bg=BG_COLOR)
        container.pack(fill="both", expand=True)

        # Let container’s single cell expand
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Store all frames
        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditPage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            # Each page fills the entire container cell
            frame.grid(row=0, column=0, sticky="nsew")

            # Make page’s own grid expand so place() inside works
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

        self.show_frame("HomePage")

    def show_frame(self, name):
        frame = self.frames[name]
        if name == "ReservationsPage":
            frame.refresh()
        frame.tkraise()


if __name__ == "__main__":
    init_db()
    app = App()
    app.mainloop()
