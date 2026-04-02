import tkinter as tk

class lawTwo:
    name = "Newton's Second Law"
    CANVAS_HEIGHT = 500
    CANVAS_WIDTH = 800
    xVelocity = 0
    yVelocity = 0
    force = 0
    mass = 0
    running = True
    speed = 0
    acceleration = 0
    timer = 0.0

    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        # Erhöhe die Höhe leicht, damit alles Platz hat
        self.window.geometry("850x800") 
        self.window.title("Newton Law Two")
        self.window.config(background="lightblue")
        
        # Initialisiere die Widgets
        self.create_window()
        
        # Starte den ersten Animationszyklus
        self.animate()

    def animate(self):
        if self.running:
            self.coordinates = self.animation_canvas.coords(self.ball)
            
            velocity = self.acceleration * self.timer

            if self.xVelocity < 0:
                self.xVelocity = -velocity
            else:
                self.xVelocity = velocity

            if self.yVelocity < 0:
                self.yVelocity = -velocity
            else:
                self.yVelocity = velocity

            if (self.coordinates[2] >= self.CANVAS_WIDTH or self.coordinates[0] <= 0):
                self.xVelocity = -self.xVelocity
            if (self.coordinates[3] >= self.CANVAS_HEIGHT or self.coordinates[1] <= 0):
                self.yVelocity = -self.yVelocity
            
            self.animation_canvas.move(self.ball, self.xVelocity, self.yVelocity)
            self.timer += 0.01
            self.speed = velocity
            self.result_text.set(f'F = {self.force}\nm = {self.mass}\na = {self.acceleration}\nv = {self.speed:.2f}')
            self.window.after(10, self.animate)

    def submit_input(self):
        try:
            self.force = self.entry_force.get()
            self.mass = self.entry_mass.get()
            self.acceleration = float(self.force)/float(self.mass)
            self.value_label.set(text=f'F = {self.force}\nm = {self.mass}\na = {self.acceleration}\nv = {self.speed}')
        except ValueError:
            self.value_label.set(text="Bitte eine Zahl eingeben!")

    def create_window(self):
        tk.Label(self.window, text="Newton's Second Law Simulation", 
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

        self.forceText = tk.StringVar()
        self.forceText.set("Force\nMass")
        self.valLabel = tk.Label(self.input_frame, textvariable=self.forceText, bg='lightblue')
        self.valLabel.pack(side='left')

        self.entry_frame = tk.Frame(self.input_frame, bg='lightblue')
        self.entry_frame.pack(side='left', padx=5)

        self.entry_force = tk.Entry(self.entry_frame, font=('Arial', 12), width=15)
        self.entry_force.pack(side='top')  

        self.entry_mass = tk.Entry(self.entry_frame, font=('Arial', 12), width=15)
        self.entry_mass.pack(side='top')

        tk.Button(self.input_frame, text='Submit', command=self.submit_input).pack(side='left')

    def create_output_window(self):
        self.output_frame = tk.Frame(self.window, bg='lightblue')
        self.output_frame.pack(pady=10)
        self.result_text = tk.StringVar()
        self.result_text.set(f'F = {self.force}\nm = {self.mass}\na = {self.acceleration}\nv = {self.speed}')
        self.value_label = tk.Label(self.output_frame,
                                    textvariable=self.result_text,
                                    font=('Arial', 12), bg='lightblue', justify="left")
        self.value_label.pack()

    def click(self):
        self.running = False
        self.window.destroy()
        self.master.deiconify()