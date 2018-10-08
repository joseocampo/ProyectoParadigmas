from tkinter import *
#THE NEXT IMPORT LET US TO USE THE FLOATING WINDOWS.
from tkinter import messagebox
from tkinter import filedialog
from functools import partial
class Calculator():
#este es un comentario para hacer commit
    def __init__(self):
        
        self.initializeComponents()
        self.createMenu()
        self.__selectedNumber = StringVar()
        self.__optionCloseApp = False
        self.__file = "Fichero No encontrado"
        self.createDigits()
        self.addButtonsToFrame()
        self.createScreenAndExtraButtons()
        
        # IT IS TO IMPORTANT TO CALL THIS METHOD HERE, BECAUSE AFTER CALL
        # ALL THE OTHER METHODS, THE WINDOWS NEEDS TO ENTER IN A INFINITE CICLE.
        self.__root.mainloop()

    def writeNumber(self,num):
        self.__selectedNumber.set(num)
    
    def showInfoSoftware(self):
        messagebox.showinfo("Bienvenido Usuario","Este software esta en desarrollo, el primer modulo es una calculadora!")
        
    def showTextHelp(self):
        messagebox.showwarning("Peligro","Usted  es digno de ayuda")
        
    def closeApplication(self):
        self.__optionCloseApp = messagebox.askquestion("Salir","Deseas cerrar la applicacion")
        if (self.__optionCloseApp == "yes"):
            self.__root.destroy()
        else:
            print("Seguimos en el programa")
    
    def openFiles(self):
        #THE ATTRIBUTE , initialdir, LET US TO INDICATE IN WICH DIR WE WOULD LIKE TO BEGIN SERCHING THE FILE.
        self.__file = filedialog.askopenfilename(title="ABRE UN DOCUMENTO PARA EL PROYECTO DE PARADIGMAS",initialdir="C:")
                                            #     filetypes=(("Ficheros de Excel",".xlsx"),("Ficheros de texto",".txt"),("Todos lo ficheros",".*")))
        print(self.__file)
            
    def initializeComponents(self):
        self.__root = Tk()
        self.__root.title("Software Calculator  (Didier)")
        self.__root.geometry("550x600")
        self.__root.resizable(False, False)
        self.__frame = Frame(self.__root, bg="gray", width="350", height="400")
        self.__frame.pack()
        
    def createMenu(self):
        self.__menuBar = Menu(self.__root)
        self.__root.config(menu=self.__menuBar)
        #ONCE WE HAVE CREATED OUR MENU, WE NEED TO ADD ITEMS TO OUR MENU, TEHN WE CALL TIS METHOD.
        self.addMenuItems()

    def addMenuItems(self):
        #tearoff=0,  THIS ATTRIBUTE IS TO AVOID SHOWING THE DEFAULT ITEM BAR IN OUR MENU ITEM.
        self.__archiveItemMenu = Menu(self.__menuBar,tearoff=0)
        self.__editItemMenu = Menu(self.__menuBar,tearoff=0)
        self.__toolsItemMenu = Menu(self.__menuBar,tearoff=0)
        self.__helpItemMenu = Menu(self.__menuBar,tearoff=0)
        self.__menuBar.add_cascade(label="Archivo", menu=self.__archiveItemMenu)
        self.__menuBar.add_cascade(label="Editar", menu=self.__editItemMenu)
        self.__menuBar.add_cascade(label="Herramientas", menu=self.__toolsItemMenu)
        self.__menuBar.add_cascade(label="Ayuda", menu=self.__helpItemMenu)
        
        #ONCE WE HAVE ADDED ITEMS TO OUR MENU, WE JUST NEED TO ADD OPCTION TO EACH MENU ITEM.
        #TEHN WE CALL THE METHOD BELOW
        self.addItemsMenuOptions()

    def addItemsMenuOptions(self):
        # WE AREA ADDING OPTIONS TO THE ITEM ARCHIVE
        self.__archiveItemMenu.add_command(label="Nuevo")
        self.__archiveItemMenu.add_command(label="Guardar")
        self.__archiveItemMenu.add_command(label="Recuperar",command=self.openFiles)
        self.__archiveItemMenu.add_separator()
        self.__archiveItemMenu.add_command(label="Salir",command=self.closeApplication)
        
        # WE AREA ADDING OPTIONS TO THE ITEM EDIT
        self.__editItemMenu.add_command(label="Copiar")
        self.__editItemMenu.add_command(label="Pegar")
        self.__editItemMenu.add_command(label="Cortar")
        
        # WE AREA ADDING OPTIONS TO THE ITEM TOOLS
        self.__toolsItemMenu.add_command(label="Preferencias")
        self.__toolsItemMenu.add_command(label="Inicializar repositorio")
        self.__toolsItemMenu.add_command(label="Conectar con Git")
        
        # WE AREA ADDING OPTIONS TO THE ITEM HELP
        self.__helpItemMenu.add_command(label="Bienvenido")
        self.__helpItemMenu.add_command(label="Ver ayuda",command=self.showTextHelp)
        self.__helpItemMenu.add_command(label="Sobre este software",command=self.showInfoSoftware)
        
    def createDigits(self):
        self.__digit0 = Button(self.__frame, text="0")
        self.__digit1 = Button(self.__frame, text="1")
        self.__digit2 = Button(self.__frame, text="2")
        self.__digit3 = Button(self.__frame, text="3")
        self.__digit4 = Button(self.__frame, text="4")
        self.__digit5 = Button(self.__frame, text="5")
        self.__digit6 = Button(self.__frame, text="6")
        self.__digit7 = Button(self.__frame, text="7")
        self.__digit8 = Button(self.__frame, text="8")
        self.__digit9 = Button(self.__frame, text="9")
        
        self.__add = Button(self.__frame, text=" + ")
        self.__subtract = Button(self.__frame, text=" - ")
        self.__multiply = Button(self.__frame, text=" * ")
        self.__divide = Button(self.__frame, text=" / ")
        
        self.__resolve = Button(self.__frame, text=" = ")
            
    def addButtonsToFrame(self):
        
        self.__digit7.grid(row=2, column=0, padx=10, pady=10, sticky="nsew",command =self.writeNumber("7"))
        
        
        
        self.__digit8.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.__digit9.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.__digit4.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.__digit5.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        self.__digit6.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")
        self.__digit1.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
        self.__digit2.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
        self.__digit3.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")
        
        self.__add.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")
        self.__subtract.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")
        self.__multiply.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")
        
        self.__digit0.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")
        self.__divide.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        self.__resolve.grid(row=5, column=2, padx=10, pady=10, sticky="nsew", columnspan=2)
    
    def createScreenAndExtraButtons(self):
        self.__screen = Entry(self.__frame,textvariable=self.__selectedNumber, bg="black", fg="#03f943")
        
        
        self.__screen.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=5)
        self.__result = Entry(self.__frame)
        self.__result.grid(row=1, column=0, columnspan=4, sticky="nsew")
    
