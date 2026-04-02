import tkinter as tk

class lawThree:
    name = "Newton's Third Law"
    CANVAS_HEIGHT = 500
    CANVAS_WIDTH = 800
    xVelocity1 = 0
    xVelocity2 = 0
    force1 = 0
    mass1 = 0
    force2 = 0
    mass2 = 0
    running = True
    speed1 = 0
    speed2 = 0
    acceleration1 = 0
    acceleration2 = 0
    timer = 0.0

    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel(master)
        self.window.geometry("850x800") 
        self.window.title("Newton Law Three")
        self.window.config(background="lightblue")
        self.create_window()
        self.animate()

    def animate(self):
        if self.running:
            self.coordinates1 = self.animation_canvas.coords(self.ball1)
            self.coordinates2 = self.animation_canvas.coords(self.ball2)
            
            velocity1 = self.acceleration1 * self.timer
            velocity2 = self.acceleration2 * self.timer

            # X-Geschwindigkeit berechnen
            if self.xVelocity1 < 0:
                self.xVelocity1 = -velocity1
            else:
                self.xVelocity1 = velocity1

            if self.xVelocity2 < 0:
                self.xVelocity2 = -velocity2
            else:
                self.xVelocity2 = velocity2

            # Kollision mit den Canvas-Rändern (links/rechts)
            if (self.coordinates1[2] >= self.CANVAS_WIDTH or self.coordinates1[0] <= 0):
                self.xVelocity1 = -self.xVelocity1

            if (self.coordinates2[2] >= self.CANVAS_WIDTH or self.coordinates2[0] <= 0):
                self.xVelocity2 = -self.xVelocity2


            if (self.coordinates1[2] >= self.coordinates2[0]):
                # Einfacher Impulstausch-Ansatz
                self.xVelocity1 = -self.xVelocity1
                self.xVelocity2 = -self.xVelocity2
                [self.force1, self.force2] = [self.force2, self.force1]
            
            # Bewegung nur auf der X-Achse (y-Parameter ist 0)
            self.animation_canvas.move(self.ball1, self.xVelocity1, 0)
            self.animation_canvas.move(self.ball2, self.xVelocity2, 0)
            
            self.timer += 0.01
            self.speed1 = velocity1
            self.speed2 = velocity2
            self.result_text.set(
                f'Ball 1: F = {self.force1}  m = {self.mass1}  a = {self.acceleration1}  v = {self.speed1:.2f}\n'
                f'Ball 2: F = {self.force2}  m = {self.mass2}  a = {self.acceleration2}  v = {self.speed2:.2f}'
            )
            self.window.after(10, self.animate)

    def submit_input(self):
        try:
            self.force1 = self.entry_force1.get()
            self.mass1 = self.entry_mass1.get()
            self.acceleration1 = float(self.force1) / float(self.mass1)
            self.force2 = self.entry_force2.get()
            self.mass2 = self.entry_mass2.get()
            # Kraft 2 wirkt in der Regel entgegen (3. Axiom), 
            # für die Animation setzen wir hier die Beschleunigung
            self.acceleration2 = float(self.force2) / float(self.mass2)
            # Initialer Richtungsstoß (Ball 2 bewegt sich nach links)
            self.xVelocity2 = -0.1 
        except (ValueError, ZeroDivisionError):
            self.result_text.set("Bitte gültige Zahlen eingeben (Masse > 0)!")

    def create_window(self):
        tk.Label(self.window, text="Newton's Third Law Simulation", 
                 font=('Arial', 20, 'bold'), bg='lightblue').pack(pady=10)
        self.create_animation_window()
        self.create_input_window()
        self.create_output_window()

        self.button_frame = tk.Frame(self.window, bg='lightblue')
        self.button_frame.pack(side='bottom', fill='x', padx=10, pady=10)
        tk.Button(self.button_frame, text='Home', font=('Arial', 20, 'bold'),
                  bg='blue', fg='lightblue', command=self.click).pack(side='right')

    def create_animation_window(self):
        self.animation_canvas = tk.Canvas(self.window, width=self.CANVAS_WIDTH, 
                                          height=self.CANVAS_HEIGHT, bg='white')
        self.animation_canvas.pack(pady=5)
        # Bälle auf gleicher Höhe (Y=230 bis 270) platziert
        self.ball1 = self.animation_canvas.create_oval(10, 230, 50, 270, fill='black')
        self.ball2 = self.animation_canvas.create_oval(700, 230, 740, 270, fill='red')

    def create_input_window(self):
        self.input_frame = tk.Frame(self.window, bg='lightblue')
        self.input_frame.pack(pady=5)

        # Ball 1
        tk.Label(self.input_frame, text="Ball 1\nForce\nMass", bg='lightblue', justify="left").pack(side='left', padx=10)
        self.entry_frame1 = tk.Frame(self.input_frame, bg='lightblue')
        self.entry_frame1.pack(side='left', padx=5)
        self.entry_force1 = tk.Entry(self.entry_frame1, font=('Arial', 12), width=10)
        self.entry_force1.pack(side='top')
        self.entry_mass1 = tk.Entry(self.entry_frame1, font=('Arial', 12), width=10)
        self.entry_mass1.pack(side='top')

        # Ball 2
        tk.Label(self.input_frame, text="Ball 2\nForce\nMass", bg='lightblue', justify="left").pack(side='left', padx=10)
        self.entry_frame2 = tk.Frame(self.input_frame, bg='lightblue')
        self.entry_frame2.pack(side='left', padx=5)
        self.entry_force2 = tk.Entry(self.entry_frame2, font=('Arial', 12), width=10)
        self.entry_force2.pack(side='top')
        self.entry_mass2 = tk.Entry(self.entry_frame2, font=('Arial', 12), width=10)
        self.entry_mass2.pack(side='top')

        tk.Button(self.input_frame, text='Submit', command=self.submit_input, bg='white').pack(side='left', padx=20)

    def create_output_window(self):
        self.output_frame = tk.Frame(self.window, bg='lightblue')
        self.output_frame.pack(pady=10)
        self.result_text = tk.StringVar()
        self.result_text.set(
            f'Ball 1: F = {self.force1}  m = {self.mass1}  a = {self.acceleration1}  v = {self.speed1}\n'
            f'Ball 2: F = {self.force2}  m = {self.mass2}  a = {self.acceleration2}  v = {self.speed2}'
        )
        self.value_label = tk.Label(self.output_frame, textvariable=self.result_text,
                                    font=('Arial', 12), bg='lightblue', justify="left")
        self.value_label.pack()

    def click(self):
        self.running = False
        self.window.destroy()
        self.master.deiconify()