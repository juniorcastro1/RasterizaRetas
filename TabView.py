import tkinter as tk
import customtkinter
import Rasteriza as rt
import random
from FrameColors import FrameColors


class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, fg_color="#F3F3F3", segmented_button_selected_color="#7056A6")

        tkEntryVar = tk.StringVar(value='-1,-0;1,1')
        tkEntryVarCurva = tk.StringVar(value='-0.5,-0.5;0.5,-0.5')
        tkEntryTVar = tk.StringVar(value='0,-1;1,0')
        tkEntrySegVar = tk.IntVar(value=5)
        tkEntryVarPoligono = tk.StringVar(value='1, 0;-0.5, -0.866;-0.5, 0.866')

        #Criando as Tabs
        self.add('Reta')
        self.add('Curva')
        self.add('Polígono')

        #Reta Tab
        self.rowconfigure((0,1), weight=1, uniform='a')

        self.entryReta = customtkinter.CTkEntry(master=self.tab('Reta'), textvariable=tkEntryVar, width=300, height=62, font=("Inconsolata", 24))
        self.buttonReta = customtkinter.CTkButton(master=self.tab('Reta'), command=lambda: self.adicionarReta(tkEntryVar), text="Adicionar", corner_radius=24, fg_color="#7056A6",font=('Inconsolata', 24), width=272, height=62)
        self.buttonRasterizarReta = customtkinter.CTkButton(master=self.tab('Reta'), command=self.rasterize,text="Rasterizar", font=("Inconsolata", 24), corner_radius=24, fg_color="#7056A6", width=272, height=62)
        self.FrameColorsReta = FrameColors(master=self.tab('Reta'))

        self.FrameColorsReta.grid(row=0, column=1)
        self.entryReta.grid(row=1, column=0, padx=20, pady=20)
        self.buttonReta.grid(row=1, column=1, padx=20, pady=20)
        self.buttonRasterizarReta.grid(row=1, column=2, padx=20, pady=20)

        #Curva Tab
        self.entryCurva = customtkinter.CTkEntry(master=self.tab('Curva'), textvariable=tkEntryVarCurva, width=300, height=62, font=("Inconsolata", 24))
        self.entryTan = customtkinter.CTkEntry(master=self.tab('Curva'), textvariable=tkEntryTVar, width=300, height=62, font=('Inconsolata', 24))
        self.entrySeg = customtkinter.CTkEntry(master=self.tab('Curva'), textvariable=tkEntrySegVar, width=50, height=62, font=('Inconsolata', 24))
        self.buttonCurva = customtkinter.CTkButton(master=self.tab('Curva'), command=lambda: self.adicionarCurva(tkEntryVarCurva, tkEntryTVar, tkEntrySegVar),text="Adicionar", corner_radius=24, fg_color="#7056A6",font=('Inconsolata', 24), width=272, height=62)
        self.buttonRasterizarCurva = customtkinter.CTkButton(master=self.tab('Curva'), command=self.rasterize, text="Rasterizar", font=("Inconsolata", 24), corner_radius=24, fg_color="#7056A6", width=272, height=62)
        self.FrameColorsCurva = FrameColors(master=self.tab('Curva'))

        self.FrameColorsCurva.grid(row = 0, column=2)
        self.entryCurva.grid(row=1, column=0, padx=20, pady=20)
        self.entryTan.grid(row=1, column=1, padx=20, pady=20)
        self.entrySeg.grid(row=1, column=2, padx=20, pady=20)
        self.buttonCurva.grid(row=1, column=3, padx=20, pady=20)
        self.buttonRasterizarCurva.grid(row=1, column=4, padx=20, pady=20)

        #Polígono Tab
        self.entryPoligono = customtkinter.CTkEntry(master=self.tab('Polígono'), textvariable=tkEntryVarPoligono, placeholder_text="ex: -1,-0;1,1", width=300, height=62, font=("Inconsolata", 24))
        self.buttonPoligono = customtkinter.CTkButton(master=self.tab('Polígono'),command=lambda: self.adicionarPoligonos(tkEntryVarPoligono), text="Adicionar", corner_radius=24, fg_color="#7056A6",font=('Inconsolata', 24), width=272, height=62)
        self.buttonRasterizarPoligono = customtkinter.CTkButton(master=self.tab('Polígono'),command=self.rasterize, text="Rasterizar", font=("Inconsolata", 24), corner_radius=24, fg_color="#7056A6", width=272, height=62)
        self.FrameColorsPoligono = FrameColors(master=self.tab('Polígono'))

        self.FrameColorsPoligono.grid(row = 0, column=1)
        self.entryPoligono.grid(row=1, column=0, padx=20, pady=20)
        self.buttonPoligono.grid(row=1, column=1, padx=20, pady=20)
        self.buttonRasterizarPoligono.grid(row=1, column=2, padx=20, pady=20)

    matrizTela = rt.Tela()

    #tkAux = tk.IntVar(value=0)

    #Métodos
    def adicionarReta(self, entryData):
        points = self.transformToRetaMatrix(entryData)
        tempLine = rt.Reta(points, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.matrizTela.add_Reta(tempLine)
        #aux = tkAux.get() + 1
        #warningLabel.config(text = ' Reta número ' + str(aux) + ' adicionada')
        #tkAux.set(value = aux)

    def adicionarCurva(self, entryData, entryTData, numSeg):
        points = self.transformToRetaMatrix(entryData)
        tangents = self.transformToRetaMatrix(entryTData)
        tempLine = rt.Curva(points, tangents,numSeg.get(), (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        self.matrizTela.add_Curva(tempLine)
        print('Curva Adicionada!')


    def transformToCurvaMatrix(self, entryData):
        pass


    def adicionarPoligonos(self, entryData):
        points = self.transformListPoligono(entryData)
        print(points)
        tempPoligono = rt.Poligono(points, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        self.matrizTela.add_Poligono(tempPoligono)
        # aux = tkAux.get() + 1
        # warningLabelPoligono.config(text = ' Poligono número ' + str(aux) + ' adicionado')
        # tkAux.set(value = aux)

    def transformToRetaMatrix(self, entryData):
        entry = entryData.get()
        temp1 = entry.split(";")
        temp2 = []
        temp3 = []
        for i in range(len(temp1)):
            temp2.append(temp1[i].split(","))
        for i in range(len(temp2)):
            aux = temp2[i]
            for j in aux:
                temp3.append(float(j))
        toReturn = [[temp3[0],temp3[1]],[temp3[2],temp3[3]]]
        return toReturn
    
    def transformToRetaList(self, entryData):
        temp1 = entryData.get().split(";")
        temp2 = []
        temp3 = []
        for i in range(len(temp1)):
            temp2.append(temp1[i].split(","))
        for i in range(len(temp2)):
            aux = temp2[i]
            for j in aux:
                temp3.append(float(j))
        return temp3

    def transformListPoligono(self, entryData):
        temp = self.transformToRetaList(entryData)
        listaDePontos = [(temp[i], temp[i+1]) for i in range(0, len(temp), 2)]
        return listaDePontos

    def rasterize(self):
        print(rt.myMatriz.matriz)
        self.matrizTela.draw_Tela(rt.myMatriz.matriz)
        rt.mostrar()


    