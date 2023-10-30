import tkinter as tk
import customtkinter

class FrameList(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, height=200, width=200, )

        self.buttonRasterizar = customtkinter.CTkButton(self, text="Rasterizar", font=("Inconsolata", 24), corner_radius=24, fg_color="#7056A6", width=272, height=62)
        self.buttonRasterizar.grid(row=1, column=2, padx=20, pady=20)