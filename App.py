import tkinter as tk
from typing import Optional, Tuple, Union
import customtkinter
from TabView import TabView
from FrameList import FrameList

customtkinter.set_appearance_mode('light')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rasterização de Retas")
        self.geometry("1480x600")
        #self.resizable(False, False)
        self.grid_rowconfigure((0,1), weight=1, uniform='a')
        self.grid_columnconfigure(0, weight=1, uniform='a')

        self.TitleLabel = customtkinter.CTkLabel(self, text="Rasterização - Computação Gráfica", font=('Inconsolata',40))
        self.TitleLabel.grid(row=0, column=0, padx=20, pady=20, sticky='s')
        
        #TabView
        self.tab_view = TabView(master=self)
        self.tab_view.grid(row=1, column=0, padx=20, pady=20, sticky='n')

        #Coordinates FrameView
        self.ListLabel = customtkinter.CTkLabel(self, text="Lista de Objetos", font=('Incosolata', 24))
        self.FrameList = FrameList(master=self)
        #self.FrameList.grid(row=1, column=1, padx=20, pady=20, sticky="ns")

    #Métodos


#Inicialização
app = App()
app.mainloop()