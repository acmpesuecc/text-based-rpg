from tkinter import *

class UIManager:
    def __init__(self, root, frame1):
        self.root = root
        self.frame1 = frame1

    def showMainWindow(self, inventory, get_room):
        inventory_button=Button(text="inventory",command=inventory)
        inventory_button.pack(side=BOTTOM)
        self.root.title("The Quest")
        self.frame1 = Frame(self.root, padx=50, pady=50)
        self.frame1.pack(padx=50, pady=50)
        self.root.geometry("500x500")
        label = Label(self.frame1, text="Welcome to The Quest!!\nStory...\nIntro")
        label.pack()

        welcome_button = Button(self.frame1, text='Next', command=lambda: get_room())
        welcome_button.pack()

        self.root.mainloop()