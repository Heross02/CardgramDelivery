from tkinter import *
from PIL import ImageTk, Image
import random
import time

class Balloon:
    def __init__(self, canvas, x, y, color, is_confetti=False):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(10, 20) if is_confetti else random.randint(20, 50)
        self.speed = random.uniform(1, 3) if is_confetti else random.randint(1, 3)

        if is_confetti:
            self.id = canvas.create_rectangle(
                x - self.radius / 2,
                y,
                x + self.radius / 2,
                y + 2 * self.radius,
                outline=color,
                fill=color,
            )
        else:
            self.id = canvas.create_oval(
                x - self.radius,
                y - self.radius,
                x + self.radius,
                y + self.radius,
                outline=color,
                fill=color,
            )

    def move(self):
        self.y += self.speed
        self.canvas.move(self.id, 0, self.speed)

        if self.y - self.radius > self.canvas.winfo_height():
            self.reset_position()

    def reset_position(self):
        self.y = 0
        if hasattr(self, 'id') and self.id:
            self.canvas.coords(
                self.id,
                self.x - self.radius / 2,
                self.y,
                self.x + self.radius / 2,
                self.y + 2 * self.radius,
            )

class Confetti(Balloon):
    def __init__(self, canvas, x, y, color):
        super().__init__(canvas, x, y, color, is_confetti=True)

def create_balloon():
    x_position = random.randint(50, 1550)
    balloon_color = random.choice(["red", "blue", "green", "yellow", "purple"])

    balloon = Balloon(myCanvas, x_position, myCanvas.winfo_height(), balloon_color)
    balloons.append(balloon)

def create_confetti():
    for _ in range(random.randint(5, 15)):
        x_position = random.randint(50, 1550)
        confetti_color = random.choice(["red", "blue", "green", "yellow", "purple"])

        confetti = Confetti(myCanvas, x_position, 0, confetti_color)
        confettis.append(confetti)

def move_balloons():
    for balloon in balloons:
        balloon.move()

def move_confetti():
    for confetti in confettis:
        confetti.move()

root = Tk()
root.title("Birthday Card")
width = 1000
height = 800
root.resizable(False, False)

# Load the original image
original_image = Image.open("bday_backdrop.jpg")

# Resize the image
resized_image = original_image.resize((width, height))

# Convert the resized image to PhotoImage
pic = ImageTk.PhotoImage(resized_image)

myCanvas = Canvas(root, width=width, height=height)
myCanvas.pack(expand=True, fill=BOTH)
myCanvas.create_image(0, 0, image=pic, anchor='nw')
myCanvas.create_text(
    950, 120,
    fill="darkblue",
    font="Times 90 italic bold",
    text=""
)

# Add more birthday-themed elements (cake, candles, etc.) here...

# Create a list to store balloon objects
balloons = []

# Create a list to store confetti objects
confettis = []

# Add a button for displaying balloons
b = Button(root, text="Show Balloons", bg="blue", fg="red", command=create_balloon)
b.pack()
b.place(x=100, y=110)

# Add a button for creating confetti
create_confetti_button = Button(root, text="Create Confetti", command=create_confetti)
create_confetti_button.pack()
create_confetti_button.place(x=200, y=110)

Refreshrate = 20  # milliseconds

while True:
    move_balloons()
    move_confetti()
    root.update()
    time.sleep(Refreshrate / 1000.0)

root.mainloop()
