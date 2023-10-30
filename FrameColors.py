import tkinter as tk
import customtkinter

class FrameColors(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=200, height=200, fg_color='#F3F3F3')

        self.rowconfigure(0, weight=1, uniform='a')

        radio_var = tk.IntVar(value=1)

        self.rbred = customtkinter.CTkRadioButton(self, text="", variable=radio_var, value=1, width=30, fg_color="#C13333", border_color="#C13333")
        self.rbgreen = customtkinter.CTkRadioButton(self, text="", variable=radio_var, value=2, width=30, fg_color="#94C133", border_color="#94C133")
        self.rbcyan = customtkinter.CTkRadioButton(self, text="", variable=radio_var, value=3, width=30, fg_color="#33C1B9", border_color="#33C1B9")
        self.rbblue = customtkinter.CTkRadioButton(self, text="", variable=radio_var, value=4, width=30, fg_color="#4F33C1", border_color="#4F33C1")
        self.rbpink = customtkinter.CTkRadioButton(self, text="", variable=radio_var, value=5, width=30, fg_color="#C13399", border_color="#C13399")

        self.rbred.grid(row=0, column=0, padx=0, pady=20)
        self.rbgreen.grid(row=0, column=1, padx=0, pady=20)
        self.rbcyan.grid(row=0, column=2, padx=0, pady=20)
        self.rbblue.grid(row=0, column=3, padx=0, pady=20)
        self.rbpink.grid(row=0, column=4, padx=0, pady=20)