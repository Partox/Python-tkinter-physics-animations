import tkinter as tk 
from newton_law_one_gui import lawOne
from newton_law_two_gui import lawTwo
from newton_law_three_gui import lawThree

class Main:
    laws = [lawOne, lawTwo, lawThree]
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("850x700")
        self.window.title("Newton Laws")
        self.window.config(background="lightblue")
        self.frame = tk.Frame(master = self.window)
        self.frame.pack()
        self.create_window()
        

        



    def click(self, law):
        self.window = law(self.window)

        self.window.withdraw()




    def create_window(self):      
        self.button_frame = tk.Frame()
        self.button_frame.config(background='lightblue',
                                pady=100 )
        self.button_frame.pack()
        
        label = tk.Label(self.frame, 
                            text="Newtons Law Simulation", 
                            font=('Arial', 20, 'bold'), 
                            fg='black', 
                            bg='lightblue',
                            relief='flat',
                            bd=0,
                            padx=0,
                            pady=0)
        label.pack()
        index = 0
        for n in self.laws:
             self.create_button(n, index)
             self.button_frame.grid_columnconfigure(index, minsize=250)
             index += 1


    def create_button(self, law, index):
            button = tk.Button(self.button_frame, text=law.name)
            button.config(command=lambda: self.click(law)) #performs callback of function
            button.config(font=('Arial', 15, 'bold'))
            button.config(bg='blue')
            button.config(fg='lightblue')
            button.config(activebackground='black')
            button.config(activeforeground='lightgreen')
            button.grid(row=0, column=index)

app = Main()
app.window.mainloop() #window on screen and listen to events

