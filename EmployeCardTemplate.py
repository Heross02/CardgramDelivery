from tkinter import *
from PIL import ImageTk
import random


def create_confetti(canvas, confetti_list, max_confetti):
    if len(confetti_list) < max_confetti:
        x = random.uniform(0, width)
        y = 0
        size = random.randint(5, 10)
        color = random.choice(['red', 'green', 'blue', 'orange', 'purple', 'pink','yellow'])

        confetti = canvas.create_rectangle(x, y, x + size, y + size, fill=color)

        # Assign a random direction (left or right) to each balloon
        direction = random.choice([-1, 1])
        confetti_list.append((confetti, direction))


def move_confetti(canvas, confetti_list):
    for confetti, direction in confetti_list:
        canvas.move(confetti, direction, 1)  # Move confetti down and left or right

def create_balloon(canvas, balloon_list, max_balloons):
    if len(balloon_list) < max_balloons:
        x = random.uniform(50, width - 50)
        y = height
        size = random.randint(10, 30)
        color = random.choice(['red', 'green', 'blue', 'orange', 'purple', 'pink'])

        balloon = canvas.create_oval(x, y, x + size, y + size, fill=color, outline='black')
        string = canvas.create_line(x + size // 2, y + size, x + size // 2, y + size + 50, width=2, fill='black')

        # Assign a random direction (left or right) to each balloon
        direction = random.choice([-1, 1])

        balloon_list.append((balloon, string, direction))

def move_balloons(canvas, balloon_list):
    for balloon, string, direction in balloon_list:
        canvas.move(balloon, direction, -1)  # Move balloon up and left or right
        canvas.move(string, direction, -1)  # Move string up and left or right

def update_animation():

    create_confetti(myCanvas, confetti_pieces, max_confetti=150)
    move_confetti(myCanvas, confetti_pieces)
    create_balloon(myCanvas, balloon_pieces, max_balloons=10)
    move_balloons(myCanvas, balloon_pieces)

    root.after(20, update_animation)  # Schedule the next update


def ResetPieces():
    global balloon_pieces, confetti_pieces
    balloon_pieces = []
    confetti_pieces = []


def Continue_to_celebrate():
    b.destroy()
    b2.destroy()
    global b3
    b3 = Button(root, text="Celebrate", bg="black", fg="white", command=disable_button)
    b3.pack()
    b3.place(x=560, y=500)

def enable_button():
    b3.config(state= NORMAL)  # Enable the button

def enableReset():
    b2.config(state=NORMAL)

def disable_button():
    b3.config(state= DISABLED)  # Disable the button
    ResetPieces()
    root.after(25000, enable_button)  # Schedule enabling after 10 seconds

def celebrateonce():
    if (b['state'] == NORMAL):
        b['state'] = DISABLED
        root.after(15000, enableReset)
        update_animation()



root = Tk()
root.title("Employee Appreciation Day")
width = 900
height = 600
root.resizable(False, False)
balloon_pieces = []
confetti_pieces = []
myCanvas = Canvas(root, width=width, height=height)
myCanvas.pack(expand=True, fill=BOTH)

# Load image and display it on the canvas
pic = ImageTk.PhotoImage(file="2021-uofl_forms1-campaign-1920x1080.jpg")
myCanvas.create_image(0, 0, image=pic, anchor='nw')

# white string across canvas
myCanvas.create_line(0, 50, 150, 130, width=6, fill='white')
myCanvas.create_line(150, 130, 250, 150, width=6, fill='white')
myCanvas.create_line(250, 150, 350, 170, width=6, fill='white')
myCanvas.create_line(350, 170, 540, 170, width=6, fill='white')
myCanvas.create_line(540, 170, 750, 130, width=6, fill='white')
myCanvas.create_line(750, 130, 950, 50, width=6, fill='white')

# Post it cards on string

myCanvas.create_rectangle(220, 110, 300, 180, fill='yellow', outline='yellow')
myCanvas.create_rectangle(320, 135, 400, 200, fill='yellow', outline='yellow')
myCanvas.create_rectangle(430, 150, 510, 210, fill='yellow', outline='yellow')
myCanvas.create_rectangle(540, 150, 620, 210, fill='yellow', outline='yellow')
myCanvas.create_rectangle(640, 120, 720, 200, fill='yellow', outline='yellow')



myCanvas.create_text(
    255, 145,
    fill="darkblue",
    font="Times 30 italic bold",
    text="H")

myCanvas.create_text(
    355, 165,
    fill="darkblue",
    font="Times 30 italic bold",
    text="A")

myCanvas.create_text(
    465, 180,
    fill="darkblue",
    font="Times 30 italic bold",
    text="P")

myCanvas.create_text(
    575, 185,
    fill="darkblue",
    font="Times 30 italic bold",
    text="P")

myCanvas.create_text(
    675, 155,
    fill="darkblue",
    font="Times 30 italic bold",
    text="Y")


# Text on Screen
myCanvas.create_text(
    width / 2, 250,
    fill="white",
    font="Times 40 italic bold",
    text="Employee Appreciation Day")

# Create medium white rectangle at the bottom center
paper_points = [330, 550, 450, 600, 550, 553, 410, 450]
myCanvas.create_polygon(paper_points, fill='white', width=2)


# Create lines on paper
#top line
myCanvas.create_line(355, 550, 400, 500, fill="black", width=2)
myCanvas.create_line(400, 500, 420, 475, fill="black", width=2)
#second line
myCanvas.create_line(365, 560, 440, 490, fill="black", width=2)
#third line
myCanvas.create_line(375, 570, 450, 510, fill="black", width=2)
#forth line that looks like is being currently written
myCanvas.create_line(405, 570, 470, 520, fill="black", width=2)

# Create pencil body
pencil_points = [550, 470, 530, 450, 490, 503, 500, 509]
myCanvas.create_polygon(pencil_points, fill='#411F02', width=2)

# Create pencil tip
pencil_points = [500, 509, 490, 503, 480, 520]
myCanvas.create_polygon(pencil_points, fill='black', width=2)

b = Button(root, text="Celebrate", bg="black", fg="white", command=celebrateonce)
b.pack()
b.place(x=560, y=500)

b2 = Button(root, text="Click to Party On Again", bg="black", fg="white",state= DISABLED, command=Continue_to_celebrate)
b2.pack()
b2.place(x=560, y=540)

root.mainloop()
