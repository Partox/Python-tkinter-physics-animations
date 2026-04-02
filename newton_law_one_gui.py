import tkinter as tk

class lawOne:
    name = "Newton's First Law"
    CANVAS_HEIGHT = 500
    CANVAS_WIDTH = 800
    xVelocity = 0
    yVelocity = 0
    running = True
    speed = 0

    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        # Erhöhe die Höhe leicht, damit alles Platz hat
        self.window.geometry("850x800") 
        self.window.title("Newton Law One")
        self.window.config(background="lightblue")
        
        # Initialisiere die Widgets
        self.create_window()
        
        # Starte den ersten Animationszyklus
        self.animate()

    def animate(self):
        if self.running:
            self.coordinates = self.animation_canvas.coords(self.ball)
            
            if (self.coordinates[2] >= self.CANVAS_WIDTH or self.coordinates[0] <= 0):
                self.xVelocity = -self.xVelocity
            if (self.coordinates[3] >= self.CANVAS_HEIGHT or self.coordinates[1] <= 0):
                self.yVelocity = -self.yVelocity
            
            self.animation_canvas.move(self.ball, self.xVelocity, self.yVelocity)
            
            self.window.after(10, self.animate)

    def submit_input(self):
        try:
            val = self.entry.get()
            self.speed = float(val)
            self.xVelocity = self.speed
            self.yVelocity = self.speed
            self.speed_label.config(text=f'The speed is {self.speed}')
        except ValueError:
            self.speed_label.config(text="Bitte eine Zahl eingeben!")

    def create_window(self):
        tk.Label(self.window, text="Newton's First Law Simulation", 
                 font=('Arial', 20, 'bold'), bg='lightblue').pack(pady=10)

        self.create_animation_window()

        self.create_input_window()

        self.create_output_window()

        self.button_frame = tk.Frame(self.window, bg='lightblue')
        self.button_frame.pack(side='bottom', fill='x', padx=10, pady=10)
        
        button = tk.Button(self.button_frame, text='Home', font=('Arial', 20, 'bold'),
                           bg='blue', fg='lightblue', command=self.click)
        button.pack(side='right')

    def create_animation_window(self):
        self.animation_canvas = tk.Canvas(self.window, width=self.CANVAS_WIDTH, 
                                        height=self.CANVAS_HEIGHT, bg='white')
        self.animation_canvas.pack(pady=5)
        self.ball = self.animation_canvas.create_oval(10, 10, 50, 50, fill='black')

    def create_input_window(self):
        self.input_frame = tk.Frame(self.window, bg='lightblue')
        self.input_frame.pack(pady=5)
        self.entry = tk.Entry(self.input_frame, font=('Arial', 14), width=15)
        self.entry.pack(side='left', padx=5)
        tk.Button(self.input_frame, text='Submit', command=self.submit_input).pack(side='left')

    def create_output_window(self):
        self.output_frame = tk.Frame(self.window, bg='lightblue')
        self.output_frame.pack(pady=10)
        self.speed_label = tk.Label(self.output_frame, text=f'The speed is {self.speed}', 
                                   font=('Arial', 14), bg='lightblue')
        self.speed_label.pack()

    def click(self):
        self.running = False
        self.window.destroy()
        self.master.deiconify()